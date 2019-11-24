from django.contrib.auth.models import User , Group
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import *
from .models import *
from HR.views import generateOTPCode
import hashlib
import random, string
from django.core.exceptions import ObjectDoesNotExist , SuspiciousOperation
from django.contrib.auth import authenticate , login , logout
from django.shortcuts import redirect , get_object_or_404
from django.conf import settings as globalSettings
from ERP.models import application, permission , module
import requests
from HR.models import profile
from django.template.loader import render_to_string, get_template
from django.core.mail import send_mail, EmailMessage
import ast


class sheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('pk','created','dated','slot','name','emailId')

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ('pk','created','user','link','attachment','mediaType','name')
        read_only_fields = ('user',)
    def create(self , validated_data):
         md = Media(**validated_data)
         md.user = self.context['request'].user
         try:
             md.name = validated_data['attachment'].name
         except:
             pass
         md.save()
         return md

defaultFields = [{'name' : "Rope (mm)",'type':'float','dimensions':'mm'},{'name' : "Rope (in)",'type':'Char','dimensions':'in','inPdf':False},{'name' : "Breaking Load (kN)",'type':'float','dimensions':'kN'},{'name' : "Breaking Load (lbs)",'type':'float','dimensions':'lbs'},{'name' : "Weight (kg/100m)",'type':'float','dimensions':'kg/100m'},{'name' : "Weight (lb/ft)",'type':'float','dimensions':'lb/ft','inPdf':False},{'name' : "Construction",'type':'Char','dimensions':' '}]


class ProductTemplateSerializer(serializers.ModelSerializer):
    media = MediaSerializer(many=True,read_only=True)
    class Meta:
        model = ProductTemplate
        fields = ('pk','created','parent_name','name','description','defaultImage','backgroundImage1','backgroundImage2','media','pdfgenerated','rteData1_en','rteData1_otl','rteData2_en','rteData2_otl','disclaimer_en','disclaimer_otl','keyword1','keyword2','keyword3','keyword4','productfields','color','catalogBG1','catalogBG2','rteDescription','des_ch','des_de','rteData1_ch','rteData2_ch','disclaimer_ch','rteDescription_de','rteDescription_ch')
    def create(self , validated_data):
        pt = ProductTemplate(**validated_data)

        pt.save()
        print self.context['request'].data
        if 'media' in self.context['request'].data:
            if ',' in str(self.context['request'].data['media']):
                for i in str(self.context['request'].data['media']).split(','):
                    pt.media.add(Media.objects.get(pk=int(i)))
            else:
                pt.media.add(Media.objects.get(pk=int(str(self.context['request'].data['media']))))
        pt.save()

        for fld in defaultFields:
            pf = ProductField(**fld)
            pf.template = pt
            pf.save()
        return pt

    def update(self ,instance, validated_data):
        for key in ['name','parent_name','description','defaultImage','backgroundImage1','backgroundImage2','media','pdfgenerated','rteData1_en','rteData1_otl','rteData2_en','rteData2_otl','disclaimer_en','disclaimer_otl','keyword1','keyword2','keyword3','keyword4','productfields','color','catalogBG1','catalogBG2','rteDescription','des_ch','des_de','rteData1_ch','rteData2_ch','disclaimer_ch','rteDescription_de','rteDescription_ch']:
            try:
                setattr(instance , key , validated_data[key])
            except:
                pass
        if 'media' in self.context['request'].data:
            instance.media.clear()
            if ',' in str(self.context['request'].data['media']):
                for i in str(self.context['request'].data['media']).split(','):
                    instance.media.add(Media.objects.get(pk=int(i)))
            else:
                instance.media.add(Media.objects.get(pk=int(str(self.context['request'].data['media']))))
        instance.save()
        return instance


class ProductFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductField
        fields = ('pk','created','name','type','required','dimensions','inPdf','inUI','template')
    def create(self , validated_data):
         pf = ProductField(**validated_data)
         pf.template = ProductTemplate.objects.get(pk = self.context['request'].data['template'])
         pf.save()
         return pf

class ProductSerializer(serializers.ModelSerializer):
    template = ProductTemplateSerializer(many=False,read_only=True)
    fieldValues = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ('pk','created','itemNumber','template','fieldValues')
    def create(self , validated_data):
         pf = Product(**validated_data)
         pf.template = ProductTemplate.objects.get(pk = self.context['request'].data['template'])
         pf.save()
         if 'fieldaData' in self.context['request'].data:
             for f in self.context['request'].data['fieldaData']:
                 print f
                 fieldObj = ProductField.objects.get(pk=int(f['pk']))
                 data = {'product':pf,'field':fieldObj}
                 if f['typ']=='Char':
                     data['char'] = str(f['value'])
                 elif f['typ']=='Boolean':
                     data['bool'] = f['value']
                 elif f['typ']=='Integer':
                     data['iValue'] = int(f['value'])
                 elif f['typ']=='float':
                     data['fValue'] = float(f['value'])
                 else:
                     continue
                 ProductValueMap.objects.create(**data)
         return pf
    def update (self, instance, validated_data):
        if 'itemNumber' in self.context['request'].data:
            instance.itemNumber = int(self.context['request'].data['itemNumber'])
        if 'fieldaData' in self.context['request'].data:
            for f in self.context['request'].data['fieldaData']:
                print f
                fieldValObj = ProductValueMap.objects.get(pk=int(f['pk']))
                if f['typ']=='Char':
                    fieldValObj.char = str(f['value'])
                elif f['typ']=='Boolean':
                    fieldValObj.bool = f['value']
                elif f['typ']=='Integer':
                    fieldValObj.iValue = int(f['value'])
                elif f['typ']=='float':
                    fieldValObj.fValue = float(f['value'])
                else:
                    continue
                fieldValObj.save()
        instance.save()
        return instance
    def get_fieldValues(self,obj):
        try:
            fieldValObj = obj.products.all().order_by('field')
            toRet = ProductValueMapSerializer(fieldValObj,many=True)
            return toRet.data
        except:
            return []

class ProductValueMapSerializer(serializers.ModelSerializer):
    field = ProductFieldSerializer(many=False,read_only=True)
    class Meta:
        model = ProductValueMap
        fields = ('pk','created','field','bool','char','fValue','iValue','product')

class PdfDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PdfDescription
        fields = ('pk','created','title','description')

class CareerFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerField
        fields = ('pk','created','name','jobtype','skills','description','status','maxctc')

# class ApptipsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Apptips
#         fields = ('pk','created','text','image')

class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Apply
        fields = ('pk', 'firstname', 'lastname','email','mobile','coverletter','resume','forg')

    def create(self , validated_data):
         ap = Apply(**validated_data)
         ap.forg = CareerField.objects.get(pk = int(self.context['request'].data['forg']))
         ap.save()

         ctx = {'fname':ap.firstname,'lname':ap.lastname,'email':ap.email,'mobile':ap.mobile,'letter':ap.coverletter,'resume':ap.resume, 'jobtype':ap.forg.jobtype, 'name':ap.forg.name, 'maxctc':ap.forg.maxctc, 'skills':ap.forg.skills, 'description': ap.forg.description }
                     # 'jobtype':request.data['jobtype'],

         email_subject = 'Successfully Applied for Position'
         email_body = get_template('app.careers.email.data.html').render(ctx)
         msg = EmailMessage(email_subject, email_body, to=[ap.email])
         # msg.attach_file('ap.forg.resume')
         msg.content_subtype = 'html'
         msg.attach_file(ap.resume.path)
                 # msg.attach(att)
         msg.send()

         return ap

class ApptipsLiteSerializer(serializers.ModelSerializer):
    class Meta:
        model =Apptips
        fields = ('pk','text','image1','heading','size','tipname','lang','mediaTyp')

class ApptipsSerializer(serializers.ModelSerializer):
    heading = ApptipsLiteSerializer(many=False,read_only=True)
    class Meta:
        model =Apptips
        fields = ('pk','text','image1','heading','size','tipname','lang','mediaTyp')
    def create(self,validated_data):
        at = Apptips(**validated_data)
        print self.context['request'].data
        if 'heading' in self.context['request'].data:
                at.heading = Apptips.objects.get(pk = int(self.context['request'].data['heading']))
        at.save()
        return at

    def update(self, instance, validated_data):
        for key in ['text','image1','heading','size','tipname','lang','mediaTyp']:
            try:
                setattr(instance , key , validated_data[key])
            except:
                pass

        if 'heading' in self.context['request'].data:
            instance.heading = Apptips.objects.get(pk = int(self.context['request'].data['heading']))
        instance.save()
        return instance

class AccessoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model =Accessories
        fields = ('pk','name','mainImage')

class AccessoriesSectionSerializer(serializers.ModelSerializer):
    media = MediaSerializer(many=True,read_only=True)
    class Meta:
        model = AccessoriesSection
        fields = ('pk','categoryName','basicProductName','productName','tagLine','title1','desc1','title2','desc2','lang','accessories','image1','image2','bottomtext','backgroundImage1','backgroundImage2','catalogBG1',"catalogBG2","media")
    def create(self,validated_data):
        accSection = AccessoriesSection(**validated_data)
        if 'accessories' in self.context['request'].data:
                accSection.accessories = Accessories.objects.get(pk = int(self.context['request'].data['accessories']))
        accSection.save()
        if 'media' in self.context['request'].data:
            if ',' in str(self.context['request'].data['media']):
                for i in str(self.context['request'].data['media']).split(','):
                    accSection.media.add(Media.objects.get(pk=int(i)))
            else:
                accSection.media.add(Media.objects.get(pk=int(str(self.context['request'].data['media']))))
        accSection.save()
        return accSection
    def update(self, instance, validated_data):
        for key in ['pk','categoryName','basicProductName','productName','tagLine','title1','desc1','title2','desc2','lang','accessories','image1','image2','bottomtext','backgroundImage1','backgroundImage2','catalogBG1','catalogBG2',"media"]:
            try:
                setattr(instance , key , validated_data[key])
            except:
                pass
        if 'accessories' in self.context['request'].data:
                instance.accessories = Accessories.objects.get(pk = int(self.context['request'].data['accessories']))
        instance.save()
        if 'media' in self.context['request'].data:
            instance.media.clear()
            print self.context['request'].data['media'],'llllllllllllllllllllllllllll'
            if ',' in str(self.context['request'].data['media']):
                for i in str(self.context['request'].data['media']).split(','):
                    instance.media.add(Media.objects.get(pk=int(i)))
            else:
                instance.media.add(Media.objects.get(pk=int(str(self.context['request'].data['media']))))
        instance.save()
        return instance

class AccessoriesFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessoriesField
        fields = ('pk','created','name','type','required','dimensions','inPdf','inUI','template','productBaseName')
    def create(self , validated_data):
         af = AccessoriesField(**validated_data)
         af.template = AccessoriesSection.objects.get(pk = self.context['request'].data['template'])
         af.save()
         return af
    def update (self, instance, validated_data):
        for key in ['type','required','dimensions','inPdf','inUI','template']:
            try:
                setattr(instance , key , validated_data[key])
            except:
                pass
        instance.save()
        return instance

class AccessoriesDataSerializer(serializers.ModelSerializer):
    template = AccessoriesSectionSerializer(many=False,read_only=True)
    accessoriesfieldValues = serializers.SerializerMethodField()
    class Meta:
        model = AccessoriesData
        fields = ('pk','created','itemNumber','template','accessoriesfieldValues','productBaseName')
    def create(self , validated_data):
         pf = AccessoriesData(**validated_data)
         pf.template = AccessoriesSection.objects.get(pk = self.context['request'].data['template'])
         pf.save()
         if 'fieldaData' in self.context['request'].data:
             for f in self.context['request'].data['fieldaData']:
                 print f
                 fieldObj = AccessoriesField.objects.get(pk=int(f['pk']))
                 data = {'product':pf,'field':fieldObj,'productBaseName':self.context['request'].data['productBaseName']}
                 if f['typ']=='Char':
                     data['char'] = str(f['value'])
                 elif f['typ']=='Boolean':
                     data['bool'] = f['value']
                 elif f['typ']=='Integer':
                     data['iValue'] = int(f['value'])
                 elif f['typ']=='float':
                     data['fValue'] = float(f['value'])
                 else:
                     continue
                 AccessoriesValueMap.objects.create(**data)
         return pf
    def update (self, instance, validated_data):
        if 'itemNumber' in self.context['request'].data:
            instance.itemNumber = int(self.context['request'].data['itemNumber'])
        if 'fieldaData' in self.context['request'].data:
            for f in self.context['request'].data['fieldaData']:
                print f
                fieldValObj = AccessoriesValueMap.objects.get(pk=int(f['pk']))
                if f['typ']=='Char':
                    fieldValObj.char = str(f['value'])
                elif f['typ']=='Boolean':
                    fieldValObj.bool = f['value']
                elif f['typ']=='Integer':
                    fieldValObj.iValue = int(f['value'])
                elif f['typ']=='float':
                    fieldValObj.fValue = float(f['value'])
                else:
                    continue
                fieldValObj.save()
        instance.save()
        return instance
    def get_accessoriesfieldValues(self,obj):
        try:
            accessoriesfieldValuesObj = AccessoriesValueMap.objects.filter(product=obj.pk)
            toRet = AccessoriesValueMapSerializer(accessoriesfieldValuesObj,many=True)
            return toRet.data
        except:
            return []

class AccessoriesValueMapSerializer(serializers.ModelSerializer):
    field = AccessoriesFieldSerializer(many=False,read_only=True)
    class Meta:
        model = AccessoriesValueMap
        fields = ('pk','created','field','bool','char','fValue','iValue','product')

class AlbumImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumImages
        fields = ('pk','created','image')


class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = ('pk','created','lat','long','address_en','address_de','address_zh','representation','name','shortUrl')
