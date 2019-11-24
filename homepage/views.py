#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User , Group
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.conf import settings as globalSettings
from django.core.exceptions import ObjectDoesNotExist , SuspiciousOperation
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework import viewsets , permissions , serializers
from rest_framework.exceptions import *
from url_filter.integrations.drf import DjangoFilterBackend
from .serializers import *
from API.permissions import *
from ERP.models import application, permission , module
from ERP.views import getApps, getModules
from django.db.models import Q
from django.http import JsonResponse
import random, string
from django.utils import timezone
from rest_framework.views import APIView
from PIM.models import blogPost
from django.utils import translation
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm,inch
from reportlab.lib import colors, utils
from reportlab.platypus import Paragraph, Table, TableStyle, Image, Frame, Spacer, PageBreak, BaseDocTemplate, PageTemplate, SimpleDocTemplate, Flowable,ListFlowable
from reportlab.platypus.flowables import HRFlowable
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet, TA_CENTER
from reportlab.graphics import barcode, renderPDF
from reportlab.graphics.shapes import *
from reportlab.platypus.flowables import Image as GNAA
from reportlab.lib.pagesizes import letter,landscape
from reportlab.lib.colors import Color,yellow, red, black,white,grey
from reportlab.graphics.shapes import Rect
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.colors import red, yellow, green, gray, white
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from reportlab.platypus import Image as LabImage
from reportlab.graphics import shapes
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics import renderPDF, renderPM
from svglib.svglib import svg2rlg
from PIL import Image, ImageFilter
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderSVG
from django.http import HttpResponse ,StreamingHttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from bs4 import BeautifulSoup
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.db.models import Max
import html2text
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import fonts, colors
from reportlab.pdfbase.ttfonts import TTFont
import math

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import A5
from reportlab.lib.pagesizes import A6
from reportlab.lib.units import cm, mm,inch
from reportlab.lib import colors, utils
from reportlab.platypus import Paragraph, Table, TableStyle, Image, Frame, Spacer, PageBreak, BaseDocTemplate, PageTemplate, SimpleDocTemplate, Flowable
from reportlab.platypus.doctemplate import BaseDocTemplate, PageTemplate, NextPageTemplate
from reportlab.platypus.flowables import HRFlowable
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet, TA_CENTER
from reportlab.graphics import barcode, renderPDF
from reportlab.graphics.shapes import *
from reportlab.platypus.flowables import Image as GNAA
from reportlab.lib.pagesizes import letter,landscape
from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet, TA_CENTER
from reportlab.lib.colors import yellow, red, black,white,grey
from reportlab.graphics.shapes import Rect
from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF
from reportlab.graphics.shapes import Drawing
from reportlab.pdfgen.canvas import Canvas
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.colors import red, yellow, green, gray, white
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.platypus import Image
from reportlab.graphics import shapes
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics import renderPDF, renderPM
from reportlab.graphics.shapes import Drawing
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from PIL import Image, ImageFilter
from svglib.svglib import svg2rlg
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderSVG
from reportlab.graphics import shapes
from reportlab.graphics.charts.textlabels import Label
from reportlab.lib.colors import Color, black, blue, red
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import ImageFont
from reportlab.pdfbase.cidfonts import UnicodeCIDFont, findCMapFile
from preppy import SafeString
from rlextra.radxml.xhtml2rml import xhtml2rml
from rlextra.radxml.html_cleaner import cleanPlain
from django.db.models import F ,Value,CharField,Prefetch
from colour import Color as rangeColors
import reportlab.rl_config


pdfmetrics.registerFont(TTFont('FrutigerR', 'Frutiger_45_Light.ttf'))
pdfmetrics.registerFont(TTFont('FrutigerB', 'frutiger-lt-65-bold.ttf'))
pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
pdfmetrics.registerFont(UnicodeCIDFont('MSung-Light'))
pageCount = 1

_family_alias = {
            'serif':'times',
            'sansserif':'helvetica',
            'monospaced':'courier',
            'arial':'helvetica',
            'chFontFamily':'STSong-Light'

}

def renderedLang(request):
    # printrequest,'pppppppppppp',request.COOKIES.get('lang'),request.COOKIES
    # printtranslation.get_language_from_request(request),'llllll'
    if request.COOKIES.get('lang') == None:
        language = translation.get_language_from_request(request)
    else:
        language = request.COOKIES.get('lang')
    # printlanguage
    translation.activate(language )
    request.LANGUAGE_CODE = translation.get_language()
    # printrequest.LANGUAGE_CODE,'pppppppppppppppppppppp'
    return request.LANGUAGE_CODE


def sitemapView(request):
    queryset = ProductTemplate.objects.all()
    lang = renderedLang(request)
    # printProductTemplate.objects.all()
    gr = []
    hr =[]
    cr = []
    for i in queryset:
        if i.parent_name =="governor-ropes":
            gr.append({'pk':i.pk,'name':i.name,"parent_name":i.parent_name})
        elif i.parent_name == "traction-ropes":
            hr.append({'pk':i.pk,'name':i.name,"parent_name":i.parent_name})
        elif i.parent_name == "compensation-ropes":
            cr.append({'pk':i.pk,'name':i.name,"parent_name":i.parent_name})
        # printgr,cr,hr
    return render(request, 'app.homepage.sitemap.html', {"home": True , "gr":gr,"hr":hr,"cr":cr ,"lang" : lang,'title':'Sitemap'})
def apptipsView(request):
    lang = renderedLang(request)
    tips = Apptips.objects.filter(heading=None, lang = lang )
    # tip = []
    # for i in queryset:
    #     tipChild=[]
    #     name = {"pk":i.pk,"tipname":i.tipname}
    #     if i.image1:
    #         image = i.image1
    #     else:
    #         image = ''
    #     tipChild.append({"pk":i.pk,"text":i.text,"image1":image,"tipname":i.tipname,'size':i.size,'heading':i.pk,'mediaTyp':i.mediaTyp})
    #     querysetChild = Apptips.objects.filter(heading__id=i.pk)
    #     for j in querysetChild:
    #         if j.image1:
    #             image1 = j.image1
    #         else:
    #             image1 = ''
    #         tipChild.append({"pk":j.pk,"text":j.text,"image1":image1,"tipname":j.tipname,'size':j.size,'heading':j.heading,'mediaTyp':j.mediaTyp})
    #     tip.append({"name":name,"values":tipChild})
    # # printtip
    return render(request, 'app.homepage.apptips.html', {"home": True , "tips": tips,"lang" : lang,'title':'Apptips' })

def referenceView(request):
    lang = renderedLang(request)
    return render(request, 'app.homepage.reference.html', {"home": True , "brandLogo" : globalSettings.BRAND_LOGO , "brandLogoInverted": globalSettings.BRAND_LOGO_INVERT,"erpUrl": globalSettings.ERP_URL_PREFIX,'apiManagerUrl':globalSettings.APIMANAGER_URL_PREFIX,"lang" : lang})

def locationsView(request):
    lang = renderedLang(request)
    locationObj =  Locations.objects.all().order_by('representation')
    toreturn = []
    for l in locationObj:
        print l.pk,'jjjjjjjjjjjjj'
        toreturn.append({"pk":l.pk,"name":l.name,"en":l.address_en,"zh":l.address_zh,"de":l.address_de,"representation":l.representation,"url":l.shortUrl})
    locations = serializers.serialize("json",Locations.objects.all())
    # print locations,'jjjjjjjj'
    # return render(request, 'locations.html', {"home": True , "brandLogo" : globalSettings.BRAND_LOGO , "brandLogoInverted": globalSettings.BRAND_LOGO_INVERT,"erpUrl": globalSettings.ERP_URL_PREFIX,'apiManagerUrl':globalSettings.APIMANAGER_URL_PREFIX,"lang" : lang })
    return render(request, 'locations.html', {"home": True ,"lang" : lang,"toreturn":toreturn,'locations':locations,'title':'Locations' })

def legalView(request):
    lang = renderedLang(request)
    return render(request, 'legal-privacy.html', {"home": True ,"lang" : lang,'title':'Legal & Privacy' })

def ProductInformationView(request):
    lang = renderedLang(request)
    return render(request, 'product-information.html', {"home": True ,"lang" : lang,'title':'Product Information' })

def TechnicalInformationView(request):
    lang = renderedLang(request)
    return render(request, 'tech-info.html', {"home": True ,"lang" : lang,'title':'Technical Information' })

def ApplicationView(request):
    lang = renderedLang(request)
    return render(request, 'application.html', {"home": True ,"lang" : lang,'title':'Application' })

from django.core import serializers
def AccessoriesView(request):
    lang = renderedLang(request)
    toreturn = []
    parentObj = Accessories.objects.all()
    for p in parentObj:
        values = []
        sectionObj = AccessoriesSection.objects.filter(lang=lang , accessories = p.id)
        if len(sectionObj)>0:
            data = {'name' : sectionObj[0].categoryName}
            for s in sectionObj:
                value = {"categoryName" : s.categoryName, "productName" : s.productName, "tagLine" : s.tagLine,"image1":s.image1,"basicProductName":s.basicProductName}
                values.append(s)
            data['values']=values
            toreturn.append(data)
    return render(request, 'accessories.html', {"home": True ,"lang" : lang, "toreturn":toreturn,'title':'Accessories' })

def AccessoriesDetailView(request,product):
    lang = renderedLang(request)
    toreturn = []
    print lang,'llllllllllllllllllllllll'
    sectionObj = AccessoriesSection.objects.get(lang=lang , basicProductName = product)
    albumImages = sectionObj.media.all()
    prodfield = AccessoriesField.objects.filter(productBaseName = product)
    prod = AccessoriesData.objects.filter(productBaseName = product)
    data = []
    listData = ['Item Number']
    for i in prodfield:
        listData.append(i.name)
    for i in prod:
        appendlist = [i.itemNumber]
        for j in prodfield:
            prodQty = AccessoriesValueMap.objects.filter( field = j.pk,product = i.pk)
            for k in prodQty:
                if j.type=='Char':
                    appendlist.append(k.char)
                if j.type=='float':
                    appendlist.append(k.fValue)
                if j.type=='Integer':
                    appendlist.append(k.iValue)
                if j.type=='Boolean':
                    appendlist.append(k.bool)
        data.append(appendlist)
    return render(request, 'accessoriesDetail.html', {"home": True ,"lang" : lang, "product":sectionObj,'heading':listData,'data':data,"albumImages":albumImages,'title':sectionObj.productName })


def index(request):
    if request.COOKIES.get('lang') == None:
        language = translation.get_language_from_request(request)
    else:
        language = request.COOKIES.get('lang')

    translation.activate(language )
    request.LANGUAGE_CODE = translation.get_language()
    # printlanguage,'languagelanguagelanguage'
    return render(request, 'index.html', {"home": True , "brandLogo" : globalSettings.BRAND_LOGO , "brandLogoInverted": globalSettings.BRAND_LOGO_INVERT,"erpUrl": globalSettings.ERP_URL_PREFIX,'apiManagerUrl':globalSettings.APIMANAGER_URL_PREFIX})

# def crmHome(request):
#     return render(request, 'crm.html', {"home": True , "brandLogo" : globalSettings.BRAND_LOGO , "brandLogoInverted": globalSettings.BRAND_LOGO_INVERT})

@csrf_exempt
def customerLoginView(request):
    authStatus = {'status' : 'default' , 'message' : '' }
    def loginRender(authStatus):
        return render(request, 'customerLogin.html', {'authStatus' : authStatus ,'useCDN' : globalSettings.USE_CDN , 'backgroundImage': globalSettings.LOGIN_PAGE_IMAGE , "brandLogo" : globalSettings.BRAND_LOGO , "brandLogoInverted": globalSettings.BRAND_LOGO_INVERT} )
    def go_next():
        nxt = request.GET.get('next','/customerhome')
        return redirect(nxt)

    if request.user.is_authenticated:
        return go_next()

    if 'GET' == request.method:
        return loginRender(authStatus)
    elif 'POST' == request.method:
        # printrequest.POST
        userObj = User.objects.filter(username = request.POST['username'])
        if len(userObj)>0:
            sObj = userObj[0].servicesContactPerson.all()
            if len(sObj)>0:
                user = authenticate(username = request.POST['username'] , password = request.POST['password'])
                if user is not None:
                    login(request , user)
                    return go_next()
                else:
                    authStatus = {'status' : 'danger' , 'message' : "Incorrect username or password."}
                    return loginRender(authStatus)
            else:
                authStatus = {'status' : 'danger' , 'message' : "Not A Right Person"}
                return loginRender(authStatus)
        else:
            authStatus = {'status' : 'danger' , 'message' : "You Don't Have An Account"}
            return loginRender(authStatus)

@login_required(login_url = '/customer/login')
def customerHomeView(request):
    return render(request, 'customerHome.html' )

from django.db.models import Q
from next_prev import next_in_order, prev_in_order
def blogDetails(request, blogname):
    lang = renderedLang(request)
    blogallobj = blogPost.objects.all().order_by('-created')
    blogobj = blogallobj.get(title=blogname)
    prv = ''
    nxt = ''
    # qs =  blogallobj
    newest = blogallobj.get(title=blogname)
    try:
        previous = prev_in_order(newest, qs=blogallobj, loop=True)
        prev =  previous.title
    except:
        prev =  ''
    try:
        next =  next_in_order(newest, qs=blogallobj)
        nxt =  next.title
    except:
        nxt =  ''

    recentBlogs = blogallobj[0:5]

    title = blogobj.title
    header = blogobj.header
    us = ''
    blogId = blogobj.pk
    count = 0
    for j in blogobj.users.all():
        if count == 0:
            us = j.first_name + ' ' + j.last_name
        else:
            us += ' , ' + j.first_name + ' ' + j.last_name
        count += 1
    date = blogobj.created
    body = blogobj.source
    image = blogobj.ogimage
    try:
        video = blogobj.shortUrl
        if video == None or len(video)<=0:
            isVideo = False
        else:
            isVideo = True
    except:
        video = ''
        isVideo = False
    return render(request, 'blogdetails.html', {"home": False, 'user': us, 'header': header, 'title': title, 'date': date, 'blogId': blogId, 'body': body,'recentBlogs':recentBlogs, 'image':image , 'video':video , "brandLogo" : globalSettings.BRAND_LOGO , "brandLogoInverted": globalSettings.BRAND_LOGO_INVERT,'previous':prev,'next':nxt,"lang" : lang,"isVideo":isVideo,})

def blog(request):
    lang = renderedLang(request)
    blogObj = blogPost.objects.all().order_by('-created')

    pagesize = 14
    try:
        page = int(request.GET.get('page', 1))
    except ValueError as error:
        page = 1
    total = blogObj.count()
    last = total/pagesize + (1 if total%pagesize !=0 else 0)
    total = blogObj.count()
    last = total/pagesize + (1 if total%pagesize !=0 else 0)
    pages = {'first':1,
			'prev':(page-1) if page >1 else 1,
			'next':(page+1) if page !=last else last,
			'last':last,
			'currentpage':page}

    firstSection = []
    second_sec1 = []
    second_sec2 = []
    thirdSection = []
      # # printlen(allBlogs),'ddddddd'
    recentBlogs = blogObj[0:5]
    for idx,val in enumerate(blogObj):
          # # printidx,val.title
          if idx < 4 :
              firstSection.append({'pk': val.id ,'title' : val.title , 'shortUrl' : val.shortUrl, 'ogimage' : val.ogimage })
          if idx >= 4 and idx < 7 :
              second_sec1.append({'pk': val.id ,'title' : val.title , 'shortUrl' : val.shortUrl, 'ogimage' : val.ogimage })
          if idx >= 7 and idx < 10 :
              second_sec2.append({'pk': val.id ,'title' : val.title , 'shortUrl' : val.shortUrl, 'ogimage' : val.ogimage })
          if idx >= 10 and idx < 14 :
              thirdSection.append({'pk': val.id ,'title' : val.title , 'shortUrl' : val.shortUrl, 'ogimage' : val.ogimage })
    # # printfirstSection
    # # printsecond_sec1
    # # printsecond_sec2
    # # printthirdSection ,'ddddthus is in blogsssss dddddddddddd'

    return render(request,"blog.html" , {"home" : False,'firstSection':firstSection,'second_sec1':second_sec1,'second_sec2':second_sec2,'thirdSection':thirdSection,'recentBlogs':recentBlogs,'pages':pages,'blogObj':blogObj,"lang" : lang,'title':'Blogs' })


def main(request):
    lang = renderedLang(request)
    albumImages = AlbumImages.objects.all()
    return render(request, 'app.homepage.index.html', {"lang" : lang , "albumImages":albumImages})

def about(request):
    lang = renderedLang(request)
    return render(request, 'about.html', {"lang" : lang , 'title':'About Us' })


def rope_selection(request):
    lang = renderedLang(request)
    return render(request, 'rope-selection.html', {"lang" : lang,'title':'Rope Selection'})

def innovation(request):
    lang = renderedLang(request)
    template = ProductTemplate.objects.get(parent_name__iexact = 'innovation')
    prodfield = ProductField.objects.filter(template = template.pk)
    prod = Product.objects.filter(template = template.pk)
    prodVal = ProductValueMap.objects.filter(field__template__id = template.pk)
    data = []
    listData = ['Item Number']
    for i in prodfield:
        listData.append(i.name)
    for i in prod:
        appendlist = [i.itemNumber]
        for j in prodfield:
            prodQty = ProductValueMap.objects.filter( field = j.pk,product = i.pk)
            for k in prodQty:
                if j.type=='Char':
                    appendlist.append(k.char)
                if j.type=='float':
                    appendlist.append(k.fValue)
                if j.type=='Integer':
                    appendlist.append(k.iValue)
                if j.type=='Boolean':
                    appendlist.append(k.bool)
        data.append(appendlist)
    keyword1= json.loads(template.keyword1)
    keyword2= json.loads(template.keyword2)
    keyword3= json.loads(template.keyword3)
    keyword4= json.loads(template.keyword4)
    return render(request, 'innovation.html',{"data":data,"template":template,"heading":listData,"keyword1":keyword1,"keyword2":keyword2,"keyword3":keyword3,"keyword4":keyword4,'title':'Innovation',"lang" : lang})

def work_culture(request):
    lang = renderedLang(request)
    return render(request, 'work-culture.html',{'title':'Work Culture',"lang" : lang ,})

def product(request):
    tractionTemples = ProductTemplate.objects.filter(parent_name__iexact = 'traction-ropes')
    compensationTemples = ProductTemplate.objects.filter(parent_name__iexact = 'compensation-ropes')
    govenorTemples = ProductTemplate.objects.filter(parent_name__iexact = 'governor-ropes')
    lang = renderedLang(request)
    return render(request, 'product.home.html',{"tractionTemples" : tractionTemples, "compensationTemples" : compensationTemples, "govenorTemples" : govenorTemples,"lang" : lang ,'title':'Products'})

def categoriesView(request,name):
    productTemples = ProductTemplate.objects.filter(parent_name__iexact = name)
    lang = renderedLang(request)
    return render(request, 'categories.html',{"productTemples" : productTemples,"lang" : lang , 'title':name})


def productsView(request,product):
    id = product.split("_")[1]
    productsPage = ProductTemplate.objects.get(pk = id)
    tempFieldsData = ProductField.objects.filter(template = productsPage)
    prodfield = ProductField.objects.filter(template = id)
    prod = Product.objects.filter(template = id)
    prodVal = ProductValueMap.objects.filter(field__template__id = id)
    weightMax = prodVal.filter(field__name = 'Weight (kg/100m)').aggregate(Max('fValue'))
    loadMax = prodVal.filter(field__name = 'Breaking Load (kN)').aggregate(Max('fValue'))
    weightlbMax = prodVal.filter(field__name = 'Weight (lb/ft)').aggregate(Max('fValue'))
    loadlbMax = prodVal.filter(field__name = 'Breaking Load (lbs)').aggregate(Max('fValue'))
    data = []
    for i in prod:
        appendlist = [int(i.itemNumber)]
        for j in prodfield:
            prodQty = ProductValueMap.objects.filter( field = j.pk,product = i.pk)
            for k in prodQty:
                if j.type=='Char':
                    appendlist.append(k.char)
                if j.type=='float':
                    appendlist.append(k.fValue)
                if j.type=='Integer':
                    appendlist.append(k.iValue)
                if j.type=='Boolean':
                    appendlist.append(k.bool)
        data.append(appendlist)
    productsPage_id = productsPage.pk
    keyword1= json.loads(productsPage.keyword1)
    keyword2= json.loads(productsPage.keyword2)
    keyword3= json.loads(productsPage.keyword3)
    keyword4= json.loads(productsPage.keyword4)
    rteData1_en= BeautifulSoup(productsPage.rteData1_en)
    rteData1_en =  rteData1_en.get_text()
    rteData2_en= BeautifulSoup(productsPage.rteData2_en)
    rteData2_en =  rteData2_en.get_text()
    rteData1_de= BeautifulSoup(productsPage.rteData1_otl)
    rteData1_de =  rteData1_de.get_text()
    rteData2_de= BeautifulSoup(productsPage.rteData2_otl)
    rteData2_de =  rteData2_de.get_text()
    rteData1_zh= BeautifulSoup(productsPage.rteData1_ch)
    rteData1_zh =  rteData1_zh.get_text()
    rteData2_zh= BeautifulSoup(productsPage.rteData2_ch)
    rteData2_zh =  rteData2_zh.get_text()
    lang = renderedLang(request)
    albumImages = productsPage.media.all()
    return render(request, 'products.html',{"templateDetails" : productsPage,"keyword1":keyword1,"lang" : lang,"keyword2":keyword2,"keyword3":keyword3,"keyword4":keyword4,"rteData1_en":rteData1_en,"rteData2_en":rteData2_en,"rteData1_de":rteData1_de,"rteData2_de":rteData2_de,"rteData1_ch":rteData1_zh,"rteData2_ch":rteData2_zh,
     "productsPage_id":productsPage_id,"tempFieldsData":tempFieldsData,"data":data,'weightMax':weightMax['fValue__max'],'loadMax':loadMax['fValue__max'],'weightlbMax':weightlbMax['fValue__max'],'loadlbMax':loadlbMax['fValue__max'],'albumImages':albumImages,'title':productsPage.name })


import ast
def productsViewRefresh(request):
    data = json.loads(request.body)
    id = data['pkVal']
    weight = data['weight']
    load = data['load']
    checkVal = data['checkVal']
    prodfield = ProductField.objects.filter(template = id)
    prod = Product.objects.filter(template = id)
    data = []
    listData = []

    listData = ['Item Number']
    for i in prodfield:
        if checkVal == 'KN':
            if i.name != 'Weight (lb/ft)' and i.name != 'Breaking Load (lbs)' and i.name!= 'Rope (in)':
                listData.append(i.name)
        elif checkVal == 'LB':
            if i.name != 'Weight (kg/100m)' and i.name != 'Breaking Load (kN)' and i.name!= 'Rope (mm)':
                listData.append(i.name)
        else:
            listData.append(i.name)
    data.append(listData)
    for i in prod:
        listData = [int(i.itemNumber)]
        appendlist = {'name':int(i.itemNumber)}
        for j in prodfield:
            prodQty = ProductValueMap.objects.filter( field = j.pk,product = i.pk)
            for k in prodQty:
                if checkVal == 'KN':
                    if k.field.name != 'Weight (lb/ft)' and k.field.name != 'Breaking Load (lbs)' and k.field.name!= 'Rope (in)':
                        if j.type=='Char':
                            appendlist.update({k.field.name : k.char})
                            listData.append(k.char)
                        if j.type=='float':
                            appendlist.update({k.field.name : k.fValue})
                            listData.append(k.fValue)
                        if j.type=='Integer':
                            appendlist.update({k.field.name : k.iValue})
                            listData.append(k.iValue)
                        if j.type=='Boolean':
                            appendlist.update({k.field.name : k.bool})
                            listData.append(k.bool)
                elif checkVal == 'LB':
                    if k.field.name != 'Weight (kg/100m)' and k.field.name != 'Breaking Load (kN)' and k.field.name!= 'Rope (mm)':
                        if j.type=='Char':
                            appendlist.update({k.field.name : k.char})
                            listData.append(k.char)
                        if j.type=='float':
                            appendlist.update({k.field.name : k.fValue})
                            listData.append(k.fValue)
                        if j.type=='Integer':
                            appendlist.update({k.field.name : k.iValue})
                            listData.append(k.iValue)
                        if j.type=='Boolean':
                            appendlist.update({k.field.name : k.bool})
                            listData.append(k.bool)
                else:
                    if j.type=='Char':
                        appendlist.update({k.field.name : k.char})
                        listData.append(k.char)
                    if j.type=='float':
                        appendlist.update({k.field.name : k.fValue})
                        listData.append(k.fValue)
                    if j.type=='Integer':
                        appendlist.update({k.field.name : k.iValue})
                        listData.append(k.iValue)
                    if j.type=='Boolean':
                        appendlist.update({k.field.name : k.bool})
                        listData.append(k.bool)
        if checkVal == 'KN':
            if 'Weight (kg/100m)' and 'Breaking Load (kN)' in  appendlist:
                if float(appendlist['Weight (kg/100m)']) >= float(weight) and float(appendlist['Breaking Load (kN)'])>=float(load):
                    data.append(listData)
        elif checkVal == 'LB':
            if 'Weight (lb/ft)' and 'Breaking Load (lbs)' in  appendlist:
                if float(appendlist['Weight (lb/ft)']) >= float(weight) and float(appendlist['Breaking Load (lbs)'])>=float(load):
                    data.append(listData)
        else:
            data.append(listData)
    return HttpResponse(data)

def news(request):
    return render(request,"newssection.html" , {"home" : False , "brandLogo" : globalSettings.BRAND_LOGO , "brandLogoInverted": globalSettings.BRAND_LOGO_INVERT})

def team(request):
    return render(request,"team.html" , {"home" : False , "brandLogo" : globalSettings.BRAND_LOGO , "brandLogoInverted": globalSettings.BRAND_LOGO_INVERT})

def career(request):
    return render(request,"career.html" , {"home" : False , "brandLogo" : globalSettings.BRAND_LOGO , "brandLogoInverted": globalSettings.BRAND_LOGO_INVERT})

def policy(request):
    return render(request,"policy.html" , {"home" : False , "brandName" : globalSettings.BRAND_NAME , "site" : globalSettings.SITE_ADDRESS , "brandLogo" : globalSettings.BRAND_LOGO , "brandLogoInverted": globalSettings.BRAND_LOGO_INVERT})

def terms(request):
    return render(request,"terms.html" , {"home" : False , "brandName" : globalSettings.BRAND_NAME  , "brandLogo" : globalSettings.BRAND_LOGO , "brandLogoInverted": globalSettings.BRAND_LOGO_INVERT})

def refund(request):
    return render(request,"refund.html" , {"home" : False , "brandName" : globalSettings.BRAND_NAME , "brandLogo" : globalSettings.BRAND_LOGO , "brandLogoInverted": globalSettings.BRAND_LOGO_INVERT})

def contacts(request):
    return render(request,"contacts.html" , {"home" : False , "brandLogo" : globalSettings.BRAND_LOGO , "brandLogoInverted": globalSettings.BRAND_LOGO_INVERT})


def registration(request):
    return render(request,"registration.html" , {"home" : False , "brandLogo" : globalSettings.BRAND_LOGO , "brandLogoInverted": globalSettings.BRAND_LOGO_INVERT})
def book(request):
    url=''
    if request.GET:
       url = str(request.GET['doc'])
       # printurl
    return render(request ,'book.html', {"home" : False , "brandLogo" : globalSettings.BRAND_LOGO , "brandLogoInverted": globalSettings.BRAND_LOGO_INVERT , "bookurl": url})


class scheduleViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny , )
    queryset = Schedule.objects.all()
    serializer_class = sheduleSerializer
    # filter_fields = ['name','vendor']
    # search_fields = ('name','web')

from ics import Calendar, Event
from datetime import date
from email.MIMEBase import MIMEBase
from datetime import datetime
import time
import datetime
from dateutil import parser

# pagesList
from os import listdir

def list_files(directory, extension):
    return (f for f in listdir(directory) if f.endswith('.' + extension))

class InvitationMailApi(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny , )
    def post(self, request, format=None):
        emailid=[]
        cc = ['ankita.k@cioc.in']
        # print request.data,'aaaaaaaaaa'
        schedule =  Schedule.objects.get(pk = request.data['value'])
        time = schedule.slot.split(' - ')
        strttime = int(time[0])
        endtime = int(time[1])
        newDate =  datetime.datetime.strptime(str(schedule.dated), '%Y-%m-%d').strftime('%Y%m%d %H:%M:%S')
        yourDate = parser.parse(newDate)

        begindate = yourDate.replace(hour=strttime, minute=00)
        enddate = yourDate.replace(hour=endtime, minute=00)
        emailid.append(schedule.emailId)
        email_subject ="Meeting as per your request"
        c = Calendar()
        e = Event()
        e.name = "Meeting"
        e.begin = begindate
        e.end = enddate
        e.organizer = 'ankita.k@cioc.in'
        c.events.add(e)
        c.attendee =  schedule.emailId
        with open('my.ics', 'w') as f:
             f.writelines(c)
        ctx = {
            # 'message': msgBody,
            'dated': schedule.dated,
            'slot' :  schedule.slot,
            'linkUrl': 'cioc.co.in',
            'linkText' : 'View Online',
            'sendersAddress' : '(C) CIOC FMCG Pvt Ltd',
            'sendersPhone' : '841101',
            'linkedinUrl' : 'https://www.linkedin.com/company/13440221/',
            'fbUrl' : 'facebook.com',
            'twitterUrl' : 'twitter.com',
        }

        icspart = MIMEBase('text', 'calendar', **{'method' : 'REQUEST', 'name' : 'my.ics'})
        icspart.set_payload( open("my.ics","rb").read() )
        icspart.add_header('Content-Transfer-Encoding', '8bit')
        icspart.add_header('Content-class', 'urn:content-classes:calendarmessage')
        email_body = get_template('app.homepage.inviteemail.html').render(ctx)
        msg = EmailMessage(email_subject, email_body,  to= emailid, cc= cc )
        msg.attach(icspart)
        msg.content_subtype = 'html'
        msg.send()

        return Response({}, status = status.HTTP_200_OK)

class MediaViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MediaSerializer
    queryset = Media.objects.all()


class ProductTemplateViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ProductTemplateSerializer
    queryset = ProductTemplate.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name','parent_name']
    def get_queryset(self):
        # printself.request.GET,'jjjj'
        if 'query' in self.request.GET:
            search =  self.request.GET['query']
            limit =  self.request.GET['limit']
            return  ProductTemplate.objects.filter(Q(name__icontains = search)|Q(parent_name__icontains=search))[:limit]

        return ProductTemplate.objects.all()


class ProductFieldViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ProductFieldSerializer
    queryset = ProductField.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['template']

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['template','itemNumber']

class ProductValueMapViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ProductValueMapSerializer
    queryset = ProductValueMap.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['product']

class PdfDescriptionViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = PdfDescriptionSerializer
    queryset = PdfDescription.objects.all()
    filter_backends = [DjangoFilterBackend]

class PdfDescriptionViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = PdfDescriptionSerializer
    queryset = PdfDescription.objects.all()
    filter_backends = [DjangoFilterBackend]

class PdfDescriptionViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = PdfDescriptionSerializer
    queryset = PdfDescription.objects.all()
    filter_backends = [DjangoFilterBackend]

class CareersFieldViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = CareerFieldSerializer
    queryset = CareerField.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name','status']


class ApplySerializer(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ApplySerializer
    queryset = Apply.objects.all()
    filter_backends = [DjangoFilterBackend]

class ApptipsViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ApptipsSerializer
    queryset = Apptips.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['tipname','heading']
    def get_queryset(self):
        # printself.request.GET,'jjjjjjjjjjjjjj'
        if 'query_data' in self.request.GET:
            search =  self.request.GET['query_data']
            limit =  self.request.GET['limit']
            return  Apptips.objects.filter(Q(heading= None)|Q(tipname__icontains=search))[:limit]
        elif 'filter_data' in self.request.GET:
            # print'hhhhhhhhhhhhhhhh'
            return  Apptips.objects.filter(heading= None)
        else:
            return Apptips.objects.all()


class LocationsViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LocationsSerializer
    queryset = Locations.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name',]




class ContactApi(APIView):
    renderer_classes = (JSONRenderer,)
    def post(self, request, format=None):
        ctx = {
            'fname':request.data['fname'],
            'lname':request.data['lname'],
            'mobile':request.data['mobile'],
            'country':request.data['country'],
            'email':request.data['email'],
            'company':request.data['company'],
            'breif':request.data['breif'],
        }
        email_body = get_template('app.homepage.contactEmail.html').render(ctx)
        email_subject = 'Contact Email'
        email_to = []
        if globalSettings.G_ADMIN:
            for i in globalSettings.G_ADMIN:
                email_to.append(str(i))
        # print email_to,'emaillllllllllllll'
        msg = EmailMessage(email_subject, email_body, to=email_to ,  )
        msg.content_subtype = 'html'
        msg.send()
        return Response({}, status = status.HTTP_200_OK)



import os
class BroucherApi(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny , )

    def get(self, request, format=None):
        id = request.GET['val']
        prodtempObj = ProductTemplate.objects.get(pk=id)

        langs = ['en','de','zh']
        try:
            for lang in langs:
                name = prodtempObj.name +'_'+str(id)+'_'+lang
                f = open(os.path.join(globalSettings.BASE_DIR, 'media_root/%s.pdf'%(name)), 'w')
                os.unlink(f.name)
        except:
            pass

        for lang in langs:
            name = prodtempObj.name +'_'+str(id)+'_'+lang
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="%s.pdf"' %(name)

            pdfCode(request,response,prodtempObj,lang)
            # elevatorCode(request,response,prodtempObj)

            f = open(os.path.join(globalSettings.BASE_DIR, 'media_root/%s.pdf'%(name)), 'wb')
            f.write(response.content)
            f.close()

        if 'saveOnly' in request.GET:
            return Response(status=status.HTTP_200_OK)
        return response


class GenerateBroucherApi(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny , )

    def get(self, request, format=None):
        # prodtempObj = ProductTemplate.objects.get(pk=request.GET['val'])
        langs = ['en','de','zh']
        try:
            for i in langs:
                f = open(os.path.join(globalSettings.BASE_DIR, 'media_root/broucher_%s.pdf'%(i)), 'w')
                os.unlink(f.name)

        except:
            pass

        productTemplatesObjects = ProductTemplate.objects.all()
        templatesTractionRopes = productTemplatesObjects.filter(parent_name = 'traction-ropes')
        templatesTractionRopes2 = list(productTemplatesObjects.filter(parent_name = 'traction-ropes'))
        templateCompensationRopes = list(productTemplatesObjects.filter(parent_name = 'compensation-ropes'))
        templatesGovernorRopes = list(productTemplatesObjects.filter(parent_name = 'governor-ropes'))
        templatesInnovation = productTemplatesObjects.filter(parent_name = 'innovation')

        totalNumberOFTempletes = len(productTemplatesObjects) - len(templatesInnovation)

        templatesTractionRopes2.extend(templateCompensationRopes)
        templatesTractionRopes2.extend(templatesGovernorRopes)

        accessoriesCat = Accessories.objects.all()

        for lang in langs:
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="broucher_%s.pdf"'%(lang)
            styles=getSampleStyleSheet()
            stylesN = styles['Normal']
            stylesH =styles['Heading1']
            width,height = A4
            c = Canvas(response,pagesize=A4)
            elevatorCode1(request,response,styles,stylesN,stylesH,width,height,c, lang,templatesTractionRopes2,accessoriesCat,productTemplatesObjects)
            f = open(os.path.join(globalSettings.BASE_DIR, 'media_root/broucher_%s.pdf'%(lang)), 'wb')
            f.write(response.content)
            f.close()
        if 'saveOnly' in request.GET:
            return Response(status=status.HTTP_200_OK)
        return response

class CtpBroucherApi(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny , )

    def get(self, request, format=None):
        # prodtempObj = ProductTemplate.objects.get(pk=request.GET['val'])
        ctpObj = ProductTemplate.objects.filter(parent_name = "innovation")
        # printctpObj, 'llllllllllllllllllllllllllllllllllll'
        langs = ['en','zh','de']
        try:
            for lang in langs:
                f = open(os.path.join(globalSettings.BASE_DIR, 'media_root/CTP_%s.pdf'%(lang)), 'w')
                os.unlink(f.name)
        except:
            pass
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="CTP.pdf"'
        for lang in langs:
            styles=getSampleStyleSheet()
            stylesN = styles['Normal']
            stylesH =styles['Heading1']
            width,height = A4
            c = Canvas(response,pagesize=A4)
            ctpCode(request,response,ctpObj,styles,stylesN,stylesH,width,height,c,lang)
            f = open(os.path.join(globalSettings.BASE_DIR, 'media_root/CTP_%s.pdf'%(lang)), 'wb')
            f.write(response.content)
            f.close()
        if 'saveOnly' in request.GET:
            return Response(status=status.HTTP_200_OK)
        return response



class SubmitAPIView(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny , )
    def post(self, request, format=None):
        # printrequest.data
        newmsg= request.data['email']
        # # printnewmsg
        email_subject = 'subject'
        msgBody= 'Hello how are you ?'
        varlist = []
        varlist.append(newmsg)
        msg = EmailMessage(email_subject, msgBody, to=varlist)
        msg.send()
        return Response({}, status = status.HTTP_200_OK)


import html2text
import sys
from reportlab.pdfbase.pdfmetrics import stringWidth
from bs4 import SoupStrainer

def addBRInRichText(text):
    test = BeautifulSoup(text, 'html.parser')
    only_new_tags = SoupStrainer("p")
    test =  test.find_all(only_new_tags)
    # printtest, "html to text"
    respone = ''
    for i in test:
        respone += str(i)+'<br/>'
    return respone

def MultiParagraph(data,c,colWidths,width1,height1,style):
    width, height = A4
    data = SafeString(xhtml2rml(data,paraStyle="normal")).replace('<para style="normal">','<para>')
    test = BeautifulSoup(data, 'html.parser')
    only_new_tags = SoupStrainer("para")
    test =  test.find_all(only_new_tags)
    # printtest, "html to text"
    for i in test:
        # printi, "paraprarar"
        name = Paragraph(str(i),style)
        tab = [[name]]
        pr = Table(tab,colWidths=colWidths)
        w1,h1 = pr.wrapOn(c, width,height)
        # printh1 , 'height'
        height1 = height1-h1
        pr.drawOn(c, width1, height1)
    return height1


def htmlRMLCanvvas(data,c,colWidths,width1,height1,style,color,lang, fontSize=10):
    try:
        data = SafeString(xhtml2rml(data)).replace('<para style="normal">','<para>').replace('\n','<br/>')
    except Exception as e:
        data = '<para>Please Enter Paragraph<br/> or list item only</para>'

    width, height = A4
    test = BeautifulSoup(data, 'html.parser')
    only_ul_tags = SoupStrainer("ul")
    only_para_tags = SoupStrainer("para")
    contents =  test.contents
    if lang == 'zh':
        style = ParagraphStyle(             'small',
                                            parent=style,
                                            textColor = color,
                                            fontName = 'STSong-Light',
                                            fontSize = fontSize,
                                            )
    else:
        style = ParagraphStyle( 'small',
                                parent=style,
                                textColor = color,
                                fontSize = fontSize,
                                )
    for content in contents:
        # printcontent, "content content"
        if content.name == 'ul':
            ListItems = []
            test =  content.find_all(only_para_tags)
            for para in test:
                # printpara
                item = Paragraph(str(para), style)
                # printitem
                ListItems.append(item)
            name = ListFlowable(ListItems, bulletType='bullet', start='circle',bulletFontSize = 5,bulletIndent = 0,bulletOffsetY = -3,leftIndent = 7)
            tab = [[name]]
            pr = Table(tab,colWidths=colWidths)
            w1,h1 = pr.wrapOn(c, width,height)
            # printh1 , 'height'
            height1 = height1-h1
            pr.drawOn(c, width1, height1)

        elif content.name == 'para':
            name = Paragraph(str(content),style)
            tab = [[name]]
            pr = Table(tab,colWidths=colWidths)
            w1,h1 = pr.wrapOn(c, width,height)
            # printh1 , 'height'
            height1 = height1-h1
            pr.drawOn(c, width1, height1)

        else:
            print content, "content"
            pass
    return height1

def addPage(c,data, prodtempObj,bg, product,styles,lang):

    if lang == 'en' or lang == 'de':
        width,height = A4
        c.drawImage(bg,0,0,width=width,height=height,mask=None)
        # c.drawImage(product,1.2*inch,6*inch,width=1.4*inch,height=1.4*inch,mask='auto')

        name = Paragraph('<para fontName = FrutigerB fontSize=13>%s</para>'%(prodtempObj.name + ' - '+prodtempObj.des_de), styles['Normal'])
        nd =[[name]]
        ndt = Table(nd)
        w,h = ndt.wrapOn(c, width,height)
        ndt.drawOn(c, 0.35*inch,height-h-15)
        name = Paragraph('<para fontName = FrutigerB fontSize=13>%s</para>'%(prodtempObj.name + ' - '+prodtempObj.description), styles['Normal'])
        nd =[[name]]
        ndt = Table(nd)
        w,h2 = ndt.wrapOn(c, width,height)
        ndt.drawOn(c, 0.35*inch,height-h2-h-15)

        _color = rangeColors(prodtempObj.color)
        c.setFillColor(_color.hex)
        c.setStrokeColor(colors.white)
        c.rect(4*inch,9.5*inch,0.6*inch,0.6*inch, fill=1)
        c.setFont("Helvetica-Bold", 7)
        c.setFillColor(colors.black)
        k = json.loads(prodtempObj.keyword1)
        k11 =[[k]]
        r11 = Table(k11,colWidths=3.6*inch,rowHeights=4*mm)
        c.setFont("Helvetica", 5)

        para101 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%(k["value1"]), styles['Normal'])
        desc101 = [[para101]]
        r101 = Table(desc101,colWidths=0.6*inch,rowHeights=1*mm)
        r101.wrapOn(c, width,height)
        r101.drawOn(c, 4*inch, 9.69*inch)

        para102 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%("N/mm2"), styles['Normal'])
        desc102 = [[para102]]
        r102 = Table(desc102,colWidths=0.6*inch,rowHeights=1*mm)
        r102.wrapOn(c, width,height)
        r102.drawOn(c, 4*inch, 9.49*inch)

        para103 = Paragraph('<para align="center" fontName = FrutigerR fontSize=7 >%s</para>'%("E-Module"), styles['Normal'])
        desc103 = [[para103]]
        r103 = Table(desc103,colWidths=0.6*inch,rowHeights=1*mm)
        r103.wrapOn(c, width,height)
        r103.drawOn(c, 4*inch, 9.15*inch)


        _color = rangeColors(prodtempObj.color,luminance=.5)
        c.setFillColor(_color.hex)
        c.rect(5*inch,9.5*inch,0.6*inch,0.6*inch, fill=1)
        c.setFont("Helvetica-Bold", 7)
        c.setFillColor(colors.black)
        k1 = json.loads(prodtempObj.keyword2)

        k12 =[[k1]]

        r12 = Table(k12,colWidths=5*inch,rowHeights=10*mm)

        para201 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%(k1["value1"]), styles['Normal'])
        desc201 = [[para201]]
        r201 = Table(desc201,colWidths=0.6*inch,rowHeights=1*mm)
        r201.wrapOn(c, width,height)
        r201.drawOn(c, 5*inch, 9.69*inch)

        para202 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%("%"), styles['Normal'])
        desc202 = [[para202]]
        r202 = Table(desc202,colWidths=0.6*inch,rowHeights=1*mm)
        r202.wrapOn(c, width,height)
        r202.drawOn(c, 5*inch, 9.49*inch)

        para203 = Paragraph('<para align="center" fontName = FrutigerR fontSize=7 >%s</para>'%("Elastic<br/>Elongation"), styles['Normal'])
        desc203 = [[para203]]
        r203 = Table(desc203,colWidths=0.65*inch,rowHeights=1*mm)
        r203.wrapOn(c, width,height)
        r203.drawOn(c, 5*inch, 647 )


        _color = rangeColors(prodtempObj.color,luminance=.7)
        c.setFillColor(_color.hex)
        c.setStrokeColor(colors.white)

        c.rect(6*inch,9.5*inch,0.6*inch,0.6*inch, fill=1)
        c.setFont("Helvetica-Bold", 7)
        c.setFillColor(colors.black)
        k2 = json.loads(prodtempObj.keyword3)

        k13 = [[k2]]

        r13 = Table(k13,colWidths=5*inch,rowHeights=10*mm)

        para301 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%(k2["value1"]), styles['Normal'])
        desc301 = [[para301]]
        r301 = Table(desc301,colWidths=0.6*inch,rowHeights=1*mm)
        r301.wrapOn(c, width,height)
        r301.drawOn(c, 6*inch, 9.69*inch)

        para302 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%("%"), styles['Normal'])
        desc302 = [[para302]]
        r302 = Table(desc302,colWidths=0.6*inch,rowHeights=1*mm)
        r302.wrapOn(c, width,height)
        r302.drawOn(c, 6*inch, 9.49*inch)

        para303 = Paragraph('<para align="center" fontName = FrutigerR fontSize=7 >%s</para>'%("Permanent<br/>Elongation"), styles['Normal'])
        desc303 = [[para303]]
        r303 = Table(desc303,colWidths=0.7*inch,rowHeights=1*mm)
        r303.wrapOn(c, width,height)
        r303.drawOn(c, 6*inch, 9*inch)


        _color = rangeColors(prodtempObj.color,luminance=.9)
        c.setFillColor(_color.hex)
        c.setStrokeColor(colors.white)
        c.rect(7*inch,9.5*inch,0.6*inch,0.6*inch, fill=1)
        c.setFont("Helvetica-Bold", 7)
        c.setFillColor(colors.black)
        k3 = json.loads(prodtempObj.keyword4)
        k14 = [[k3]]
        r14 = Table(k14,colWidths=5*inch,rowHeights=10*mm)

        para401 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%(k3["value1"]), styles['Normal'])
        desc401 = [[para401]]
        r401 = Table(desc401,colWidths=0.6*inch,rowHeights=1*mm)
        r401.wrapOn(c, width,height)
        r401.drawOn(c, 7*inch, 9.69*inch)

        para402 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%("m"), styles['Normal'])
        desc402 = [[para402]]
        r402 = Table(desc402,colWidths=0.6*inch,rowHeights=1*mm)
        r402.wrapOn(c, width,height)
        r402.drawOn(c, 7*inch, 9.49*inch)

        para403 = Paragraph('<para align="center" fontName = FrutigerR fontSize=7 >%s</para>'%("Lifting<br/>Height"), styles['Normal'])
        desc403 = [[para403]]
        r403 = Table(desc403,colWidths=0.6*inch,rowHeights=1*mm)
        r403.wrapOn(c, width,height)
        r403.drawOn(c, 7*inch, 9*inch)

        height2 = height - 100
        height2 = htmlRMLCanvvas(prodtempObj.rteData2_otl,c,3.2*inch,0.35*inch,height2,styles['Normal'],colors.black,lang)
        height2 = height2 -50
        height2 = htmlRMLCanvvas(prodtempObj.rteData2_en,c,3.2*inch,0.35*inch,height2,styles['Normal'],colors.black,lang='en')

        # para3 = addBRInRichText(prodtempObj.rteData2_otl)
        # para2 = Paragraph('%s'%(para3), styles['Normal'])
        # tab = [[para2]]
        # r = Table(tab,colWidths=3.5*inch)
        # w,h1 = r.wrapOn(c, width,height)
        # height2 = height - h1 - 100
        # # printheight2, h1, "first text height"
        # r.drawOn(c, 0.35*inch, height2)
        # para4 = addBRInRichText(prodtempObj.rteData2_en)
        # para22 = Paragraph('%s'%(para4), styles['Normal'])
        # tab = [[para22]]
        # s = Table(tab,colWidths=3.5*inch)
        # w,h2 = s.wrapOn(c, width,height)
        # height2 = height2 - h2 - 50
        # # printheight2, h2, "second text height"
        # s.drawOn(c, 0.35*inch, height2)
        height2 = height2 - 150
        c.drawImage(product,1.2*inch,height2,width=1.4*inch,height=1.4*inch,mask='auto')


        t5 = Table(data)
        t5.setStyle(TableStyle([
                             ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                             ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                             ('FONTSIZE', (0, 0), (-1, -1), 7),
                             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                             ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                             ('BACKGROUND', (1,0), (-5,-1), '#DCDCDC'),
                             ]))
        w, h = t5.wrapOn(c, width, height)
        # printheight , h,w, "heighttttt"
        height3 = height-h-250
        t5.drawOn(c, 240,height3 )


        # printprodtempObj.disclaimer_otl, prodtempObj.disclaimer_en, "asdasdasa"
        test = prodtempObj.disclaimer_otl + "<br/>"+ prodtempObj.disclaimer_en
        # # printtest , "testsat"
        para2 = Paragraph('<para fontName = Helvetica fontSize=6 >%s</para>'%(test), styles['Normal'])
        tab = [[para2]]
        r = Table(tab,colWidths=3.25*inch)
        w,h1 = r.wrapOn(c, width,height)
        height3 = height3 - h1
        r.drawOn(c, 240, height3)


        # height3 = htmlRMLCanvvas(test,c,4.5*inch,265,height3,styles['Normal'],colors.black,lang,fontSize = 7)

        # height3 = htmlRMLCanvvas(prodtempObj.rteData2_en,c,4.5*inch,265,height3,styles['Normal'],colors.black,lang='en',fontSize = 7)

        textobject = c.beginText()
        textobject.setTextOrigin(0.3*inch, 1.3*inch)
        textobject.setFont("Helvetica", 7)
        c.setFillColorRGB(255,255,255)
        textobject.textLines('''
                        Ein Unternehemen der Gruppe BRUGG''')
        c.drawText(textobject)


        textobject = c.beginText()
        textobject.setTextOrigin(0.3*inch, 1.15*inch)
        textobject.setFont("Helvetica", 7)
        c.setFillColorRGB(0,0,0)
        textobject.textLines('''
                        A company of the BRUGG Group''')
        c.drawText(textobject)


        textobject = c.beginText()
        textobject.setTextOrigin(0.3*inch, 0.6*inch)
        textobject.setFont("Helvetica", 7)
        c.setFillColorRGB(255,255,255)
        textobject.textLines('''
                        Anderungen vorbehalten. Massangaben unverbindlich.
                        Keine Gewahrleistung fur Druckfehler oder irrtumer.''')
        c.drawText(textobject)

        textobject = c.beginText()
        textobject.setTextOrigin(0.3*inch, 0.35*inch)
        textobject.setFont("Helvetica", 7)
        c.setFillColorRGB(0,0,0)
        textobject.textLines('''Subject to changes.Nonbinding indication of measures.
                            No warranty for printing errors of errors.''')
        c.drawText(textobject)

        textobject = c.beginText()
        textobject.setTextOrigin(5.9*inch, 0.4*inch)
        textobject.moveCursor(14,14)
        textobject.setFont("Helvetica", 15)
        textobject.setFillColor(colors.white)
        textobject.textLines('''
        www.brugglifting.com''')
        c.drawText(textobject)
        c.showPage()



    elif lang == 'zh':
        width,height = A4
        c.drawImage(bg,0,0,width=width,height=height,mask=None)
        # c.drawImage(product,1.2*inch,6*inch,width=1.4*inch,height=1.4*inch,mask='auto')

        name = Paragraph('<para fontName = STSong-Light fontSize=13>%s</para>'%(prodtempObj.name + ' - '+prodtempObj.des_ch), styles['Normal'])
        nd =[[name]]
        ndt = Table(nd)
        w,h = ndt.wrapOn(c, width,height)
        ndt.drawOn(c, 0.35*inch,height-h-15)
        name = Paragraph('<para fontName = FrutigerB fontSize=13>%s</para>'%(prodtempObj.name + ' - '+prodtempObj.description), styles['Normal'])
        nd =[[name]]
        ndt = Table(nd)
        w,h2 = ndt.wrapOn(c, width,height)
        ndt.drawOn(c, 0.35*inch,height-h2-h-15)


        _color = rangeColors(prodtempObj.color)
        c.setFillColor(_color.hex)
        c.setStrokeColor(colors.white)
        c.rect(4*inch,9.5*inch,0.6*inch,0.6*inch, fill=1)
        c.setFont("Helvetica-Bold", 7)
        c.setFillColor(colors.black)
        k = json.loads(prodtempObj.keyword1)
        k11 =[[k]]
        r11 = Table(k11,colWidths=3.6*inch,rowHeights=4*mm)
        c.setFont("Helvetica", 5)

        para101 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%(k["value1"]), styles['Normal'])
        desc101 = [[para101]]
        r101 = Table(desc101,colWidths=0.6*inch,rowHeights=1*mm)
        r101.wrapOn(c, width,height)
        r101.drawOn(c, 4*inch, 9.69*inch)

        para102 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%("N/mm2"), styles['Normal'])
        desc102 = [[para102]]
        r102 = Table(desc102,colWidths=0.6*inch,rowHeights=1*mm)
        r102.wrapOn(c, width,height)
        r102.drawOn(c, 4*inch, 9.49*inch)

        para103 = Paragraph('<para align="center" fontName = FrutigerR fontSize=7 >%s</para>'%("E-Module"), styles['Normal'])
        desc103 = [[para103]]
        r103 = Table(desc103,colWidths=0.6*inch,rowHeights=1*mm)
        r103.wrapOn(c, width,height)
        r103.drawOn(c, 4*inch, 9.15*inch)


        _color = rangeColors(prodtempObj.color,luminance=.5)
        c.setFillColor(_color.hex)
        c.rect(5*inch,9.5*inch,0.6*inch,0.6*inch, fill=1)
        c.setFont("Helvetica-Bold", 7)
        c.setFillColor(colors.black)
        k1 = json.loads(prodtempObj.keyword2)

        k12 =[[k1]]

        r12 = Table(k12,colWidths=5*inch,rowHeights=10*mm)

        para201 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%(k1["value1"]), styles['Normal'])
        desc201 = [[para201]]
        r201 = Table(desc201,colWidths=0.6*inch,rowHeights=1*mm)
        r201.wrapOn(c, width,height)
        r201.drawOn(c, 5*inch, 9.69*inch)

        para202 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%("%"), styles['Normal'])
        desc202 = [[para202]]
        r202 = Table(desc202,colWidths=0.6*inch,rowHeights=1*mm)
        r202.wrapOn(c, width,height)
        r202.drawOn(c, 5*inch, 9.49*inch)

        para203 = Paragraph('<para align="center" fontName = FrutigerR fontSize=7 >%s</para>'%("Elastic<br/>Elongation"), styles['Normal'])
        desc203 = [[para203]]
        r203 = Table(desc203,colWidths=0.65*inch,rowHeights=1*mm)
        r203.wrapOn(c, width,height)
        r203.drawOn(c, 5*inch, 647 )


        _color = rangeColors(prodtempObj.color,luminance=.7)
        c.setFillColor(_color.hex)
        c.setStrokeColor(colors.white)

        c.rect(6*inch,9.5*inch,0.6*inch,0.6*inch, fill=1)
        c.setFont("Helvetica-Bold", 7)
        c.setFillColor(colors.black)
        k2 = json.loads(prodtempObj.keyword3)

        k13 = [[k2]]

        r13 = Table(k13,colWidths=5*inch,rowHeights=10*mm)

        para301 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%(k2["value1"]), styles['Normal'])
        desc301 = [[para301]]
        r301 = Table(desc301,colWidths=0.6*inch,rowHeights=1*mm)
        r301.wrapOn(c, width,height)
        r301.drawOn(c, 6*inch, 9.69*inch)

        para302 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%("%"), styles['Normal'])
        desc302 = [[para302]]
        r302 = Table(desc302,colWidths=0.6*inch,rowHeights=1*mm)
        r302.wrapOn(c, width,height)
        r302.drawOn(c, 6*inch, 9.49*inch)

        para303 = Paragraph('<para align="center" fontName = FrutigerR fontSize=7 >%s</para>'%("Permanent<br/>Elongation"), styles['Normal'])
        desc303 = [[para303]]
        r303 = Table(desc303,colWidths=0.7*inch,rowHeights=1*mm)
        r303.wrapOn(c, width,height)
        r303.drawOn(c, 6*inch, 9*inch)


        _color = rangeColors(prodtempObj.color,luminance=.9)
        c.setFillColor(_color.hex)
        c.setStrokeColor(colors.white)
        c.rect(7*inch,9.5*inch,0.6*inch,0.6*inch, fill=1)
        c.setFont("Helvetica-Bold", 7)
        c.setFillColor(colors.black)
        k3 = json.loads(prodtempObj.keyword4)
        k14 = [[k3]]
        r14 = Table(k14,colWidths=5*inch,rowHeights=10*mm)

        para401 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%(k3["value1"]), styles['Normal'])
        desc401 = [[para401]]
        r401 = Table(desc401,colWidths=0.6*inch,rowHeights=1*mm)
        r401.wrapOn(c, width,height)
        r401.drawOn(c, 7*inch, 9.69*inch)

        para402 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%("m"), styles['Normal'])
        desc402 = [[para402]]
        r402 = Table(desc402,colWidths=0.6*inch,rowHeights=1*mm)
        r402.wrapOn(c, width,height)
        r402.drawOn(c, 7*inch, 9.49*inch)

        para403 = Paragraph('<para align="center" fontName = FrutigerR fontSize=7 >%s</para>'%("Lifting<br/>Height"), styles['Normal'])
        desc403 = [[para403]]
        r403 = Table(desc403,colWidths=0.6*inch,rowHeights=1*mm)
        r403.wrapOn(c, width,height)
        r403.drawOn(c, 7*inch, 9*inch)

        # para3 = addBRInRichText(prodtempObj.rteData2_ch)
        # para2 = Paragraph('%s'%(para3), styles['Normal'])
        # tab = [[para2]]
        # r = Table(tab,colWidths=3.5*inch)
        # w,h1 = r.wrapOn(c, width,height)
        # height2 = height - h1 - 100
        # # printheight2, h1, "first text height"
        # r.drawOn(c, 0.35*inch, height2)

        height2 = height - 100
        height2 = htmlRMLCanvvas(prodtempObj.rteData2_ch,c,3.2*inch,0.35*inch,height2,styles['Normal'],colors.black,lang)
        height2 = height2 -50
        height2 = htmlRMLCanvvas(prodtempObj.rteData2_en,c,3.2*inch,0.35*inch,height2,styles['Normal'],colors.black,lang='en')
        # para4 = addBRInRichText(prodtempObj.rteData2_en)
        # para22 = Paragraph('%s'%(para4), styles['Normal'])
        # tab = [[para22]]
        # s = Table(tab,colWidths=3.5*inch)
        # w,h2 = s.wrapOn(c, width,height)
        # height2 = height2 - h2 - 50
        # # printheight2, h2, "second text height"
        # s.drawOn(c, 0.35*inch, height2)
        height2 = height2 - 150
        c.drawImage(product,1.2*inch,height2,width=1.4*inch,height=1.4*inch,mask='auto')


        t5 = Table(data)
        t5.setStyle(TableStyle([
                             ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                             ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                             ('FONTSIZE', (0, 0), (-1, -1), 7),
                             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                             ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                             ('BACKGROUND', (1,0), (-5,-1), '#DCDCDC'),
                             ]))
        w, h = t5.wrapOn(c, width, height)
        # printheight , h,w, "heighttttt"
        height3 = height-h-250
        t5.drawOn(c, 240,height3 )


        # printprodtempObj.disclaimer_otl, prodtempObj.disclaimer_en, "asdasdasa"
        test = prodtempObj.disclaimer_ch + "<br/>"+ prodtempObj.disclaimer_en
        # printtest , "testsat"
        para2 = Paragraph('<para fontName = STSong-Light fontSize=6 >%s</para>'%(test), styles['Normal'])
        tab = [[para2]]
        r = Table(tab,colWidths=3.25*inch)
        w,h1 = r.wrapOn(c, width,height)
        height3 = height3 - h1
        r.drawOn(c, 240, height3)

        # height3 = htmlRMLCanvvas(prodtempObj.disclaimer_ch,c,3.5*inch,265,height3,styles['Normal'],colors.black,lang)
        #
        # height3 = htmlRMLCanvvas(prodtempObj.rteData2_en,c,3.5*inch,265,height3,styles['Normal'],colors.black,lang='en')

        textobject = c.beginText()
        textobject.setTextOrigin(0.3*inch, 1.3*inch)
        textobject.setFont("Helvetica", 7)
        c.setFillColorRGB(255,255,255)
        textobject.textLines('''
                        Ein Unternehemen der Gruppe BRUGG''')
        c.drawText(textobject)


        textobject = c.beginText()
        textobject.setTextOrigin(0.3*inch, 1.15*inch)
        textobject.setFont("Helvetica", 7)
        c.setFillColorRGB(0,0,0)
        textobject.textLines('''
                        A company of the BRUGG Group''')
        c.drawText(textobject)


        textobject = c.beginText()
        textobject.setTextOrigin(0.3*inch, 0.6*inch)
        textobject.setFont("Helvetica", 7)
        c.setFillColorRGB(255,255,255)
        textobject.textLines('''
                        Anderungen vorbehalten. Massangaben unverbindlich.
                        Keine Gewahrleistung fur Druckfehler oder irrtumer.''')
        c.drawText(textobject)

        textobject = c.beginText()
        textobject.setTextOrigin(0.3*inch, 0.35*inch)
        textobject.setFont("Helvetica", 7)
        c.setFillColorRGB(0,0,0)
        textobject.textLines('''Subject to changes.Nonbinding indication of measures.
                            No warranty for printing errors of errors.''')
        c.drawText(textobject)

        textobject = c.beginText()
        textobject.setTextOrigin(5.9*inch, 0.4*inch)
        textobject.moveCursor(14,14)
        textobject.setFont("Helvetica", 15)
        textobject.setFillColor(colors.white)
        textobject.textLines('''
        www.brugglifting.com''')
        c.drawText(textobject)
        c.showPage()


def pdfCode(request,response,prodtempObj,lang):
    folder = os.path.dirname(reportlab.__file__) + os.sep + 'fonts'
    print folder , 'registerFont'
    if lang =='en' or lang == 'de':
        prodfield = ProductField.objects.filter(template = prodtempObj.pk)

        prod = Product.objects.filter(template = prodtempObj.pk)

        styles=getSampleStyleSheet()
        stylesN = styles['Normal']
        stylesH =styles['Heading1']
        width,height = A4
        c = Canvas(response,pagesize=A4)
        c.setTitle("Brugglifting_%s"%prodtempObj.name)
        logo = os.path.join(globalSettings.BASE_DIR , 'static_shared/images',"brugglifting.svg")
        if prodtempObj.backgroundImage1:
            logo1 = prodtempObj.backgroundImage1.path
        else:
            logo1 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images',"brugg.jpg")
        # rope = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','ropetech.png')
        if prodtempObj.defaultImage:
            product = prodtempObj.defaultImage.path
        else:
            product = os.path.join(globalSettings.BASE_DIR , 'static_shared/images',"stars.jpeg")

        # bg = prodtempObj.backgroundImage2.path
        if prodtempObj.backgroundImage2:
            bg = prodtempObj.backgroundImage2.path
        else:
            bg = os.path.join(globalSettings.BASE_DIR , 'static_shared/images',"cables.jpg")


        c.drawImage(logo1,0,0,width=width, height= height,mask='auto')

        height2 = height - 150
        height2 = htmlRMLCanvvas(prodtempObj.rteData1_otl,c,4.5*inch,40,height2,stylesN,colors.white,lang)
        height2 = height2 -30


        # printprodtempObj.rteData1_en
        height2 = htmlRMLCanvvas(prodtempObj.rteData1_en,c,4.5*inch,40,height2,stylesN,colors.black,lang='en')

        # height2 = MultiParagraph(prodtempObj.rteData1_en,c,4.5*inch,40,height2,stylesN)
        w = pdfmetrics.stringWidth(prodtempObj.name, "FrutigerB", 54)

        name = Paragraph('<para fontName = FrutigerB fontSize=54>%s</para>'%(prodtempObj.name), styles['Normal'])
        nd =[[name]]
        ndt = Table(nd)
        w3, h3 = ndt.wrapOn(c, width,height)
        width2 = 40
        ndt.drawOn(c, width2,6.45*inch)

        name = Paragraph('<para fontName = FrutigerR fontSize=12.5>%s</para>'%(prodtempObj.des_de ), styles['Normal'])
        des =[[name]]
        dest = Table(des, colWidths = 8*cm)
        w4, h3 = dest.wrapOn(c, width,height)
        width2 = width2 + w + 10
        dest.drawOn(c, width2,460-h3)
        name = Paragraph('<para fontName = FrutigerR fontSize=12.5>%s</para>'%(prodtempObj.description), styles['Normal'])
        des =[[name]]
        dest = Table(des, colWidths = 8*cm)
        w4, h4 = dest.wrapOn(c, width,height)
        # width2 = width2 + w + 10
        dest.drawOn(c, width2,460-h3-h4)
        # name = Paragraph('<para fontName = FrutigerR fontSize=12.5>%s</para>'%(prodtempObj.description), styles['Normal'])
        # des =[[name]]
        # dest = Table(des, colWidths = 8*cm)
        # w4, h4 = dest.wrapOn(c, width,height)
        # width2 = width2 + w + 10
        # dest.drawOn(c, width2,420-h4-h3)
        c.showPage()

        data = []
        # data2 = []
        dataHeading = ['Item Number']
        dataHeading2 = ['']
        list1 = []
        list2 = []
        for j in prodfield:
            # printprodfield
            if j.inPdf ==True:

                # printj.name,'kkkkkkkkkkkkk'
                try:
                    name1, name2 = j.name.split('(')
                    # printname2[:-1]
                    name2 = ''+name2[:-1]
                    # printname2
                except:
                    name1 = j.name
                    name2 = ''

                # printname1, ' ' , name2

                list1.append(name1)
                list2.append(name2)
        for a in list1:
            dataHeading.append(a)
        for b in list2:
            dataHeading2.append(b)



        for i in prod:
            appendlist = [i.itemNumber]
            for j in prodfield:
                prodQty = ProductValueMap.objects.filter( field = j.pk,product = i.pk)
                for k in prodQty:
                    if j.inPdf ==True:
                        if j.type=='Char':
                            appendlist.append(k.char)
                        if j.type=='float':
                            appendlist.append(k.fValue)
                        if j.type=='Integer':
                            appendlist.append(k.iValue)
                        if j.type=='Boolean':
                            appendlist.append(k.bool)
            data.append(appendlist)
        dataLength =  len(data)
        # printlen(data), "data length"
        maxNumberItems = 20
        index = float(len(data))/maxNumberItems
        # printindex
        index = int(math.ceil(index))
        # printindex, range(index),"index ...."
        for i in range(index):
            if i == index:
                if dataLength>0:
                    data1 = data[maxNumberItems*i:-1]
                    data1.insert(0,dataHeading)
                    data1.insert(1,dataHeading2)
                else:
                    data1 = []
                # printlen(data1)
            else:
                data1 = data[maxNumberItems*i:maxNumberItems*(i+1)-1]
                data1.insert(0,dataHeading)
                data1.insert(1,dataHeading2)
                # printlen(data1)
            # printdata1, "datapass "
            addPage(c, data1, prodtempObj,bg, product,styles,lang)


        c.save()
        prodtempObj.pdfgenerated = True
        prodtempObj.save()


    elif lang =='zh':
        prodfield = ProductField.objects.filter(template = prodtempObj.pk)

        prod = Product.objects.filter(template = prodtempObj.pk)

        styles=getSampleStyleSheet()
        stylesN = styles['Normal']
        stylesH =styles['Heading1']
        width,height = A4
        c = Canvas(response,pagesize=A4)
        c.setTitle("Brugglifting_%s"%prodtempObj.name)
        logo = os.path.join(globalSettings.BASE_DIR , 'static_shared/images',"brugglifting.svg")
        if prodtempObj.backgroundImage1:
            logo1 = prodtempObj.backgroundImage1.path
        else:
            logo1 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images',"brugg.jpg")
        # rope = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','ropetech.png')
        if prodtempObj.defaultImage:
            product = prodtempObj.defaultImage.path
        else:
            product = os.path.join(globalSettings.BASE_DIR , 'static_shared/images',"stars.jpeg")

        # bg = prodtempObj.backgroundImage2.path
        if prodtempObj.backgroundImage2:
            bg = prodtempObj.backgroundImage2.path
        else:
            bg = os.path.join(globalSettings.BASE_DIR , 'static_shared/images',"cables.jpg")


        c.drawImage(logo1,0,0,width=width, height= height,mask='auto')

        height2 = height - 150
        height2 = htmlRMLCanvvas(prodtempObj.rteData1_ch,c,4.5*inch,40,height2,stylesN,colors.white,lang)
        height2 = height2 -30


        # printprodtempObj.rteData1_en
        height2 = htmlRMLCanvvas(prodtempObj.rteData1_en,c,4.5*inch,40,height2,stylesN,colors.black,lang='en')

        # height2 = MultiParagraph(prodtempObj.rteData1_en,c,4.5*inch,40,height2,stylesN)
        w = pdfmetrics.stringWidth(prodtempObj.name, "FrutigerB", 54)

        name = Paragraph('<para fontName = FrutigerB fontSize=54>%s</para>'%(prodtempObj.name), styles['Normal'])
        nd =[[name]]
        ndt = Table(nd)
        w3, h3 = ndt.wrapOn(c, width,height)
        width2 = 40
        ndt.drawOn(c, width2,6.45*inch)

        name = Paragraph('<para fontName = STSong-Light fontSize=12.5>%s</para>'%(prodtempObj.des_ch ), styles['Normal'])
        des =[[name]]
        dest = Table(des, colWidths = 8*cm)
        w4, h3 = dest.wrapOn(c, width,height)
        width2 = width2 + w + 10
        dest.drawOn(c, width2,460-h3)
        name = Paragraph('<para fontName = FrutigerR fontSize=12.5>%s</para>'%(prodtempObj.description), styles['Normal'])
        des =[[name]]
        dest = Table(des, colWidths = 8*cm)
        w4, h4 = dest.wrapOn(c, width,height)
        # width2 = width2 + w + 10
        dest.drawOn(c, width2,460-h3-h4)
        c.showPage()

        data = []
        # data2 = []
        dataHeading = ['Item Number']
        dataHeading2 = ['']
        list1 = []
        list2 = []
        for j in prodfield:
            # printprodfield
            if j.inPdf ==True:

                # printj.name,'kkkkkkkkkkkkk'
                try:
                    name1, name2 = j.name.split('(')
                    # printname2[:-1]
                    name2 = ''+name2[:-1]
                    # printname2
                except:
                    name1 = j.name
                    name2 = ''

                # printname1, ' ' , name2

                list1.append(name1)
                list2.append(name2)
        for a in list1:
            dataHeading.append(a)
        for b in list2:
            dataHeading2.append(b)



        for i in prod:
            appendlist = [i.itemNumber]
            for j in prodfield:
                prodQty = ProductValueMap.objects.filter( field = j.pk,product = i.pk)
                for k in prodQty:
                    if j.inPdf ==True:
                        if j.type=='Char':
                            appendlist.append(k.char)
                        if j.type=='float':
                            appendlist.append(k.fValue)
                        if j.type=='Integer':
                            appendlist.append(k.iValue)
                        if j.type=='Boolean':
                            appendlist.append(k.bool)
            data.append(appendlist)
        dataLength = len(data)
        # printlen(data), "data length"
        maxNumberItems = 20
        index = float(len(data))/maxNumberItems
        # printindex
        index = int(math.ceil(index))
        # printindex, range(index),"index ...."
        for i in range(index):
            if i == index:
                if dataLength>0:
                    data1 = data[maxNumberItems*i:-1]
                    data1.insert(0,dataHeading)
                    data1.insert(1,dataHeading2)
                else:
                    data1 = []
            else:
                data1 = data[maxNumberItems*i:maxNumberItems*(i+1)-1]
                data1.insert(0,dataHeading)
                data1.insert(1,dataHeading2)
                # printlen(data1)
            # printdata1, "datapass "
            addPage(c, data1, prodtempObj,bg, product,styles,lang)


        c.save()
        prodtempObj.pdfgenerated = True
        prodtempObj.save()


class AccessoriesViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = AccessoriesSerializer
    queryset = Accessories.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name']

class AccessoriesSectionViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = AccessoriesSectionSerializer
    queryset = AccessoriesSection.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['lang','accessories','basicProductName']
    def get_queryset(self):
        if 'basicProductName_query' in self.request.GET:
            search =  self.request.GET['basicProductName_query']
            limit =  self.request.GET['limit']
            toreturn =[]
            temparr =[]
            searchValue = AccessoriesSection.objects.filter(basicProductName__icontains = search)
            for i in searchValue:
                if len(toreturn)>0:
                    for j in toreturn:
                        if j.basicProductName == i.basicProductName:
                            pass
                        else:
                            temparr.append(int(i.pk))
                            toreturn.append(i)
                else:
                    temparr.append(int(i.pk))
                    toreturn.append(i)
            return AccessoriesSection.objects.filter(pk__in = temparr)
        else:
            return AccessoriesSection.objects.all()


class AccessoriesFieldViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = AccessoriesFieldSerializer
    queryset = AccessoriesField.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['template','productBaseName']

class AccessoriesDataViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = AccessoriesDataSerializer
    queryset = AccessoriesData.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['productBaseName','itemNumber']

class AlbumImagesViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = AlbumImagesSerializer
    queryset = AlbumImages.objects.all()




import html2text
import sys


def addTemplateList(c,width,height,data,stylesN,page6BG,pageCount,lang):
    if lang=='en':
        height2 = 450
        c.drawImage(page6BG,0,0,width=width,height=height,mask = 'auto')
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold",22)
        c.drawString(30, 8.3*inch, "ROPES AT A GLANCE")
        for template in data:
            # printtemplate.name, 'name name'
            if template.defaultImage:
                productImage = template.defaultImage.path
            else:
                product = os.path.join(globalSettings.BASE_DIR , 'static_shared/images',"stars.jpeg")

            c.drawImage(productImage,10,height2,width = 80, height = 80, mask= 'auto')

            height2 = height2 + 20
            height3 = height2 + 15
            height4 = height2
            height5 = height2 - 30
            height6 = height2
            test =  template.parent_name
            test = test.split("-")
            text = ''
            for i in test:
                text += i.upper() + " "

            para101 = Paragraph('<para align="left" fontName = FrutigerB fontSize=11 >%s</para>'%(text), stylesN)
            desc101 = [[para101]]
            r101 = Table(desc101,colWidths=8*cm)
            w, h = r101.wrapOn(c, width,height)
            r101.drawOn(c, 90, height6+40)
            height4 = height6 +60 -h

            height7 = htmlRMLCanvvas(template.rteDescription,c,8*cm,90,height4,stylesN,colors.black,lang)


            _color = rangeColors(template.color)
            c.setFillColor(_color.hex)
            c.setStrokeColor(colors.white)
            c.rect(220,height2,1.3*inch,0.8*inch, fill=1)

            para101 = Paragraph('<para align="center" fontName = FrutigerB fontSize=20 >%s</para>'%(template.name), stylesN)
            desc101 = [[para101]]
            r101 = Table(desc101,colWidths=1*inch)
            w, h = r101.wrapOn(c, width,height)
            r101.drawOn(c, 225, height2+23)


            _color = rangeColors(template.color,luminance=.4)
            c.setFillColor(_color.hex)
            c.setStrokeColor(colors.white)
            c.rect(4.5*inch,height2,0.8*inch,0.8*inch, fill=1)
            c.setFont("Helvetica-Bold", 9)
            c.setFillColor(colors.black)
            k = json.loads(template.keyword1)
            k11 =[[k]]
            r11 = Table(k11,colWidths=3.6*inch,rowHeights=4*mm)
            c.setFont("Helvetica", 7)

            para101 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%(k["value1"]), stylesN)
            desc101 = [[para101]]
            r101 = Table(desc101,colWidths=0.8*inch,rowHeights=1*mm)
            w, h = r101.wrapOn(c, width,height)
            r101.drawOn(c, 4.5*inch, height3+23)

            para102 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%("N/mm2"), stylesN)
            desc102 = [[para102]]
            r102 = Table(desc102,colWidths=0.6*inch,rowHeights=1*mm)
            r102.wrapOn(c, width,height)
            r102.drawOn(c, 4.6*inch, height3+10)

            para101 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%(k["value2"]), stylesN)
            desc101 = [[para101]]
            r101 = Table(desc101,colWidths=0.8*inch,rowHeights=1*mm)
            w, h = r101.wrapOn(c, width,height)
            r101.drawOn(c, 4.5*inch, height3-5)

            para102 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%("psi"), stylesN)
            desc102 = [[para102]]
            r102 = Table(desc102,colWidths=0.6*inch,rowHeights=1*mm)
            r102.wrapOn(c, width,height)
            r102.drawOn(c, 4.6*inch, height3-15)


            _color = rangeColors(template.color,luminance=.5)
            c.setFillColor(_color.hex)
            c.rect(5.4*inch,height2,0.8*inch,0.8*inch, fill=1)
            c.setFont("Helvetica-Bold", 9)
            c.setFillColor(colors.black)
            k1 = json.loads(template.keyword2)

            k12 =[[k1]]

            r12 = Table(k12,colWidths=5*inch,rowHeights=10*mm)

            para201 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%(k1["value1"]), stylesN)
            desc201 = [[para201]]
            r201 = Table(desc201,colWidths=0.8*inch)
            w,h = r201.wrapOn(c, width,height)
            r201.drawOn(c, 5.4*inch, height3+23)

            para202 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%("%"), stylesN)
            desc202 = [[para202]]
            r202 = Table(desc202,colWidths=0.6*inch,rowHeights=1*mm)
            r202.wrapOn(c, width,height)
            r202.drawOn(c, 5.5*inch, height3+10)


            para201 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%(k1["value2"]), stylesN)
            desc201 = [[para201]]
            r201 = Table(desc201,colWidths=0.8*inch)
            w,h = r201.wrapOn(c, width,height)

            r201.drawOn(c, 5.4*inch, height3-5)

            para202 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%("in/100ft"), stylesN)
            desc202 = [[para202]]
            r202 = Table(desc202,colWidths=0.8*inch,rowHeights=1*mm)
            r202.wrapOn(c, width,height)
            r202.drawOn(c, 5.4*inch, height3-15)

            _color = rangeColors(template.color,luminance=.7)
            c.setFillColor(_color.hex)
            c.setStrokeColor(colors.white)

            c.rect(6.3*inch,height2,0.8*inch,0.8*inch, fill=1)
            c.setFont("Helvetica-Bold", 7)
            c.setFillColor(colors.black)
            k2 = json.loads(template.keyword3)

            k13 = [[k2]]

            r13 = Table(k13,colWidths=5*inch,rowHeights=10*mm)

            para301 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%(k2["value1"]), stylesN)
            desc301 = [[para301]]
            r301 = Table(desc301,colWidths=0.8*inch,rowHeights=1*mm)
            r301.wrapOn(c, width,height)
            r301.drawOn(c, 6.3*inch, height3+23)

            para302 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%("%"), stylesN)
            desc302 = [[para302]]
            r302 = Table(desc302,colWidths=0.6*inch,rowHeights=1*mm)
            r302.wrapOn(c, width,height)
            r302.drawOn(c, 6.4*inch, height3+10)


            para301 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%(k2["value2"]), stylesN)
            desc301 = [[para301]]
            r301 = Table(desc301,colWidths=0.8*inch,rowHeights=1*mm)
            r301.wrapOn(c, width,height)
            r301.drawOn(c, 6.3*inch, height3-5)

            para302 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%("in/100ft"), stylesN)
            desc302 = [[para302]]
            r302 = Table(desc302,colWidths=0.8*inch,rowHeights=1*mm)
            r302.wrapOn(c, width,height)
            r302.drawOn(c, 6.3*inch, height3-15)

            _color = rangeColors(template.color,luminance=.9)
            c.setFillColor(_color.hex)
            c.setStrokeColor(colors.white)
            c.rect(7.2*inch,height2,0.8*inch,0.8*inch, fill=1)
            c.setFont("Helvetica-Bold", 7)
            c.setFillColor(colors.black)
            k3 = json.loads(template.keyword4)
            k14 = [[k3]]
            r14 = Table(k14,colWidths=5*inch,rowHeights=10*mm)

            para401 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%(k3["value1"]), stylesN)
            desc401 = [[para401]]
            r401 = Table(desc401,colWidths=0.8*inch,rowHeights=1*mm)
            r401.wrapOn(c, width,height)
            r401.drawOn(c, 7.2*inch, height3+23)

            para402 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%("m"), stylesN)
            desc402 = [[para402]]
            r402 = Table(desc402,colWidths=0.6*inch,rowHeights=1*mm)
            r402.wrapOn(c, width,height)
            r402.drawOn(c, 7.3*inch, height3+10)

            para401 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%(k3["value2"]), stylesN)
            desc401 = [[para401]]
            r401 = Table(desc401,colWidths=0.8*inch,rowHeights=1*mm)
            r401.wrapOn(c, width,height)
            r401.drawOn(c, 7.2*inch, height3-5)

            para402 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%("ft"), stylesN)
            desc402 = [[para402]]
            r402 = Table(desc402,colWidths=0.6*inch,rowHeights=1*mm)
            r402.wrapOn(c, width,height)
            r402.drawOn(c, 7.3*inch, height3-15)

            height2 = height2 - 120


        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)

        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1
        return pageCount

    elif lang=='de':
        height2 = 450
        c.drawImage(page6BG,0,0,width=width,height=height,mask = 'auto')
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold",22)
        c.drawString(30, 8.3*inch, "ROPES AT A GLANCE")
        for template in data:
            # printtemplate.name, 'name name'
            if template.defaultImage:
                productImage = template.defaultImage.path
            else:
                product = os.path.join(globalSettings.BASE_DIR , 'static_shared/images',"stars.jpeg")

            c.drawImage(productImage,10,height2,width = 80, height = 80, mask= 'auto')

            height2 = height2 + 20
            height3 = height2 + 15
            height4 = height2
            height5 = height2 - 30
            height6 = height2
            test =  template.parent_name
            test = test.split("-")
            text = ''
            for i in test:
                text += i.upper() + " "

            para101 = Paragraph('<para align="left" fontName = FrutigerB fontSize=11 >%s</para>'%(text), stylesN)
            desc101 = [[para101]]
            r101 = Table(desc101,colWidths=8*cm)
            w, h = r101.wrapOn(c, width,height)
            r101.drawOn(c, 90, height6+40)
            height4 = height6 +60 -h

            height7 = htmlRMLCanvvas(template.rteDescription_de,c,8*cm,90,height4,stylesN,colors.black,lang)


            _color = rangeColors(template.color)
            c.setFillColor(_color.hex)
            c.setStrokeColor(colors.white)
            c.rect(220,height2,1.3*inch,0.8*inch, fill=1)

            para101 = Paragraph('<para align="center" fontName = FrutigerB fontSize=20 >%s</para>'%(template.name), stylesN)
            desc101 = [[para101]]
            r101 = Table(desc101,colWidths=1*inch)
            w, h = r101.wrapOn(c, width,height)
            r101.drawOn(c, 225, height2+23)


            _color = rangeColors(template.color,luminance=.4)
            c.setFillColor(_color.hex)
            c.setStrokeColor(colors.white)
            c.rect(4.5*inch,height2,0.8*inch,0.8*inch, fill=1)
            c.setFont("Helvetica-Bold", 9)
            c.setFillColor(colors.black)
            k = json.loads(template.keyword1)
            k11 =[[k]]
            r11 = Table(k11,colWidths=3.6*inch,rowHeights=4*mm)
            c.setFont("Helvetica", 7)

            para101 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%(k["value1"]), stylesN)
            desc101 = [[para101]]
            r101 = Table(desc101,colWidths=0.8*inch,rowHeights=1*mm)
            w, h = r101.wrapOn(c, width,height)
            r101.drawOn(c, 4.5*inch, height3+23)

            para102 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%("N/mm2"), stylesN)
            desc102 = [[para102]]
            r102 = Table(desc102,colWidths=0.6*inch,rowHeights=1*mm)
            r102.wrapOn(c, width,height)
            r102.drawOn(c, 4.6*inch, height3+10)

            para101 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%(k["value2"]), stylesN)
            desc101 = [[para101]]
            r101 = Table(desc101,colWidths=0.8*inch,rowHeights=1*mm)
            w, h = r101.wrapOn(c, width,height)
            r101.drawOn(c, 4.5*inch, height3-5)

            para102 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%("psi"), stylesN)
            desc102 = [[para102]]
            r102 = Table(desc102,colWidths=0.6*inch,rowHeights=1*mm)
            r102.wrapOn(c, width,height)
            r102.drawOn(c, 4.6*inch, height3-15)


            _color = rangeColors(template.color,luminance=.5)
            c.setFillColor(_color.hex)
            c.rect(5.4*inch,height2,0.8*inch,0.8*inch, fill=1)
            c.setFont("Helvetica-Bold", 9)
            c.setFillColor(colors.black)
            k1 = json.loads(template.keyword2)

            k12 =[[k1]]

            r12 = Table(k12,colWidths=5*inch,rowHeights=10*mm)

            para201 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%(k1["value1"]), stylesN)
            desc201 = [[para201]]
            r201 = Table(desc201,colWidths=0.8*inch)
            w,h = r201.wrapOn(c, width,height)
            r201.drawOn(c, 5.4*inch, height3+23)

            para202 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%("%"), stylesN)
            desc202 = [[para202]]
            r202 = Table(desc202,colWidths=0.6*inch,rowHeights=1*mm)
            r202.wrapOn(c, width,height)
            r202.drawOn(c, 5.5*inch, height3+10)


            para201 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%(k1["value2"]), stylesN)
            desc201 = [[para201]]
            r201 = Table(desc201,colWidths=0.8*inch)
            w,h = r201.wrapOn(c, width,height)

            r201.drawOn(c, 5.4*inch, height3-5)

            para202 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%("in/100ft"), stylesN)
            desc202 = [[para202]]
            r202 = Table(desc202,colWidths=0.8*inch,rowHeights=1*mm)
            r202.wrapOn(c, width,height)
            r202.drawOn(c, 5.4*inch, height3-15)

            _color = rangeColors(template.color,luminance=.7)
            c.setFillColor(_color.hex)
            c.setStrokeColor(colors.white)

            c.rect(6.3*inch,height2,0.8*inch,0.8*inch, fill=1)
            c.setFont("Helvetica-Bold", 7)
            c.setFillColor(colors.black)
            k2 = json.loads(template.keyword3)

            k13 = [[k2]]

            r13 = Table(k13,colWidths=5*inch,rowHeights=10*mm)

            para301 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%(k2["value1"]), stylesN)
            desc301 = [[para301]]
            r301 = Table(desc301,colWidths=0.8*inch,rowHeights=1*mm)
            r301.wrapOn(c, width,height)
            r301.drawOn(c, 6.3*inch, height3+23)

            para302 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%("%"), stylesN)
            desc302 = [[para302]]
            r302 = Table(desc302,colWidths=0.6*inch,rowHeights=1*mm)
            r302.wrapOn(c, width,height)
            r302.drawOn(c, 6.4*inch, height3+10)


            para301 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%(k2["value2"]), stylesN)
            desc301 = [[para301]]
            r301 = Table(desc301,colWidths=0.8*inch,rowHeights=1*mm)
            r301.wrapOn(c, width,height)
            r301.drawOn(c, 6.3*inch, height3-5)

            para302 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%("in/100ft"), stylesN)
            desc302 = [[para302]]
            r302 = Table(desc302,colWidths=0.8*inch,rowHeights=1*mm)
            r302.wrapOn(c, width,height)
            r302.drawOn(c, 6.3*inch, height3-15)

            _color = rangeColors(template.color,luminance=.9)
            c.setFillColor(_color.hex)
            c.setStrokeColor(colors.white)
            c.rect(7.2*inch,height2,0.8*inch,0.8*inch, fill=1)
            c.setFont("Helvetica-Bold", 7)
            c.setFillColor(colors.black)
            k3 = json.loads(template.keyword4)
            k14 = [[k3]]
            r14 = Table(k14,colWidths=5*inch,rowHeights=10*mm)

            para401 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%(k3["value1"]), stylesN)
            desc401 = [[para401]]
            r401 = Table(desc401,colWidths=0.8*inch,rowHeights=1*mm)
            r401.wrapOn(c, width,height)
            r401.drawOn(c, 7.2*inch, height3+23)

            para402 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%("m"), stylesN)
            desc402 = [[para402]]
            r402 = Table(desc402,colWidths=0.6*inch,rowHeights=1*mm)
            r402.wrapOn(c, width,height)
            r402.drawOn(c, 7.3*inch, height3+10)

            para401 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%(k3["value2"]), stylesN)
            desc401 = [[para401]]
            r401 = Table(desc401,colWidths=0.8*inch,rowHeights=1*mm)
            r401.wrapOn(c, width,height)
            r401.drawOn(c, 7.2*inch, height3-5)

            para402 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%("ft"), stylesN)
            desc402 = [[para402]]
            r402 = Table(desc402,colWidths=0.6*inch,rowHeights=1*mm)
            r402.wrapOn(c, width,height)
            r402.drawOn(c, 7.3*inch, height3-15)

            height2 = height2 - 120


        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1
        return pageCount

    elif lang=='zh':
        height2 = 450
        c.drawImage(page6BG,0,0,width=width,height=height,mask = 'auto')
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold",22)
        c.drawString(30, 8.3*inch, "ROPES AT A GLANCE")
        for template in data:
            # printtemplate.name, 'name name'
            if template.defaultImage:
                productImage = template.defaultImage.path
            else:
                product = os.path.join(globalSettings.BASE_DIR , 'static_shared/images',"stars.jpeg")

            c.drawImage(productImage,10,height2,width = 80, height = 80, mask= 'auto')

            height2 = height2 + 20
            height3 = height2 + 15
            height4 = height2
            height5 = height2 - 30
            height6 = height2
            test =  template.parent_name
            test = test.split("-")
            text = ''
            for i in test:
                text += i.upper() + " "

            para101 = Paragraph('<para align="left" fontName = FrutigerB fontSize=11 >%s</para>'%(text), stylesN)
            desc101 = [[para101]]
            r101 = Table(desc101,colWidths=8*cm)
            w, h = r101.wrapOn(c, width,height)
            r101.drawOn(c, 90, height6+40)
            height4 = height6 +60 -h

            height7 = htmlRMLCanvvas(template.rteDescription_ch,c,8*cm,90,height4,stylesN,colors.black,lang)


            _color = rangeColors(template.color)
            c.setFillColor(_color.hex)
            c.setStrokeColor(colors.white)
            c.rect(220,height2,1.3*inch,0.8*inch, fill=1)

            para101 = Paragraph('<para align="center" fontName = FrutigerB fontSize=20 >%s</para>'%(template.name), stylesN)
            desc101 = [[para101]]
            r101 = Table(desc101,colWidths=1*inch)
            w, h = r101.wrapOn(c, width,height)
            r101.drawOn(c, 225, height2+23)


            _color = rangeColors(template.color,luminance=.4)
            c.setFillColor(_color.hex)
            c.setStrokeColor(colors.white)
            c.rect(4.5*inch,height2,0.8*inch,0.8*inch, fill=1)
            c.setFont("Helvetica-Bold", 9)
            c.setFillColor(colors.black)
            k = json.loads(template.keyword1)
            k11 =[[k]]
            r11 = Table(k11,colWidths=3.6*inch,rowHeights=4*mm)
            c.setFont("Helvetica", 7)

            para101 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%(k["value1"]), stylesN)
            desc101 = [[para101]]
            r101 = Table(desc101,colWidths=0.8*inch,rowHeights=1*mm)
            w, h = r101.wrapOn(c, width,height)
            r101.drawOn(c, 4.5*inch, height3+23)

            para102 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%("N/mm2"), stylesN)
            desc102 = [[para102]]
            r102 = Table(desc102,colWidths=0.6*inch,rowHeights=1*mm)
            r102.wrapOn(c, width,height)
            r102.drawOn(c, 4.6*inch, height3+10)

            para101 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%(k["value2"]), stylesN)
            desc101 = [[para101]]
            r101 = Table(desc101,colWidths=0.8*inch,rowHeights=1*mm)
            w, h = r101.wrapOn(c, width,height)
            r101.drawOn(c, 4.5*inch, height3-5)

            para102 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%("psi"), stylesN)
            desc102 = [[para102]]
            r102 = Table(desc102,colWidths=0.6*inch,rowHeights=1*mm)
            r102.wrapOn(c, width,height)
            r102.drawOn(c, 4.6*inch, height3-15)


            _color = rangeColors(template.color,luminance=.5)
            c.setFillColor(_color.hex)
            c.rect(5.4*inch,height2,0.8*inch,0.8*inch, fill=1)
            c.setFont("Helvetica-Bold", 9)
            c.setFillColor(colors.black)
            k1 = json.loads(template.keyword2)

            k12 =[[k1]]

            r12 = Table(k12,colWidths=5*inch,rowHeights=10*mm)

            para201 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%(k1["value1"]), stylesN)
            desc201 = [[para201]]
            r201 = Table(desc201,colWidths=0.8*inch)
            w,h = r201.wrapOn(c, width,height)
            r201.drawOn(c, 5.4*inch, height3+23)

            para202 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%("%"), stylesN)
            desc202 = [[para202]]
            r202 = Table(desc202,colWidths=0.6*inch,rowHeights=1*mm)
            r202.wrapOn(c, width,height)
            r202.drawOn(c, 5.5*inch, height3+10)


            para201 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%(k1["value2"]), stylesN)
            desc201 = [[para201]]
            r201 = Table(desc201,colWidths=0.8*inch)
            w,h = r201.wrapOn(c, width,height)

            r201.drawOn(c, 5.4*inch, height3-5)

            para202 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%("in/100ft"), stylesN)
            desc202 = [[para202]]
            r202 = Table(desc202,colWidths=0.8*inch,rowHeights=1*mm)
            r202.wrapOn(c, width,height)
            r202.drawOn(c, 5.4*inch, height3-15)

            _color = rangeColors(template.color,luminance=.7)
            c.setFillColor(_color.hex)
            c.setStrokeColor(colors.white)

            c.rect(6.3*inch,height2,0.8*inch,0.8*inch, fill=1)
            c.setFont("Helvetica-Bold", 7)
            c.setFillColor(colors.black)
            k2 = json.loads(template.keyword3)

            k13 = [[k2]]

            r13 = Table(k13,colWidths=5*inch,rowHeights=10*mm)

            para301 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%(k2["value1"]), stylesN)
            desc301 = [[para301]]
            r301 = Table(desc301,colWidths=0.8*inch,rowHeights=1*mm)
            r301.wrapOn(c, width,height)
            r301.drawOn(c, 6.3*inch, height3+23)

            para302 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%("%"), stylesN)
            desc302 = [[para302]]
            r302 = Table(desc302,colWidths=0.6*inch,rowHeights=1*mm)
            r302.wrapOn(c, width,height)
            r302.drawOn(c, 6.4*inch, height3+10)


            para301 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%(k2["value2"]), stylesN)
            desc301 = [[para301]]
            r301 = Table(desc301,colWidths=0.8*inch,rowHeights=1*mm)
            r301.wrapOn(c, width,height)
            r301.drawOn(c, 6.3*inch, height3-5)

            para302 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%("in/100ft"), stylesN)
            desc302 = [[para302]]
            r302 = Table(desc302,colWidths=0.8*inch,rowHeights=1*mm)
            r302.wrapOn(c, width,height)
            r302.drawOn(c, 6.3*inch, height3-15)

            _color = rangeColors(template.color,luminance=.9)
            c.setFillColor(_color.hex)
            c.setStrokeColor(colors.white)
            c.rect(7.2*inch,height2,0.8*inch,0.8*inch, fill=1)
            c.setFont("Helvetica-Bold", 7)
            c.setFillColor(colors.black)
            k3 = json.loads(template.keyword4)
            k14 = [[k3]]
            r14 = Table(k14,colWidths=5*inch,rowHeights=10*mm)

            para401 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%(k3["value1"]), stylesN)
            desc401 = [[para401]]
            r401 = Table(desc401,colWidths=0.8*inch,rowHeights=1*mm)
            r401.wrapOn(c, width,height)
            r401.drawOn(c, 7.2*inch, height3+23)

            para402 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%("m"), stylesN)
            desc402 = [[para402]]
            r402 = Table(desc402,colWidths=0.6*inch,rowHeights=1*mm)
            r402.wrapOn(c, width,height)
            r402.drawOn(c, 7.3*inch, height3+10)

            para401 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%(k3["value2"]), stylesN)
            desc401 = [[para401]]
            r401 = Table(desc401,colWidths=0.8*inch,rowHeights=1*mm)
            r401.wrapOn(c, width,height)
            r401.drawOn(c, 7.2*inch, height3-5)

            para402 = Paragraph('<para align="center" fontName = FrutigerB fontSize=9 >%s</para>'%("ft"), stylesN)
            desc402 = [[para402]]
            r402 = Table(desc402,colWidths=0.6*inch,rowHeights=1*mm)
            r402.wrapOn(c, width,height)
            r402.drawOn(c, 7.3*inch, height3-15)


            height2 = height2 - 120


        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1
        return pageCount

def initialPages(request,response,styles,stylesN,stylesH,width,height,c,productTemplatesObjects, pageCount,lang):


    page1BG = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes','page1a.jpg')
    page2BG = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes','page2a.jpg')
    page3BG = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes','page3.jpg')
    page4BG = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes','page4a.jpg')
    page5BG = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes','page5a.jpg')
    page6BG = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes','page6a.jpg')
    page7BG = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes','page7a.jpg')
    page8BG = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes','page8a.jpg')
    page9BG = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes','page9a.jpg')
    page10BG = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes','page10a.jpg')
    page11BG = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes','page11a.jpg')

    if(lang=='en'):
        c.drawImage(page1BG,0,0,width=width, height=height, mask = 'auto')

        c.setFont("Helvetica-Bold",27)
        c.setFillColor('#000000')
        c.drawString(185, 5.9*inch, "ELEVATOR")

        c.setFont("Helvetica-Bold",27)
        c.setFillColor('#ffffff')
        c.drawString(340, 5.9*inch, "ROPES")

        c.showPage()
        pageCount +=1

        #page2
        c.drawImage(page2BG,0,0,width=width, height=height, mask = 'auto')

        c.setFillColor('#696969')


        c.setFont("Helvetica-Bold",20)
        c.setFillColor('#0080ff')
        c.drawString(35, 8.6*inch, "GOING UP")

        c.setFont("Helvetica-Bold",20)
        c.setFillColor('#ffffff')
        c.drawString(155, 8.6*inch, "IS OUR MOTTO.")

        tp = Paragraph('<para fontName = FrutigerR fontsize=9 align="Justify" leading=15> Through our three production facilities located in Switzerland, the U.S.A. and China, we produce elevator ropes to service the global market. Over decades, our ropes have transported millions of passengers in a secure and comfortable way. It is especially in high-rise high speed installations that BRUGG LIFTING elevator ropes show their excellent performance,ensuring smoothness of ride, above-average lifetime and high economic efficiency.</para>',stylesN)

        tp1 = Paragraph('<para fontName = FrutigerR fontsize=9 align="Justify" leading=17>The development of new and innovative products, the continuous improvement of existing products as well as the optimization of production processes ensures, that customers of BRUGG LIFTING can demand and expect consistently high product quality and optimum performance.</para>',stylesN)

        tp2 = Paragraph('<para fontName = FrutigerR fontsize=9 align="Justify" leading=17>For additional flexibility and innovation BRUGG LIFTING also produce hoist and governor ropes in compliance with individual customer specifications.</para>',stylesN)

        tp3 = Paragraph('<para fontName = FrutigerR fontsize=9 align="Justify" leading=17>Working with our global logistics and distribution partners ensures,that our products are correctly packaged, labeled and available for our customers everywhere at the right place and time  every time.</para>',stylesN)

        tp4 = Paragraph('<para fontName = FrutigerR fontsize=9 align="Justify" leading=17>Our performance parameters are convincing.That`s why international elevator engineering groups to local small and medium-sized companies rely on BRUGG LIFTING elevator ropes.</para>',stylesN)
        tpt=[[tp],[tp1],[tp2],[tp3],[tp4]]
        tptab=Table(tpt ,colWidths=4.2*inch)
        tptab.setStyle(TableStyle([
                            ('TOPPADDING',(0,0),(-1,-1),10)

                             ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,200,90)


        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        #page3
        c.drawImage(page3BG,0,0,width=width, height=height, mask = 'auto')


        b00 =Paragraph('<para fontName = FrutigerR fontsize=9>828m</para>',stylesN)
        b001 =Paragraph('<para fontName = FrutigerR fontsize=9>2.717ft</para>',stylesN)
        b002 =Paragraph('<para fontName = FrutigerR fontsize=9>Burj Khalifa Dubai UAE</para>',stylesN)

        data1 = [[b00,b001,b002]]
        t1 = Table(data1,colWidths=[1.5*cm,1.75*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,320,750)

        b991 =Paragraph('<para fontName = FrutigerR fontsize=9>553m</para>',stylesN)
        b9912 =Paragraph('<para fontName = FrutigerR fontsize=9>1.814ft</para>',stylesN)
        b9913 =Paragraph('<para fontName = FrutigerR fontsize=9> CN Tower.Tornto.CDN</para>',stylesN)

        data1 = [[b991,b9912,b9913]]
        t1 = Table(data1,colWidths=[1.5*cm,1.75*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,320,500)

        b882 =Paragraph('<para fontName = FrutigerR fontsize=9>541m</para>',stylesN)
        b8821 =Paragraph('<para fontName = FrutigerR fontsize=9>1.775ft</para>',stylesN)
        b8822 =Paragraph('<para fontName = FrutigerR fontsize=9>One World Trade Center New York USA</para>',stylesN)

        data1 = [[b882,b8821,b8822]]
        t1 = Table(data1,colWidths=[1.5*cm,1.75*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,320,513)

        b3 =Paragraph('<para fontName = FrutigerR fontsize=9>468m</para>',stylesN)
        b31 =Paragraph('<para fontName = FrutigerR fontsize=9>1.535ft</para>',stylesN)
        b32 =Paragraph('<para fontName = FrutigerR fontsize=9>Oriental Pearl.Shangai.CN</para>',stylesN)

        data1 = [[b3,b31,b32]]
        t1 = Table(data1,colWidths=[1.5*cm,1.75*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,320,435)


        b4 =Paragraph('<para fontName = FrutigerR fontsize=9>452m</para>',stylesN)
        b41 =Paragraph('<para fontName = FrutigerR fontsize=9>1.483ft</para>',stylesN)
        b42 =Paragraph('<para fontName = FrutigerR fontsize=9>Petroans Tower. Kulala Lumpur.MAL</para>',stylesN)

        data1 = [[b4,b41,b42]]
        t1 = Table(data1,colWidths=[1.5*cm,1.75*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,320,425)

        b5 =Paragraph('<para fontName = FrutigerR fontsize=9>449m</para>',stylesN)
        b51 =Paragraph('<para fontName = FrutigerR fontsize=9>1.473ft</para>',stylesN)
        b52 =Paragraph('<para fontName = FrutigerR fontsize=9>Empire State Building.NewYork .USA</para>',stylesN)

        data1 = [[b5,b51,b52]]
        t1 = Table(data1,colWidths=[1.5*cm,1.75*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,320,415)

        b6 =Paragraph('<para fontName = FrutigerR fontsize=9>448m</para>',stylesN)
        b61 =Paragraph('<para fontName = FrutigerR fontsize=9>1.470ft</para>',stylesN)
        b62 =Paragraph('<para fontName = FrutigerR fontsize=9>Federation Tower. Moscow.RUS</para>',stylesN)

        data1 = [[b6,b61,b62]]
        t1 = Table(data1,colWidths=[1.5*cm,1.75*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,320,400)

        b7 =Paragraph('<para fontName = FrutigerR fontsize=9>412m</para>',stylesN)
        b71 =Paragraph('<para fontName = FrutigerR fontsize=9>1.352ft</para>',stylesN)
        b72 =Paragraph('<para fontName = FrutigerR fontsize=9>IFC .Hongkong .CN</para>',stylesN)

        data1 = [[b7,b71,b72]]
        t1 = Table(data1,colWidths=[1.5*cm,1.75*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,320,375)

        b8 =Paragraph('<para fontName = FrutigerR fontsize=9>351m</para>',stylesN)
        b81 =Paragraph('<para fontName = FrutigerR fontsize=9>1.033ft</para>',stylesN)
        b82 =Paragraph('<para fontName = FrutigerR fontsize=9>Stratosphere Tower. Las Vegas. USA</para>',stylesN)

        data1 = [[b8,b81,b82]]
        t1 = Table(data1,colWidths=[1.5*cm,1.75*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,320,340)

        height2 = 293


        b11 =Paragraph('<para fontName = FrutigerR fontsize=9>310m</para>',stylesN)
        b111 =Paragraph('<para fontName = FrutigerR fontsize=9>1.017ft</para>',stylesN)
        b112 =Paragraph('<para fontName = FrutigerR fontsize=9>Telekom HQ. Kuala Lumpur.MAL</para>',stylesN)

        data1 = [[b11,b111,b112]]
        t1 = Table(data1,colWidths=[1.5*cm,1.75*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,320,height2)
        height2 = height2 -10

        b12 =Paragraph('<para fontName = FrutigerR fontsize=9>297m</para>',stylesN)
        b121 =Paragraph('<para fontName = FrutigerR fontsize=9>974ft</para>',stylesN)
        b122 =Paragraph('<para fontName = FrutigerR fontsize=9>Comcast Center . Philadelphia.USA</para>',stylesN)

        data1 = [[b12,b121,b122]]
        t1 = Table(data1,colWidths=[1.5*cm,1.75*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,320,height2)
        height2 = height2 -10

        b13 =Paragraph('<para fontName = FrutigerR fontsize=9>288m</para>',stylesN)
        b131 =Paragraph('<para fontName = FrutigerR fontsize=9>945ft</para>',stylesN)
        b132 =Paragraph('<para fontName = FrutigerR fontsize=9>Plaza 66. Shangai .CN</para>',stylesN)

        data1 = [[b13,b131,b132]]
        t1 = Table(data1,colWidths=[1.5*cm,1.75*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,320,height2)
        height2 = height2 -10

        b14 =Paragraph('<para fontName = FrutigerR fontsize=9>284m</para>',stylesN)
        b141 =Paragraph('<para fontName = FrutigerR fontsize=9>932ft</para>',stylesN)
        b142 =Paragraph('<para fontName = FrutigerR fontsize=9>Tomorrow Square. Shanghai . CN</para>',stylesN)

        data1 = [[b14,b141,b142]]
        t1 = Table(data1,colWidths=[1.5*cm,1.75*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,320,height2)
        height2 = height2 -10

        b15 =Paragraph('<para fontName = FrutigerR fontsize=9>280m</para>',stylesN)
        b151 =Paragraph('<para fontName = FrutigerR fontsize=9>919ft</para>',stylesN)
        b152 =Paragraph('<para fontName = FrutigerR fontsize=9>Foreign Ministry . MOscow. RUS</para>',stylesN)

        data1 = [[b15,b151,b152]]
        t1 = Table(data1,colWidths=[1.5*cm,1.75*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,320,height2)
        height2 = height2 -10

        b16 =Paragraph('<para fontName = FrutigerR fontsize=9>233m</para>',stylesN)
        b161 =Paragraph('<para fontName = FrutigerR fontsize=9>764ft</para>',stylesN)
        b162 =Paragraph('<para fontName = FrutigerR fontsize=9>Harbourfront.Hong Kong . CN</para>',stylesN)
        data1 = [[b16,b161,b162]]
        t1 = Table(data1,colWidths=[1.5*cm,1.75*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,320,height2)
        height2 = height2 -10

        b17 =Paragraph('<para fontName = FrutigerR fontsize=9>225m</para>',stylesN)
        b171 =Paragraph('<para fontName = FrutigerR fontsize=9>738ft</para>',stylesN)
        b172 =Paragraph('<para fontName = FrutigerR fontsize=9>Torre Mayor . Mexico City. MEX</para>',stylesN)
        data1 = [[b17,b171,b172]]
        t1 = Table(data1,colWidths=[1.5*cm,1.75*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,320,height2)
        height2 = height2 -10

        b18 =Paragraph('<para fontName = FrutigerR fontsize=9>218m</para>',stylesN)
        b181 =Paragraph('<para fontName = FrutigerR fontsize=9>715ft</para>',stylesN)
        b182 =Paragraph('<para fontName = FrutigerR fontsize=9>Shang Mao Real Estate. Nnanjing. CN</para>',stylesN)
        data1 = [[b18,b181,b182]]
        t1 = Table(data1,colWidths=[1.5*cm,1.75*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,320,height2)
        height2 = height2 -10

        b19 =Paragraph('<para fontName = FrutigerR fontsize=9>213m</para>',stylesN)
        b191 =Paragraph('<para fontName = FrutigerR fontsize=9>699ft</para>',stylesN)
        b192 =Paragraph('<para fontName = FrutigerR fontsize=9>Shangria-La . Hong Kong. CN</para>',stylesN)
        data1 = [[b19,b191,b192]]
        t1 = Table(data1,colWidths=[1.5*cm,1.75*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,320,height2)
        height2 = height2 -35

        b20 =Paragraph('<para fontName = FrutigerR fontsize=9>177m</para>',stylesN)
        b201 =Paragraph('<para fontName = FrutigerR fontsize=9>581ft</para>',stylesN)
        b202 =Paragraph('<para fontName = FrutigerR fontsize=9>Millenium Tower . Vienna .A</para>',stylesN)
        data1 = [[b20,b201,b202]]
        t1 = Table(data1,colWidths=[1.5*cm,1.75*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,320,height2)
        height2 = height2 -10

        b21 =Paragraph('<para fontName = FrutigerR fontsize=9>169m</para>',stylesN)
        b211 =Paragraph('<para fontName = FrutigerR fontsize=9>554ft</para>',stylesN)
        b212 =Paragraph('<para fontName = FrutigerR fontsize=9>Shalom Center . Tele Aviv. IL</para>',stylesN)
        data1 = [[b21,b211,b212]]
        t1 = Table(data1,colWidths=[1.5*cm,1.75*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,320,height2)
        height2 = height2 -10

        b22 =Paragraph('<para fontName = FrutigerR fontsize=9>153m</para>',stylesN)
        b221 =Paragraph('<para fontName = FrutigerR fontsize=9>502ft</para>',stylesN)
        b222 =Paragraph('<para fontName = FrutigerR fontsize=9>Fairmont (Park Plaza).Dubai.UAE</para>',stylesN)
        data1 = [[b22,b221,b222]]
        t1 = Table(data1,colWidths=[1.5*cm,1.75*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,320,height2)
        height2 = height2 -10

        b23 =Paragraph('<para fontName = FrutigerR fontsize=9>138m</para>',stylesN)
        b231 =Paragraph('<para fontName = FrutigerR fontsize=9>453ft</para>',stylesN)
        b232 =Paragraph('<para fontName = FrutigerR fontsize=9>Twintower.Vienna. A</para>',stylesN)
        data1 = [[b23,b231,b232]]
        t1 = Table(data1,colWidths=[1.5*cm,1.75*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,320,height2)
        height2 = height2 -10

        b24 =Paragraph('<para fontName = FrutigerR fontsize=9>135m</para>',stylesN)
        b241 =Paragraph('<para fontName = FrutigerR fontsize=9>443ft</para>',stylesN)
        b242 =Paragraph('<para fontName = FrutigerR fontsize=9>Nurnberger Versicherung . Nuremberg . DE</para>',stylesN)
        data1 = [[b24,b241,b242]]
        t1 = Table(data1,colWidths=[1.5*cm,1.75*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,320,height2)
        height2 = height2 -10



        b25 =Paragraph('<para fontName = FrutigerR fontsize=9>130m</para>',stylesN)
        b251 =Paragraph('<para fontName = FrutigerR fontsize=9>427ft</para>',stylesN)
        b252 =Paragraph('<para fontName = FrutigerR fontsize=9>Castor. Frankfurt.DE</para>',stylesN)
        data1 = [[b25,b251,b252]]
        t1 = Table(data1,colWidths=[1.5*cm,1.75*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,320,height2)
        height2 = height2 -30



        b26 =Paragraph('<para fontName = FrutigerR fontsize=9>105m</para>',stylesN)
        b261 =Paragraph('<para fontName = FrutigerR fontsize=9>344ft</para>',stylesN)
        b262 =Paragraph('<para fontName = FrutigerR fontsize=9>Messeturm .BelevatorCodeasel.CH</para>',stylesN)
        data1 = [[b26,b261,b262]]
        t1 = Table(data1,colWidths=[1.5*cm,1.75*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,320,height2)
        height2 = height2 -20


        b27 =Paragraph('<para fontName = FrutigerR fontsize=9>96m</para>',stylesN)
        b271 =Paragraph('<para fontName = FrutigerR fontsize=9>226ft</para>',stylesN)
        b272 =Paragraph('<para fontName = FrutigerR fontsize=9>Platinum Tower.Tel Aviv .IL</para>',stylesN)
        data1 = [[b27,b271,b272]]
        t1 = Table(data1,colWidths=[1.5*cm,1.75*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,320,height2)


        # data1 = [['','',''],['','',''],['','',''],['','',''],[b882,b8821,b8822],[b3,b31,b32],[b4,b41,b42],[b5,b51,b52],[b6,b61,b62],['','',''],[b7,b71,b72],['','',''],['','',''],[b8,b81,b82],['','',''],[b10,b101,b102],[b11,b111,b112],[b12,b121,b122],[b13,b131,b132],[b14,b141,b142],[b15,b151,b152],[b16,b161,b162],[b17,b171,b172],[b18,b181,b182],[b19,b191,b192],[',',''],[b20,b201,b202],[b21,b211,b212],[b22,b221,b222],[b23,b231,b232],[b24,b241,b242],[b25,b251,b252],['','',''],[b26,b261,b262],[b27,b271,b272]]
        # t1 = Table(data1,colWidths=[1.5*cm,1.75*cm,7.25*cm])
        # t1.wrapOn(c,width,height)
        # t1.drawOn(c,4.4*inch,100)

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        #page 4

        c.drawImage(page4BG,0,0,width=width, height=height, mask = 'auto')

        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold",22)
        c.drawString(40, 8.3*inch, "SERVICES")
        c.setFillGray(0.5)


        tp = Paragraph('<para fontName = FrutigerB fontsize=12 leftindent=13  ><b>System Provider</b></para>',stylesN)
        tp2 = Paragraph('<para fontName = FrutigerR fontsize=9  align="Justify" leading=15> We offer to you a wide assortment of elevator ropes, accessories and tools to meet all of your requirements. We supply you with complete solutions or individually combined components as individual or pre-assembled parts to suit your needs.</para>',stylesN)
        tpt=[[tp],[tp2]]
        tptab=Table(tpt,colWidths=6*inch)
        tptab.setStyle(TableStyle([
                                    ('LEFTPADDING',(0,1),(-1,-1),20),
                               ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,1.7*inch, 450)

        tp = Paragraph('<para fontName = FrutigerB fontsize=12 leftindent=13  ><b>Customized</b></para>',stylesN)
        tp2 = Paragraph('<para fontName = FrutigerR fontsize=9  align="Justify" leading=15> Our wide assortment of elevator ropes, accessories and tools provides nearly all products required for your applications. If none of the articles depicted in the catalog solvesyour problem, or if your elevator is to meet specific requirements, we will be glad to advise you and to develop customized solutions together with you.</para>',stylesN)
        tpt=[[tp],[tp2]]
        tptab=Table(tpt,colWidths=6*inch)
        tptab.setStyle(TableStyle([
                                    ('LEFTPADDING',(0,1),(-1,-1),20),
                               ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,1.7*inch, 350)


        tp = Paragraph('<para fontName = FrutigerB fontsize=12 leftindent=13  ><b>Availability</b></para>',stylesN)
        tp2 = Paragraph('<para fontName = FrutigerR fontsize=9 align="Justify" leading=15 >Due to our three production facilities located in Switzerland and China, as well as due toour global network of warehouse locations, our products will be delivered to your factory or your construction site within a very short time. Please contact us if you have anyquestions regarding deadlines, individual deliveries and specific projects.</para>',stylesN)
        tpt=[[tp],[tp2]]
        tptab=Table(tpt,colWidths=6*inch)
        tptab.setStyle(TableStyle([
                                    ('LEFTPADDING',(0,1),(-1,-1),20),
                               ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,1.7*inch, 260)


        tp = Paragraph('<para fontName = FrutigerB fontsize=12 leftindent=13  ><b>Express Service</b></para>',stylesN)
        tp2 = Paragraph('<para fontName = FrutigerR fontsize=9 align="Justify" leading=15 >In urgent cases we provide the required materials ex works within the hour and ship it to you as quickly as possible by courier all over the world.</para>',stylesN)
        tpt=[[tp],[tp2]]
        tptab=Table(tpt,colWidths=6*inch)
        tptab.setStyle(TableStyle([

                                    ('LEFTPADDING',(0,1),(-1,-1),20)
                               ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,1.7*inch, 200)

        tp = Paragraph('<para fontName = FrutigerB fontsize=12 leftindent=13  ><b>International Standards</b></para>',stylesN)
        tp2 = Paragraph('<para fontName = FrutigerR fontsize=9 align="Justify" leading=15 >All of our products meet the valid international standards.<br/> BRUGG LIFTING is certified according to ISO 9001:2008 and ISO 14001:2004.</para>',stylesN)
        tpt=[[tp],[tp2]]
        tptab=Table(tpt,colWidths=6*inch)
        tptab.setStyle(TableStyle([

                                    ('LEFTPADDING',(0,1),(-1,-1),20),
                               ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,1.7*inch, 140)

        tp = Paragraph('<para fontName = FrutigerB fontsize=12 leftindent=13  ><b>Training/Specialist Workshops</b></para>',stylesN)
        tp2 = Paragraph('<para fontName = FrutigerR fontsize=9 align="Justify" leading=15 >Our aim is to ensure that you will enjoy an optimal use and an increase service life of your elevator ropes. Make use of our offering of qualified and customized training units for your staff.</para>',stylesN)
        tpt=[[tp],[tp2]]
        tptab=Table(tpt,colWidths=6*inch)
        tptab.setStyle(TableStyle([

                                    ('LEFTPADDING',(0,1),(-1,-1),20),
                               ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,1.7*inch, 60)

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        #page 5

        c.drawImage(page5BG,0,0,width=width, height=height, mask = 'auto')

        gm = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>Going up is our Motto</para>',stylesN)
        n = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>2</para>',stylesN)
        gm1 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>Services</para>',stylesN)
        gmn1 = Paragraph('<para fontName = FrutigerR fontName = FrutigerR fontsize=8  leading=10>4</para>',stylesN)
        gm2 = Paragraph('<para fontName = FrutigerR fontName = FrutigerR fontsize=8  leading=10>Ropes at Glance</para>',stylesN)
        gmn2 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>6</para>',stylesN)

        gm3 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>Rope Comparision</para>',stylesN)
        gmn3 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>8</para>',stylesN)

        gm4 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>Rope Comparision . i-Line</para>',stylesN)
        gmn4 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>9</para>',stylesN)

        gm5 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10><b>Elevator Ropes.Accessories</b></para>',stylesN)
        gmn5 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>10</para>',stylesN)

        gm6 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>Hoist Ropes</para>',stylesN)
        gm7 = Paragraph('<para fontName = FrutigerR fontsize=8 leftindent = 15 leading=10>HRS</para>',stylesN)
        gmn7 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>12</para>',stylesN)

        gm8 = Paragraph('<para fontName = FrutigerR fontsize=8  leftindent = 15 leading=10>DP9</para>',stylesN)
        gmn8 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>13</para>',stylesN)
        gm9 = Paragraph('<para fontName = FrutigerR fontsize=8 leftindent = 15  leading=10>MCX9</para>',stylesN)
        gmn9 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>15</para>',stylesN)

        gm10 = Paragraph('<para fontName = FrutigerR fontsize=8 leftindent = 15  leading=8>SCX9</para>',stylesN)
        gmn10 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=8>14</para>',stylesN)

        gm11 = Paragraph('<para fontName = FrutigerR fontsize=8 leftindent = 15  leading=10>8x19</para>',stylesN)
        gmn11 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>16</para>',stylesN)

        gm12 = Paragraph('<para fontName = FrutigerR fontsize=8  leftindent = 15 leading=10>TSR</para>',stylesN)
        gmn12 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>17</para>',stylesN)
        gm13 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>Compensation Ropes</para>',stylesN)
        gm14 = Paragraph('<para fontName = FrutigerR fontsize=8  leftindent = 15 leading=10>8x19.8x25</para>',stylesN)
        gmn14 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>18</para>',stylesN)
        gm15 = Paragraph('<para fontName = FrutigerR fontsize=8  leftindent = 15 leading=10>6x25</para>',stylesN)
        gmn15 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>19</para>',stylesN)
        gm16 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>Governor Ropes</para>',stylesN)
        gm17 = Paragraph('<para fontName = FrutigerR fontsize=8  leftindent = 15 leading=10>6x19.8x19</para>',stylesN)
        gmn17 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>20</para>',stylesN)

        gm18 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>Designations and Classifications</para>',stylesN)
        gmn18 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>21</para>',stylesN)

        gm19 = Paragraph('<para fontName = FrutigerR fontsize=8   leftindent = 15 leading=10>APAG Threaded Swaged Sockets</para>',stylesN)
        gmn19 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>22</para>',stylesN)

        gm20 = Paragraph('<para fontName = FrutigerR fontsize=8  leftindent = 15 leading=10>Eyelet Bolt with Swaged Thimble</para>',stylesN)
        gmn20 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>23</para>',stylesN)

        gm21 = Paragraph('<para fontName = FrutigerR fontsize=8   leftindent = 15 leading=10>Wedge Socket Symmetrical</para>',stylesN)
        gmn21 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>24</para>',stylesN)

        gm22 = Paragraph('<para fontName = FrutigerR fontsize=8 leftindent = 15  leading=10>Wedge Socket ASymmetrical</para>',stylesN)
        gmn22 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>26</para>',stylesN)

        gm23 = Paragraph('<para fontName = FrutigerR fontsize=8 leftindent = 15 leading=10>Elastomer Buffers</para>',stylesN)
        gmn23 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>28</para>',stylesN)

        gm24 = Paragraph('<para fontName = FrutigerR fontsize=8  leftindent = 15 leading=10>Spring</para>',stylesN)
        gmn24 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>29</para>',stylesN)

        gm25 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>Door Closing Rope Sets</para>',stylesN)
        gmn25 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>30</para>',stylesN)

        gm25 = Paragraph('<para fontName = FrutigerR fontsize=8  leftindent = 15 leading=10>Door Closing Rope Flex . Rope clamp</para>',stylesN)
        gmn25 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>31</para>',stylesN)
        gm26 = Paragraph('<para fontName = FrutigerR fontsize=8  leftindent = 15 leading=10>RPM Rope Performance Measurement Device</para>',stylesN)
        gmn26 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>31</para>',stylesN)

        gm27 = Paragraph('<para fontName = FrutigerR fontsize=8  leftindent = 15 leading=10>GDC Grove Depth Comparator</para>',stylesN)
        gmn27 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>33</para>',stylesN)


        gm29 = Paragraph('<para fontName = FrutigerR fontsize=8 leftindent = 15 leading=10>RWG Rope Wear Gauge</para>',stylesN)
        gmn29 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>33</para>',stylesN)
        gm30 = Paragraph('<para fontName = FrutigerR fontsize=8  leftindent = 15 leading=10>VT-Lube Lubricant</para>',stylesN)
        gmn30 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>34</para>',stylesN)
        gm31 = Paragraph('<para fontName = FrutigerR fontsize=8 leftindent = 15 leading=10>Rope Cutters</para>',stylesN)
        gmn31 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>34</para>',stylesN)
        gm32 = Paragraph('<para fontName = FrutigerR fontsize=8 leftindent = 15 leading=10>Packaging</para>',stylesN)
        gmn32 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>35</para>',stylesN)
        gm33 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10><b>Support</b></para>',stylesN)
        gmn33 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>38</para>',stylesN)
        gm34 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>Contacts</para>',stylesN)
        gmn34 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>39</para>',stylesN)

        data =  [[gm,n],[gm1,gmn1],[gm2,gmn2],[gm3,gmn3],[gm4,gmn4],['',''],[gm5,gmn5],[gm6],[gm7,gmn7],[gm8,gmn8],[gm10,gmn10],[gm9,gmn9],[gm11,gmn11],[gm12,gmn12],[gm13],[gm14,gmn14],[gm15,gmn15],[gm16],[gm17,gmn17],[gm18,gmn18],[gm19,gmn19],[gm20,gmn20],[gm21,gmn21],[gm22,gmn22],[gm23,gmn23],[gm24,gmn24],[gm25,gmn25],[gm26,gmn26],[gm27,gmn27],[gm29,gmn29],[gm30,gmn30],[gm31,gmn31],[gm32,gmn32],['',''],[gm33,gmn33],[gm34,gmn34]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.white),
                            ('LINEBELOW',(0,0),(-1,-1),0.1,colors.white),
                            ('FONTSIZE', (0, 0), (-1, -1), 7),
                            ('ALIGN',(0,13),(-2,-16),'CENTER'),
                            ('ALIGN',(0,19),(-2,-10),'CENTER'),
                            ('ALIGN',(0,20),(-2,-3),'LEFT'),
                            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                             ]))

        t.wrapOn(c,width, height)
        t.drawOn(c, 4.75*inch,0.3*inch)


        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)
        t.drawOn(c, -3*inch,0.2*inch)

        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        # maa = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P7TransStrip.png')
        c.drawImage(page6BG,0,0,width=width,height=height,mask = 'auto')

        height2 = 450
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold",22)
        c.drawString(30, 8.3*inch, "ROPES AT A GLANCE")

        templatesTractionRopes = productTemplatesObjects.filter(parent_name = 'traction-ropes')
        templatesTractionRopes2 = list(productTemplatesObjects.filter(parent_name = 'traction-ropes'))
        templateCompensationRopes = list(productTemplatesObjects.filter(parent_name = 'compensation-ropes'))
        templatesGovernorRopes = list(productTemplatesObjects.filter(parent_name = 'governor-ropes'))
        templatesInnovation = productTemplatesObjects.filter(parent_name = 'innovation')

        totalNumberOFTempletes = len(productTemplatesObjects) - len(templatesInnovation)

        templatesTractionRopes2.extend(templateCompensationRopes)
        templatesTractionRopes2.extend(templatesGovernorRopes)


        if totalNumberOFTempletes>5:
            maxNumberItems = 5
            index = float(totalNumberOFTempletes)/maxNumberItems
            # printindex
            index = int(math.ceil(index))
            # printindex, range(index),"index ...."
            for i in range(index):
                if i == index:
                    data = templatesTractionRopes2[maxNumberItems*i+1:-1]

                else:
                    data = templatesTractionRopes2[maxNumberItems*i:maxNumberItems*(i+1)]
                # printlen(data), "data length"
                pageCount =  addTemplateList(c,width, height,data,stylesN,page6BG,pageCount,lang)


        else:
            pageCount = addTemplateList(c,width, height,templatesTractionRopes2,stylesN,page6BG,pageCount,lang)

        #page 8

        c.drawImage(page8BG,0,0,width=width,height=height,mask='auto')

        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold",20)
        c.drawCentredString(138, 8*inch, "ROPE COMPARISON")

        # textobject = c.beginText()
        # textobject.setTextOrigin(40, 7.9*inch)
        # c.setFillColor('#3C434B')
        # textobject.setFont("Helvetica-Bold", 12)
        # textobject.textLines('''
        #                         Elastic Elongation
        #                          ''')
        # c.drawText(textobject)

        # c.drawImage(i3,40,4.2*inch,width=3.5*inch,height=3.5*inch)
        #
        # c.drawImage(i4,43,0.5*inch,width=3.75*inch,height=3*inch)

        ad1 = Paragraph('<para fontName = FrutigerR leftindent=10 align="justify"fontsize=10 leading=15><bullet>&bull;</bullet>Elongation of the  rope occurring whenever a rope is loaded. When the load is removed, the rope is restored to its initial state</para>',stylesN)
        ad2 = Paragraph('<para fontName = FrutigerR leftindent=10 align="justify"fontsize=10 leading=15><bullet>&bull;</bullet>E xample: With a DP9 rope, a load of 8.3 % of the minimum breaking force results in an elastic elongation of ca. 0.109 % of the length of the rope (with a length of 100 m, this is equivalent to 109 mm)</para>',stylesN)
        ad3 = Paragraph('<para fontName = FrutigerR leftindent=10 align="justify"fontsize=10 leading=15><bullet>&bull;</bullet>Elevator ropes from BRUGG LIFTING are especially characterized by a very low elastic elongation</para>',stylesN)

        a = [[ad1],[ad2],[ad3]]
        at=Table(a,colWidths=9.5*cm)
        at.wrapOn(c,width,height)
        at.drawOn(c,4.5*inch,5.1*inch)

        ad1 = Paragraph('<para fontName = FrutigerR leftindent=10 align="justify"fontsize=10 leading=15><bullet>&bull;</bullet>Elongation of the rope occurring until the rope has settled as a result of operation. This elongation is expected to occur at about 2% of the estimated rope service life</para>',stylesN)
        ad2 = Paragraph('<para fontName = FrutigerR leftindent=10 align="justify"fontsize=10 leading=15><bullet>&bull;</bullet>The graphic compares the permanent elongation of the different types of suspension ropes</para>',stylesN)
        ad3 = Paragraph('<para fontName = FrutigerR leftindent=10 align="justify"fontsize=10 leading=15><bullet>&bull;</bullet>Elevator ropes from BRUGG LIFTING are especially characterized by a very low permanent elongation</para>',stylesN)

        a = [[ad1],[ad2],[ad3]]
        at=Table(a,colWidths=9.5*cm)
        at.wrapOn(c,width,height)
        at.drawOn(c,4.5*inch,1.5*inch)
        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        #page 9

        # bg8 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P9Hbox.svg')
        # i5 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','i5.png')

        # c.drawImage(b3,0*inch,8.25*inch,width=8.5*inch,height=3*inch)
        #
        # c.drawImage(bg7,0*inch,8.25*inch,width=8.5*inch,height=0.25*inch,mask='auto')

        c.drawImage(page9BG,0,0,width=width,height=height,mask='auto')


        i = Paragraph('<para color=white fontsize=18><b>ROPE COMPARISON.<span color=rgb(0,157,224)><b> i</b></span>LINE</b></para>',stylesN)
        di = [[i]]
        dti = Table(di)
        dti.wrapOn(c,width,height)
        dti.drawOn(c,30,8*inch)


        # textobject = c.beginText()
        # textobject.setTextOrigin(40, 7.9*inch)
        # c.setFillColor('#3C434B')
        # textobject.setFont("Helvetica-Bold", 12)
        # textobject.textLines('''
        #                         Minimum Breaking Load
        #                          ''')
        # c.drawText(textobject)

        # c.drawImage(i5,40,4.7*inch,width=4*inch,height=3*inch)
        #
        # c.drawImage(i6,370,1.3*inch,width=2*inch,height=2.5*inch)
        #
        # c.drawImage(i7,535,0.7*inch,width=1*inch,height=3*inch)

        ad1 = Paragraph('<para fontName= FrutigerR leftindent=10 align="justify" fontsize=10 leading=15><bullet>&bull;</bullet>MBL represents the minimum load that can be applied to a rope before it breakse</para>',stylesN)
        ad2 = Paragraph('<para fontName= FrutigerR leftindent=10 align="justify"fontsize=10 leading=15><bullet>&bull;</bullet>The graphic compares the minimum breaking load of the different types of suspension ropes</para>',stylesN)
        ad3 = Paragraph('<para fontName= FrutigerR leftindent=10 align="justify"fontsize=10 leading=15><bullet>&bull;</bullet>Reference: 100 % = 8x19 suspension rope with natural fiber core</para>',stylesN)

        a = [[ad1],[ad2],[ad3]]
        at=Table(a,colWidths=9.5*cm)
        at.wrapOn(c,width,height)
        at.drawOn(c,4.5*inch,5.5*inch)

        id =Paragraph('<para fontName= FrutigerB fontsize=15 spaceAfter=2><span color=rgb(0,157,224)><b>i</b></span><b>Line & Color Coding</b><br/></para>',stylesN)
        id1 =Paragraph('<para fontName= FrutigerR fontsize=10 leading=13 align="justify">Correctly installed hoist ropes increase the service life and the safety.They improve the riding comfort and avoid downtimes. Independent of the construction and the producer, every hoist rope is susceptible to untwisting during the installation.</para>',stylesN)
        id2 =Paragraph('<para fontName= FrutigerR fontsize=10 leading=13 align="justify">With the help of the i-LINE, which is applied to our hoist ropes by BRUGG LIFTING already during the production, untwisted hoist ropes can be detected easily and fast, located and adjusted correctly.</para>',stylesN)

        idd = [[id],'',[id1],[id2]]
        idt = Table(idd,colWidths=10*cm)
        idt.wrapOn(c,width,height)
        idt.drawOn(c,40,1.75*inch)

        ad = Paragraph('<para  fontName= FrutigerB align="justify" fontsize=13 leading=15><b>Advantages of the <span color=rgb(0,157,224)><b>i</b></span>LINE</b></para>',stylesN)
        ad1 = Paragraph('<para fontName= FrutigerR leftindent=13 align="justify" fontsize=10 leading=15><bullet>&bull;</bullet>simple and correct installation</para>',stylesN)
        ad2 = Paragraph('<para fontName= FrutigerR leftindent=10 align="justify"fontsize=10 leading=15><bullet>&bull;</bullet>safe installation aid</para>',stylesN)
        ad3 = Paragraph('<para fontName= FrutigerR leftindent=10 align="justify"fontsize=10 leading=15><bullet>&bull;</bullet>optimizes product performance</para>',stylesN)
        ad4 = Paragraph('<para fontName= FrutigerR leftindent=10 align="justify"fontsize=10 leading=15><bullet>&bull;</bullet>colour code for the identification of the rope type</para>',stylesN)


        a = [[ad],[ad1],[ad2],[ad3],[ad4]]
        at=Table(a,colWidths=9.5*cm)
        at.wrapOn(c,width,height)
        at.drawOn(c,40,0.2*inch)


        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        #page 10
        # bg9 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P11Hbox.svg')
        # e5 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P10bgGred.png')
        # e2 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P10Bannerimg.png')
        # e1 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P10Strip.png')
        # e3 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P11Strip.png')
        # e4 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P11Strip.svg')
        # e6 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P11img3.png')
        # e7 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P10BruggLiftingCom.png')
        # bgp11 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','p11BannerImg.png')


        # c.drawImage(e5,0*inch,0*inch,width=8.5*inch,height=8.25*inch)
        #
        # c.drawImage(e2,0*inch,8.25*inch,width=8.5*inch,height=3*inch)
        # c.drawImage(e1,0*inch,8.25*inch,width=8.5*inch,height=0.9*inch,mask='auto')

        c.drawImage(page10BG,0,0,width=width,height=height,mask='auto')

        # drawing = svg2rlg(logo)
        # scaleFactor = 1./1.8
        # drawing.width *= scaleFactor
        # drawing.height *= scaleFactor
        # drawing.scale(scaleFactor, scaleFactor)
        # renderPDF.draw(drawing, c, 20,10.2*inch)

        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold",20)
        c.drawString(30, 8*inch, "ELEVATOR ROPES . ACCESSORIES")
        c.setFillGray(0.5)
        # c.rect(448,8.5*inch, 6*inch, 0.25*inch,stroke=0,fill=1)

        p = Paragraph('''<para fontName = FrutigerR fontsize=9  leading=12 align="justify">BRUGG LIFTING elevator ropes are a symbol of the highest quality.<br/><br/>To ensure that our customers can rely on the consistent excellent quality of our products, we control all our manufacturing processes very tightly and continuously validate the quality of our products with a sophisticated system. Already the wire material is selected by us with the greatest care. We purchase our raw materials exclusively from suppliers that permanently meet our high standards. Further essential factors for the high product quality are modern production technologies
        and especially the experience of many years of our qualified skilled workers.In order to guarantee a complete production quality we use the most modern measuring and monitoring techniques in our production lines.After that all our products are subjected to fatigue tests and property analysis with statistical evaluation at our in-house test facility. <br/><br/> As a customer you benefit from the products that stand out due to the very best values concerning elongation, breaking load, smoothness of ride and service ife. Thus BRUGG LIFTING elevator ropes symbolize the highest economic value  and a cost performance ratio that convinces again and again.</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,3.35*inch)

        # c.drawImage(i1,4.4*inch,3.75*inch,width=3.4*inch,height=3.75*inch)

        # c.drawImage(z9,0*inch,8.1*inch,width=8.5*inch,height=0.3*inch)

        # drawing = svg2rlg(z2)
        # scaleFactor = 1/1.85
        # drawing.width *= scaleFactor
        # drawing.height *= scaleFactor
        # drawing.scale(scaleFactor, scaleFactor)
        # renderPDF.draw(drawing, c, 0,8.1*inch)

        textobject = c.beginText()
        textobject.setTextOrigin(2*inch, 0.4*inch)
        textobject.setFont("Helvetica-Bold", 50)
        textobject.setFillColorRGB(255,255,255)
        textobject.textLines('''
                                brugglifting.com
                              ''')
        c.drawText(textobject)


        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        #page 11
        c.drawImage(page11BG,0,0,width=width,height=height,mask='auto')



        p = Paragraph('''<para fontName =FrutigerR fontsize=9  leading=15 align="justify">As system supplier we have the corresponding end termi-nations, buffer systems and accessories for all elevator
        ropes in our range of products.<br/><br/> Most items are available from inventory, allowing short delivery times and state of the art logistics.<br/><br/> We are specialized in the development and manufacture of threaded swaged end fittings and are also able to provide customized end terminations.
        </para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,4*inch)

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1
        # print'in english lang'
        return pageCount

    if(lang == 'de'):

        c.drawImage(page1BG,0,0,width=width, height=height, mask = 'auto')

        c.setFont("Helvetica-Bold",26)
        c.setFillColor('#000000')
        c.drawString(185, 5.9*inch, "AUFZUG")

        c.setFont("Helvetica-Bold",26)
        c.setFillColor('#ffffff')
        c.drawString(300, 5.9*inch, "SEILE")

        c.showPage()
        pageCount +=1

        #page2
        c.drawImage(page2BG,0,0,width=width, height=height, mask = 'auto')

        c.setFillColor('#696969')

        c.setFont("Helvetica-Bold",22)
        c.setFillColor('#0080ff')
        c.drawString(35, 8.3*inch, "GOING UP")

        c.setFont("Helvetica-Bold",22)
        c.setFillColor('#ffffff')
        c.drawString(165, 8.3*inch, "IST UNSERE DEVISE .")

        tp = Paragraph('<para fontName = FrutigerR fontsize=8.75 align="Justify" leading=13> Mit unseren zwei Produktionsstätten in der Schweiz und in China produ-zieren wir Aufzugseile für den Weltmarkt. Seit Jahrzehnten haben sichunsere Seile im Einsatz bewährt und befördern täglich Millionen vonPassagieren und Millionen Tonnen an Gütern sicher und komfortabel.Besonders in schnellen Anlagen mit großen Förderhöhen beweisen Aufzugseile von Brugg Lifting ihre ausgezeichnete Leistungsfähigkeitund sorgen dabei für Laufruhe, eine überdurchschnittliche Lebensdau-er und eine hohe Wirtschaftlichkeit.</para>',stylesN)

        tp1 = Paragraph('<para fontName = FrutigerR fontsize=8.75 align="Justify" leading=15>Die Entwicklung neuer und innovativer Produkte, die stetige Ver-besserung bereits bestehender Produkte sowie die Optimierung der Produktionsabläufe sorgen dafür, dass Brugg Lifting-Kunden sich stets auf eine konstant hohe Produktqualität verlassen und immer über die leistungsfähigsten Produkte verfügen können.</para>',stylesN)

        tp2 = Paragraph('<para fontName = FrutigerR fontsize=8.75 align="Justify" leading=15>Um unseren Kunden mehr Flexibilität und Innovationsspielraum zuermöglichen, fertigen wir unsere Trag- und Reglerseile auch nach ent-sprechender Kundenspezifikation</para>',stylesN)

        tp3 = Paragraph('<para fontName = FrutigerR fontsize=8.75 align="Justify" leading=15>Gemeinsam mit unseren Logistik- und Vertriebspartnern stellen wir weltweit sicher, dass unsere Produkte korrekt verpackt und beschriftet zur richtigen Zeit am richtigen Ort für unsere Kunden verfügbar sind. Unsere Leistungsmerkmale überzeugen. Deshalb setzen nicht nur in-ternationale Aufzugsbaukonzerne, sondern auch immer mehr mittlere und kleine Unternehmen auf Aufzugseile von Brugg Lifting.</para>',stylesN)

        tpt=[[tp],[tp1],[tp2],[tp3]]
        tptab=Table(tpt ,colWidths=4*inch)
        tptab.setStyle(TableStyle([
                            ('TOPPADDING',(0,0),(-1,-1),10)

                             ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,215,90)


        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        #page3
        c.drawImage(page3BG,0,0,width=width, height=height, mask = 'auto')


        b00 =Paragraph('<para fontName = FrutigerR fontsize=9>828m</para>',stylesN)
        # b001 =Paragraph('<para fontName = FrutigerR fontsize=9>2.717ft</para>',stylesN)
        b002 =Paragraph('<para fontName = FrutigerR fontsize=9>Burj Khalifa·Dubai.VAE</para>',stylesN)

        data1 = [[b00,b002]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,750)

        b991 =Paragraph('<para fontName = FrutigerR fontsize=9>553m</para>',stylesN)
        # b9912 =Paragraph('<para fontName = FrutigerR fontsize=9>1.814ft</para>',stylesN)
        b9913 =Paragraph('<para fontName = FrutigerR fontsize=9>One World Trade Center New York USA</para>',stylesN)

        data1 = [[b991,b9913]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,500)

        b882 =Paragraph('<para fontName = FrutigerR fontsize=9>541m</para>',stylesN)
        # b8821 =Paragraph('<para fontName = FrutigerR fontsize=9>1.775ft</para>',stylesN)
        b8822 =Paragraph('<para fontName = FrutigerR fontsize=9>CN Tower·Toronto.CDN</para>',stylesN)

        data1 = [[b882,b8822]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,513)

        b3 =Paragraph('<para fontName = FrutigerR fontsize=9>468m</para>',stylesN)
        # b31 =Paragraph('<para fontName = FrutigerR fontsize=9>1.535ft</para>',stylesN)
        b32 =Paragraph('<para fontName = FrutigerR fontsize=9>Oriental Pearl.Shangai.CN</para>',stylesN)

        data1 = [[b3,b32]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,435)


        b4 =Paragraph('<para fontName = FrutigerR fontsize=9>452m</para>',stylesN)
        # b41 =Paragraph('<para fontName = FrutigerR fontsize=9>1.483ft</para>',stylesN)
        b42 =Paragraph('<para fontName = FrutigerR fontsize=9>Petroans Tower. Kulala Lumpur.MAL</para>',stylesN)

        data1 = [[b4,b42]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,425)

        b5 =Paragraph('<para fontName = FrutigerR fontsize=9>449m</para>',stylesN)
        # b51 =Paragraph('<para fontName = FrutigerR fontsize=9>1.473ft</para>',stylesN)
        b52 =Paragraph('<para fontName = FrutigerR fontsize=9>Empire State Building.NewYork .USA</para>',stylesN)

        data1 = [[b5,b52]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,415)

        b6 =Paragraph('<para fontName = FrutigerR fontsize=9>448m</para>',stylesN)
        # b61 =Paragraph('<para fontName = FrutigerR fontsize=9>1.470ft</para>',stylesN)
        b62 =Paragraph('<para fontName = FrutigerR fontsize=9>Federation Tower. Moscow.RUS</para>',stylesN)

        data1 = [[b6,b62]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,400)

        b7 =Paragraph('<para fontName = FrutigerR fontsize=9>412m</para>',stylesN)
        # b71 =Paragraph('<para fontName = FrutigerR fontsize=9>1.352ft</para>',stylesN)
        b72 =Paragraph('<para fontName = FrutigerR fontsize=9>IFC .Hongkong .CN</para>',stylesN)

        data1 = [[b7,b72]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,375)

        b8 =Paragraph('<para fontName = FrutigerR fontsize=9>351m</para>',stylesN)
        # b81 =Paragraph('<para fontName = FrutigerR fontsize=9>1.033ft</para>',stylesN)
        b82 =Paragraph('<para fontName = FrutigerR fontsize=9>Stratosphere Tower. Las Vegas. USA</para>',stylesN)

        data1 = [[b8,b82]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,340)

        height2 = 293


        b11 =Paragraph('<para fontName = FrutigerR fontsize=9>310m</para>',stylesN)
        # b111 =Paragraph('<para fontName = FrutigerR fontsize=9>1.017ft</para>',stylesN)
        b112 =Paragraph('<para fontName = FrutigerR fontsize=9>Telekom HQ. Kuala Lumpur.MAL</para>',stylesN)

        data1 = [[b11,b112]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,height2)
        height2 = height2 -10

        b12 =Paragraph('<para fontName = FrutigerR fontsize=9>297m</para>',stylesN)
        # b121 =Paragraph('<para fontName = FrutigerR fontsize=9>974ft</para>',stylesN)
        b122 =Paragraph('<para fontName = FrutigerR fontsize=9>Comcast Center . Philadelphia.USA</para>',stylesN)

        data1 = [[b12,b122]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,height2)
        height2 = height2 -10

        b13 =Paragraph('<para fontName = FrutigerR fontsize=9>288m</para>',stylesN)
        # b131 =Paragraph('<para fontName = FrutigerR fontsize=9>945ft</para>',stylesN)
        b132 =Paragraph('<para fontName = FrutigerR fontsize=9>Plaza 66. Shangai .CN</para>',stylesN)

        data1 = [[b13,b132]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,height2)
        height2 = height2 -10

        b14 =Paragraph('<para fontName = FrutigerR fontsize=9>284m</para>',stylesN)
        # b141 =Paragraph('<para fontName = FrutigerR fontsize=9>932ft</para>',stylesN)
        b142 =Paragraph('<para fontName = FrutigerR fontsize=9>Tomorrow Square. Shanghai . CN</para>',stylesN)

        data1 = [[b14,b142]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,height2)
        height2 = height2 -10

        b15 =Paragraph('<para fontName = FrutigerR fontsize=9>280m</para>',stylesN)
        # b151 =Paragraph('<para fontName = FrutigerR fontsize=9>919ft</para>',stylesN)
        b152 =Paragraph('<para fontName = FrutigerR fontsize=9>Foreign Ministry . MOscow. RUS</para>',stylesN)

        data1 = [[b15,b152]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,height2)
        height2 = height2 -10

        b16 =Paragraph('<para fontName = FrutigerR fontsize=9>233m</para>',stylesN)
        # b161 =Paragraph('<para fontName = FrutigerR fontsize=9>764ft</para>',stylesN)
        b162 =Paragraph('<para fontName = FrutigerR fontsize=9>Harbourfront.Hong Kong . CN</para>',stylesN)
        data1 = [[b16,b162]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,height2)
        height2 = height2 -10

        b17 =Paragraph('<para fontName = FrutigerR fontsize=9>225m</para>',stylesN)
        # b171 =Paragraph('<para fontName = FrutigerR fontsize=9>738ft</para>',stylesN)
        b172 =Paragraph('<para fontName = FrutigerR fontsize=9>Torre Mayor . Mexico City. MEX</para>',stylesN)
        data1 = [[b17,b172]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,height2)
        height2 = height2 -10

        b18 =Paragraph('<para fontName = FrutigerR fontsize=9>218m</para>',stylesN)
        # b181 =Paragraph('<para fontName = FrutigerR fontsize=9>715ft</para>',stylesN)
        b182 =Paragraph('<para fontName = FrutigerR fontsize=9>Shang Mao Real Estate. Nnanjing. CN</para>',stylesN)
        data1 = [[b18,b182]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,height2)
        height2 = height2 -10

        b19 =Paragraph('<para fontName = FrutigerR fontsize=9>213m</para>',stylesN)
        # b191 =Paragraph('<para fontName = FrutigerR fontsize=9>699ft</para>',stylesN)
        b192 =Paragraph('<para fontName = FrutigerR fontsize=9>Shangria-La . Hong Kong. CN</para>',stylesN)
        data1 = [[b19,b192]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,height2)
        height2 = height2 -35

        b20 =Paragraph('<para fontName = FrutigerR fontsize=9>177m</para>',stylesN)
        # b201 =Paragraph('<para fontName = FrutigerR fontsize=9>581ft</para>',stylesN)
        b202 =Paragraph('<para fontName = FrutigerR fontsize=9>Millenium Tower . Vienna .A</para>',stylesN)
        data1 = [[b20,b202]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,height2)
        height2 = height2 -10

        b21 =Paragraph('<para fontName = FrutigerR fontsize=9>169m</para>',stylesN)
        # b211 =Paragraph('<para fontName = FrutigerR fontsize=9>554ft</para>',stylesN)
        b212 =Paragraph('<para fontName = FrutigerR fontsize=9>Shalom Center . Tele Aviv. IL</para>',stylesN)
        data1 = [[b21,b212]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,height2)
        height2 = height2 -10

        b22 =Paragraph('<para fontName = FrutigerR fontsize=9>153m</para>',stylesN)
        # b221 =Paragraph('<para fontName = FrutigerR fontsize=9>502ft</para>',stylesN)
        b222 =Paragraph('<para fontName = FrutigerR fontsize=9>Fairmont (Park Plaza).Dubai.UAE</para>',stylesN)
        data1 = [[b22,b222]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,height2)
        height2 = height2 -10

        b23 =Paragraph('<para fontName = FrutigerR fontsize=9>138m</para>',stylesN)
        # b231 =Paragraph('<para fontName = FrutigerR fontsize=9>453ft</para>',stylesN)
        b232 =Paragraph('<para fontName = FrutigerR fontsize=9>Twintower.Vienna. A</para>',stylesN)
        data1 = [[b23,b232]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,height2)
        height2 = height2 -10

        b24 =Paragraph('<para fontName = FrutigerR fontsize=9>135m</para>',stylesN)
        # b241 =Paragraph('<para fontName = FrutigerR fontsize=9>443ft</para>',stylesN)
        b242 =Paragraph('<para fontName = FrutigerR fontsize=9>Nurnberger Versicherung . Nuremberg . DE</para>',stylesN)
        data1 = [[b24,b242]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,height2)
        height2 = height2 -10



        b25 =Paragraph('<para fontName = FrutigerR fontsize=9>130m</para>',stylesN)
        # b251 =Paragraph('<para fontName = FrutigerR fontsize=9>427ft</para>',stylesN)
        b252 =Paragraph('<para fontName = FrutigerR fontsize=9>Castor. Frankfurt.DE</para>',stylesN)
        data1 = [[b25,b252]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,height2)
        height2 = height2 -30



        b26 =Paragraph('<para fontName = FrutigerR fontsize=9>105m</para>',stylesN)
        # b261 =Paragraph('<para fontName = FrutigerR fontsize=9>344ft</para>',stylesN)
        b262 =Paragraph('<para fontName = FrutigerR fontsize=9>Messeturm .BelevatorCodeasel.CH</para>',stylesN)
        data1 = [[b26,b262]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,height2)
        height2 = height2 -20


        b27 =Paragraph('<para fontName = FrutigerR fontsize=9>96m</para>',stylesN)
        # b271 =Paragraph('<para fontName = FrutigerR fontsize=9>226ft</para>',stylesN)
        b272 =Paragraph('<para fontName = FrutigerR fontsize=9>Platinum Tower.Tel Aviv .IL</para>',stylesN)
        data1 = [[b27,b272]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,height2)

        # data1 = [['','',''],['','',''],['','',''],['','',''],[b882,b8821,b8822],[b3,b31,b32],[b4,b41,b42],[b5,b51,b52],[b6,b61,b62],['','',''],[b7,b71,b72],['','',''],['','',''],[b8,b81,b82],['','',''],[b10,b101,b102],[b11,b111,b112],[b12,b121,b122],[b13,b131,b132],[b14,b141,b142],[b15,b151,b152],[b16,b161,b162],[b17,b171,b172],[b18,b181,b182],[b19,b191,b192],[',',''],[b20,b201,b202],[b21,b211,b212],[b22,b221,b222],[b23,b231,b232],[b24,b241,b242],[b25,b251,b252],['','',''],[b26,b261,b262],[b27,b271,b272]]
        # t1 = Table(data1,colWidths=[1.5*cm,1.75*cm,7.25*cm])
        # t1.wrapOn(c,width,height)
        # t1.drawOn(c,4.4*inch,100)

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        #page 4

        c.drawImage(page4BG,0,0,width=width, height=height, mask = 'auto')

        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold",22)
        c.drawString(40, 8.3*inch, "LEISTUNGEN, DIE ÜBERZEUGEN.")
        c.setFillGray(0.5)

        tp = Paragraph('<para fontName = FrutigerB fontsize=12 leftindent=13  ><b>Systemlieferant</b></para>',stylesN)
        tp2 = Paragraph('<para fontName = FrutigerR fontsize=9  align="Justify" leading=15>Sie finden bei uns ein umfassendes Sortiment an Aufzugseilen, Zubehör und Hilfs-mitteln, um Ihre Bedürfnisse vollständig abzudecken. Wir beliefern Sie mit Komplett-lösungen oder individuell zusammengestellten Komponenten, als Einzelteile oder vormontiert, ganz nach Ihren Wünschen.</para>',stylesN)
        tpt=[[tp],[tp2]]
        tptab=Table(tpt,colWidths=5.5*inch)
        tptab.setStyle(TableStyle([
                                    ('LEFTPADDING',(0,1),(-1,-1),20),
                               ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,1.25*inch, 420)

        tp = Paragraph('<para fontName = FrutigerB fontsize=12 leftindent=13  ><b>Kundenspezifisch</b></para>',stylesN)
        tp2 = Paragraph('<para fontName = FrutigerR fontsize=9  align="Justify" leading=15>In unserem breiten Sortiment an Aufzugseilen, Zubehör und Hilfsmitteln finden Siebeinahe alle benötigten Produkte für Ihre Anwendung. Falls keiner der im Katalog abgebildeten Artikel Ihr Problem löst, oder Ihr Aufzug spezifische Anforderungen er-füllen soll, beraten wir Sie gerne und erarbeiten individuelle Lösungen.</para>',stylesN)
        tpt=[[tp],[tp2]]
        tptab=Table(tpt,colWidths=5.5*inch)
        tptab.setStyle(TableStyle([
                                    ('LEFTPADDING',(0,1),(-1,-1),20),
                               ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,1.25*inch, 340)

        tp = Paragraph('<para fontName = FrutigerB fontsize=12 leftindent=13  ><b>Verfügbarkeit</b></para>',stylesN)
        tp2 = Paragraph('<para fontName = FrutigerR fontsize=9 align="Justify" leading=15 >Dank unserer zwei Produktionsstätten in der Schweiz und in China sowie einem globalen Netz an Lagerstandorten werden unsere Produkte innert kürzester Zeit in Ihr Werk oder auf Ihre Baustelle geliefert. Kontaktieren Sie uns bei Fragen zu Terminen, individuellen Lieferungen und spezifischen Projekten.</para>',stylesN)
        tpt=[[tp],[tp2]]
        tptab=Table(tpt,colWidths=5.5*inch)
        tptab.setStyle(TableStyle([
                                    ('LEFTPADDING',(0,1),(-1,-1),20),
                               ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,1.25*inch, 250)

        tp = Paragraph('<para fontName = FrutigerB fontsize=12 leftindent=13  ><b>Expressdienst</b></para>',stylesN)
        tp2 = Paragraph('<para fontName = FrutigerR fontsize=9 align="Justify" leading=15 >In dringenden Fällen stellen wir das benötigte Material in Stundenfrist ab Werk bereit und schicken es Ihnen schnellstmöglich per Kurier weltweit zu.</para>',stylesN)
        tpt=[[tp],[tp2]]
        tptab=Table(tpt,colWidths=5.5*inch)
        tptab.setStyle(TableStyle([

                                    ('LEFTPADDING',(0,1),(-1,-1),20)
                               ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,1.25*inch, 200)

        tp = Paragraph('<para fontName = FrutigerB fontsize=12 leftindent=13  ><b>Internationale Standards</b></para>',stylesN)
        tp2 = Paragraph('<para fontName = FrutigerR fontsize=9 align="Justify" leading=15 >BRUGG LIFTING ist nach ISO 9001:2015 und ISO 14001:2015 zertifiziert.</para>',stylesN)
        tpt=[[tp],[tp2]]
        tptab=Table(tpt,colWidths=5.5*inch)
        tptab.setStyle(TableStyle([
                                    ('LEFTPADDING',(0,1),(-1,-1),20),
                               ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,1.25*inch, 140)

        tp = Paragraph('<para fontName = FrutigerB fontsize=12 leftindent=13  ><b>Schulungen/Fachseminare</b></para>',stylesN)
        tp2 = Paragraph('<para fontName = FrutigerR fontsize=9 align="Justify" leading=15 >Unser Ziel ist, Sie beim optimalen Einsatz und der Erhöhung der maximalen Lebens-dauer Ihrer Aufzugseile zu unterstützen. Zur Aus- und Weiterbildung Ihrer Mitarbeiter bieten wir Ihnen qualifizierte und individualisierte Schulungen an.</para>',stylesN)
        tpt=[[tp],[tp2]]
        tptab=Table(tpt,colWidths=5.5*inch)
        tptab.setStyle(TableStyle([
                                    ('LEFTPADDING',(0,1),(-1,-1),20),
                               ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,1.25*inch, 60)

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        #page 5

        c.drawImage(page5BG,0,0,width=width, height=height, mask = 'auto')

        gm = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>Going up ist unsere Devise.</para>',stylesN)
        n = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>2</para>',stylesN)
        gm1 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>Leistungen, die überzeugen</para>',stylesN)
        gmn1 = Paragraph('<para fontName = FrutigerR fontName = FrutigerR fontsize=8  leading=10>4</para>',stylesN)
        gm2 = Paragraph('<para fontName = FrutigerR fontName = FrutigerR fontsize=8  leading=10>Seile im Überblick</para>',stylesN)
        gmn2 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>6</para>',stylesN)

        gm3 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>Seilvergleich</para>',stylesN)
        gmn3 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>8</para>',stylesN)

        gm4 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>Seilvergleich . i-Line</para>',stylesN)
        gmn4 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>9</para>',stylesN)

        gm5 = Paragraph('<para fontName = FrutigerB fontsize=8  leading=10><b>Aufzugseile . Zubehör</b></para>',stylesN)
        gmn5 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>10</para>',stylesN)

        gm6 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>Tragseile</para>',stylesN)
        gm7 = Paragraph('<para fontName = FrutigerR fontsize=8 leftindent = 15 leading=10>HRS</para>',stylesN)
        gmn7 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>12</para>',stylesN)

        gm8 = Paragraph('<para fontName = FrutigerR fontsize=8  leftindent = 15 leading=10>DP9</para>',stylesN)
        gmn8 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>13</para>',stylesN)
        gm9 = Paragraph('<para fontName = FrutigerR fontsize=8 leftindent = 15  leading=10>MCX9</para>',stylesN)
        gmn9 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>15</para>',stylesN)

        gm10 = Paragraph('<para fontName = FrutigerR fontsize=8 leftindent = 15  leading=8>SCX9</para>',stylesN)
        gmn10 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=8>14</para>',stylesN)

        gm11 = Paragraph('<para fontName = FrutigerR fontsize=8 leftindent = 15  leading=10>8x19</para>',stylesN)
        gmn11 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>16</para>',stylesN)

        gm12 = Paragraph('<para fontName = FrutigerR fontsize=8  leftindent = 15 leading=10>TSR</para>',stylesN)
        gmn12 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>17</para>',stylesN)
        gm13 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>Gewichtsausgleichsseile</para>',stylesN)
        gm14 = Paragraph('<para fontName = FrutigerR fontsize=8  leftindent = 15 leading=10>8x19.8x25</para>',stylesN)
        gmn14 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>18</para>',stylesN)
        gm15 = Paragraph('<para fontName = FrutigerR fontsize=8  leftindent = 15 leading=10>6x25</para>',stylesN)
        gmn15 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>19</para>',stylesN)
        gm16 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>Geschwindigkeitsbegrenzerseile</para>',stylesN)
        gm17 = Paragraph('<para fontName = FrutigerR fontsize=8  leftindent = 15 leading=10>6x19.8x19</para>',stylesN)
        gmn17 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>20</para>',stylesN)

        gm18 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>Bezeichnungen und Klassifizierungen</para>',stylesN)
        gmn18 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>21</para>',stylesN)

        gm19 = Paragraph('<para fontName = FrutigerR fontsize=8   leftindent = 15 leading=10>APAG Anpress-Aussengewinde</para>',stylesN)
        gmn19 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>22</para>',stylesN)

        gm20 = Paragraph('<para fontName = FrutigerR fontsize=8  leftindent = 15 leading=10>Ösenschraube mit Kausche verpresst</para>',stylesN)
        gmn20 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>23</para>',stylesN)

        gm21 = Paragraph('<para fontName = FrutigerR fontsize=8   leftindent = 15 leading=10>Seilschloss asymmetrisch</para>',stylesN)
        gmn21 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>24</para>',stylesN)

        gm22 = Paragraph('<para fontName = FrutigerR fontsize=8 leftindent = 15  leading=10>Elastomerpuffer</para>',stylesN)
        gmn22 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>26</para>',stylesN)

        gm23 = Paragraph('<para fontName = FrutigerR fontsize=8 leftindent = 15 leading=10>Feder</para>',stylesN)
        gmn23 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>27</para>',stylesN)

        gm24 = Paragraph('<para fontName = FrutigerR fontsize=8  leftindent = 15 leading=10>Türseilsets</para>',stylesN)
        gmn24 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>28</para>',stylesN)

        gm25 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>Türseil Flex . Bügelseilklemme</para>',stylesN)
        gmn25 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>29</para>',stylesN)

        gm25 = Paragraph('<para fontName = FrutigerR fontsize=8  leftindent = 15 leading=10>RPM Seilspannungsmessgerät</para>',stylesN)
        gmn25 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>30</para>',stylesN)

        gm26 = Paragraph('<para fontName = FrutigerR fontsize=8  leftindent = 15 leading=10>GDC Rillenmessgerät</para>',stylesN)
        gmn26 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>31</para>',stylesN)

        gm27 = Paragraph('<para fontName = FrutigerR fontsize=8  leftindent = 15 leading=10>RWG Seilprüflehre</para>',stylesN)
        gmn27 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>31</para>',stylesN)


        gm29 = Paragraph('<para fontName = FrutigerR fontsize=8 leftindent = 15 leading=10>VT-Lube Seilschmiermittel</para>',stylesN)
        gmn29 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>32</para>',stylesN)

        gm30 = Paragraph('<para fontName = FrutigerR fontsize=8  leftindent = 15 leading=10>Drahtseilscheren</para>',stylesN)
        gmn30 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>32</para>',stylesN)

        gm31 = Paragraph('<para fontName = FrutigerR fontsize=8 leftindent = 15 leading=10>Verpackung</para>',stylesN)
        gmn31 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>33</para>',stylesN)

        # gm32 = Paragraph('<para fontName = FrutigerR fontsize=8 leftindent = 15 leading=10>Packaging</para>',stylesN)
        # gmn32 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>35</para>',stylesN)

        gm33 = Paragraph('<para fontName = FrutigerB fontsize=8  leading=10><b>Support</b></para>',stylesN)
        gmn33 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>34</para>',stylesN)

        gm34 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>Kontakt</para>',stylesN)
        gmn34 = Paragraph('<para fontName = FrutigerR fontsize=8  leading=10>35</para>',stylesN)

        data =  [[gm,n],[gm1,gmn1],[gm2,gmn2],[gm3,gmn3],[gm4,gmn4],['',''],[gm5,gmn5],[gm6],[gm7,gmn7],[gm8,gmn8],[gm10,gmn10],[gm9,gmn9],[gm11,gmn11],[gm12,gmn12],[gm13],[gm14,gmn14],[gm15,gmn15],[gm16],[gm17,gmn17],[gm18,gmn18],[gm19,gmn19],[gm20,gmn20],[gm21,gmn21],[gm22,gmn22],[gm23,gmn23],[gm24,gmn24],[gm25,gmn25],[gm26,gmn26],[gm27,gmn27],[gm29,gmn29],[gm30,gmn30],[gm31,gmn31],['',''],[gm33,gmn33],[gm34,gmn34]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5*mm)
        t.setStyle(TableStyle([
                            # ('LINEABOVE',(0,0),(-1,-1),0.1,colors.white),
                            ('LINEBELOW',(0,0),(-1,-1),0.1,colors.white),
                            ('FONTSIZE', (0, 0), (-1, -1), 7),
                            ('ALIGN',(0,13),(-2,-16),'CENTER'),
                            ('ALIGN',(0,19),(-2,-10),'CENTER'),
                            ('ALIGN',(0,20),(-2,-3),'LEFT'),
                            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                             ]))

        t.wrapOn(c,width, height)
        t.drawOn(c, 4.75*inch,0.5*inch)

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.white),
                             ]))
        t.wrapOn(c,width, height)
        t.drawOn(c, -3*inch,0.2*inch)

        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        # maa = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P7TransStrip.png')
        c.drawImage(page6BG,0,0,width=width,height=height,mask = 'auto')

        height2 = 450
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold",22)
        c.drawString(30, 8.3*inch, "ROPES AT A GLANCE")

        templatesTractionRopes = productTemplatesObjects.filter(parent_name = 'traction-ropes')
        templatesTractionRopes2 = list(productTemplatesObjects.filter(parent_name = 'traction-ropes'))
        templateCompensationRopes = list(productTemplatesObjects.filter(parent_name = 'compensation-ropes'))
        templatesGovernorRopes = list(productTemplatesObjects.filter(parent_name = 'governor-ropes'))
        templatesInnovation = productTemplatesObjects.filter(parent_name = 'innovation')

        totalNumberOFTempletes = len(productTemplatesObjects) - len(templatesInnovation)

        templatesTractionRopes2.extend(templateCompensationRopes)
        templatesTractionRopes2.extend(templatesGovernorRopes)

        if totalNumberOFTempletes>5:
            maxNumberItems = 5
            index = float(totalNumberOFTempletes)/maxNumberItems
            # printindex
            index = int(math.ceil(index))
            # printindex, range(index),"index ...."
            for i in range(index):
                if i == index:
                    data = templatesTractionRopes2[maxNumberItems*i+1:-1]

                else:
                    data = templatesTractionRopes2[maxNumberItems*i:maxNumberItems*(i+1)]
                # printlen(data), "data length"
                pageCount =  addTemplateList(c,width, height,data,stylesN,page6BG,pageCount,lang)

        else:
            pageCount = addTemplateList(c,width, height,templatesTractionRopes2,stylesN,page6BG,pageCount,lang)



        #page 8

        c.drawImage(page8BG,0,0,width=width,height=height,mask='auto')

        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold",22)
        c.drawCentredString(138, 8.25*inch, "SEILVERGLEICH")

        # textobject = c.beginText()
        # textobject.setTextOrigin(40, 7.9*inch)
        # c.setFillColor('#3C434B')
        # textobject.setFont("Helvetica-Bold", 12)
        # textobject.textLines('''
        #                         Elastic Elongation
        #                          ''')
        # c.drawText(textobject)

        # c.drawImage(i3,40,4.2*inch,width=3.5*inch,height=3.5*inch)
        #
        # c.drawImage(i4,43,0.5*inch,width=3.75*inch,height=3*inch)

        ad1 = Paragraph('<para fontName = FrutigerR leftindent=10 align="justify"fontsize=9 leading=10><bullet>&bull;</bullet>Seildehnung, die durch die Belastung des Seils entsteht</para>',stylesN)
        ad2 = Paragraph('<para fontName = FrutigerR leftindent=10 align="justify"fontsize=9 leading=10><bullet>&bull;</bullet>Bei Aufhebung der Belastung formt sich das Seil wieder in den Aus-gangszustand zurück</para>',stylesN)
        ad3 = Paragraph('<para fontName = FrutigerR leftindent=10 align="justify"fontsize=9 leading=10><bullet>&bull;</bullet>Beispiel: Bei einem DP9 Seil entsteht bei einer Belastung von 8,3 %der Mindestbruchkraft eine elastische Dehnung von ca. 0,109 % derSeillänge (bei einer Seillänge von 100 m entspricht dies 109 mm)</para>',stylesN)
        ad4 = Paragraph('<para fontName = FrutigerR leftindent=10 align="justify"fontsize=9 leading=10><bullet>&bull;</bullet>Aufzugseile von BRUGG LIFTING zeichnen sich insbesondere durcheine sehr geringe elastische Dehnung aus</para>',stylesN)

        a = [[ad1],[ad2],[ad3],[ad4]]
        at=Table(a,colWidths=9.5*cm)
        at.wrapOn(c,width,height)
        at.drawOn(c,4*inch,5.1*inch)

        ad1 = Paragraph('<para fontName = FrutigerR leftindent=10 align="justify"fontsize=9 leading=12><bullet>&bull;</bullet>Die Grafik zeigt die Dehnung des Seiles, die eintritt bissich das Seil durch den Betrieb gesetzt hat. Diese wird bei etwa 2% der mutmasslichen Seillebensdauer erwartet</para>',stylesN)
        ad2 = Paragraph('<para fontName = FrutigerR leftindent=10 align="justify"fontsize=9 leading=12><bullet>&bull;</bullet>Hier wird die bleibende Dehnung der unterschiedlichen Tragseiltypen verglichen</para>',stylesN)
        ad3 = Paragraph('<para fontName = FrutigerR leftindent=10 align="justify"fontsize=9 leading=12><bullet>&bull;</bullet>Aufzugseile von BRUGG LIFTING zeichnen sich insbe- sondere durch eine sehr geringe bleibende Dehnungaus</para>',stylesN)

        a = [[ad1],[ad2],[ad3]]
        at=Table(a,colWidths=9.25*cm)
        at.wrapOn(c,width,height)
        at.drawOn(c,4.25*inch,1.85*inch)
        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        #page 9

        # bg8 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P9Hbox.svg')
        # i5 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','i5.png')

        # c.drawImage(b3,0*inch,8.25*inch,width=8.5*inch,height=3*inch)
        #
        # c.drawImage(bg7,0*inch,8.25*inch,width=8.5*inch,height=0.25*inch,mask='auto')

        c.drawImage(page9BG,0,0,width=width,height=height,mask='auto')


        i = Paragraph('<para color=white fontsize=22><b>SEILVERGLEICH .<span color=rgb(0,157,224)><b> i</b></span>LINE</b></para>',stylesN)
        di = [[i]]
        dti = Table(di)
        dti.wrapOn(c,width,height)
        dti.drawOn(c,30,8.25*inch)


        # textobject = c.beginText()
        # textobject.setTextOrigin(40, 7.9*inch)
        # c.setFillColor('#3C434B')
        # textobject.setFont("Helvetica-Bold", 12)
        # textobject.textLines('''
        #                         Minimum Breaking Load
        #                          ''')
        # c.drawText(textobject)

        # c.drawImage(i5,40,4.7*inch,width=4*inch,height=3*inch)
        #
        # c.drawImage(i6,370,1.3*inch,width=2*inch,height=2.5*inch)
        #
        # c.drawImage(i7,535,0.7*inch,width=1*inch,height=3*inch)

        ad1 = Paragraph('<para fontName= FrutigerR leftindent=10 align="justify" fontsize=9 leading=12><bullet>&bull;</bullet>MBK zeigt die Kraft mit welcher ein Seil mindestens belastet werden kann bevor es bricht</para>',stylesN)
        ad2 = Paragraph('<para fontName= FrutigerR leftindent=10 align="justify"fontsize=9 leading=12><bullet>&bull;</bullet>Die Grafik vergleicht die Mindestbruchkräfte der unter-schiedlichen Tragseiltypen</para>',stylesN)
        ad3 = Paragraph('<para fontName= FrutigerR leftindent=10 align="justify"fontsize=9 leading=12><bullet>&bull;</bullet>Referenz: 100 % = 8x19 Tragseil mit Naturfasereinlage</para>',stylesN)

        a = [[ad1],[ad2],[ad3]]
        at=Table(a,colWidths=9*cm)
        at.wrapOn(c,width,height)
        at.drawOn(c,4.25*inch,5.95*inch)

        id =Paragraph('<para fontName= FrutigerB fontsize=15 spaceAfter=2><span color=rgb(0,157,224)><b>i</b></span><b>Line & Farbcode</b><br/></para>',stylesN)
        id1 =Paragraph('<para fontName= FrutigerR fontsize=10 leading=13 align="justify">Korrekt installierte Tragseile erhöhen die Lebensdauer und die Sicher-heit. Sie verbessern den Fahrkomfort und vermeiden Stillstandzeiten.Unabhängig von Konstruktion und Hersteller ist jedes Tragseil während der Installation anfällig gegenüber Aufdrehen.</para>',stylesN)
        id2 =Paragraph('<para fontName= FrutigerR fontsize=10 leading=13 align="justify">Mit Hilfe der i-LINE, die von BRUGG LIFTING bereits während der Pro-duktion auf die Tragseile aufgebracht wird, lassen sich aufgedrehte Tragseile jedoch leicht und schnell erkennen, lokalisieren und korrekt ausrichten.</para>',stylesN)

        idd = [[id],'',[id1],[id2]]
        idt = Table(idd,colWidths=10*cm)
        idt.wrapOn(c,width,height)
        idt.drawOn(c,40,2*inch)

        ad = Paragraph('<para  fontName= FrutigerB align="justify" fontsize=13 leading=15><b>Vorteile der<span color=rgb(0,157,224)><b>i</b></span>LINE</b></para>',stylesN)
        ad1 = Paragraph('<para fontName= FrutigerR leftindent=13 align="justify" fontsize=10 leading=15><bullet>&bull;</bullet>einfache und korrekte Installation</para>',stylesN)
        ad2 = Paragraph('<para fontName= FrutigerR leftindent=10 align="justify"fontsize=10 leading=15><bullet>&bull;</bullet>maximale Anwendersicherheit</para>',stylesN)
        ad3 = Paragraph('<para fontName= FrutigerR leftindent=10 align="justify"fontsize=10 leading=15><bullet>&bull;</bullet>optimale Produktleistung</para>',stylesN)
        ad4 = Paragraph('<para fontName= FrutigerR leftindent=10 align="justify"fontsize=10 leading=15><bullet>&bull;</bullet>Farbcode zur Seiltyperkennung</para>',stylesN)

        a = [[ad],[ad1],[ad2],[ad3],[ad4]]
        at=Table(a,colWidths=9.5*cm)
        at.wrapOn(c,width,height)
        at.drawOn(c,40,0.3*inch)

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        #page 10
        # bg9 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P11Hbox.svg')
        # e5 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P10bgGred.png')
        # e2 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P10Bannerimg.png')
        # e1 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P10Strip.png')
        # e3 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P11Strip.png')
        # e4 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P11Strip.svg')
        # e6 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P11img3.png')
        # e7 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P10BruggLiftingCom.png')
        # bgp11 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','p11BannerImg.png')


        # c.drawImage(e5,0*inch,0*inch,width=8.5*inch,height=8.25*inch)
        #
        # c.drawImage(e2,0*inch,8.25*inch,width=8.5*inch,height=3*inch)
        # c.drawImage(e1,0*inch,8.25*inch,width=8.5*inch,height=0.9*inch,mask='auto')

        c.drawImage(page10BG,0,0,width=width,height=height,mask='auto')

        # drawing = svg2rlg(logo)
        # scaleFactor = 1./1.8
        # drawing.width *= scaleFactor
        # drawing.height *= scaleFactor
        # drawing.scale(scaleFactor, scaleFactor)
        # renderPDF.draw(drawing, c, 20,10.2*inch)

        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold",22)
        c.drawString(30, 8.25*inch, "AUFZUGSEILE . ZUBEHÖR")
        c.setFillGray(0.5)
        # c.rect(448,8.5*inch, 6*inch, 0.25*inch,stroke=0,fill=1)

        p = Paragraph('''<para fontName = FrutigerR fontsize=9  leading=12 align="justify">Aufzugseile von BRUGG LIFTING stehen für höchste Qualität.<br/><br/>Damit sich unsere Kunden auf die konstant hervorragende Qualität un-serer Produkte verlassen können, setzen wir vor, während und nachder Produktion ein umfassendes Vorgabe-, Prüf- und Kontrollsystemum. Bereits das Drahtmaterial wählen wir mit grösster Sorgfalt aus.Unsere Rohmaterialien beziehen wir ausschliesslich von Lieferanten,welche unsere hohen Anforderungen dauerhaft erfüllen. Eine moderneFertigungstechnologie und besonders die langjährige Erfahrung unsererqualifizierten Facharbeiter sind weitere wesentliche Faktoren für diehohe Produktqualität. Um dies garantieren zu können, kommt in denFertigungslinien modernste Mess- und Überwachungstechnik zum Ein-satz. Abschliessend durchlaufen alle unsere Produkte in unserem haus-eigenen Prüffeld umfangreiche Lebensdauer- und Eigenschaftstestsmit statistischer Auswertung.<br/><br/> Als Kunde profitieren Sie von Produkten, die sich durch allerbeste Wertehinsichtlich Dehnung, Bruchkraft, Laufruhe und Lebensdauer unddurch eine einfache Handhabung auszeichnen. Damit stehen Aufzug-seile von BRUGG LIFTING für höchste Wirtschaftlichkeit – und einPreis-Leistungsverhältnis, das immer wieder überzeugt. </para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=4*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,3.35*inch)

        # c.drawImage(i1,4.4*inch,3.75*inch,width=3.4*inch,height=3.75*inch)

        # c.drawImage(z9,0*inch,8.1*inch,width=8.5*inch,height=0.3*inch)

        # drawing = svg2rlg(z2)
        # scaleFactor = 1/1.85
        # drawing.width *= scaleFactor
        # drawing.height *= scaleFactor
        # drawing.scale(scaleFactor, scaleFactor)
        # renderPDF.draw(drawing, c, 0,8.1*inch)

        textobject = c.beginText()
        textobject.setTextOrigin(2*inch, 0.4*inch)
        textobject.setFont("Helvetica-Bold", 50)
        textobject.setFillColorRGB(255,255,255)
        textobject.textLines('''
                                brugglifting.com
                              ''')
        c.drawText(textobject)


        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        #page 11
        c.drawImage(page11BG,0,0,width=width,height=height,mask='auto')



        p = Paragraph('''<para fontName =FrutigerR fontsize=9  leading=12 align="justify">Als Systemanbieter führen wir in unserem Sortimentfür alle Aufzugseile entsprechende Endbefestigungen, Dämpfungssysteme und weiteres Zubehör.<br/><br/> Ein umfangreiches Lager, kurze Lieferzeiten und eine flexible Logistik sichern unseren Kunden eine hohe Ver-fügbarkeit.<br/><br/> Als Spezialist in der Entwicklung und Fertigung von Anpress-Aussengewinden verfügt BRUGG LIFTING über Fachkompetenz und Erfahrung, auch kundenspezifische Endbefestigungen anbieten zu können.</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths = 3.5*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,4.85*inch)

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.white),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1
        # print'in de lang'
        return pageCount


    if(lang == 'zh'):

        c.drawImage(page1BG,0,0,width=width, height=height, mask = 'auto')

        c.setFont("STSong-Light",37)
        c.setFillColor('#000000')
        c.drawString(185, 5.9*inch, "电梯钢丝绳")

        # c.setFont("MSung-Light",27)
        # c.setFillColor('#ffffff')
        # c.drawString(340, 5.9*inch, "丝绳")

        c.showPage()
        pageCount +=1

        #page2
        c.drawImage(page2BG,0,0,width=width, height=height, mask = 'auto')

        c.setFillColor('#696969')


        c.setFont("Helvetica-Bold",27)
        c.setFillColor('#0080ff')
        c.drawString(35, 8.3*inch, "GOING UP")

        c.setFont("STSong-Light",27)
        c.setFillColor('#ffffff')
        c.drawString(185, 8.3*inch, "是我们的励志箴言")


        tp = Paragraph('<para fontName = STSong-Light fontsize=11 align="Justify" leading=15>通过我们在瑞士、中国的生产基地,我们向全球的客户提供高品质的电梯 钢丝绳以及相关配套的服务。在一百多年的历史中,我们的产品与服务保证 了全球数以千万计的人们对于电梯安全,舒适的要求。我们的钢丝绳产品 因其良好的品质性能,在高速梯的使用中有着非常优良的表现,更长的寿 命以及经济价值。</para>',stylesN)

        tp1 = Paragraph('<para fontName = STSong-Light fontsize=11 align="Justify" leading=17>我们对新产品的不断开发和创新,对现有产品和工艺流程的持续改善和优 化,值得所有布鲁格用户的信赖。我们将始终保证产品的最高品质和最佳 性能。</para>',stylesN)

        tp2 = Paragraph('<para fontName = STSong-Light fontsize=11 align="Justify" leading=17>当然,我们还能够灵活的根据客户的特殊要求定制生产曳引绳和限速器绳。</para>',stylesN)

        tp3 = Paragraph('<para fontName = STSong-Light fontsize=11 align="Justify" leading=17>我们与遍布全球的物流和分销合作伙伴一起努力,确保我们在把产品准确 包装和标识后,按照顾客要求的时间和地点送达。</para>',stylesN)

        tp4 = Paragraph('<para fontName = STSong-Light fontsize=11 align="Justify" leading=17>我们产品的性能指标令人信服。因此,不仅是国际电梯生产集团,越来越多的中小型企业也都选择布鲁格电梯钢丝绳。</para>',stylesN)
        tpt=[[tp],[tp1],[tp2],[tp3],[tp4]]
        tptab=Table(tpt ,colWidths=3.8*inch)
        tptab.setStyle(TableStyle([
                            ('TOPPADDING',(0,0),(-1,-1),10)

                             ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,220,120)


        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        #page3
        c.drawImage(page3BG,0,0,width=width, height=height, mask = 'auto')


        b00 =Paragraph('<para fontName = FrutigerR fontsize=9>828m</para>',stylesN)
        # b001 =Paragraph('<para fontName = FrutigerR fontsize=9>2.717ft</para>',stylesN)
        b002 =Paragraph('<para fontName = STSong-Light fontsize=10>阿联酋 迪拜 迪拜塔</para>',stylesN)

        data1 = [[b00,b002]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,750)

        b991 =Paragraph('<para fontName = FrutigerR fontsize=9>553m</para>',stylesN)
        # b9912 =Paragraph('<para fontName = FrutigerR fontsize=9>1.814ft</para>',stylesN)
        b9913 =Paragraph('<para fontName = STSong-Light fontsize=10> 加拿大 多伦多 国家电视塔</para>',stylesN)

        data1 = [[b991,b9913]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,500)

        b882 =Paragraph('<para fontName = FrutigerR fontsize=9>541m</para>',stylesN)
        # b8821 =Paragraph('<para fontName = FrutigerR fontsize=9>1.775ft</para>',stylesN)
        b8822 =Paragraph('<para fontName = STSong-Light fontsize=10>美国 纽约 世贸中心大厦</para>',stylesN)

        data1 = [[b882,b8822]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,513)

        b3 =Paragraph('<para fontName = FrutigerR fontsize=9>468m</para>',stylesN)
        # b31 =Paragraph('<para fontName = FrutigerR fontsize=9>1.535ft</para>',stylesN)
        b32 =Paragraph('<para fontName = STSong-Light fontsize=10>中国 上海 东方明珠电视塔</para>',stylesN)

        data1 = [[b3,b32]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,435)


        b4 =Paragraph('<para fontName = FrutigerR fontsize=10>452m</para>',stylesN)
        # b41 =Paragraph('<para fontName = FrutigerR fontsize=9>1.483ft</para>',stylesN)
        b42 =Paragraph('<para fontName = STSong-Light fontsize=9>马来西亚 吉隆坡 双子星塔</para>',stylesN)

        data1 = [[b4,b42]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,425)

        b5 =Paragraph('<para fontName = FrutigerR fontsize=10>449m</para>',stylesN)
        # b51 =Paragraph('<para fontName = FrutigerR fontsize=9>1.473ft</para>',stylesN)
        b52 =Paragraph('<para fontName = STSong-Light fontsize=9>美国 纽约 帝国大厦</para>',stylesN)

        data1 = [[b5,b52]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,415)

        b6 =Paragraph('<para fontName = FrutigerR fontsize=10>448m</para>',stylesN)
        # b61 =Paragraph('<para fontName = FrutigerR fontsize=9>1.470ft</para>',stylesN)
        b62 =Paragraph('<para fontName = STSong-Light fontsize=9>俄罗斯 莫斯科 联盟大厦</para>',stylesN)

        data1 = [[b6,b62]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,400)

        b7 =Paragraph('<para fontName = FrutigerR fontsize=10>412m</para>',stylesN)
        # b71 =Paragraph('<para fontName = FrutigerR fontsize=9>1.352ft</para>',stylesN)
        b72 =Paragraph('<para fontName = STSong-Light fontsize=9>香港国际金融中心</para>',stylesN)

        data1 = [[b7,b72]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,375)

        b8 =Paragraph('<para fontName = FrutigerR fontsize=10>351m</para>',stylesN)
        # b81 =Paragraph('<para fontName = FrutigerR fontsize=9>1.033ft</para>',stylesN)
        b82 =Paragraph('<para fontName = STSong-Light fontsize=9>美国 拉斯维加斯 云霄塔</para>',stylesN)

        data1 = [[b8,b82]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,340)

        height2 = 293


        b11 =Paragraph('<para fontName = FrutigerR fontsize=10>310m</para>',stylesN)
        # b111 =Paragraph('<para fontName = FrutigerR fontsize=9>1.017ft</para>',stylesN)
        b112 =Paragraph('<para fontName = STSong-Light fontsize=9>马来西亚 吉隆坡 电讯大厦</para>',stylesN)

        data1 = [[b11,b112]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,height2)
        height2 = height2 -10

        b12 =Paragraph('<para fontName = FrutigerR fontsize=10>297m</para>',stylesN)
        # b121 =Paragraph('<para fontName = FrutigerR fontsize=9>974ft</para>',stylesN)
        b122 =Paragraph('<para fontName = STSong-Light fontsize=9>美国 费城 康卡斯特中心</para>',stylesN)

        data1 = [[b12,b122]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,height2)
        height2 = height2 -10

        b13 =Paragraph('<para fontName = FrutigerR fontsize=10>288m</para>',stylesN)
        # b131 =Paragraph('<para fontName = FrutigerR fontsize=9>945ft</para>',stylesN)
        b132 =Paragraph('<para fontName = STSong-Light fontsize=9>中国 上海 恒隆广场</para>',stylesN)

        data1 = [[b13,b132]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,height2)
        height2 = height2 -10

        b14 =Paragraph('<para fontName = FrutigerR fontsize=10>284m</para>',stylesN)
        # b141 =Paragraph('<para fontName = FrutigerR fontsize=9>932ft</para>',stylesN)
        b142 =Paragraph('<para fontName = STSong-Light fontsize=9>中国 上海 明天大厦</para>',stylesN)

        data1 = [[b14,b142]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,height2)
        height2 = height2 -10

        b15 =Paragraph('<para fontName = FrutigerR fontsize=10>280m</para>',stylesN)
        # b151 =Paragraph('<para fontName = FrutigerR fontsize=9>919ft</para>',stylesN)
        b152 =Paragraph('<para fontName = STSong-Light fontsize=9>俄罗斯 莫斯科 外交部大楼</para>',stylesN)

        data1 = [[b15,b152]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,height2)
        height2 = height2 -10

        b16 =Paragraph('<para fontName = FrutigerR fontsize=10>233m</para>',stylesN)
        # b161 =Paragraph('<para fontName = FrutigerR fontsize=9>764ft</para>',stylesN)
        b162 =Paragraph('<para fontName = STSong-Light fontsize=9>中国 香港 海名轩大厦</para>',stylesN)
        data1 = [[b16,b162]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,height2)
        height2 = height2 -10

        b17 =Paragraph('<para fontName = FrutigerR fontsize=10>225m</para>',stylesN)
        # b171 =Paragraph('<para fontName = FrutigerR fontsize=9>738ft</para>',stylesN)
        b172 =Paragraph('<para fontName = STSong-Light fontsize=9>墨西哥 墨西哥城 市长大厦</para>',stylesN)
        data1 = [[b17,b172]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,height2)
        height2 = height2 -10

        b18 =Paragraph('<para fontName = FrutigerR fontsize=10>218m</para>',stylesN)
        # b181 =Paragraph('<para fontName = FrutigerR fontsize=9>715ft</para>',stylesN)
        b182 =Paragraph('<para fontName =STSong-Light fontsize=9>中国 南京 商贸世纪广场</para>',stylesN)
        data1 = [[b18,b182]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,height2)
        height2 = height2 -10

        b19 =Paragraph('<para fontName = FrutigerR fontsize=10>213m</para>',stylesN)
        # b191 =Paragraph('<para fontName = FrutigerR fontsize=9>699ft</para>',stylesN)
        b192 =Paragraph('<para fontName =STSong-Light fontsize=9>中国 香港 香格里拉大酒店</para>',stylesN)
        data1 = [[b19,b192]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,height2)
        height2 = height2 -35

        b20 =Paragraph('<para fontName = FrutigerR fontsize=10>177m</para>',stylesN)
        # b201 =Paragraph('<para fontName = FrutigerR fontsize=9>581ft</para>',stylesN)
        b202 =Paragraph('<para fontName =STSong-Light fontsize=9>奥地利 维也纳 千禧大厦</para>',stylesN)
        data1 = [[b20,b202]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,height2)
        height2 = height2 -10

        b21 =Paragraph('<para fontName = FrutigerR fontsize=10>169m</para>',stylesN)
        # b211 =Paragraph('<para fontName = FrutigerR fontsize=9>554ft</para>',stylesN)
        b212 =Paragraph('<para fontName = STSong-Light fontsize=9>以色列 特拉维夫 沙勒中心</para>',stylesN)
        data1 = [[b21,b212]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,height2)
        height2 = height2 -10

        b22 =Paragraph('<para fontName = FrutigerR fontsize=10>153m</para>',stylesN)
        # b221 =Paragraph('<para fontName = FrutigerR fontsize=9>502ft</para>',stylesN)
        b222 =Paragraph('<para fontName = STSong-Light fontsize=9>阿联酋 迪拜 费尔蒙酒店</para>',stylesN)
        data1 = [[b22,b222]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,height2)
        height2 = height2 -10

        b23 =Paragraph('<para fontName = FrutigerR fontsize=10>138m</para>',stylesN)
        # b231 =Paragraph('<para fontName = FrutigerR fontsize=9>453ft</para>',stylesN)
        b232 =Paragraph('<para fontName = STSong-Light fontsize=9>奥地利 维也纳 双子塔</para>',stylesN)
        data1 = [[b23,b232]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,height2)
        height2 = height2 -10


        b24 =Paragraph('<para fontName = FrutigerR fontsize=10>135m</para>',stylesN)
        # b241 =Paragraph('<para fontName = FrutigerR fontsize=9>443ft</para>',stylesN)
        b242 =Paragraph('<para fontName = STSong-Light fontsize=9>德国 纽伦堡 纽伦堡保险大厦</para>',stylesN)
        data1 = [[b24,b242]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,height2)
        height2 = height2 -10


        b25 =Paragraph('<para fontName = FrutigerR fontsize=10>130m</para>',stylesN)
        # b251 =Paragraph('<para fontName = FrutigerR fontsize=9>427ft</para>',stylesN)
        b252 =Paragraph('<para fontName =STSong-Light fontsize=9>德国 法兰克福 卡斯特大楼</para>',stylesN)
        data1 = [[b25,b252]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,height2)
        height2 = height2 -30


        b26 =Paragraph('<para fontName = FrutigerR fontsize=10>105m</para>',stylesN)
        # b261 =Paragraph('<para fontName = FrutigerR fontsize=9>344ft</para>',stylesN)
        b262 =Paragraph('<para fontName = STSong-Light fontsize=9>瑞士 巴塞尔 集市钟楼</para>',stylesN)
        data1 = [[b26,b262]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,height2)
        height2 = height2 -20


        b27 =Paragraph('<para fontName = FrutigerR fontsize=10>96m</para>',stylesN)
        # b271 =Paragraph('<para fontName = FrutigerR fontsize=9>226ft</para>',stylesN)
        b272 =Paragraph('<para fontName = STSong-Light fontsize=9>以色列 特拉维夫 铂金塔</para>',stylesN)
        data1 = [[b27,b272]]
        t1 = Table(data1,colWidths=[1.5*cm,7.25*cm])
        t1.wrapOn(c,width,height)
        t1.drawOn(c,350,height2)


        # data1 = [['','',''],['','',''],['','',''],['','',''],[b882,b8821,b8822],[b3,b31,b32],[b4,b41,b42],[b5,b51,b52],[b6,b61,b62],['','',''],[b7,b71,b72],['','',''],['','',''],[b8,b81,b82],['','',''],[b10,b101,b102],[b11,b111,b112],[b12,b121,b122],[b13,b131,b132],[b14,b141,b142],[b15,b151,b152],[b16,b161,b162],[b17,b171,b172],[b18,b181,b182],[b19,b191,b192],[',',''],[b20,b201,b202],[b21,b211,b212],[b22,b221,b222],[b23,b231,b232],[b24,b241,b242],[b25,b251,b252],['','',''],[b26,b261,b262],[b27,b271,b272]]
        # t1 = Table(data1,colWidths=[1.5*cm,1.75*cm,7.25*cm])
        # t1.wrapOn(c,width,height)
        # t1.drawOn(c,4.4*inch,100)

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1


        #page 4


        c.drawImage(page4BG,0,0,width=width, height=height, mask = 'auto')

        c.setFillColor(colors.white)
        c.setFont("STSong-Light",22)
        c.drawString(40, 8.3*inch, "最顶级的服务")
        c.setFillGray(0.5)


        tp = Paragraph('<para fontName = STSong-Light fontsize=13 leftindent=13  ><b>系统供应商</b></para>',stylesN)
        tp2 = Paragraph('<para fontName = STSong-Light fontsize=10  align="Justify" leading=15>我们是一个系统的供应商,同时提供各种规格的电梯钢丝绳、配件和工具,可以根据客户 需求提供产品预组装服务。</para>',stylesN)
        tpt=[[tp],[tp2]]
        tptab=Table(tpt,colWidths=5*inch)
        tptab.setStyle(TableStyle([
                                    ('LEFTPADDING',(0,1),(-1,-1),20),
                               ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,1.3*inch, 450)

        tp = Paragraph('<para fontName = STSong-Light fontsize=13 leftindent=13  ><b>产品</b></para>',stylesN)
        tp2 = Paragraph('<para fontName = STSong-Light fontsize=10  align="Justify" leading=15>我们提供各种类型和规格的产品以满足客户的不同需求。如果您没有在我们的产品目录中找到您需要的产品,请直接联系我们。我们的工程师非常愿意按照您的特殊需求为您定制 产品,包括不同的钢丝强度、捻向、直径、材料、表面镀层等。</para>',stylesN)
        tpt=[[tp],[tp2]]
        tptab=Table(tpt,colWidths=4.9*inch)
        tptab.setStyle(TableStyle([
                                    ('LEFTPADDING',(0,1),(-1,-1),20),
                               ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,1.3*inch, 350)


        tp = Paragraph('<para fontName = STSong-Light fontsize=13 leftindent=13  ><b>周期</b></para>',stylesN)
        tp2 = Paragraph('<para fontName = STSong-Light fontsize=10 align="Justify" leading=15 >我们中国大陆区域内的标准交货期是6-10个工作日,即从我们的仓库运送到您的工厂或施工现场,关于其它地区的交货期,请与我们另行确认。</para>',stylesN)
        tpt=[[tp],[tp2]]
        tptab=Table(tpt,colWidths=4.9*inch)
        tptab.setStyle(TableStyle([
                                    ('LEFTPADDING',(0,1),(-1,-1),20),
                               ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,1.3*inch, 260)


        tp = Paragraph('<para fontName = STSong-Light fontsize=13 leftindent=13  ><b>快递服务</b></para>',stylesN)
        tp2 = Paragraph('<para fontName = STSong-Light fontsize=10 align="Justify" leading=15 >遇到紧急的情况,我们可以在24小时内备好货物,并向国内范围发货</para>',stylesN)
        tpt=[[tp],[tp2]]
        tptab=Table(tpt,colWidths=4.9*inch)
        tptab.setStyle(TableStyle([

                                    ('LEFTPADDING',(0,1),(-1,-1),20)
                               ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,1.3*inch, 200)

        tp = Paragraph('<para fontName = STSong-Light fontsize=13 leftindent=13  ><b>国际标准</b></para>',stylesN)
        tp2 = Paragraph('<para fontName = STSong-Light fontsize=10 align="Justify" leading=15 >我们所有的产品均符合国际、国内现行标准要求。布鲁格已经通过ISO 9001:2015和ISO 14001:2015认证的。</para>',stylesN)
        tpt=[[tp],[tp2]]
        tptab=Table(tpt,colWidths=4.9*inch)
        tptab.setStyle(TableStyle([

                                    ('LEFTPADDING',(0,1),(-1,-1),20),
                               ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,1.3*inch, 140)

        tp = Paragraph('<para fontName = STSong-Light fontsize=13 leftindent=13  ><b>培训/研讨会</b></para>',stylesN)
        tp2 = Paragraph('<para fontName = STSong-Light fontsize=10 align="Justify" leading=15 >为了更好的帮助您,我们可以为您与您的员工提供有关电梯钢丝绳的基础知识和专题培训</para>',stylesN)
        tpt=[[tp],[tp2]]
        tptab=Table(tpt,colWidths=4.9*inch)
        tptab.setStyle(TableStyle([

                                    ('LEFTPADDING',(0,1),(-1,-1),20),
                               ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,1.3*inch, 60)


        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        #page 5

        c.drawImage(page5BG,0,0,width=width, height=height, mask = 'auto')

        gm = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>Going up 是我们的励志箴言</para>',stylesN)
        n = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>2</para>',stylesN)
        gm1 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>顶级服务</para>',stylesN)
        gmn1 = Paragraph('<para fontName = STSong-Light fontName = STSong-Light fontsize=9  leading=10>4</para>',stylesN)
        gm2 = Paragraph('<para fontName = STSong-Light fontName = STSong-Light fontsize=9  leading=10>钢绳规格一览表</para>',stylesN)
        gmn2 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>6</para>',stylesN)

        gm3 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>钢丝绳性能对比</para>',stylesN)
        gmn3 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>8</para>',stylesN)

        # gm4 = Paragraph('<para fontName = STSong-Light fontsize=8  leading=10>电梯钢丝绳 . 配件</para>',stylesN)
        # gmn4 = Paragraph('<para fontName = STSong-Light fontsize=8  leading=10>9</para>',stylesN)

        gm5 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10><b>电梯钢丝绳 . 配件</b></para>',stylesN)
        gmn5 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>10</para>',stylesN)

        gm6 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>电梯钢丝绳</para>',stylesN)
        gm7 = Paragraph('<para fontName = STSong-Light fontsize=9 leftindent = 15 leading=10>HRS</para>',stylesN)
        gmn7 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>12</para>',stylesN)

        gm8 = Paragraph('<para fontName = STSong-Light fontsize=9  leftindent = 15 leading=10>DP9</para>',stylesN)
        gmn8 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>13</para>',stylesN)

        gm10 = Paragraph('<para fontName = STSong-Light fontsize=9 leftindent = 15  leading=10>MCX9</para>',stylesN)
        gmn10 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>14</para>',stylesN)

        gm9 = Paragraph('<para fontName = STSong-Light fontsize=9 leftindent = 15  leading=8>SCX9</para>',stylesN)
        gmn9 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=8>14</para>',stylesN)

        gm11 = Paragraph('<para fontName = STSong-Light fontsize=9 leftindent = 15  leading=10>8x19</para>',stylesN)
        gmn11 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>16</para>',stylesN)

        gm12 = Paragraph('<para fontName = STSong-Light fontsize=9  leftindent = 15 leading=10>TSR</para>',stylesN)
        gmn12 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>17</para>',stylesN)

        gm13 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>补偿钢丝绳</para>',stylesN)

        gm14 = Paragraph('<para fontName = STSong-Light fontsize=9  leftindent = 15 leading=10>8x19.8x25</para>',stylesN)
        gmn14 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>18</para>',stylesN)

        gm15 = Paragraph('<para fontName = STSong-Light fontsize=9  leftindent = 15 leading=10>6x25</para>',stylesN)
        gmn15 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>19</para>',stylesN)

        gm16 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>限速器绳</para>',stylesN)

        gm17 = Paragraph('<para fontName = STSong-Light fontsize=9  leftindent = 15 leading=10>6x19.8x19</para>',stylesN)
        gmn17 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>20</para>',stylesN)

        gm18 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>钢丝绳的名称与分类</para>',stylesN)
        gmn18 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>21</para>',stylesN)

        gm32 = Paragraph('<para fontName = STSong-Light fontsize=9 leftindent = 15 leading=10>配件</para>',stylesN)
        gmn32 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10></para>',stylesN)

        gm19 = Paragraph('<para fontName = STSong-Light fontsize=9   leftindent = 15 leading=10>APAG 螺纹锻造绳头</para>',stylesN)
        gmn19 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>22</para>',stylesN)

        gm20 = Paragraph('<para fontName = STSong-Light fontsize=9  leftindent = 15 leading=10>活节螺栓</para>',stylesN)
        gmn20 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>23</para>',stylesN)

        gm21 = Paragraph('<para fontName = STSong-Light fontsize=9   leftindent = 15 leading=10>非对称楔型连接绳头</para>',stylesN)
        gmn21 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>24</para>',stylesN)

        gm22 = Paragraph('<para fontName = STSong-Light fontsize=9 leftindent = 15  leading=10>缓冲垫</para>',stylesN)
        gmn22 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>26</para>',stylesN)

        gm23 = Paragraph('<para fontName = STSong-Light fontsize=9 leftindent = 15 leading=10>弹簧</para>',stylesN)
        gmn23 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>27</para>',stylesN)

        gm24 = Paragraph('<para fontName = STSong-Light fontsize=9  leftindent = 15 leading=10>门钢丝绳组件</para>',stylesN)
        gmn24 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>28</para>',stylesN)

        gm25 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>电梯门用钢丝绳</para>',stylesN)
        gmn25 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>29</para>',stylesN)

        gm25 = Paragraph('<para fontName = STSong-Light fontsize=9  leftindent = 15 leading=10>RPM 钢丝绳性能测量仪</para>',stylesN)
        gmn25 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>30</para>',stylesN)

        gm26 = Paragraph('<para fontName = STSong-Light fontsize=9  leftindent = 15 leading=10>GDC 沟槽深度比较仪</para>',stylesN)
        gmn26 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>31</para>',stylesN)

        gm27 = Paragraph('<para fontName = STSong-Light fontsize=9  leftindent = 15 leading=10>RWG 钢丝绳磨损量规</para>',stylesN)
        gmn27 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>31</para>',stylesN)


        gm29 = Paragraph('<para fontName = STSong-Light fontsize=9 leftindent = 15 leading=10>VT-LUBE 专用润滑油</para>',stylesN)
        gmn29 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>32</para>',stylesN)

        gm30 = Paragraph('<para fontName = STSong-Light fontsize=9  leftindent = 15 leading=10>钢丝绳切割器</para>',stylesN)
        gmn30 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>32</para>',stylesN)

        gm31 = Paragraph('<para fontName = STSong-Light fontsize=9 leftindent = 15 leading=10>包装</para>',stylesN)
        gmn31 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>33</para>',stylesN)

        # gm32 = Paragraph('<para fontName = STSong-Light fontsize=8 leftindent = 15 leading=10>Packaging</para>',stylesN)
        # gmn32 = Paragraph('<para fontName = STSong-Light fontsize=8  leading=10>35</para>',stylesN)

        gm33 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10><b>技术支持</b></para>',stylesN)
        gmn33 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>34</para>',stylesN)
        gm34 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>联系方式</para>',stylesN)
        gmn34 = Paragraph('<para fontName = STSong-Light fontsize=9  leading=10>35</para>',stylesN)

        data =  [[gm,n],[gm1,gmn1],[gm2,gmn2],[gm3,gmn3],['',''],[gm5,gmn5],[gm6],[gm7,gmn7],[gm8,gmn8],[gm10,gmn10],[gm9,gmn9],[gm11,gmn11],[gm12,gmn12],[gm13],[gm14,gmn14],[gm15,gmn15],[gm16],[gm17,gmn17],[gm18,gmn18],[gm32,gmn32],[gm19,gmn19],[gm20,gmn20],[gm21,gmn21],[gm22,gmn22],[gm23,gmn23],[gm24,gmn24],[gm25,gmn25],[gm26,gmn26],[gm27,gmn27],[gm29,gmn29],[gm30,gmn30],[gm31,gmn31],['',''],[gm33,gmn33],[gm34,gmn34]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=4.75*mm)
        t.setStyle(TableStyle([
                            # ('LINEABOVE',(0,0),(-1,-1),0.1,colors.white),
                            ('LINEBELOW',(0,0),(-1,-1),0.1,colors.white),
                            ('FONTSIZE', (0, 0), (-1, -1), 7),
                            ('ALIGN',(0,13),(-2,-16),'CENTER'),
                            ('ALIGN',(0,19),(-2,-10),'CENTER'),
                            ('ALIGN',(0,20),(-2,-3),'LEFT'),
                            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                             ]))

        t.wrapOn(c,width, height)
        t.drawOn(c, 4.75*inch,0.75*inch)


        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)
        t.drawOn(c, -3*inch,0.2*inch)

        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        # maa = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P7TransStrip.png')
        c.drawImage(page6BG,0,0,width=width,height=height,mask = 'auto')

        height2 = 450
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold",22)
        c.drawString(30, 8.3*inch, "ROPES AT A GLANCE")

        templatesTractionRopes = productTemplatesObjects.filter(parent_name = 'traction-ropes')
        templatesTractionRopes2 = list(productTemplatesObjects.filter(parent_name = 'traction-ropes'))
        templateCompensationRopes = list(productTemplatesObjects.filter(parent_name = 'compensation-ropes'))
        templatesGovernorRopes = list(productTemplatesObjects.filter(parent_name = 'governor-ropes'))
        templatesInnovation = productTemplatesObjects.filter(parent_name = 'innovation')

        totalNumberOFTempletes = len(productTemplatesObjects) - len(templatesInnovation)

        templatesTractionRopes2.extend(templateCompensationRopes)
        templatesTractionRopes2.extend(templatesGovernorRopes)


        if totalNumberOFTempletes>5:
            maxNumberItems = 5
            index = float(totalNumberOFTempletes)/maxNumberItems
            # printindex
            index = int(math.ceil(index))
            # printindex, range(index),"index ...."
            for i in range(index):
                if i == index:
                    data = templatesTractionRopes2[maxNumberItems*i+1:-1]

                else:
                    data = templatesTractionRopes2[maxNumberItems*i:maxNumberItems*(i+1)]
                # printlen(data), "data length"
                pageCount =  addTemplateList(c,width, height,data,stylesN,page6BG,pageCount,lang)


        else:
            pageCount = addTemplateList(c,width, height,templatesTractionRopes2,stylesN,page6BG,pageCount,lang)


        #page 8


        c.drawImage(page8BG,0,0,width=width,height=height,mask='auto')



        c.setFillColor(colors.white)
        c.setFont("STSong-Light",23)
        c.drawCentredString(138, 8.25*inch, "钢丝绳性能对比")

        # textobject = c.beginText()
        # textobject.setTextOrigin(40, 7.9*inch)
        # c.setFillColor('#3C434B')
        # textobject.setFont("Helvetica-Bold", 12)
        # textobject.textLines('''
        #                         Elastic Elongation
        #                          ''')
        # c.drawText(textobject)

        # c.drawImage(i3,40,4.2*inch,width=3.5*inch,height=3.5*inch)
        #
        # c.drawImage(i4,43,0.5*inch,width=3.75*inch,height=3*inch)

        ad1 = Paragraph('<para fontName = STSong-Light leftindent=10 align="justify"fontsize=10 leading=12><bullet>&bull;</bullet>在 绳索伸长时进行加载,当负荷去掉时,绳子会被恢复成初始状态。</para>',stylesN)
        ad2 = Paragraph('<para fontName = STSong-Light leftindent=10 align="justify"fontsize=10 leading=12><bullet>&bull;</bullet>例子:以DP9绳为例,承载8.3%的最小破断力的结果是弹性伸长量约绳子长度的0.109%((对绳长100m的绳子 来说仅相当于109mm)</para>',stylesN)
        ad3 = Paragraph('<para fontName = STSong-Light leftindent=10 align="justify"fontsize=10 leading=12><bullet>&bull;</bullet>布鲁格的钢丝绳的弹性伸长量非常低</para>',stylesN)

        a = [[ad1],[ad2],[ad3]]
        at=Table(a,colWidths=9.5*cm)
        at.wrapOn(c,width,height)
        at.drawOn(c,4*inch,5.1*inch)

        ad1 = Paragraph('<para fontName = STSong-Light leftindent=10 align="justify"fontsize=10 leading=12><bullet>&bull;</bullet>钢丝绳在使用后会产生延伸,这个延伸预计发生在钢丝 绳使用的初始阶段,占整个寿命阶段的2%左右</para>',stylesN)
        ad2 = Paragraph('<para fontName = STSong-Light leftindent=10 align="justify"fontsize=10 leading=12><bullet>&bull;</bullet>图片比较了不同类型的悬挂绳的残余伸长量</para>',stylesN)
        ad3 = Paragraph('<para fontName = STSong-Light leftindent=10 align="justify"fontsize=10 leading=12><bullet>&bull;</bullet>布鲁格的钢丝绳的残余伸长量非常低</para>',stylesN)

        a = [[ad1],[ad2],[ad3]]
        at=Table(a,colWidths=9.5*cm)
        at.wrapOn(c,width,height)
        at.drawOn(c,4.5*inch,1.5*inch)
        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        #page 9

        # bg8 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P9Hbox.svg')
        # i5 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','i5.png')

        # c.drawImage(b3,0*inch,8.25*inch,width=8.5*inch,height=3*inch)
        #
        # c.drawImage(bg7,0*inch,8.25*inch,width=8.5*inch,height=0.25*inch,mask='auto')

        c.drawImage(page9BG,0,0,width=width,height=height,mask='auto')

        i = Paragraph('<para color=white fontName= STSong-Light fontsize=23><b>钢丝绳性能对比 .<span color=rgb(0,157,224)><b> i</b></span> LINE</b></para>',stylesN)
        di = [[i]]
        dti = Table(di)
        dti.wrapOn(c,width,height)
        dti.drawOn(c,30,8.25*inch)

        # textobject = c.beginText()
        # textobject.setTextOrigin(40, 7.9*inch)
        # c.setFillColor('#3C434B')
        # textobject.setFont("Helvetica-Bold", 12)
        # textobject.textLines('''
        #                         Minimum Breaking Load
        #                          ''')
        # c.drawText(textobject)

        # c.drawImage(i5,40,4.7*inch,width=4*inch,height=3*inch)
        #
        # c.drawImage(i6,370,1.3*inch,width=2*inch,height=2.5*inch)
        #
        # c.drawImage(i7,535,0.7*inch,width=1*inch,height=3*inch)

        ad1 = Paragraph('<para fontName= STSong-Light leftindent=10 align="justify" fontsize=10 leading=12><bullet>&bull;</bullet>MBL表示在钢丝绳断裂之前可承受的最小破断载荷</para>',stylesN)
        ad2 = Paragraph('<para fontName= STSong-Light leftindent=10 align="justify"fontsize=10 leading=12><bullet>&bull;</bullet>图片比较了不同类型的悬挂绳的最小破断拉力</para>',stylesN)
        ad3 = Paragraph('<para fontName= STSong-Light leftindent=10 align="justify"fontsize=10 leading=12><bullet>&bull;</bullet>参考: 100 % = 8x19 悬挂绳天然纤维芯</para>',stylesN)

        a = [[ad1],[ad2],[ad3]]
        at=Table(a,colWidths=9.5*cm)
        at.wrapOn(c,width,height)
        at.drawOn(c,4.5*inch,6.25*inch)

        id =Paragraph('<para fontName= STSong-Light fontsize=15 spaceAfter=2>安装辅助线和颜色编码</para>',stylesN)
        id1 =Paragraph('<para fontName= STSong-Light fontsize=10 leading=13 align="justify">正确安装的曳引绳会延长其服务期限并增加安全性,还能提高电梯运行的 舒适性并减少故障,任何曳引绳在安装过程中都应避免扭转。</para>',stylesN)
        id2 =Paragraph('<para fontName= STSong-Light fontsize=10 leading=13 align="justify">布鲁格钢丝绳表面标注了安装辅助线,产生扭转的曳引绳能够简单快速的 被识别,从而便于正确的定位和调校。</para>',stylesN)

        idd = [[id],'',[id1],[id2]]
        idt = Table(idd,colWidths=10*cm)
        idt.wrapOn(c,width,height)
        idt.drawOn(c,40,1.9*inch)

        ad = Paragraph('<para  fontName= STSong-Light align="justify" fontsize=13 leading=15>安装辅助线的优点</para>',stylesN)
        ad1 = Paragraph('<para fontName= STSong-Light leftindent=13 align="justify" fontsize=10 leading=15><bullet>&bull;</bullet> 安装简易 </para>',stylesN)
        ad2 = Paragraph('<para fontName= STSong-Light leftindent=10 align="justify"fontsize=10 leading=15><bullet>&bull;</bullet> 提高安全性 </para>',stylesN)
        ad3 = Paragraph('<para fontName= STSong-Light leftindent=10 align="justify"fontsize=10 leading=15><bullet>&bull;</bullet> 优化产品性能 </para>',stylesN)
        ad4 = Paragraph('<para fontName= STSong-Light leftindent=10 align="justify"fontsize=10 leading=15><bullet>&bull;</bullet>彩色标注线易于识别产品类型</para>',stylesN)


        a = [[ad],[ad1],[ad2],[ad3],[ad4]]
        at=Table(a,colWidths=9.5*cm)
        at.wrapOn(c,width,height)
        at.drawOn(c,40,0.3*inch)


        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        #page 10
        # bg9 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P11Hbox.svg')
        # e5 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P10bgGred.png')
        # e2 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P10Bannerimg.png')
        # e1 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P10Strip.png')
        # e3 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P11Strip.png')
        # e4 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P11Strip.svg')
        # e6 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P11img3.png')
        # e7 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P10BruggLiftingCom.png')
        # bgp11 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','p11BannerImg.png')


        # c.drawImage(e5,0*inch,0*inch,width=8.5*inch,height=8.25*inch)
        #
        # c.drawImage(e2,0*inch,8.25*inch,width=8.5*inch,height=3*inch)
        # c.drawImage(e1,0*inch,8.25*inch,width=8.5*inch,height=0.9*inch,mask='auto')

        c.drawImage(page10BG,0,0,width=width,height=height,mask='auto')

        # drawing = svg2rlg(logo)
        # scaleFactor = 1./1.8
        # drawing.width *= scaleFactor
        # drawing.height *= scaleFactor
        # drawing.scale(scaleFactor, scaleFactor)
        # renderPDF.draw(drawing, c, 20,10.2*inch)

        c.setFillColor(colors.white)
        c.setFont("STSong-Light",20)
        c.drawString(30, 8*inch, "电梯钢丝绳 . 配件")
        c.setFillGray(0.5)
        # c.rect(448,8.5*inch, 6*inch, 0.25*inch,stroke=0,fill=1)

        p = Paragraph('''<para fontName = STSong-Light fontsize=10 leading=12 align="justify">布鲁格电梯钢丝绳意味着最高的品质。<br/><br/> 为了保证产品性能和质量始终得到客户信赖,我们一直严格控制生产工艺 并以精密的系统来保障产品的质量。为了在材料选择上严格把关,我们仅 在符合标准的原材料供应商处进行采购。此外,我们拥有先进的生产技术 和一批具有丰富经验的熟练技工。为保证产品的最优品质,我们还在生产 线上采用了最先进的测量和监测技术。最终,我们的产品都必须经过系统 的疲劳测试和数据评估分析。<br/><br/>成为我们的客户,您将在很多方面获益,例如产品的伸长率、破断载荷、运行平稳和服务期限等。因此,布鲁格电梯钢丝绳代表了最大经济价值和最佳性价比。</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=4*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,4.75*inch)

        # c.drawImage(i1,4.4*inch,3.75*inch,width=3.4*inch,height=3.75*inch)

        # c.drawImage(z9,0*inch,8.1*inch,width=8.5*inch,height=0.3*inch)

        # drawing = svg2rlg(z2)
        # scaleFactor = 1/1.85
        # drawing.width *= scaleFactor
        # drawing.height *= scaleFactor
        # drawing.scale(scaleFactor, scaleFactor)
        # renderPDF.draw(drawing, c, 0,8.1*inch)

        textobject = c.beginText()
        textobject.setTextOrigin(2*inch, 0.4*inch)
        textobject.setFont("Helvetica-Bold", 50)
        textobject.setFillColorRGB(255,255,255)
        textobject.textLines('''
                                brugglifting.com
                              ''')
        c.drawText(textobject)


        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        #page 11
        c.drawImage(page11BG,0,0,width=width,height=height,mask='auto')


        p = Paragraph('''<para fontName = STSong-Light fontsize=10  leading=12 align="justify">作为系统供应商,我们拥有我们生产的所有电梯钢丝绳所相对应的端口、缓冲系统和配件.<br/><br/>
        大部分项目都可以直接从库存发出,通过先进的物流在最短的交货时间进行交货 .<br/><br/> 我们专门从事制造开发螺纹锻造接头,并能够提供定制的端口。</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,5.5*inch)

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1
        # print'in zh lang'
        return pageCount





def addAccessoriePageExtra(c, data1, access,stylesN,productImage,pageCount,lang):

    if lang == 'en':
        width,height = A4

        if pageCount%2 == 0:
            if access.catalogBG1:
                background = access.catalogBG1.path
            else:
                background = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes',"page22a.jpg")
            c.drawImage(background,0,0,width=width, height=height, mask = 'auto')
            # name = Paragraph('<para fontName = FrutigerB fontSize=30>%s</para>'%(access.productName), stylesN)
            # nd =[[name]]
            # w = pdfmetrics.stringWidth(access.productName, "FrutigerB", 30)
            # # printw, "text width "
            # ndt = Table(nd)
            # w1,h1 = ndt.wrapOn(c, width,height)
            # width2 = width - w -50
            # ndt.drawOn(c, width2,570)


        else:
            if access.catalogBG2:
                background = access.catalogBG2.path
            else:
                background = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes',"page22a.jpg")
            c.drawImage(background,0,0,width=width, height=height, mask = 'auto')
            # name = Paragraph('<para fontName = FrutigerB fontSize=30>%s</para>'%(access.productName), stylesN)
            # nd =[[name]]
            # w = pdfmetrics.stringWidth(access.productName, "FrutigerB", 30)
            # # printw, "text width "
            # ndt = Table(nd)
            # w1,h1 = ndt.wrapOn(c, width,height)
            # width2 = 50
            # ndt.drawOn(c, width2,570)


        accessoriesPK = access.accessories
        # printaccessoriesPK.name, "accessory name"

        name = Paragraph('<para fontName = FrutigerB fontSize=25>%s</para>'%(access.productName), stylesN)
        nd =[[name]]
        w = pdfmetrics.stringWidth(access.productName, "FrutigerB", 30)
        # printw, "text width "
        ndt = Table(nd)
        w1,h1 = ndt.wrapOn(c, width,height)
        width2 = 50
        ndt.drawOn(c, width2,570)
        name = Paragraph('<para  fontName = FrutigerB fontSize=15>%s</para>'%((access.categoryName).upper()), stylesN)
        des =[[name]]
        dest = Table(des,colWidths=8*cm)
        w2, h3 = dest.wrapOn(c, width,height)
        # # printw2,w1, "tag width"
        w2 = pdfmetrics.stringWidth((access.categoryName).upper(), "FrutigerB", 15)
        print w, "tagline width"
        width2 = width - w2 - 20
        dest.drawOn(c, width2,560)

        #
        # name = Paragraph('<para  fontName = FrutigerB fontSize=15>%s</para>'%((accessoriesPK.name).upper()), stylesN)
        # des =[[name]]
        # dest = Table(des,colWidths=8*cm)
        # dest.wrapOn(c, width,height)
        # # # printw2,w1, "tag width"
        # # width2 = width2 + w +10
        # # # printwidth2, "tagline width"
        # dest.drawOn(c, 200,555)

        height2 = 600 -h1 -20
        img = utils.ImageReader(productImage)
        iw, ih = img.getSize()
        c.drawImage(productImage,30,height2-ih,width=150,preserveAspectRatio=True,mask='auto')



        table = Table(data1,rowHeights=[20]*len(data1))
        table.setStyle(TableStyle([
                             ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                             ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                             ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                             ('FONTSIZE', (0, 0), (-1, -1), 7),
                             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                             ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                             ]))
        w5, h5 = table.wrapOn(c, width, height)
        height2 = height2 - h5 - 50
        table.drawOn(c, 200, height2)

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1
        return pageCount


    elif lang == 'de':
        width,height = A4

        if pageCount%2 == 0:
            if access.catalogBG1:
                background = access.catalogBG1.path
            else:
                background = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes',"page22a.jpg")
            c.drawImage(background,0,0,width=width, height=height, mask = 'auto')
            # name = Paragraph('<para fontName = FrutigerB fontSize=30>%s</para>'%(access.productName), stylesN)
            # nd =[[name]]
            # w = pdfmetrics.stringWidth(access.productName, "FrutigerB", 30)
            # # printw, "text width "
            # ndt = Table(nd)
            # w1,h1 = ndt.wrapOn(c, width,height)
            # width2 = width - w -50
            # ndt.drawOn(c, width2,570)


        else:
            if access.catalogBG2:
                background = access.catalogBG2.path
            else:
                background = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes',"page22a.jpg")
            c.drawImage(background,0,0,width=width, height=height, mask = 'auto')
            # name = Paragraph('<para fontName = FrutigerB fontSize=30>%s</para>'%(access.productName), stylesN)
            # nd =[[name]]
            # w = pdfmetrics.stringWidth(access.productName, "FrutigerB", 30)
            # # printw, "text width "
            # ndt = Table(nd)
            # w1,h1 = ndt.wrapOn(c, width,height)
            # width2 = 50
            # ndt.drawOn(c, width2,570)


        accessoriesPK = access.accessories
        # printaccessoriesPK.name, "accessory name"


        name = Paragraph('<para fontName = FrutigerB fontSize=25>%s</para>'%(access.productName), stylesN)
        nd =[[name]]
        w = pdfmetrics.stringWidth(access.productName, "FrutigerB", 30)
        # printw, "text width "
        ndt = Table(nd)
        w1,h1 = ndt.wrapOn(c, width,height)
        width2 = 50
        ndt.drawOn(c, width2,570)
        name = Paragraph('<para  fontName = FrutigerB fontSize=15>%s</para>'%((access.categoryName).upper()), stylesN)
        des =[[name]]
        dest = Table(des,colWidths=8*cm)
        w2, h3 = dest.wrapOn(c, width,height)
        # # printw2,w1, "tag width"
        w2 = pdfmetrics.stringWidth((access.categoryName).upper(), "FrutigerB", 15)
        print w, "tagline width"
        width2 = width - w2 - 20
        dest.drawOn(c, width2,560)

        # name = Paragraph('<para  fontName = FrutigerB fontSize=15>%s</para>'%((access.categoryName).upper()), stylesN)
        # des =[[name]]
        # dest = Table(des,colWidths=8*cm)
        # dest.wrapOn(c, width,height)
        # # # printw2,w1, "tag width"
        # # width2 = width2 + w +10
        # # # printwidth2, "tagline width"
        # dest.drawOn(c, 200,555)

        height2 = 600 - h1 -20
        img = utils.ImageReader(productImage)
        iw, ih = img.getSize()
        c.drawImage(productImage,30,height2-ih,width=150,preserveAspectRatio=True,mask='auto')
        #
        # name = Paragraph('<para fontName = FrutigerB fontSize=20>%s</para>'%(access.productName), stylesN)
        # nd =[[name]]
        # ndt = Table(nd,colWidths=10*cm)
        # w1,h1 = ndt.wrapOn(c, width,height)
        # height2 = height-h1-100
        # ndt.drawOn(c, 50,800)

        # printdata1, "data1 in new page"

        table = Table(data1,rowHeights=[20]*len(data1))
        table.setStyle(TableStyle([
                             ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                             ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                             ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                             ('FONTSIZE', (0, 0), (-1, -1), 7),
                             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                             ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                             ]))
        w5, h5 = table.wrapOn(c, width, height)
        height2 = height2 - h5 - 50
        table.drawOn(c, 200, height2)

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1
        return pageCount

    elif lang == 'zh':
        width,height = A4

        if pageCount%2 == 0:
            if access.catalogBG1:
                background = access.catalogBG1.path
            else:
                background = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes',"page22a.jpg")
            c.drawImage(background,0,0,width=width, height=height, mask = 'auto')
            # name = Paragraph('<para fontName = STSong-Light fontSize=30>%s</para>'%(access.productName), stylesN)
            # nd =[[name]]
            # w = pdfmetrics.stringWidth(access.productName, "FrutigerB", 30)
            # # printw, "text width "
            # ndt = Table(nd)
            # w1,h1 = ndt.wrapOn(c, width,height)
            # width2 = width - w -50
            # ndt.drawOn(c, width2,570)


        else:
            if access.catalogBG2:
                background = access.catalogBG2.path
            else:
                background = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes',"page22a.jpg")
            c.drawImage(background,0,0,width=width, height=height, mask = 'auto')
            # name = Paragraph('<para fontName = STSong-Light fontSize=30>%s</para>'%(access.productName), stylesN)
            # nd =[[name]]
            # w = pdfmetrics.stringWidth(access.productName, "FrutigerB", 30)
            # # printw, "text width "
            # ndt = Table(nd)
            # w1,h1 = ndt.wrapOn(c, width,height)
            # width2 = 50
            # ndt.drawOn(c, width2,570)


        accessoriesPK = access.accessories
        # printaccessoriesPK.name, "accessory name"

        name = Paragraph('<para fontName = STSong-Light fontSize=25>%s</para>'%(access.productName), stylesN)
        nd =[[name]]
        w = pdfmetrics.stringWidth(access.productName, "FrutigerB", 30)
        # printw, "text width "
        ndt = Table(nd)
        w1,h1 = ndt.wrapOn(c, width,height)
        width2 = 50
        ndt.drawOn(c, width2,570)
        name = Paragraph('<para  fontName = STSong-Light fontSize=15>%s</para>'%((access.categoryName).upper()), stylesN)
        des =[[name]]
        dest = Table(des,colWidths=8*cm)
        w2, h3 = dest.wrapOn(c, width,height)
        # # printw2,w1, "tag width"
        w2 = pdfmetrics.stringWidth((access.categoryName).upper(), "STSong-Light", 15)
        print w, "tagline width"
        width2 = width - w2 - 20
        dest.drawOn(c, width2,560)

        # name = Paragraph('<para  fontName = STSong-Light fontSize=15>%s</para>'%((access.categoryName).upper()), stylesN)
        # des =[[name]]
        # dest = Table(des,colWidths=8*cm)
        # dest.wrapOn(c, width,height)
        # # # printw2,w1, "tag width"
        # # width2 = width2 + w +10
        # # # printwidth2, "tagline width"
        # dest.drawOn(c, 200,555)

        height2 = 600 - h1
        img = utils.ImageReader(productImage)
        iw, ih = img.getSize()
        c.drawImage(productImage,50,height2-ih,width=150,preserveAspectRatio=True,mask='auto')
        #
        # name = Paragraph('<para fontName = FrutigerB fontSize=20>%s</para>'%(access.productName), stylesN)
        # nd =[[name]]
        # ndt = Table(nd,colWidths=10*cm)
        # w1,h1 = ndt.wrapOn(c, width,height)
        # height2 = height-h1-100
        # ndt.drawOn(c, 50,800)

        # printdata1, "data1 in new page"

        table = Table(data1,rowHeights=[20]*len(data1))
        table.setStyle(TableStyle([
                             ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                             ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                             ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                             ('FONTSIZE', (0, 0), (-1, -1), 7),
                             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                             ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                             ]))
        w5, h5 = table.wrapOn(c, width, height)
        height2 = height2 - h5 - 50
        table.drawOn(c, 200, height2)

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1
        return pageCount


def addAccessoriePage(c,access, prodfield,itemNumbers, itemNumberValues, stylesN):

    width,height = A4

    if access.image2:
        productImage = access.image2.path
    else:
        productImage = os.path.join(globalSettings.BASE_DIR , 'static_shared/images',"stars.jpeg")


    name = Paragraph('<para fontName = FrutigerB fontSize=54>%s</para>'%(access.productName), stylesN)
    nd =[[name]]
    w = pdfmetrics.stringWidth(access.productName, "FrutigerB", 54)
    # printw, "text width "
    ndt = Table(nd)
    w1,h1 = ndt.wrapOn(c, width,height)
    width2 = 50
    ndt.drawOn(c, width2,600)

    name = Paragraph('<para  fontName = FrutigerB fontSize=12.5>%s</para>'%(access.tagLine), stylesN)
    des =[[name]]
    dest = Table(des,colWidths=8*cm)
    w2, h3 = dest.wrapOn(c, width,height)
    # printw2,w1, "tag width"
    width2 = width2 + w +10
    # printwidth2, "tagline width"
    dest.drawOn(c, width2,570)

    height2 = 600

    img = utils.ImageReader(productImage)
    iw, ih = img.getSize()
    height3 = height2 - ih
    c.drawImage(productImage,50,height3,width=150,preserveAspectRatio=True,mask='auto')



    name = Paragraph('<para fontName = FrutigerB fontSize=15>%s</para>'%(access.title1), stylesN)
    nd =[[name]]
    ndt = Table(nd,colWidths=10*cm)
    w1,h1 = ndt.wrapOn(c, width,height)
    height2 = height2-h1-100
    ndt.drawOn(c, 200,height2)

    name = Paragraph('%s'%(access.desc1), stylesN)
    des =[[name]]
    dest = Table(des,colWidths=10*cm)
    w2, h2 = dest.wrapOn(c, width,height)
    # printw2, h2, "height of para1"
    height2 = height2 -h2
    dest.drawOn(c, 200,height2)

    name = Paragraph('<para fontName = FrutigerB fontSize=15>%s</para>'%(access.title2), stylesN)
    nd =[[name]]
    ndt = Table(nd,colWidths=10*cm)
    w3,h3 = ndt.wrapOn(c, width,height)
    height2 = height2 -h3-30
    ndt.drawOn(c, 200,height2)


    name = Paragraph('%s'%(access.desc2), stylesN)
    des =[[name]]
    dest = Table(des,colWidths=10*cm, rowHeights=30*mm)
    w4, h4 = dest.wrapOn(c, width,height)
    height2 = height2 -h4
    dest.drawOn(c, 200,height2)




    data = []
    # data2 = []
    dataHeading = ['Item Number']
    dataHeading2 = ['']
    list1 = []
    list2 = []
    for j in prodfield:
        # printprodfield
        if j.inPdf ==True:

            # printj.name,'kkkkkkkkkkkkk'
            try:
                name1, name2 = j.name.split('(')
                # printname2[:-1]
                name2 = ''+name2[:-1]
                # printname2
            except:
                name1 = j.name
                name2 = ''

            # printname1, ' ' , name2

            list1.append(name1)
            list2.append(name2)
    for a in list1:
        dataHeading.append(a)
    for b in list2:
        dataHeading2.append(b)


    # printdataHeading, dataHeading2, "fields  "


    for i in itemNumbers:
        appendlist = [i.itemNumber]
        for j in prodfield:
            prodQty = itemNumberValues.filter( field = j.pk,product = i.pk)
            for k in prodQty:
                if j.inPdf ==True:
                    if j.type=='Char':
                        appendlist.append(k.char)
                    if j.type=='float':
                        appendlist.append(k.fValue)
                    if j.type=='Integer':
                        appendlist.append(k.iValue)
                    if j.type=='Boolean':
                        appendlist.append(k.bool)
        data.append(appendlist)

    # printlen(data), "data length"
    # printdata , "item number data"


    data.insert(0,dataHeading)
    # printdata,len(data), "final data"

    # # printheight2, "height2"
    height2 = height2-40
    leftHeight = height2-120
    numberRows = int(leftHeight/20)
    # printheight2, leftHeight, numberRows, "number of rows"

    if len(data)<= numberRows:
            t5 = Table(data,rowHeights=[20]*len(data))
            t5.setStyle(TableStyle([
                                 ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                                 ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                                 ('FONTSIZE', (0, 0), (-1, -1), 7),
                                 ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                 ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                                 ]))
            w5, h5 = t5.wrapOn(c, width, height)
            height2 = height2 - h5
            t5.drawOn(c, 200, height2)
            c.showPage()
    else:
        # print"in else"
        data1 = data[:numberRows-1]
        # printdata1, "data1"
        data2 = data[numberRows:-1]
        # printdata2, "data2"
        t5 = Table(data1,rowHeights=[20]*len(data1))
        t5.setStyle(TableStyle([
                             ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                             ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                             ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                             ('FONTSIZE', (0, 0), (-1, -1), 7),
                             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                             ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                             ]))
        w5, h5 = t5.wrapOn(c, width, height)
        height2 = height2 - h5
        t5.drawOn(c, 200, height2)

        c.showPage()

        maxNumberItems = 20

        index = float(len(data2))/maxNumberItems
        # printindex
        index = int(math.ceil(index))
        # printindex, range(index),"index ...."
        for i in range(index):
            if i == index-1:
                data1 = data2[maxNumberItems*i:-1]
                data1.insert(0,dataHeading)
                # printlen(data1), i , "if loop"
            else:
                data1 = data2[maxNumberItems*i:maxNumberItems*(i+1)-1]
                data1.insert(0,dataHeading)
                # printlen(data1), i, "else loop"
            # printdata1, "datapass "
            addAccessoriePageExtra(c, data1, access,stylesN,productImage)



def addElevatorPage(c, data1,template,stylesN,pageCount,lang):
    if lang == 'en':

        width, height = A4
        if pageCount%2 == 0:
            if template.catalogBG1:
                background = template.catalogBG1.path
            else:
                background = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes',"page13.jpg")
            c.drawImage(background,0,0,width=width, height=height, mask = 'auto')
            name = Paragraph('<para fontName = FrutigerB fontSize=30>%s</para>'%(template.name), stylesN)
            nd =[[name]]
            w = pdfmetrics.stringWidth(template.name, "FrutigerB", 30)
            # printw, "text width "
            ndt = Table(nd)
            w1,h1 = ndt.wrapOn(c, width,height)
            width2 = width - w -50
            ndt.drawOn(c, width2,570)


        else:
            if template.catalogBG2:
                background = template.catalogBG2.path
            else:
                background = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes',"page12.jpg")
            c.drawImage(background,0,0,width=width, height=height, mask = 'auto')
            name = Paragraph('<para fontName = FrutigerB fontSize=30>%s</para>'%(template.name), stylesN)
            nd =[[name]]
            w = pdfmetrics.stringWidth(template.name, "FrutigerB", 30)
            # printw, "text width "
            ndt = Table(nd)
            w1,h1 = ndt.wrapOn(c, width,height)
            width2 = 50
            ndt.drawOn(c, width2,570)



        test =  template.parent_name
        test = test.split("-")
        text = ''
        for i in test:
            text += i.upper() + " "
        name = Paragraph('<para fontName = FrutigerB fontSize=15>%s</para>'%(text), stylesN)
        nd =[[name]]
        w = pdfmetrics.stringWidth(template.parent_name, "FrutigerB", 10)
        # printw, "text width "
        ndt = Table(nd)
        w1,h1 = ndt.wrapOn(c, width,height)

        ndt.drawOn(c, 200,548)

        table = Table(data1,rowHeights=[20]*len(data1))
        table.setStyle(TableStyle([
                             ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                             ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                             ('FONTSIZE', (0, 0), (-1, -1), 7),
                             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                             ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                             ]))
        w5, h5 = table.wrapOn(c, width, height)
        height2 = height - h5-350
        table.drawOn(c, 200, height2)


        para2 = Paragraph('<para fontName = Helvetica fontSize=6 >%s</para>'%(template.disclaimer_en), stylesN)
        tab = [[para2]]
        r = Table(tab,colWidths=3.25*inch)
        w,h1 = r.wrapOn(c, width,height)
        height2 = height2 - h1
        r.drawOn(c, 200, height2)

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1
        return pageCount

    elif lang == 'de':

        width, height = A4
        if pageCount%2 == 0:
            if template.catalogBG1:
                background = template.catalogBG1.path
            else:
                background = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes',"page13.jpg")
            c.drawImage(background,0,0,width=width, height=height, mask = 'auto')
            name = Paragraph('<para fontName = FrutigerB fontSize=30>%s</para>'%(template.name), stylesN)
            nd =[[name]]
            w = pdfmetrics.stringWidth(template.name, "FrutigerB", 30)
            # printw, "text width "
            ndt = Table(nd)
            w1,h1 = ndt.wrapOn(c, width,height)
            width2 = width - w -50
            ndt.drawOn(c, width2,570)


        else:
            if template.catalogBG2:
                background = template.catalogBG2.path
            else:
                background = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes',"page12.jpg")
            c.drawImage(background,0,0,width=width, height=height, mask = 'auto')
            name = Paragraph('<para fontName = FrutigerB fontSize=30>%s</para>'%(template.name), stylesN)
            nd =[[name]]
            w = pdfmetrics.stringWidth(template.name, "FrutigerB", 30)
            # printw, "text width "
            ndt = Table(nd)
            w1,h1 = ndt.wrapOn(c, width,height)
            width2 = 50
            ndt.drawOn(c, width2,570)



        test =  template.parent_name
        test = test.split("-")
        text = ''
        for i in test:
            text += i.upper() + " "
        name = Paragraph('<para fontName = FrutigerB fontSize=15>%s</para>'%(text), stylesN)
        nd =[[name]]
        w = pdfmetrics.stringWidth(template.parent_name, "FrutigerB", 10)
        # printw, "text width "
        ndt = Table(nd)
        w1,h1 = ndt.wrapOn(c, width,height)

        ndt.drawOn(c, 200,548)

        table = Table(data1,rowHeights=[20]*len(data1))
        table.setStyle(TableStyle([
                             ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                             ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                             ('FONTSIZE', (0, 0), (-1, -1), 7),
                             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                             ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                             ]))
        w5, h5 = table.wrapOn(c, width, height)
        height2 = height - h5-350
        table.drawOn(c, 200, height2)


        para2 = Paragraph('<para fontName = Helvetica fontSize=6 >%s</para>'%(template.disclaimer_otl), stylesN)
        tab = [[para2]]
        r = Table(tab,colWidths=3.25*inch)
        w,h1 = r.wrapOn(c, width,height)
        height2 = height2 - h1
        r.drawOn(c, 200, height2)

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1
        return pageCount

    elif lang == 'zh':

        width, height = A4
        if pageCount%2 == 0:
            if template.catalogBG1:
                background = template.catalogBG1.path
            else:
                background = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes',"page13.jpg")
            c.drawImage(background,0,0,width=width, height=height, mask = 'auto')
            name = Paragraph('<para fontName = FrutigerB fontSize=30>%s</para>'%(template.name), stylesN)
            nd =[[name]]
            w = pdfmetrics.stringWidth(template.name, "FrutigerB", 30)
            # printw, "text width "
            ndt = Table(nd)
            w1,h1 = ndt.wrapOn(c, width,height)
            width2 = width - w -50
            ndt.drawOn(c, width2,570)


        else:
            if template.catalogBG2:
                background = template.catalogBG2.path
            else:
                background = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes',"page12.jpg")
            c.drawImage(background,0,0,width=width, height=height, mask = 'auto')
            name = Paragraph('<para fontName = FrutigerB fontSize=30>%s</para>'%(template.name), stylesN)
            nd =[[name]]
            w = pdfmetrics.stringWidth(template.name, "FrutigerB", 30)
            # printw, "text width "
            ndt = Table(nd)
            w1,h1 = ndt.wrapOn(c, width,height)
            width2 = 50
            ndt.drawOn(c, width2,570)



        test =  template.parent_name
        test = test.split("-")
        text = ''
        for i in test:
            text += i.upper() + " "
        name = Paragraph('<para fontName = FrutigerB fontSize=15>%s</para>'%(text), stylesN)
        nd =[[name]]
        w = pdfmetrics.stringWidth(template.parent_name, "FrutigerB", 10)
        # printw, "text width "
        ndt = Table(nd)
        w1,h1 = ndt.wrapOn(c, width,height)

        ndt.drawOn(c, 200,548)

        table = Table(data1,rowHeights=[20]*len(data1))
        table.setStyle(TableStyle([
                             ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                             ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                             ('FONTSIZE', (0, 0), (-1, -1), 7),
                             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                             ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                             ]))
        w5, h5 = table.wrapOn(c, width, height)
        height2 = height - h5-350
        table.drawOn(c, 200, height2)


        para2 = Paragraph('<para fontName =  STSong-Light fontSize=6 >%s</para>'%(template.disclaimer_ch), stylesN)
        tab = [[para2]]
        r = Table(tab,colWidths=3.25*inch)
        w,h1 = r.wrapOn(c, width,height)
        height2 = height2 - h1
        r.drawOn(c, 200, height2)

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1
        return pageCount

def endPagesElevatorRope(request,response,styles,stylesN,stylesH,width,height,c,pageCount,lang):

    P37Swis = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P37Swis.png')
    P37USA = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P37USA.png')
    P37China = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P37China.png')
    P37WorldWide = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P37Worldwide.png')
    if lang == 'en':
        pageTLastBG = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes','page36.jpg')
        pageSLastBG = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes','page37.jpg')

        c.drawImage(pageTLastBG,0,0,width=width, height=height, mask='auto')

        q1  = Paragraph('<para fontsize=20 align="justify" color = white > <b>WE SUPPORT YOU.</b><span color=rgb(0,157,224)><b>WORLDWIDE</b></span></para>',stylesN)
        t= [[q1]]
        tq = Table(t)
        tq.wrapOn(c,width,height)
        tq.drawOn(c,30,8.2*inch)

        p1  = Paragraph('<para fontName = FrutigerR fontsize=10 align="justify"> <b>brugglifting.com.</b> The compact informative homepage</para>',stylesN)
        w1  = Paragraph('<para fontName = FrutigerR fontsize=10 align="justify" leading=13> Our Homepage provides you with vivid depictions of our entire product range. You can intuitively make preselections to meet your individual requirements and find your BRUGG LIFTING contacts all over the world with just a click. For the latest information, just visit our start page.</para>',stylesN)

        p2  = Paragraph('<para fontName = FrutigerR fontsize=10 align="justify" > <b>RLP . </b>Calculate the service life  of your ropes</para>',stylesN)
        w2  = Paragraph('<para fontName = FrutigerR fontsize=10 align="justify" leading=13> Login in to our service life calculator on our wevsite and enter the data of your ropes tp calculate their service life..</para>',stylesN)

        p3  = Paragraph('<para fontName = FrutigerR fontsize=10 align="justify" > <b>Instructions for Use . </b>Important tips for rope handling</para>',stylesN)
        w3  = Paragraph('<para fontName = FrutigerR fontsize=10 align="justify" leading=13> Login in to our service life calculator on our wevsite and enter the data of your ropes tp calculate their service life..</para>',stylesN)

        p4  = Paragraph('<para fontName = FrutigerR fontsize=10 align="justify" > <b>User Reference Guide . </b>About the handling our ropes</para>',stylesN)
        w4  = Paragraph('<para fontName = FrutigerR fontsize=10 align="justify" leading=13>Make use of our extenxive know-hoe rope handling. A quick Link on our website thakes you to our User Reference Guide where you both find comprehensive technical details and tips and may retrieve the requested information via a targeted ful-text Search You may store all data as a PDF file.</para>',stylesN)

        tp = [[p1],[w1],[''],[p2],[w2],[''],[''],[''],[''],[p3],[w3],[''],[''],[''],[''],[''],[p4],[w4]]
        tpt = Table(tp,colWidths=12.25*cm)
        tpt.wrapOn(c,width,height)
        tpt.drawOn(c,3.25*inch, 1.25*inch)


        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        c.drawImage(pageSLastBG,0,0,width=width, height=height, mask='auto')

        textobject = c.beginText()
        textobject.setTextOrigin(2*inch, 0.4*inch)
        textobject.setFont("Helvetica-Bold", 50)
        textobject.setFillColorRGB(192,192,192)
        textobject.textLines('''
                                brugglifting.com
                              ''')
        c.drawText(textobject)

        # c.drawInlineImage(rope,3.25*inch,7.45*inch,width=1.75*inch,height=1.4*inch,preserveAspectRatio=True)



        d1 = Paragraph('<para><img src="{0}" valign="middle" /></para>'.format(P37Swis),stylesN)
        d2 = Paragraph('<para fontsize=10 leftindent=-65><b> SWITZERLAND</b></para>',stylesN)
        d3 = Paragraph('<para fontsize=8 leading=17 leftindent=24><b>BRUGG LIFTING</b><br/>Wydenstrasse 36<br/>5242 Birr<br/> Switzerlad<br/> T +41 (0)56 464 42 42<br/> F +41(0)56 464 42 84<br/>info.lifting@brugg.com<br/>brugglifting.com</para>',stylesN)
        dt=[[d1,d2],[d3]]
        dtt =Table(dt,colWidths=[5*cm,3.5*cm])
        dtt.setStyle(TableStyle([
                                        ('TOPPADDING',(0,0),(-1,-1),20),
                               ]))
        dtt.wrapOn(c,width,height)
        dtt.drawOn(c,30, 4.75*inch)

        d1 = Paragraph('<para><img src="{0}" valign="middle" /></para>'.format(P37Swis),stylesN)
        d2 = Paragraph('<para fontsize=10 leftindent=-65><b> SWITZERLAND</b></para>',stylesN)
        d3 = Paragraph('<para  align="Justify"fontsize=8 leading=17 leftindent=20><b>BRUGG LIFTING</b><br/>Chemin de Foret 12<br/>1024 Ecublens<br/> Switzerlad<br/> T +41 (0)21 634 20 21<br/> F +41(0)21 635 09 71<br/>vente.lifting@brugg.co<br/>brugglifting.com</para>',stylesN)
        dt=[[d1,d2],[d3]]
        dtt =Table(dt,colWidths=[5*cm,3.5*cm])
        dtt.setStyle(TableStyle([
                                        ('TOPPADDING',(0,0),(-1,-1),20),
                               ]))
        dtt.wrapOn(c,width,height)
        dtt.drawOn(c,3.1*inch, 4.75*inch)

        d1 = Paragraph('<para><img src="{0}" valign="middle" /></para>'.format(P37USA),stylesN)
        d2 = Paragraph('<para fontsize=10 leftindent=-65><b>USA</b></para>',stylesN)
        d3 = Paragraph('<para fontsize=8 leading=17 leftindent=22><b>Brugg Wire Rope LLC</b><br/>3411 Turkey Mountain Road NE<br/>US-Rome,GA 30161<br/> T +1 706 314 29 82<br/> F +1 706 235 60 35<br/>lifting.usa@brugg.com<br/>brugglifting.com</para>',stylesN)
        dt=[[d1,d2],[d3]]
        dtt =Table(dt,colWidths=[5*cm,3.5*cm])
        dtt.setStyle(TableStyle([
                                        ('TOPPADDING',(0,0),(-1,-1),20),
                               ]))
        dtt.wrapOn(c,width,height)
        dtt.drawOn(c,5.75*inch, 4.75*inch)

        d1 = Paragraph('<para><img src="{0}" valign="middle" /></para>'.format(P37China),stylesN)
        d2 = Paragraph('<para fontsize=10 leftindent=-65><b>CHINA</b></para>',stylesN)
        d3 = Paragraph('<para fontsize=8 leading=17 leftindent=22><b>BRUGG LIFTING</b><br/>Plant 1, Nr.88 jingling East Road<br/>Suzhou Industrial Park<br/> jiangsu Province,215121<br/>P.R. China<br/>T +86 512 6299 0779<br/> F +86 512 6299 0774<br/>lifting.cn@brugg.com<br/>brugglifting.cn</para>',stylesN)
        dt=[[d1,d2],[d3]]
        dtt =Table(dt,colWidths=[5*cm,3.5*cm])
        dtt.setStyle(TableStyle([
                                        ('TOPPADDING',(0,0),(-1,-1),20),
                               ]))
        dtt.wrapOn(c,width,height)
        dtt.drawOn(c,30, 1.65*inch)

        d1 = Paragraph('<para><img src="{0}" valign="middle" /></para>'.format(P37WorldWide),stylesN)
        d2 = Paragraph('<para fontsize=10 leftindent=-65><b> WORLDWIDE</b></para>',stylesN)
        d3 = Paragraph('<para  align="Justify"fontsize=8 leading=17 leftindent=22> Our quality products are  available from more than 20 distributing partners         around the world.</para>',stylesN)
        dt=[[d1,d2],[d3]]
        dtt =Table(dt,colWidths=[5*cm,3.5*cm])
        dtt.setStyle(TableStyle([
                                        ('TOPPADDING',(0,0),(-1,-1),20),
                               ]))
        dtt.wrapOn(c,width,height)
        dtt.drawOn(c,3.1*inch, 3*inch)

        textobject = c.beginText()
        textobject.setTextOrigin(40, 1.1*inch)
        c.setFillColor('#C0C0C0')
        textobject.setFont("Helvetica-Bold",57)
        textobject.textLines('''
                                brugglifting.com
                                 ''')
        c.drawText(textobject)

        textobject = c.beginText()
        textobject.setTextOrigin(40, 0.75*inch)
        c.setFillColor('#C0C0C0')
        textobject.setFont("Helvetica", 7)
        textobject.textLines('''
                                Creation date 10 / 2018
                                Subject to changes. Nonbinding indication of measures. No warranty for printing errors or errors.
                                If not agreed otherwise, our general conditions of sale and delivery are valid.
                                We thank  OSMAAufzuge for the provision of the photos on the following pages 9, 13
                                Design, realization: www.schaefer-design.com

                                 ''')
        c.drawText(textobject)

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        if pageCount %2 == 0:
            print "dont worry"
        else:
            c.showPage()
            pageCount +=1

        lp = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P38BG.png')
        c.drawImage(lp,0,0,width=width,height=height, mask='auto')

        textobject = c.beginText()
        textobject.setTextOrigin(250, 40)
        textobject.setFont("FrutigerB", 12)
        # textobject.setFillColorRGB(192,192,192)
        textobject.setFillColor(colors.white)
        textobject.textLines('''
                                brugglifting.com
                              ''')
        c.drawText(textobject)

        c.showPage()
        pageCount +=1

    elif lang == 'de':
        pageTLastBG = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes','page36.jpg')
        pageSLastBG = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes','page37.jpg')

        c.drawImage(pageTLastBG,0,0,width=width, height=height, mask='auto')

        q1  = Paragraph('<para fontsize=22 align="justify" color = white > <b>WIR SIND FÜR SIE DA .</b><span color=rgb(0,157,224)><b>WELTWEIT.</b></span></para>',stylesN)
        t= [[q1]]
        tq = Table(t)
        tq.wrapOn(c,width,height)
        tq.drawOn(c,30,8.2*inch)


        p1  = Paragraph('<para fontName = FrutigerR fontsize=10 align="justify">brugglifting.com · Die kompakt informative Homepage</para>',stylesN)
        w1  = Paragraph('<para fontName = FrutigerR fontsize=10 align="justify" leading=13> Auf unserer Homepage präsentieren wir Ihnen anschaulich unser ge-samtes Produktsortiment. Intuitiv können Sie eine Vorauswahl für Ihre individuelle Anforderung treffen und finden auf einen Klick den Kon-takt zu Ihrem BRUGG LIFTING-Ansprechpartner weltweit. Aktuelles erfahren Sie immer direkt auf der Startseite – besuchen Sie uns.</para>',stylesN)
        #
        # p2  = Paragraph('<para fontName = FrutigerR fontsize=10 align="justify" > <b>RLP . </b>Calculate the service life  of your ropes</para>',stylesN)
        # w2  = Paragraph('<para fontName = FrutigerR fontsize=10 align="justify" leading=13> Login in to our service life calculator on our wevsite and enter the data of your ropes tp calculate their service life..</para>',stylesN)

        p3  = Paragraph('<para fontName = FrutigerR fontsize=10 align="justify" > Anwendungshinweise · Wichtige Tipps zur Seilhandhabung</para>',stylesN)
        w3  = Paragraph('<para fontName = FrutigerR fontsize=10 align="justify" leading=13> Mit jedem von uns gelieferten Seil erhalten Sie unsere illustrierten An-wendungshinweise für die richtige Handhabung. Vom Transport bis hinzur Seilüberwachung sehen Sie alle nützlichen Informationen auf einen Blick.</para>',stylesN)

        p4  = Paragraph('<para fontName = FrutigerR fontsize=10 align="justify" > User Reference Guide · Zur Handhabung unserer Seile [EN]</para>',stylesN)
        w4  = Paragraph('<para fontName = FrutigerR fontsize=10 align="justify" leading=13>Nutzen Sie unser umfangreiches Know-how zur Seilhandhabung. Ein Quicklink auf unserer Homepage bringt Sie zu unserem User Reference Guide, in dem Sie nicht nur umfangreiche, technische Details und Tipps finden, sondern auch gezielt über eine Volltextsuche, die von Ihnen gewünschten Informationen abrufen können. Alle Daten können Sie als PDF abspeichern.</para>',stylesN)

        tp = [[p1],[w1],[''],[''],[''],[''],[p3],[w3],[''],[''],[''],[''],[''],[p4],[w4]]
        tpt = Table(tp,colWidths=11.15*cm)
        tpt.wrapOn(c,width,height)
        tpt.drawOn(c,3.5*inch, 1*inch)


        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)




        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1


        c.drawImage(pageSLastBG,0,0,width=width, height=height, mask='auto')

        textobject = c.beginText()
        textobject.setTextOrigin(2*inch, 0.4*inch)
        textobject.setFont("Helvetica-Bold", 50)
        textobject.setFillColorRGB(192,192,192)
        textobject.textLines('''
                                brugglifting.com
                              ''')
        c.drawText(textobject)

        # c.drawInlineImage(rope,3.25*inch,7.45*inch,width=1.75*inch,height=1.4*inch,preserveAspectRatio=True)
        # P37Swis = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P37Swis.png')

        d1 = Paragraph('<para><img src="{0}" valign="middle" /></para>'.format(P37Swis),stylesN)
        d2 = Paragraph('<para fontsize=10 leftindent=-65><b>SCHWEIZ</b></para>',stylesN)
        d3 = Paragraph('<para fontsize=8 leading=17 leftindent=24><b>BRUGGLIFTING</b><br/>Wydenstrasse 36<br/>5242 Birr<br/>Schweiz<br/>T +41 (0) 56 464 42 42<br/> F +41 (0) 56 464 42 84<br/>orders.elevator@brugg.com<br/>brugglifting.com</para>',stylesN)
        dt=[[d1,d2],[d3]]
        dtt =Table(dt,colWidths=[5*cm,3.5*cm])
        dtt.setStyle(TableStyle([
                                        ('TOPPADDING',(0,0),(-1,-1),20),
                               ]))
        dtt.wrapOn(c,width,height)
        dtt.drawOn(c,30, 4.75*inch)

        d1 = Paragraph('<para><img src="{0}" valign="middle" /></para>'.format(P37Swis),stylesN)
        d2 = Paragraph('<para fontsize=10 leftindent=-65><b> SCHWEIZ</b></para>',stylesN)
        d3 = Paragraph('<para  align="Justify"fontsize=8 leading=17 leftindent=20><b>BRUGG LIFTING</b><br/>Chemin de Forét 12<br/>1024 Ecublens<br/>Schweiz<br/>T +41 (0) 21 634 20 21<br/> F +41 (0) 21 635 09 71<br/>vente.lifting@brugg.com<br/>brugglifting.com</para>',stylesN)
        dt=[[d1,d2],[d3]]
        dtt =Table(dt,colWidths=[5*cm,3.5*cm])
        dtt.setStyle(TableStyle([
                                        ('TOPPADDING',(0,0),(-1,-1),20),
                               ]))
        dtt.wrapOn(c,width,height)
        dtt.drawOn(c,3.1*inch, 4.75*inch)

        d1 = Paragraph('<para><img src="{0}" valign="middle" /></para>'.format(P37USA),stylesN)
        d2 = Paragraph('<para fontsize=10 leftindent=-65><b>USA</b></para>',stylesN)
        d3 = Paragraph('<para fontsize=8 leading=17 leftindent=22><b>Brugg Wire Rope LLC</b><br/>3411 Turkey Mountain Road NE<br/>US-Rome, GA 30161<br/> T +1 706 314 29 82<br/> F +1 706 235 60 35<br/>lifting.usa@brugg.com<br/>brugglifting.com</para>',stylesN)
        dt=[[d1,d2],[d3]]
        dtt =Table(dt,colWidths=[5*cm,3.5*cm])
        dtt.setStyle(TableStyle([
                                        ('TOPPADDING',(0,0),(-1,-1),20),
                               ]))
        dtt.wrapOn(c,width,height)
        dtt.drawOn(c,5.75*inch, 4.75*inch)

        d1 = Paragraph('<para><img src="{0}" valign="middle" /></para>'.format(P37China),stylesN)
        d2 = Paragraph('<para fontsize=10 leftindent=-65><b>CHINA</b></para>',stylesN)
        d3 = Paragraph('<para fontsize=8 leading=17 leftindent=22><b>BRUGG LIFTING</b><br/>Plant 1, Nr. 88 Jinling East Road<br/>Suzhou Industrial Park<br/>Jiangsu Province, 215121<br/>P.R. China<br/>T +86 512 6299 0779<br/> F +86 512 6299 0774<br/>lifting.cn@brugg.com<br/>brugglifting.cn</para>',stylesN)
        dt=[[d1,d2],[d3]]
        dtt =Table(dt,colWidths=[5*cm,3.5*cm])
        dtt.setStyle(TableStyle([
                                        ('TOPPADDING',(0,0),(-1,-1),20),
                               ]))
        dtt.wrapOn(c,width,height)
        dtt.drawOn(c,30, 1.65*inch)

        d1 = Paragraph('<para><img src="{0}" valign="middle" /></para>'.format(P37WorldWide),stylesN)
        d2 = Paragraph('<para fontsize=10 leftindent=-65><b> WELTWEIT</b></para>',stylesN)
        d3 = Paragraph('<para  align="Justify"fontsize=8 leading=17 leftindent=22> Weltweit erhalten Sie unsere Qualitäts-Produkte bei über 20 Vertriebspartnern.</para>',stylesN)
        dt=[[d1,d2],[d3]]
        dtt =Table(dt,colWidths=[5*cm,3.5*cm])
        dtt.setStyle(TableStyle([
                                        ('TOPPADDING',(0,0),(-1,-1),20),
                               ]))
        dtt.wrapOn(c,width,height)
        dtt.drawOn(c,3.1*inch, 3*inch)

        textobject = c.beginText()
        textobject.setTextOrigin(40, 1.1*inch)
        c.setFillColor('#C0C0C0')
        textobject.setFont("Helvetica-Bold",57)
        textobject.textLines('''
                                brugglifting.com
                                 ''')
        c.drawText(textobject)

        textobject = c.beginText()
        textobject.setTextOrigin(40, 0.75*inch)
        c.setFillColor('#C0C0C0')
        textobject.setFont("Helvetica", 7)
        textobject.textLines('''
                                Erstellungsdatum 03 / 2019
                                Änderungen vorbehalten. Massangaben unverbindlich. Keine Gewährleistung für Druckfehler oder Irrtümer.
                                Sofern nichts anderes vereinbart, gelten unsere allgemeinen Verkaufs- und Lieferbedingungen.
                                Wir bedanken uns bei © OSMA - Aufzüge für die Bereitstellung der Fotos auf folgenden Seiten: 9, 13
                                Gestaltung, Umsetzung: schaefer-design.de
                                 ''')
        c.drawText(textobject)

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        if pageCount %2 == 0:
            print "dont worry"
        else:
            c.showPage()
            pageCount +=1

        lp = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P38BG.png')
        c.drawImage(lp,0,0,width=width,height=height, mask='auto')

        textobject = c.beginText()
        textobject.setTextOrigin(250, 40)
        textobject.setFont("FrutigerB", 12)
        # textobject.setFillColorRGB(192,192,192)
        textobject.setFillColor(colors.white)
        textobject.textLines('''
                                brugglifting.com
                              ''')
        c.drawText(textobject)

        c.showPage()
        pageCount +=1

    elif lang == 'zh':
        pageTLastBG = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes','page36.jpg')
        pageSLastBG = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes','page37.jpg')

        c.drawImage(pageTLastBG,0,0,width=width, height=height, mask='auto')

        q1  = Paragraph('<para fontsize=23 fontName= STSong-Light align="justify" color = white > <b>我们在全球范围.</b><span color=rgb(0,157,224)><b>内为您提供服务.</b></span></para>',stylesN)
        t= [[q1]]
        tq = Table(t)
        tq.wrapOn(c,width,height)
        tq.drawOn(c,30,8.2*inch)



        p1  = Paragraph('<para fontName = STSong-Light fontsize=10 align="justify"> brugglifting.com · 紧凑的主页</para>',stylesN)
        w1  = Paragraph('<para fontName = STSong-Light fontsize=10 align="justify" leading=13> 我们的主页为您生动的描绘了我们的整个产品范围。获取最新的信息,只需要访问我们的主页。</para>',stylesN)

        # p2  = Paragraph('<para fontName = STSong-Light fontsize=10 align="justify" > <b>RLP . </b>Calculate the service life  of your ropes</para>',stylesN)
        # w2  = Paragraph('<para fontName = STSong-Light fontsize=10 align="justify" leading=13> Login in to our service life calculator on our wevsite and enter the data of your ropes tp calculate their service life..</para>',stylesN)

        p3  = Paragraph('<para fontName = STSong-Light fontsize=10 align="justify" > 使用说明 · 重要的钢丝绳使用提示</para>',stylesN)
        w3  = Paragraph('<para fontName = STSong-Light fontsize=10 align="justify" leading=13>我们所交付每一根钢绳都附有正确安装和使用指导。从产品运输到安装后的监测,您都可以在我们提供的指导中找到所有相关的信息。</para>',stylesN)

        p4  = Paragraph('<para fontName = STSong-Light fontsize=10 align="justify" > 用户参考指南 · 钢绳的运输安装</para>',stylesN)
        w4  = Paragraph('<para fontName = STSong-Light fontsize=10 align="justify" leading=13>在绳子的运输和安装方面,您可以利用我们专业知识与经验:在我们的主页 上,通过快速链接带您到我们的目录,该目录不仅提供全面的技术细节而 且还能通过全文搜索信息,您所选定的所有数据都可以存储为PDF文件。</para>',stylesN)

        tp = [[''],[''],[p1],[w1],[''],[''],[''],[''],[''],[''],[p3],[w3],[''],[''],[''],[''],[''],[''],[''],[''],[p4],[w4]]
        tpt = Table(tp,colWidths=11.25*cm)
        tpt.wrapOn(c,width,height)
        tpt.drawOn(c,3.25*inch, 1*inch)


        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        c.drawImage(pageSLastBG,0,0,width=width, height=height, mask='auto')

        textobject = c.beginText()
        textobject.setTextOrigin(2*inch, 0.4*inch)
        textobject.setFont("Helvetica-Bold", 50)
        textobject.setFillColorRGB(192,192,192)
        textobject.textLines('''
                                brugglifting.com
                              ''')
        c.drawText(textobject)

        # c.drawInlineImage(rope,3.25*inch,7.45*inch,width=1.75*inch,height=1.4*inch,preserveAspectRatio=True)

        d1 = Paragraph('<para><img src="{0}" valign="middle" /></para>'.format(P37Swis),stylesN)
        d2 = Paragraph('<para fontName = STSong-Light fontsize=10 leftindent=-65><b> 瑞士 </b></para>',stylesN)
        d3 = Paragraph('<para fontName = STSong-Light fontsize=8 leading=17 leftindent=24><b>BRUGG LIFTING</b><br/>Wydenstrasse 36<br/>5242 Birr<br/> Switzerlad<br/> 电话 +41 (0)56 464 42 42<br/> 传真 +41(0)56 464 42 84<br/>info.lifting@brugg.com<br/>brugglifting.com</para>',stylesN)
        dt=[[d1,d2],[d3]]
        dtt =Table(dt,colWidths=[5*cm,3.5*cm])
        dtt.setStyle(TableStyle([
                                        ('TOPPADDING',(0,0),(-1,-1),20),
                               ]))
        dtt.wrapOn(c,width,height)
        dtt.drawOn(c,30, 4.75*inch)

        d1 = Paragraph('<para><img src="{0}" valign="middle" /></para>'.format(P37Swis),stylesN)
        d2 = Paragraph('<para fontName = STSong-Light fontsize=10 leftindent=-65><b> 瑞士 </b></para>',stylesN)
        d3 = Paragraph('<para fontName = STSong-Light align="Justify" fontsize=8 leading=17 leftindent=20><b>BRUGG LIFTING</b><br/>Chemin de Foret 12<br/>1024 Ecublens<br/> Switzerlad<br/> 电话 +41 (0)21 634 20 21<br/> 传真 +41(0)21 635 09 71<br/>vente.lifting@brugg.co<br/>brugglifting.com</para>',stylesN)
        dt=[[d1,d2],[d3]]
        dtt =Table(dt,colWidths=[5*cm,3.5*cm])
        dtt.setStyle(TableStyle([
                                        ('TOPPADDING',(0,0),(-1,-1),20),
                               ]))
        dtt.wrapOn(c,width,height)
        dtt.drawOn(c,3.1*inch, 4.75*inch)

        d1 = Paragraph('<para><img src="{0}" valign="middle" /></para>'.format(P37USA),stylesN)
        d2 = Paragraph('<para fontName = STSong-Light fontsize=10 leftindent=-65><b>中国</b></para>',stylesN)
        d3 = Paragraph('<para fontName = STSong-Light fontsize=8 leading=17 leftindent=22><b>Brugg Wire Rope LLC</b><br/>3411 Turkey Mountain Road NE<br/>US-Rome,GA 30161<br/> 电话 +1 706 314 29 82<br/> 传真 +1 706 235 60 35<br/>lifting.usa@brugg.com<br/>brugglifting.com</para>',stylesN)
        dt=[[d1,d2],[d3]]
        dtt =Table(dt,colWidths=[5*cm,3.5*cm])
        dtt.setStyle(TableStyle([
                                        ('TOPPADDING',(0,0),(-1,-1),20),
                               ]))
        dtt.wrapOn(c,width,height)
        dtt.drawOn(c,5.75*inch, 4.95*inch)

        d1 = Paragraph('<para><img src="{0}" valign="middle" /></para>'.format(P37China),stylesN)
        d2 = Paragraph('<para fontName = STSong-Light fontsize=10 leftindent=-65><b>美国</b></para>',stylesN)
        d3 = Paragraph('<para fontName = STSong-Light fontsize=8 leading=17 leftindent=22><b>BRUGG LIFTING</b><br/>Plant 1, Nr.88 jingling East Road<br/>Suzhou Industrial Park<br/> jiangsu Province,215121<br/>P.R. China<br/>电话 +86 512 6299 0779<br/> 传真 +86 512 6299 0774<br/>lifting.cn@brugg.com<br/>brugglifting.cn</para>',stylesN)
        dt=[[d1,d2],[d3]]
        dtt =Table(dt,colWidths=[5*cm,3.5*cm])
        dtt.setStyle(TableStyle([
                                        ('TOPPADDING',(0,0),(-1,-1),20),
                               ]))
        dtt.wrapOn(c,width,height)
        dtt.drawOn(c,30, 1.65*inch)

        d1 = Paragraph('<para><img src="{0}" valign="middle" /></para>'.format(P37WorldWide),stylesN)
        d2 = Paragraph('<para fontName = STSong-Light fontsize=10 leftindent=-65><b>世界范围</b></para>',stylesN)
        d3 = Paragraph('<para fontName = STSong-Light align="Justify"fontsize=8 leading=17 leftindent=22>您可以从我们遍布全球的20多个分销商那里购买到优质的布鲁格产品</para>',stylesN)
        dt=[[d1,d2],[d3]]
        dtt =Table(dt,colWidths=[5*cm,3.5*cm])
        dtt.setStyle(TableStyle([
                                        ('TOPPADDING',(0,0),(-1,-1),20),
                               ]))
        dtt.wrapOn(c,width,height)
        dtt.drawOn(c,3.1*inch, 3*inch)

        textobject = c.beginText()
        textobject.setTextOrigin(40, 1.1*inch)
        c.setFillColor('#C0C0C0')
        textobject.setFont("Helvetica-Bold",57)
        textobject.textLines('''
                                brugglifting.com
                                 ''')
        c.drawText(textobject)

        textobject = c.beginText()
        textobject.setTextOrigin(40, 0.75*inch)
        c.setFillColor('#C0C0C0')
        textobject.setFont("STSong-Light", 7)
        textobject.textLines('''
                                版本日期 03 / 2019
                                我们的产品介绍如有变化,印刷错误或其它问题
                                以公司解释为准
                                感谢 © OSMA-Aufzüge 为第9和第15页提供图片
                                以及 www.schaefer-design.com 为目录进行设计和印刷
                                 ''')
        c.drawText(textobject)

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        if pageCount %2 == 0:
            print "dont worry"
        else:
            c.showPage()
            pageCount +=1

        lp = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','P38BG.png')
        c.drawImage(lp,0,0,width=width,height=height, mask='auto')

        textobject = c.beginText()
        textobject.setTextOrigin(250, 40)
        textobject.setFont("FrutigerB", 12)
        # textobject.setFillColorRGB(192,192,192)
        textobject.setFillColor(colors.white)
        textobject.textLines('''
                                brugglifting.com
                              ''')
        c.drawText(textobject)

        c.showPage()
        pageCount +=1


def templateAndAccess(request,response,styles,stylesN,stylesH,width,height,c,lang,templatesTractionRopes2,accessoriesCat,pageCount):
    if lang == 'en':

        for template in templatesTractionRopes2:

            prodfield = ProductField.objects.filter(template = template.pk)
            # # printprodfield
            prod = Product.objects.filter(template = template.pk)
            # # printprod



            if pageCount%2 == 0:



                if template.catalogBG1:
                    background = template.catalogBG1.path
                else:
                    background = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes',"page13.jpg")

                c.drawImage(background,0,0,width=width, height=height, mask = 'auto')
                name2 = Paragraph('<para fontName = FrutigerB fontSize=30>%s</para>'%(template.name), stylesN)
                nd =[[name2]]
                w = pdfmetrics.stringWidth(template.name, "FrutigerB", 30)
                # # printw, "text width "
                ndt = Table(nd)
                w1,h1 = ndt.wrapOn(c, width,height)
                width2 = width - w -50
                ndt.drawOn(c, width2,570)

            else:
                if template.catalogBG2:
                    background = template.catalogBG2.path
                else:
                    background = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes',"page12.jpg")
                c.drawImage(background,0,0,width=width, height=height, mask = 'auto')
                name2 = Paragraph('<para fontName = FrutigerB fontSize=30>%s</para>'%(template.name), stylesN)
                nd =[[name2]]
                w = pdfmetrics.stringWidth(template.name, "FrutigerB", 30)
                # # printw, "text width "
                ndt = Table(nd)
                w1,h1 = ndt.wrapOn(c, width,height)
                width2 = 50
                ndt.drawOn(c, width2,570)

            test =  template.parent_name
            test = test.split("-")
            text = ''
            for i in test:
                text += i.upper() + " "
            name = Paragraph('<para fontName = FrutigerB fontSize=15>%s</para>'%(text), styles['Normal'])
            nd =[[name]]
            w = pdfmetrics.stringWidth(template.parent_name, "FrutigerB", 10)
            # # printw, "text width "
            ndt = Table(nd)
            w1,h1 = ndt.wrapOn(c, width,height)

            ndt.drawOn(c, 200,548)

            c.drawImage(template.defaultImage.path,50,400,width=1.4*inch,height=1.4*inch, mask='auto')
            height2 = height - 330
            # printtemplate.disclaimer_en, 'desclaimer english '
            height2 = htmlRMLCanvvas(template.rteData1_en,c,4.5*inch,200,height2,stylesN,colors.black,lang)


            height2 = height2 - 50
            height3 = height2 + 15
            height4 = height2
            height5 = height2 - 30
            _color = rangeColors(template.color)
            c.setFillColor(_color.hex)
            c.setStrokeColor(colors.white)
            c.rect(3.3*inch,height2,0.6*inch,0.6*inch, fill=1)
            c.setFont("Helvetica-Bold", 7)
            c.setFillColor(colors.black)
            k = json.loads(template.keyword1)
            k11 =[[k]]
            r11 = Table(k11,colWidths=3.6*inch,rowHeights=4*mm)
            c.setFont("Helvetica", 5)

            para101 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%(k["value1"]), styles['Normal'])
            desc101 = [[para101]]
            r101 = Table(desc101,colWidths=0.6*inch,rowHeights=1*mm)
            w, h = r101.wrapOn(c, width,height)
            r101.drawOn(c, 3.3*inch, height3)

            para102 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%("N/mm2"), styles['Normal'])
            desc102 = [[para102]]
            r102 = Table(desc102,colWidths=0.6*inch,rowHeights=1*mm)
            r102.wrapOn(c, width,height)
            r102.drawOn(c, 3.3*inch, height4)

            para103 = Paragraph('<para align="center" fontName = FrutigerR fontSize=7 >%s</para>'%("E-Module"), styles['Normal'])
            desc103 = [[para103]]
            r103 = Table(desc103,colWidths=0.6*inch,rowHeights=1*mm)
            r103.wrapOn(c, width,height)
            r103.drawOn(c, 3.3*inch, height5)


            _color = rangeColors(template.color,luminance=.5)
            c.setFillColor(_color.hex)
            c.rect(4.3*inch,height2,0.6*inch,0.6*inch, fill=1)
            c.setFont("Helvetica-Bold", 7)
            c.setFillColor(colors.black)
            k1 = json.loads(template.keyword2)

            k12 =[[k1]]

            r12 = Table(k12,colWidths=5*inch,rowHeights=10*mm)

            para201 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%(k1["value1"]), styles['Normal'])
            desc201 = [[para201]]
            r201 = Table(desc201,colWidths=0.6*inch)
            w,h = r201.wrapOn(c, width,height)

            r201.drawOn(c, 4.3*inch, height3)

            para202 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%("%"), styles['Normal'])
            desc202 = [[para202]]
            r202 = Table(desc202,colWidths=0.6*inch,rowHeights=1*mm)
            r202.wrapOn(c, width,height)
            r202.drawOn(c, 4.3*inch, height4)

            para203 = Paragraph('<para align="center" fontName = FrutigerR fontSize=7 >%s</para>'%("Elastic<br/>Elongation"), styles['Normal'])
            desc203 = [[para203]]
            r203 = Table(desc203,colWidths=0.65*inch,rowHeights=1*mm)
            r203.wrapOn(c, width,height)
            r203.drawOn(c, 4.3*inch, height5 )


            _color = rangeColors(template.color,luminance=.7)
            c.setFillColor(_color.hex)
            c.setStrokeColor(colors.white)

            c.rect(5.3*inch,height2,0.6*inch,0.6*inch, fill=1)
            c.setFont("Helvetica-Bold", 7)
            c.setFillColor(colors.black)
            k2 = json.loads(template.keyword3)

            k13 = [[k2]]

            r13 = Table(k13,colWidths=5*inch,rowHeights=10*mm)

            para301 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%(k2["value1"]), styles['Normal'])
            desc301 = [[para301]]
            r301 = Table(desc301,colWidths=0.6*inch,rowHeights=1*mm)
            r301.wrapOn(c, width,height)
            r301.drawOn(c, 5.3*inch, height3)

            para302 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%("%"), styles['Normal'])
            desc302 = [[para302]]
            r302 = Table(desc302,colWidths=0.6*inch,rowHeights=1*mm)
            r302.wrapOn(c, width,height)
            r302.drawOn(c, 5.3*inch, height4)

            para303 = Paragraph('<para align="center" fontName = FrutigerR fontSize=7 >%s</para>'%("Permanent<br/>Elongation"), styles['Normal'])
            desc303 = [[para303]]
            r303 = Table(desc303,colWidths=0.7*inch,rowHeights=1*mm)
            r303.wrapOn(c, width,height)
            r303.drawOn(c, 5.3*inch, height5)


            _color = rangeColors(template.color,luminance=.9)
            c.setFillColor(_color.hex)
            c.setStrokeColor(colors.white)
            c.rect(6.3*inch,height2,0.6*inch,0.6*inch, fill=1)
            c.setFont("Helvetica-Bold", 7)
            c.setFillColor(colors.black)
            k3 = json.loads(template.keyword4)
            k14 = [[k3]]
            r14 = Table(k14,colWidths=5*inch,rowHeights=10*mm)

            para401 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%(k3["value1"]), styles['Normal'])
            desc401 = [[para401]]
            r401 = Table(desc401,colWidths=0.6*inch,rowHeights=1*mm)
            r401.wrapOn(c, width,height)
            r401.drawOn(c, 6.3*inch, height3)

            para402 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%("m"), styles['Normal'])
            desc402 = [[para402]]
            r402 = Table(desc402,colWidths=0.6*inch,rowHeights=1*mm)
            r402.wrapOn(c, width,height)
            r402.drawOn(c, 6.3*inch, height4)

            para403 = Paragraph('<para align="center" fontName = FrutigerR fontSize=7 >%s</para>'%("Lifting<br/>Height"), styles['Normal'])
            desc403 = [[para403]]
            r403 = Table(desc403,colWidths=0.6*inch,rowHeights=1*mm)
            r403.wrapOn(c, width,height)
            r403.drawOn(c, 6.3*inch, height5)


            height2 = height5

            data = []
            # data2 = []
            dataHeading = ['Item Number']
            dataHeading2 = ['']
            list1 = []
            list2 = []
            for j in prodfield:
                # printprodfield
                if j.inPdf ==True:

                    # printj.name,'kkkkkkkkkkkkk'
                    try:
                        name1, name2 = j.name.split('(')
                        # # printname2[:-1]
                        name2 = ''+name2[:-1]
                        # # printname2
                    except:
                        name1 = j.name
                        name2 = ''

                    # # printname1, ' ' , name2

                    list1.append(name1)
                    list2.append(name2)
            for a in list1:
                dataHeading.append(a)
            for b in list2:
                dataHeading2.append(b)



            for i in prod:
                appendlist = [i.itemNumber]
                for j in prodfield:
                    prodQty = ProductValueMap.objects.filter( field = j.pk,product = i.pk)
                    for k in prodQty:
                        if j.inPdf ==True:
                            if j.type=='Char':
                                appendlist.append(k.char)
                            if j.type=='float':
                                appendlist.append(k.fValue)
                            if j.type=='Integer':
                                appendlist.append(k.iValue)
                            if j.type=='Boolean':
                                appendlist.append(k.bool)
                data.append(appendlist)

            height2 = height2-40
            leftHeight = height2-70
            numberRows = int(leftHeight/20)
            # printheight2, leftHeight, numberRows, "number of rows"
            dataLength = len(data)
            data.insert(0,dataHeading)
            data.insert(1,dataHeading2)

            if len(data)<= numberRows:
                if dataLength>0:
                    t5 = Table(data,rowHeights=[20]*len(data))
                    t5.setStyle(TableStyle([
                                         ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                                         ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                                         ('FONTSIZE', (0, 0), (-1, -1), 7),
                                         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                         ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                                         ]))
                    w5, h5 = t5.wrapOn(c, width, height)
                    height2 = height2 - h5
                    t5.drawOn(c, 200, height2)


                para2 = Paragraph('<para fontName = Helvetica fontSize=6 >%s</para>'%(template.disclaimer_en), styles['Normal'])
                tab = [[para2]]
                r = Table(tab,colWidths=3.25*inch)
                w,h1 = r.wrapOn(c, width,height)
                height2 = height2 - h1
                r.drawOn(c, 200, height2)

                gm934 = Paragraph('<para></para>',stylesN)
                gmn934 = Paragraph('<para></para>',stylesN)

                data =  [[gm934,gmn934]]

                t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
                t.setStyle(TableStyle([
                                    ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                                     ]))
                t.wrapOn(c,width, height)


                c.setFillColor(colors.black)
                c.setFont("Helvetica-Bold",10)
                if pageCount%2==0:
                    t.drawOn(c, -3*inch,0.2*inch)
                    c.drawString(20, 0.15*inch, str(pageCount))
                else:
                    t.drawOn(c, width-35,0.2*inch)
                    c.drawString(width-30, 0.15*inch, str(pageCount))

                c.showPage()
                pageCount +=1
            else:

                data1 = data[:numberRows-1]

                data2 = data[numberRows:-1]

                t5 = Table(data1,rowHeights=[20]*len(data1))
                t5.setStyle(TableStyle([
                                     ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                                     ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                                     ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                                     ('FONTSIZE', (0, 0), (-1, -1), 7),
                                     ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                     ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                                     ]))
                w5, h5 = t5.wrapOn(c, width, height)
                height2 = height2 - h5
                t5.drawOn(c, 200, height2)



                para2 = Paragraph('<para fontName = Helvetica fontSize=6 >%s</para>'%(template.disclaimer_en), styles['Normal'])
                tab = [[para2]]
                r = Table(tab,colWidths=3.25*inch)
                w,h1 = r.wrapOn(c, width,height)
                height2 = height2 - h1
                r.drawOn(c, 200, height2)

                gm934 = Paragraph('<para></para>',stylesN)
                gmn934 = Paragraph('<para></para>',stylesN)

                data =  [[gm934,gmn934]]

                t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
                t.setStyle(TableStyle([
                                    ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                                     ]))
                t.wrapOn(c,width, height)


                c.setFillColor(colors.black)
                c.setFont("Helvetica-Bold",10)
                if pageCount%2==0:
                    t.drawOn(c, -3*inch,0.2*inch)
                    c.drawString(20, 0.15*inch, str(pageCount))
                else:
                    t.drawOn(c, width-35,0.2*inch)
                    c.drawString(width-30, 0.15*inch, str(pageCount))

                c.showPage()
                pageCount +=1
                maxNumberItems = 15

                index = float(len(data2))/maxNumberItems

                index = int(math.ceil(index))

                for i in range(index):
                    if i == index-1:
                        data1 = data2[maxNumberItems*i:-1]
                        data1.insert(0,dataHeading)
                        data1.insert(1,dataHeading2)

                    else:
                        data1 = data2[maxNumberItems*i:maxNumberItems*(i+1)-1]
                        data1.insert(0,dataHeading)
                        data1.insert(1,dataHeading2)

                    pageCount = addElevatorPage(c, data1,template,stylesN,pageCount,lang)


        #new page

        # sha1 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes','PageShadowRightSide.png')
        # sha = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes','PageShadowLeftSide.png')
        bg1 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes',"page21Img.png")


        c.drawImage(bg1,0*inch,0,width=8.3*inch,height=11.7*inch,mask='auto')

        # c.drawImage(sha,0*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

        c.setFont("Helvetica-Bold",10)

        tp = Paragraph('<para fontsize=9>Desingation and Classification of wire ropes(EN 12385-2 formerly ISO 17893)</para>',stylesN)
        tpt=[[tp]]
        tptab=Table(tpt)
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,3.6*inch,7*inch)

        c.setFillColor('#D0D0D0')
        c.rect(4*inch,6.35*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
        c.setFont("Helvetica-Bold",8)

        c.setFillColor('#000000')
        c.drawCentredString(4.07*inch,6.37*inch,"A")

        tr = Paragraph('<para fontSize=8 ><b >Rope nominal Diameter in mm</b><br/>(see coresponding table for each )</para>',stylesN)
        trt=[[tr]]
        trtab=Table(trt)
        trtab.wrapOn(c,width,height)
        trtab.drawOn(c,4.25*inch,6.1*inch)


        c.setFillColor('#D8D8D8')
        c.rect(4*inch,5.9*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
        c.setFont("Helvetica-Bold",8)
        c.setFillColor('#3C434B')
        c.drawCentredString(4.07*inch,5.93*inch,"B")
        tr = Paragraph('<para fontSize=8 ><b >Rope Construction</b><br/></para>',stylesN)
        trt=[[tr]]
        trtab=Table(trt)
        trtab.wrapOn(c,width,height)
        trtab.drawOn(c,4.25*inch,5.85*inch)

        tr = Paragraph('<para fontSize=8 ><b >Construction and Lay Direction</b><br/></para>',stylesN)
        trt=[[tr]]
        trtab=Table(trt)
        trtab.wrapOn(c,width,height)
        trtab.drawOn(c,4.25*inch,5.6*inch)

        c.setFillColor('#DCDCDC')
        c.rect(4*inch,5.65*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
        c.setFont("Helvetica-Bold",8)
        c.setFillColor('#3C434B')
        c.drawCentredString(4.07*inch,5.68*inch,"C")
        data1 = [['-','simple lay strand',''],
                ['' , 'example for strand construction','7 d.h.(1-6)'],
                ['s' , 'seale parallel lay',''],
                ['' , 'example for strand construction','19S d.h. (1-9-9)'],
                ['W','Warrington parallel lay',''],
                ['' , 'example for strand construction','19W d.h. (1-6-6+6)'],
                ['F' , 'Filler parallel lay',''],
                ['' , 'example for strand construction','21F d.h. (1-5-5F-10)'],
                ['' , '','25F d.h. (1-6-6F-12)'],
                ['WS' , 'combined (warrington seale) parallel lay',''],
                ['' , 'example for strand construction','31WS d.h. (1-6-6+6-12)'],
        ]

        r = Table(data1,colWidths=[0.75*cm,3.25*cm,2*cm],rowHeights=3.25*mm)
        r.setStyle(TableStyle([
                            ('FONTSIZE',(0,0),(-1,-1),7),
                                    ('LEFTPADDING',(1,0),(-1,-1),7),
                                     ('LEFTPADDING',(2,0),(-1,-1),50),
                                     ('VALIGN',(0,0),(-1,-1),'TOP')
                               ]))
        r.wrapOn(c,width,height)
        r.drawOn(c,4.15*inch,4.25*inch)

        c.setFillColor('#DCDCDC')
        c.rect(4*inch,3.9*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
        c.setFont("Helvetica-Bold",8)
        c.setFillColor('#3C434B')
        c.drawCentredString(4.07*inch,3.93*inch,"D")

        tr = Paragraph('<para fontSize=8 ><b >Construction of Core</b><br/></para>',stylesN)
        trt=[[tr]]
        trtab=Table(trt)
        trtab.wrapOn(c,width,height)
        trtab.drawOn(c,4.25*inch,3.85*inch)

        data2 = [['Single layer rope with fibre core FC',''],
                ['NFC' , 'natural fibre core'],
                ['SFC' , 'synthetic fibre core'],
                ['' , ''],
                ['Single layer rope with fibre core WC',''],
                ['WSC' , 'wire strand core'],
                ['IWRC' , 'independant wire rope core',''],
                ['' , ''],
                ['Rope with parallel lay'],
                ['PWRC' , 'parallel wire rope core',''],
        ]

        s = Table(data2,colWidths=17*mm,rowHeights=2.75*mm)
        s.setStyle(TableStyle([
                                    ('FONTSIZE',(0,0),(-1,-1),7),
                                    ('LEFTPADDING',(1,0),(-1,-1),7),
                                    ('LEFTPADDING',(2,0),(-1,-1),20),('VALIGN',(0,0),(-1,-1),'TOP')
                               ]))
        s.wrapOn(c,width,height)
        s.drawOn(c,4.2*inch,2.85*inch)

        c.setFillColor('#DCDCDC')
        c.rect(4*inch,2.4*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
        c.setFont("Helvetica-Bold",8)
        c.setFillColor('#3C434B')
        c.drawCentredString(4.07*inch,2.43*inch,"E")

        tr = Paragraph('<para fontSize=8 ><b >Nominal Tensile Grade of wires in N/mm2</b><br/></para>',stylesN)
        trt=[[tr]]
        trtab=Table(trt)
        trtab.wrapOn(c,width,height)
        trtab.drawOn(c,4.25*inch,2.35*inch)


        c.setFillColor('#DCDCDC')
        c.rect(4*inch,2.1*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
        c.setFont("Helvetica-Bold",8)
        c.setFillColor('#3C434B')
        c.drawCentredString(4.07*inch,2.12*inch,"F")
        tr = Paragraph('<para fontSize=8 ><b >Surface Finish of Wires</b><br/></para>',stylesN)
        trt=[[tr]]
        trtab=Table(trt)
        trtab.wrapOn(c,width,height)
        trtab.drawOn(c,4.25*inch,2.05*inch)

        data3 = [['U','bright'],
                ['B' , 'zinc coated (classB)'],
        ]

        u = Table(data3,colWidths=17*mm,rowHeights=3*mm)
        u.setStyle(TableStyle([
                            ('FONTSIZE',(0,0),(-1,-1),7),
                            ('LEFTPADDING',(1,0),(-1,-1),7),
                            ('VALIGN',(0,0),(-1,-1),'TOP')
                               ]))
        u.wrapOn(c,width,height)
        u.drawOn(c,4.25*inch,1.75*inch)

        c.setFillColor('#DCDCDC')
        c.rect(4*inch,1.5*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
        c.setFont("Helvetica-Bold",8)
        c.setFillColor('#3C434B')
        c.drawCentredString(4.07*inch,1.53*inch,"G")
        tr = Paragraph('<para fontSize=8 ><b >Type and Direction of Lay</b><br/></para>',stylesN)
        trt=[[tr]]
        trtab=Table(trt)
        trtab.wrapOn(c,width,height)
        trtab.drawOn(c,4.35*inch,1.43*inch)

        data3 = [['z','right lay (strand)'],
                ['s','left lay (strand)'],
                ['Z','right lay (rope)'],
                ['S','left lay (rope)'],
                ['sZ(RRL)','regular lay,right hand'],
                ['zS(RLL)','rregular lay,left-hand'],
        ]

        u = Table(data3,colWidths=17*mm,rowHeights=3.5*mm)
        u.setStyle(TableStyle([
                            ('FONTSIZE',(0,0),(-1,-1),7),
                                    ('LEFTPADDING',(1,0),(-1,-1),7),
                                     ('VALIGN',(0,0),(-1,-1),'TOP')
                               ]))
        u.wrapOn(c,width,height)
        u.drawOn(c,4.25*inch,0.6*inch)

        c.setFont("Helvetica",12)
        c.setFillColor('#ffffff')
        c.drawString(250, 7.65*inch, "ABBREVIATED DESIGNATIONS")

        c.setFont("Helvetica",10)
        c.setFillColor('#000000')
        c.drawString(30, 7*inch, "Example")

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        for accessorie in accessoriesCat:
            accessObjects = AccessoriesSection.objects.filter(accessories=accessorie,lang = "en")
            # # printaccessObjects,'accessObjects'

            for access in accessObjects:
                # # printaccess.productName, "product name"
                prodfield = AccessoriesField.objects.filter(productBaseName = access.basicProductName)
                # # printprodfield, "product fields "
                itemNumbers = AccessoriesData.objects.filter(productBaseName = access.basicProductName)
                # # printitemNumbers, "item numbers"
                itemNumberValues = AccessoriesValueMap.objects.filter(productBaseName = access.basicProductName)
                # # printitemNumberValues, "itemNumberValues"
                # addAccessoriePage(c,access, prodfield,itemNumbers, itemNumberValues, stylesN)
                # width,height = A4
                accessoriesPK = access.accessories
                if access.image2:
                    productImage = access.image2.path
                else:
                    productImage = os.path.join(globalSettings.BASE_DIR , 'static_shared/images',"stars.jpeg")



                if pageCount%2 == 0:
                    if access.catalogBG1:
                        background = access.catalogBG1.path
                    else:
                        background = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes',"page22a.jpg")
                    c.drawImage(background,0,0,width=width, height=height, mask = 'auto')

                    # name = Paragraph('<para fontName = FrutigerB fontSize=25>%s</para>'%(access.productName), stylesN)
                    # nd =[[name]]
                    # w = pdfmetrics.stringWidth(access.productName, "FrutigerB", 30)
                    # # printw, "text width "
                    # ndt = Table(nd)
                    # w1,h1 = ndt.wrapOn(c, width,height)
                    # width2 = width - w
                    # ndt.drawOn(c, width2,570)
                    # name = Paragraph('<para  fontName = FrutigerB fontSize=15>%s</para>'%((access.categoryName).upper()), stylesN)
                    # des =[[name]]
                    # dest = Table(des,colWidths=8*cm)
                    # w2, h3 = dest.wrapOn(c, width,height)
                    # # # printw2,w1, "tag width"
                    # # width2 = width2 + w +10
                    # print w, "tagline width"
                    # width2 = width2-w2 + 50
                    # dest.drawOn(c, width2,560)



                else:
                    if access.catalogBG2:
                        background = access.catalogBG2.path
                    else:
                        background = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes',"page22a.jpg")
                    c.drawImage(background,0,0,width=width, height=height, mask = 'auto')
                    # name = Paragraph('<para fontName = FrutigerB fontSize=25>%s</para>'%(access.productName), stylesN)
                    # nd =[[name]]
                    # w = pdfmetrics.stringWidth(access.productName, "FrutigerB", 30)
                    # # printw, "text width "
                    # ndt = Table(nd)
                    # w1,h1 = ndt.wrapOn(c, width,height)
                    # width2 = 50
                    # ndt.drawOn(c, width2,570)
                    # name = Paragraph('<para  fontName = FrutigerB fontSize=15>%s</para>'%((access.categoryName).upper()), stylesN)
                    # des =[[name]]
                    # dest = Table(des,colWidths=8*cm)
                    # w2, h3 = dest.wrapOn(c, width,height)
                    # # # printw2,w1, "tag width"
                    # # width2 = width2 + w +10
                    # print w, "tagline width"
                    # width2 = w
                    # dest.drawOn(c, width2,560)
                    #

                name = Paragraph('<para fontName = FrutigerB fontSize=25>%s</para>'%(access.productName), stylesN)
                nd =[[name]]
                w = pdfmetrics.stringWidth(access.productName, "FrutigerB", 30)
                # printw, "text width "
                ndt = Table(nd)
                w1,h1 = ndt.wrapOn(c, width,height)
                width2 = 50
                ndt.drawOn(c, width2,570)
                name = Paragraph('<para  fontName = FrutigerB fontSize=15>%s</para>'%((access.categoryName).upper()), stylesN)
                des =[[name]]
                dest = Table(des,colWidths=8*cm)
                w2, h3 = dest.wrapOn(c, width,height)
                # # printw2,w1, "tag width"
                # width2 = width2 + w +10
                w2 = pdfmetrics.stringWidth((access.categoryName).upper(), "FrutigerB", 15)
                print w, "tagline width"
                width2 = width - w2 - 20
                dest.drawOn(c, width2,560)

                # accessoriesPK = access.accessories
                # # printaccessoriesPK.name, "accessory name"
                #
                # name = Paragraph('<para  fontName = FrutigerB fontSize=15>%s</para>'%((access.categoryName).upper()), stylesN)
                # des =[[name]]
                # dest = Table(des,colWidths=8*cm)
                # w2, h3 = dest.wrapOn(c, width,height)
                # # # printw2,w1, "tag width"
                # # width2 = width2 + w +10
                # print w, "tagline width"
                # width2 = w
                # dest.drawOn(c, width2,560)

                height2 = 550

                img = utils.ImageReader(productImage)
                iw, ih = img.getSize()
                height3 = height2 - ih
                c.drawImage(productImage,30,height3,width=150,preserveAspectRatio=True,mask='auto')

                name = Paragraph('<para fontName = FrutigerB fontSize=15>%s</para>'%(access.title1), stylesN)
                nd =[[name]]
                ndt = Table(nd,colWidths=10*cm)
                w1,h1 = ndt.wrapOn(c, width,height)
                height2 = height2-h1 -20
                ndt.drawOn(c, 200,height2)

                name = Paragraph('<para fontName = FrutigerR fontSize=12>%s</para>'%(access.desc1), stylesN)
                des =[[name]]
                dest = Table(des,colWidths=10*cm)
                w2, h2 = dest.wrapOn(c, width,height)
                # printw2, h2, "height of para1"
                height2 = height2 -h2
                dest.drawOn(c, 200,height2)

                name = Paragraph('<para fontName = FrutigerB fontSize=15>%s</para>'%(access.title2), stylesN)
                nd =[[name]]
                ndt = Table(nd,colWidths=10*cm)
                w3,h3 = ndt.wrapOn(c, width,height)
                height2 = height2 -h3-30
                ndt.drawOn(c, 200,height2)


                name = Paragraph('<para fontName = FrutigerR fontSize=12>%s</para>'%(access.desc2), stylesN)
                des =[[name]]
                dest = Table(des,colWidths=10*cm)
                w4, h4 = dest.wrapOn(c, width,height)
                height2 = height2 -h4
                dest.drawOn(c, 200,height2)

                data = []
                # data2 = []
                dataHeading = ['Item Number']
                dataHeading2 = ['']
                list1 = []
                list2 = []
                for j in prodfield:
                    # printprodfield
                    if j.inPdf ==True:

                        # printj.name,'kkkkkkkkkkkkk'
                        try:
                            name1, name2 = j.name.split('(')
                            # printname2[:-1]
                            name2 = ''+name2[:-1]
                            # printname2
                        except:
                            name1 = j.name
                            name2 = ''

                        # printname1, ' ' , name2

                        list1.append(name1)
                        list2.append(name2)
                for a in list1:
                    dataHeading.append(a)
                for b in list2:
                    dataHeading2.append(b)

                # printdataHeading, dataHeading2, "fields  "

                for i in itemNumbers:
                    appendlist = [i.itemNumber]
                    for j in prodfield:
                        prodQty = itemNumberValues.filter( field = j.pk,product = i.pk)
                        for k in prodQty:
                            if j.inPdf ==True:
                                if j.type=='Char':
                                    appendlist.append(k.char)
                                if j.type=='float':
                                    appendlist.append(k.fValue)
                                if j.type=='Integer':
                                    appendlist.append(k.iValue)
                                if j.type=='Boolean':
                                    appendlist.append(k.bool)
                    data.append(appendlist)

                # printlen(data), "data length"
                # printdata , "item number data"

                dataLength = len(data)
                data.insert(0,dataHeading)
                # printdata,len(data), "final data"

                # # printheight2, "height2"
                height2 = height2-40
                leftHeight = height2-120
                numberRows = int(leftHeight/20)
                # printheight2, leftHeight, numberRows, "number of rows"

                if len(data)<= numberRows:
                    if dataLength>0:
                        t5 = Table(data,rowHeights=[20]*len(data))
                        t5.setStyle(TableStyle([
                                             ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                                             ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                                             ('FONTSIZE', (0, 0), (-1, -1), 7),
                                             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                             ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                                             ]))
                        w5, h5 = t5.wrapOn(c, width, height)
                        height2 = height2 - h5
                        t5.drawOn(c, 200, height2)


                    gm934 = Paragraph('<para></para>',stylesN)
                    gmn934 = Paragraph('<para></para>',stylesN)

                    data =  [[gm934,gmn934]]

                    t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
                    t.setStyle(TableStyle([
                                        ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                                         ]))
                    t.wrapOn(c,width, height)


                    c.setFillColor(colors.black)
                    c.setFont("Helvetica-Bold",10)
                    if pageCount%2==0:
                        t.drawOn(c, -3*inch,0.2*inch)
                        c.drawString(20, 0.15*inch, str(pageCount))
                    else:
                        t.drawOn(c, width-35,0.2*inch)
                        c.drawString(width-30, 0.15*inch, str(pageCount))

                    c.showPage()
                    pageCount +=1
                else:
                    # print"in else"
                    data1 = data[:numberRows-1]
                    # printdata1, "data1"
                    data2 = data[numberRows:-1]
                    # printdata2, "data2"
                    t5 = Table(data1,rowHeights=[20]*len(data1))
                    t5.setStyle(TableStyle([
                                         ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                                         ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                                         ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                                         ('FONTSIZE', (0, 0), (-1, -1), 7),
                                         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                         ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                                         ]))
                    w5, h5 = t5.wrapOn(c, width, height)
                    height2 = height2 - h5
                    t5.drawOn(c, 200, height2)

                    gm934 = Paragraph('<para></para>',stylesN)
                    gmn934 = Paragraph('<para></para>',stylesN)

                    data =  [[gm934,gmn934]]

                    t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
                    t.setStyle(TableStyle([
                                        ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                                         ]))
                    t.wrapOn(c,width, height)


                    c.setFillColor(colors.black)
                    c.setFont("Helvetica-Bold",10)
                    if pageCount%2==0:
                        t.drawOn(c, -3*inch,0.2*inch)
                        c.drawString(20, 0.15*inch, str(pageCount))
                    else:
                        t.drawOn(c, width-35,0.2*inch)
                        c.drawString(width-30, 0.15*inch, str(pageCount))

                    c.showPage()
                    pageCount +=1

                    maxNumberItems = 20

                    index = float(len(data2))/maxNumberItems
                    # printindex
                    index = int(math.ceil(index))
                    # printindex, range(index),"index ...."
                    for i in range(index):
                        if i == index-1:
                            data1 = data2[maxNumberItems*i:-1]
                            data1.insert(0,dataHeading)
                            # printlen(data1), i , "if loop"
                        else:
                            data1 = data2[maxNumberItems*i:maxNumberItems*(i+1)-1]
                            data1.insert(0,dataHeading)
                            # printlen(data1), i, "else loop"
                        # printdata1, "datapass "
                        pageCount = addAccessoriePageExtra(c, data1, access,stylesN,productImage,pageCount,lang)



    elif lang == 'zh':

        for template in templatesTractionRopes2:

            prodfield = ProductField.objects.filter(template = template.pk)
            # printprodfield
            prod = Product.objects.filter(template = template.pk)
            # printprod



            if pageCount%2 == 0:
                if template.catalogBG1:
                    background = template.catalogBG1.path
                else:
                    background = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes',"page13.jpg")

                c.drawImage(background,0,0,width=width, height=height, mask = 'auto')
                name = Paragraph('<para fontName = FrutigerB fontSize=30>%s</para>'%(template.name), stylesN)
                nd =[[name]]
                w = pdfmetrics.stringWidth(template.name, "FrutigerB", 30)
                # printw, "text width "
                ndt = Table(nd)
                w1,h1 = ndt.wrapOn(c, width,height)
                width2 = width - w -50
                ndt.drawOn(c, width2,570)



            else:
                if template.catalogBG2:
                    background = template.catalogBG2.path
                else:
                    background = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes',"page12.jpg")
                c.drawImage(background,0,0,width=width, height=height, mask = 'auto')
                name = Paragraph('<para fontName = FrutigerB fontSize=30>%s</para>'%(template.name), stylesN)
                nd =[[name]]
                w = pdfmetrics.stringWidth(template.name, "FrutigerB", 30)
                # printw, "text width "
                ndt = Table(nd)
                w1,h1 = ndt.wrapOn(c, width,height)
                width2 = 50
                ndt.drawOn(c, width2,570)


            test =  template.parent_name
            test = test.split("-")
            text = ''
            for i in test:
                text += i.upper() + " "
            name = Paragraph('<para fontName = FrutigerB fontSize=15>%s</para>'%(text), styles['Normal'])
            nd =[[name]]
            w = pdfmetrics.stringWidth(template.parent_name, "FrutigerB", 10)
            # printw, "text width "
            ndt = Table(nd)
            w1,h1 = ndt.wrapOn(c, width,height)

            ndt.drawOn(c, 200,548)

            c.drawImage(template.defaultImage.path,50,400,width=1.4*inch,height=1.4*inch, mask='auto')

            height2 = height - 330
            # printtemplate.disclaimer_en, 'desclaimer english '
            height2 = htmlRMLCanvvas(template.rteData1_ch,c,4.5*inch,200,height2,stylesN,colors.black,lang)


            height2 = height2 - 50
            height3 = height2 + 15
            height4 = height2
            height5 = height2 - 30
            _color = rangeColors(template.color)
            c.setFillColor(_color.hex)
            c.setStrokeColor(colors.white)
            c.rect(3.3*inch,height2,0.6*inch,0.6*inch, fill=1)
            c.setFont("Helvetica-Bold", 7)
            c.setFillColor(colors.black)
            k = json.loads(template.keyword1)
            k11 =[[k]]
            r11 = Table(k11,colWidths=3.6*inch,rowHeights=4*mm)
            c.setFont("Helvetica", 5)

            para101 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%(k["value1"]), styles['Normal'])
            desc101 = [[para101]]
            r101 = Table(desc101,colWidths=0.6*inch,rowHeights=1*mm)
            w, h = r101.wrapOn(c, width,height)
            r101.drawOn(c, 3.3*inch, height3)

            para102 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%("N/mm2"), styles['Normal'])
            desc102 = [[para102]]
            r102 = Table(desc102,colWidths=0.6*inch,rowHeights=1*mm)
            r102.wrapOn(c, width,height)
            r102.drawOn(c, 3.3*inch, height4)

            para103 = Paragraph('<para align="center" fontName = FrutigerR fontSize=7 >%s</para>'%("E-Module"), styles['Normal'])
            desc103 = [[para103]]
            r103 = Table(desc103,colWidths=0.6*inch,rowHeights=1*mm)
            r103.wrapOn(c, width,height)
            r103.drawOn(c, 3.3*inch, height5)


            _color = rangeColors(template.color,luminance=.5)
            c.setFillColor(_color.hex)
            c.rect(4.3*inch,height2,0.6*inch,0.6*inch, fill=1)
            c.setFont("Helvetica-Bold", 7)
            c.setFillColor(colors.black)
            k1 = json.loads(template.keyword2)

            k12 =[[k1]]

            r12 = Table(k12,colWidths=5*inch,rowHeights=10*mm)

            para201 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%(k1["value1"]), styles['Normal'])
            desc201 = [[para201]]
            r201 = Table(desc201,colWidths=0.6*inch)
            w,h = r201.wrapOn(c, width,height)

            r201.drawOn(c, 4.3*inch, height3)

            para202 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%("%"), styles['Normal'])
            desc202 = [[para202]]
            r202 = Table(desc202,colWidths=0.6*inch,rowHeights=1*mm)
            r202.wrapOn(c, width,height)
            r202.drawOn(c, 4.3*inch, height4)

            para203 = Paragraph('<para align="center" fontName = FrutigerR fontSize=7 >%s</para>'%("Elastic<br/>Elongation"), styles['Normal'])
            desc203 = [[para203]]
            r203 = Table(desc203,colWidths=0.65*inch,rowHeights=1*mm)
            r203.wrapOn(c, width,height)
            r203.drawOn(c, 4.3*inch, height5 )


            _color = rangeColors(template.color,luminance=.7)
            c.setFillColor(_color.hex)
            c.setStrokeColor(colors.white)

            c.rect(5.3*inch,height2,0.6*inch,0.6*inch, fill=1)
            c.setFont("Helvetica-Bold", 7)
            c.setFillColor(colors.black)
            k2 = json.loads(template.keyword3)

            k13 = [[k2]]

            r13 = Table(k13,colWidths=5*inch,rowHeights=10*mm)

            para301 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%(k2["value1"]), styles['Normal'])
            desc301 = [[para301]]
            r301 = Table(desc301,colWidths=0.6*inch,rowHeights=1*mm)
            r301.wrapOn(c, width,height)
            r301.drawOn(c, 5.3*inch, height3)

            para302 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%("%"), styles['Normal'])
            desc302 = [[para302]]
            r302 = Table(desc302,colWidths=0.6*inch,rowHeights=1*mm)
            r302.wrapOn(c, width,height)
            r302.drawOn(c, 5.3*inch, height4)

            para303 = Paragraph('<para align="center" fontName = FrutigerR fontSize=7 >%s</para>'%("Permanent<br/>Elongation"), styles['Normal'])
            desc303 = [[para303]]
            r303 = Table(desc303,colWidths=0.7*inch,rowHeights=1*mm)
            r303.wrapOn(c, width,height)
            r303.drawOn(c, 5.3*inch, height5)


            _color = rangeColors(template.color,luminance=.9)
            c.setFillColor(_color.hex)
            c.setStrokeColor(colors.white)
            c.rect(6.3*inch,height2,0.6*inch,0.6*inch, fill=1)
            c.setFont("Helvetica-Bold", 7)
            c.setFillColor(colors.black)
            k3 = json.loads(template.keyword4)
            k14 = [[k3]]
            r14 = Table(k14,colWidths=5*inch,rowHeights=10*mm)

            para401 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%(k3["value1"]), styles['Normal'])
            desc401 = [[para401]]
            r401 = Table(desc401,colWidths=0.6*inch,rowHeights=1*mm)
            r401.wrapOn(c, width,height)
            r401.drawOn(c, 6.3*inch, height3)

            para402 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%("m"), styles['Normal'])
            desc402 = [[para402]]
            r402 = Table(desc402,colWidths=0.6*inch,rowHeights=1*mm)
            r402.wrapOn(c, width,height)
            r402.drawOn(c, 6.3*inch, height4)

            para403 = Paragraph('<para align="center" fontName = FrutigerR fontSize=7 >%s</para>'%("Lifting<br/>Height"), styles['Normal'])
            desc403 = [[para403]]
            r403 = Table(desc403,colWidths=0.6*inch,rowHeights=1*mm)
            r403.wrapOn(c, width,height)
            r403.drawOn(c, 6.3*inch, height5)


            height2 = height5

            data = []
            # data2 = []
            dataHeading = ['Item Number']
            dataHeading2 = ['']
            list1 = []
            list2 = []
            for j in prodfield:
                # printprodfield
                if j.inPdf ==True:

                    # printj.name,'kkkkkkkkkkkkk'
                    try:
                        name1, name2 = j.name.split('(')
                        # printname2[:-1]
                        name2 = ''+name2[:-1]
                        # printname2
                    except:
                        name1 = j.name
                        name2 = ''

                    # printname1, ' ' , name2

                    list1.append(name1)
                    list2.append(name2)
            for a in list1:
                dataHeading.append(a)
            for b in list2:
                dataHeading2.append(b)

            for i in prod:
                appendlist = [i.itemNumber]
                for j in prodfield:
                    prodQty = ProductValueMap.objects.filter( field = j.pk,product = i.pk)
                    for k in prodQty:
                        if j.inPdf ==True:
                            if j.type=='Char':
                                appendlist.append(k.char)
                            if j.type=='float':
                                appendlist.append(k.fValue)
                            if j.type=='Integer':
                                appendlist.append(k.iValue)
                            if j.type=='Boolean':
                                appendlist.append(k.bool)
                data.append(appendlist)

            height2 = height2-40
            leftHeight = height2-100
            numberRows = int(leftHeight/20)
            # printheight2, leftHeight, numberRows, "number of rows"

            data.insert(0,dataHeading)
            data.insert(1,dataHeading2)

            if len(data)<= numberRows:
                    t5 = Table(data,rowHeights=[20]*len(data))
                    t5.setStyle(TableStyle([
                                         ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                                         ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                                         ('FONTSIZE', (0, 0), (-1, -1), 7),
                                         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                         ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                                         ]))
                    w5, h5 = t5.wrapOn(c, width, height)
                    height2 = height2 - h5
                    t5.drawOn(c, 200, height2)


                    para2 = Paragraph('<para fontName = STSong-Light fontSize=6 >%s</para>'%(template.disclaimer_ch), styles['Normal'])
                    tab = [[para2]]
                    r = Table(tab,colWidths=3.25*inch)
                    w,h1 = r.wrapOn(c, width,height)
                    height2 = height2 - h1
                    r.drawOn(c, 200, height2)

                    gm934 = Paragraph('<para></para>',stylesN)
                    gmn934 = Paragraph('<para></para>',stylesN)

                    data =  [[gm934,gmn934]]

                    t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
                    t.setStyle(TableStyle([
                                        ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                                         ]))
                    t.wrapOn(c,width, height)


                    c.setFillColor(colors.black)
                    c.setFont("Helvetica-Bold",10)
                    if pageCount%2==0:
                        t.drawOn(c, -3*inch,0.2*inch)
                        c.drawString(20, 0.15*inch, str(pageCount))
                    else:
                        t.drawOn(c, width-35,0.2*inch)
                        c.drawString(width-30, 0.15*inch, str(pageCount))

                    c.showPage()
                    pageCount +=1
            else:

                data1 = data[:numberRows-1]

                data2 = data[numberRows:-1]

                t5 = Table(data1,rowHeights=[20]*len(data1))
                t5.setStyle(TableStyle([
                                     ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                                     ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                                     ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                                     ('FONTSIZE', (0, 0), (-1, -1), 7),
                                     ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                     ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                                     ]))
                w5, h5 = t5.wrapOn(c, width, height)
                height2 = height2 - h5
                t5.drawOn(c, 200, height2)



                para2 = Paragraph('<para fontName = STSong-Light fontSize=6 >%s</para>'%(template.disclaimer_ch), styles['Normal'])
                tab = [[para2]]
                r = Table(tab,colWidths=3.25*inch)
                w,h1 = r.wrapOn(c, width,height)
                height2 = height2 - h1
                r.drawOn(c, 200, height2)

                gm934 = Paragraph('<para></para>',stylesN)
                gmn934 = Paragraph('<para></para>',stylesN)

                data =  [[gm934,gmn934]]

                t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
                t.setStyle(TableStyle([
                                    ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                                     ]))
                t.wrapOn(c,width, height)

                c.setFillColor(colors.black)
                c.setFont("Helvetica-Bold",10)
                if pageCount%2==0:
                    t.drawOn(c, -3*inch,0.2*inch)
                    c.drawString(20, 0.15*inch, str(pageCount))
                else:
                    t.drawOn(c, width-35,0.2*inch)
                    c.drawString(width-30, 0.15*inch, str(pageCount))

                c.showPage()
                pageCount +=1
                maxNumberItems = 15

                index = float(len(data2))/maxNumberItems

                index = int(math.ceil(index))

                for i in range(index):
                    if i == index-1:
                        data1 = data2[maxNumberItems*i:-1]
                        data1.insert(0,dataHeading)
                        data1.insert(1,dataHeading2)

                    else:
                        data1 = data2[maxNumberItems*i:maxNumberItems*(i+1)-1]
                        data1.insert(0,dataHeading)
                        data1.insert(1,dataHeading2)

                    pageCount = addElevatorPage(c, data1,template,stylesN,pageCount,lang)


        # sha1 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes','PageShadowRightSide.png')
        # sha = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes','PageShadowLeftSide.png')
        bg1 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes',"page21Img.png")

        c.drawImage(bg1,0*inch,0,width=8.3*inch,height=11.7*inch,mask='auto')

        # c.drawImage(sha,0*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

        c.setFont("Helvetica-Bold",10)

        tp = Paragraph('<para fontName = STSong-Light fontsize=9>钢丝绳的名称及分类(EN 12385-2 前身 ISO 17893)</para>',stylesN)
        tpt=[[tp]]
        tptab=Table(tpt)
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,3.6*inch,7*inch)

        c.setFillColor('#D0D0D0')
        c.rect(4*inch,6.35*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
        c.setFont("Helvetica-Bold",8)

        c.setFillColor('#000000')
        c.drawCentredString(4.07*inch,6.37*inch,"A")

        tr = Paragraph('<para fontName = STSong-Light fontSize=8 ><b >表示主绳直径</b><br/>单位为毫米)</para>',stylesN)
        trt=[[tr]]
        trtab=Table(trt)
        trtab.wrapOn(c,width,height)
        trtab.drawOn(c,4.25*inch,6.1*inch)


        c.setFillColor('#D8D8D8')
        c.rect(4*inch,5.9*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
        c.setFont("Helvetica-Bold",8)
        c.setFillColor('#3C434B')
        c.drawCentredString(4.07*inch,5.93*inch,"B")
        tr = Paragraph('<para fontName = STSong-Light fontSize=8 ><b >表示绳的结构</b><br/></para>',stylesN)
        trt=[[tr]]
        trtab=Table(trt)
        trtab.wrapOn(c,width,height)
        trtab.drawOn(c,4.25*inch,5.85*inch)

        tr = Paragraph('<para fontName = STSong-Light fontSize=8 ><b >捻的结构和方向</b><br/></para>',stylesN)
        trt=[[tr]]
        trtab=Table(trt)
        trtab.wrapOn(c,width,height)
        trtab.drawOn(c,4.25*inch,5.6*inch)

        c.setFillColor('#DCDCDC')
        c.rect(4*inch,5.65*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
        c.setFont("Helvetica-Bold",8)
        c.setFillColor('#3C434B')
        c.drawCentredString(4.07*inch,5.68*inch,"C")
        data1 = [['-','单股结构',''],
                ['' , '例如:','7 d.h.(1-6)'],
                ['s' , '西鲁型平行股结构',''],
                ['' , '例如:','19S d.h. (1-9-9)'],
                ['W','瓦灵顿型平行股结构',''],
                ['' , '例如:','19W d.h. (1-6-6+6)'],
                ['F' , '填充型平行股结构',''],
                ['' , '例如','21F d.h. (1-5-5F-10)'],
                ['' , '','25F d.h. (1-6-6F-12)'],
                ['WS' , '混合(瓦林吞和西鲁)平行捻结构',''],
                ['' , '例如','31WS d.h. (1-6-6+6-12)'],
        ]

        r = Table(data1,colWidths=[0.75*cm,3.25*cm,2*cm],rowHeights=3.25*mm)
        r.setStyle(TableStyle([
                            ('FONTSIZE',(0,0),(-1,-1),7),
                                    ('LEFTPADDING',(1,0),(-1,-1),7),
                                    ('LEFTPADDING',(2,0),(-1,-1),50),
                                    ('VALIGN',(0,0),(-1,-1),'TOP'),
                                    ('FONTNAME', (0, 0), (1,10), "STSong-Light"),
                               ]))
        r.wrapOn(c,width,height)
        r.drawOn(c,4.15*inch,4.25*inch)

        c.setFillColor('#DCDCDC')
        c.rect(4*inch,3.9*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
        c.setFont("Helvetica-Bold",8)
        c.setFillColor('#3C434B')
        c.drawCentredString(4.07*inch,3.93*inch,"D")

        tr = Paragraph('<para fontName = STSong-Light fontSize=8 ><b >绳芯结构</b><br/></para>',stylesN)
        trt=[[tr]]
        trtab=Table(trt)
        trtab.wrapOn(c,width,height)
        trtab.drawOn(c,4.25*inch,3.85*inch)

        data2 = [['单股纤维绳芯 FC',''],
                ['NFC' , '天然纤维绳芯'],
                ['SFC' , '人造纤维绳芯'],
                ['' , ''],
                ['单股钢芯 WC',''],
                ['WSC' , '钢丝股绳芯'],
                ['IWRC' , '单独的钢丝绳绳芯',''],
                ['' , ''],
                ['平行股钢丝绳'],
                ['PWRC' , '平行股钢丝绳绳芯',''],
        ]

        s = Table(data2,colWidths=17*mm,rowHeights=2.75*mm)
        s.setStyle(TableStyle([
                                    ('FONTSIZE',(0,0),(-1,-1),7),
                                    ('LEFTPADDING',(1,0),(-1,-1),7),
                                    ('LEFTPADDING',(2,0),(-1,-1),20),('VALIGN',(0,0),(-1,-1),'TOP'),
                                    ('FONTNAME', (0, 0), (1,9), "STSong-Light"),
                               ]))
        s.wrapOn(c,width,height)
        s.drawOn(c,4.2*inch,2.85*inch)

        c.setFillColor('#DCDCDC')
        c.rect(4*inch,2.4*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
        c.setFont("Helvetica-Bold",8)
        c.setFillColor('#3C434B')
        c.drawCentredString(4.07*inch,2.43*inch,"E")

        tr = Paragraph('<para fontName = STSong-Light fontSize=8 ><b >钢丝绳抗拉强度 N/mm2</b><br/></para>',stylesN)
        trt=[[tr]]
        trtab=Table(trt)
        trtab.wrapOn(c,width,height)
        trtab.drawOn(c,4.25*inch,2.35*inch)


        c.setFillColor('#DCDCDC')
        c.rect(4*inch,2.1*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
        c.setFont("Helvetica-Bold",8)
        c.setFillColor('#3C434B')
        c.drawCentredString(4.07*inch,2.12*inch,"F")
        tr = Paragraph('<para fontName = STSong-Light fontSize=8 ><b >钢丝表面</b><br/></para>',stylesN)
        trt=[[tr]]
        trtab=Table(trt)
        trtab.wrapOn(c,width,height)
        trtab.drawOn(c,4.25*inch,2.05*inch)

        data3 = [['U','光面'],
                ['B' , '镀锌 (B级)'],
        ]

        u = Table(data3,colWidths=17*mm,rowHeights=3*mm)
        u.setStyle(TableStyle([
                            ('FONTSIZE',(0,0),(-1,-1),7),
                            ('LEFTPADDING',(1,0),(-1,-1),7),
                            ('VALIGN',(0,0),(-1,-1),'TOP'),
                            # ('FONTNAME', (0, 0), (0,1), "STSong-Light"),
                            ('FONTNAME', (0, 0), (1,1), "STSong-Light"),
                               ]))
        u.wrapOn(c,width,height)
        u.drawOn(c,4.25*inch,1.75*inch)

        c.setFillColor('#DCDCDC')
        c.rect(4*inch,1.5*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
        c.setFont("Helvetica-Bold",8)
        c.setFillColor('#3C434B')
        c.drawCentredString(4.07*inch,1.53*inch,"G")
        tr = Paragraph('<para fontName = STSong-Light fontSize=8 ><b >捻向</b><br/></para>',stylesN)
        trt=[[tr]]
        trtab=Table(trt)
        trtab.wrapOn(c,width,height)
        trtab.drawOn(c,4.35*inch,1.43*inch)

        data3 = [['z','右向捻 (股)'],
                ['s','左向捻 (股))'],
                ['Z','右向捻 (绳)'],
                ['S','左向捻 (绳)'],
                ['sZ(RRL)','右向交互捻'],
                ['zS(RLL)','左向交互捻'],
        ]

        u = Table(data3,colWidths=17*mm,rowHeights=3.5*mm)
        u.setStyle(TableStyle([
                            ('FONTSIZE',(0,0),(-1,-1),7),
                                    ('LEFTPADDING',(1,0),(-1,-1),7),
                                     ('VALIGN',(0,0),(-1,-1),'TOP'),
                                    ('FONTNAME', (0, 0), (1,5), "STSong-Light"),
                               ]))
        u.wrapOn(c,width,height)
        u.drawOn(c,4.25*inch,0.6*inch)

        c.setFont("STSong-Light",12)
        c.setFillColor('#ffffff')
        c.drawString(250, 7.65*inch, "钢丝绳的名称与分类")

        c.setFont("STSong-Light",10)
        c.setFillColor('#000000')
        c.drawString(30, 7*inch, "例")

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1










        for accessorie in accessoriesCat:
            accessObjects = AccessoriesSection.objects.filter(accessories=accessorie,lang = "zh")
            # printaccessObjects,'accessObjects'

            for access in accessObjects:
                # printaccess.productName, "product name"
                prodfield = AccessoriesField.objects.filter(productBaseName = access.basicProductName)
                # printprodfield, "product fields "
                itemNumbers = AccessoriesData.objects.filter(productBaseName = access.basicProductName)
                # printitemNumbers, "item numbers"
                itemNumberValues = AccessoriesValueMap.objects.filter(productBaseName = access.basicProductName)
                # printitemNumberValues, "itemNumberValues"
                # addAccessoriePage(c,access, prodfield,itemNumbers, itemNumberValues, stylesN)
                # width,height = A4

                if access.image2:
                    productImage = access.image2.path
                else:
                    productImage = os.path.join(globalSettings.BASE_DIR , 'static_shared/images',"stars.jpeg")


                if pageCount%2 == 0:
                    if access.catalogBG1:
                        background = access.catalogBG1.path
                    else:
                        background = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes',"page22a.jpg")
                    c.drawImage(background,0,0,width=width, height=height, mask = 'auto')
                    #
                    # name = Paragraph('<para fontName = STSong-Light fontSize=30>%s</para>'%(access.productName), stylesN)
                    # nd =[[name]]
                    # w = pdfmetrics.stringWidth(access.productName, "FrutigerB", 30)
                    # # printw, "text width "
                    # ndt = Table(nd)
                    # w1,h1 = ndt.wrapOn(c, width,height)
                    # width2 = width - w -50
                    # ndt.drawOn(c, width2,570)



                else:
                    if access.catalogBG2:
                        background = access.catalogBG2.path
                    else:
                        background = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes',"page22a.jpg")
                    c.drawImage(background,0,0,width=width, height=height, mask = 'auto')
                    # name = Paragraph('<para fontName = STSong-Light fontSize=30>%s</para>'%(access.productName), stylesN)
                    # nd =[[name]]
                    # w = pdfmetrics.stringWidth(access.productName, "FrutigerB", 30)
                    # # printw, "text width "
                    # ndt = Table(nd)
                    # w1,h1 = ndt.wrapOn(c, width,height)
                    # width2 = 50
                    # ndt.drawOn(c, width2,570)



                accessoriesPK = access.accessories
                # printaccessoriesPK.name, "accessory name"

                name = Paragraph('<para fontName = STSong-Light fontSize=25>%s</para>'%(access.productName), stylesN)
                nd =[[name]]
                w = pdfmetrics.stringWidth(access.productName, "FrutigerB", 30)
                # printw, "text width "
                ndt = Table(nd)
                w1,h1 = ndt.wrapOn(c, width,height)
                width2 = 50
                ndt.drawOn(c, width2,570)
                name = Paragraph('<para  fontName = STSong-Light fontSize=15>%s</para>'%((access.categoryName).upper()), stylesN)
                des =[[name]]
                dest = Table(des,colWidths=8*cm)
                w2, h3 = dest.wrapOn(c, width,height)
                # # printw2,w1, "tag width"
                w2 = pdfmetrics.stringWidth((access.categoryName).upper(), "STSong-Light", 15)
                print w, "tagline width"
                width2 = width - w2 - 20
                dest.drawOn(c, width2,560)



                # name = Paragraph('<para  fontName = STSong-Light fontSize=15>%s</para>'%((access.categoryName).upper()), stylesN)
                # des =[[name]]
                # dest = Table(des,colWidths=8*cm)
                # w2, h3 = dest.wrapOn(c, width,height)
                # # # printw2,w1, "tag width"
                # # width2 = width2 + w +10
                # # # printwidth2, "tagline width"
                # dest.drawOn(c, 200,555)


                height2 = 550

                img = utils.ImageReader(productImage)
                iw, ih = img.getSize()
                height3 = height2 - ih
                c.drawImage(productImage,50,height3,width=150,preserveAspectRatio=True,mask='auto')



                name = Paragraph('<para fontName = STSong-Light fontSize=12>%s</para>'%(access.title1), stylesN)
                nd =[[name]]
                ndt = Table(nd,colWidths=10*cm)
                w1,h1 = ndt.wrapOn(c, width,height)
                height2 = height2-h1 -20
                ndt.drawOn(c, 200,height2)

                name = Paragraph('<para fontName = STSong-Light fontSize=9>%s</para>'%(access.desc1), stylesN)
                des =[[name]]
                dest = Table(des,colWidths=10*cm)
                w2, h2 = dest.wrapOn(c, width,height)
                # printw2, h2, "height of para1"
                height2 = height2 -h2
                dest.drawOn(c, 200,height2)

                name = Paragraph('<para fontName = STSong-Light fontSize=12>%s</para>'%(access.title2), stylesN)
                nd =[[name]]
                ndt = Table(nd,colWidths=10*cm)
                w3,h3 = ndt.wrapOn(c, width,height)
                height2 = height2 -h3-30
                ndt.drawOn(c, 200,height2)


                name = Paragraph('<para fontName = STSong-Light fontSize=9>%s</para>'%(access.desc2), stylesN)
                des =[[name]]
                dest = Table(des,colWidths=10*cm)
                w4, h4 = dest.wrapOn(c, width,height)
                height2 = height2 -h4
                dest.drawOn(c, 200,height2)


                data = []
                # data2 = []
                dataHeading = ['Item Number']
                dataHeading2 = ['']
                list1 = []
                list2 = []
                for j in prodfield:
                    # printprodfield
                    if j.inPdf ==True:

                        # printj.name,'kkkkkkkkkkkkk'
                        try:
                            name1, name2 = j.name.split('(')
                            # printname2[:-1]
                            name2 = ''+name2[:-1]
                            # printname2
                        except:
                            name1 = j.name
                            name2 = ''

                        # printname1, ' ' , name2

                        list1.append(name1)
                        list2.append(name2)
                for a in list1:
                    dataHeading.append(a)
                for b in list2:
                    dataHeading2.append(b)


                # printdataHeading, dataHeading2, "fields  "


                for i in itemNumbers:
                    appendlist = [i.itemNumber]
                    for j in prodfield:
                        prodQty = itemNumberValues.filter( field = j.pk,product = i.pk)
                        for k in prodQty:
                            if j.inPdf ==True:
                                if j.type=='Char':
                                    appendlist.append(k.char)
                                if j.type=='float':
                                    appendlist.append(k.fValue)
                                if j.type=='Integer':
                                    appendlist.append(k.iValue)
                                if j.type=='Boolean':
                                    appendlist.append(k.bool)
                    data.append(appendlist)

                # printlen(data), "data length"
                # printdata , "item number data"


                data.insert(0,dataHeading)
                # printdata,len(data), "final data"

                # # printheight2, "height2"
                height2 = height2-40
                leftHeight = height2-120
                numberRows = int(leftHeight/20)
                # printheight2, leftHeight, numberRows, "number of rows"

                if len(data)<= numberRows:
                        t5 = Table(data,rowHeights=[20]*len(data))
                        t5.setStyle(TableStyle([
                                             ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                                             ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                                             ('FONTSIZE', (0, 0), (-1, -1), 7),
                                             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                             ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                                             ]))
                        w5, h5 = t5.wrapOn(c, width, height)
                        height2 = height2 - h5
                        t5.drawOn(c, 200, height2)


                        gm934 = Paragraph('<para></para>',stylesN)
                        gmn934 = Paragraph('<para></para>',stylesN)

                        data =  [[gm934,gmn934]]

                        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
                        t.setStyle(TableStyle([
                                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                                             ]))
                        t.wrapOn(c,width, height)


                        c.setFillColor(colors.black)
                        c.setFont("Helvetica-Bold",10)
                        if pageCount%2==0:
                            t.drawOn(c, -3*inch,0.2*inch)
                            c.drawString(20, 0.15*inch, str(pageCount))
                        else:
                            t.drawOn(c, width-35,0.2*inch)
                            c.drawString(width-30, 0.15*inch, str(pageCount))

                        c.showPage()
                        pageCount +=1
                else:
                    # print"in else"
                    data1 = data[:numberRows-1]
                    # printdata1, "data1"
                    data2 = data[numberRows:-1]
                    # printdata2, "data2"
                    t5 = Table(data1,rowHeights=[20]*len(data1))
                    t5.setStyle(TableStyle([
                                         ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                                         ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                                         ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                                         ('FONTSIZE', (0, 0), (-1, -1), 7),
                                         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                         ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                                         ]))
                    w5, h5 = t5.wrapOn(c, width, height)
                    height2 = height2 - h5
                    t5.drawOn(c, 200, height2)

                    gm934 = Paragraph('<para></para>',stylesN)
                    gmn934 = Paragraph('<para></para>',stylesN)

                    data =  [[gm934,gmn934]]

                    t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
                    t.setStyle(TableStyle([
                                        ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                                         ]))
                    t.wrapOn(c,width, height)


                    c.setFillColor(colors.black)
                    c.setFont("Helvetica-Bold",10)
                    if pageCount%2==0:
                        t.drawOn(c, -3*inch,0.2*inch)
                        c.drawString(20, 0.15*inch, str(pageCount))
                    else:
                        t.drawOn(c, width-35,0.2*inch)
                        c.drawString(width-30, 0.15*inch, str(pageCount))

                    c.showPage()
                    pageCount +=1

                    maxNumberItems = 20

                    index = float(len(data2))/maxNumberItems
                    # printindex
                    index = int(math.ceil(index))
                    # printindex, range(index),"index ...."
                    for i in range(index):
                        if i == index-1:
                            data1 = data2[maxNumberItems*i:-1]
                            data1.insert(0,dataHeading)
                            # printlen(data1), i , "if loop"
                        else:
                            data1 = data2[maxNumberItems*i:maxNumberItems*(i+1)-1]
                            data1.insert(0,dataHeading)
                            # printlen(data1), i, "else loop"
                        # printdata1, "datapass "
                        pageCount = addAccessoriePageExtra(c, data1, access,stylesN,productImage,pageCount,lang)


    elif lang == 'de':

        for template in templatesTractionRopes2:

            prodfield = ProductField.objects.filter(template = template.pk)
            # printprodfield
            prod = Product.objects.filter(template = template.pk)
            # printprod



            if pageCount%2 == 0:
                if template.catalogBG1:
                    background = template.catalogBG1.path
                else:
                    background = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes',"page13.jpg")

                c.drawImage(background,0,0,width=width, height=height, mask = 'auto')
                name = Paragraph('<para fontName = FrutigerB fontSize=30>%s</para>'%(template.name), stylesN)
                nd =[[name]]
                w = pdfmetrics.stringWidth(template.name, "FrutigerB", 30)
                # printw, "text width "
                ndt = Table(nd)
                w1,h1 = ndt.wrapOn(c, width,height)
                width2 = width - w -50
                ndt.drawOn(c, width2,570)



            else:
                if template.catalogBG2:
                    background = template.catalogBG2.path
                else:
                    background = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes',"page12.jpg")
                c.drawImage(background,0,0,width=width, height=height, mask = 'auto')
                name = Paragraph('<para fontName = FrutigerB fontSize=30>%s</para>'%(template.name), stylesN)
                nd =[[name]]
                w = pdfmetrics.stringWidth(template.name, "FrutigerB", 30)
                # printw, "text width "
                ndt = Table(nd)
                w1,h1 = ndt.wrapOn(c, width,height)
                width2 = 50
                ndt.drawOn(c, width2,570)


            test =  template.parent_name
            test = test.split("-")
            text = ''
            for i in test:
                text += i.upper() + " "
            name = Paragraph('<para fontName = FrutigerB fontSize=15>%s</para>'%(text), styles['Normal'])
            nd =[[name]]
            w = pdfmetrics.stringWidth(template.parent_name, "FrutigerB", 10)
            # printw, "text width "
            ndt = Table(nd)
            w1,h1 = ndt.wrapOn(c, width,height)

            ndt.drawOn(c, 200,548)

            c.drawImage(template.defaultImage.path,50,400,width=1.4*inch,height=1.4*inch, mask='auto')

            height2 = height - 330
            # printtemplate.disclaimer_en, 'desclaimer english '
            height2 = htmlRMLCanvvas(template.rteData1_otl,c,4.5*inch,200,height2,stylesN,colors.black,lang)


            height2 = height2 - 50
            height3 = height2 + 15
            height4 = height2
            height5 = height2 - 30
            _color = rangeColors(template.color)
            c.setFillColor(_color.hex)
            c.setStrokeColor(colors.white)
            c.rect(3.3*inch,height2,0.6*inch,0.6*inch, fill=1)
            c.setFont("Helvetica-Bold", 7)
            c.setFillColor(colors.black)
            k = json.loads(template.keyword1)
            k11 =[[k]]
            r11 = Table(k11,colWidths=3.6*inch,rowHeights=4*mm)
            c.setFont("Helvetica", 5)

            para101 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%(k["value1"]), styles['Normal'])
            desc101 = [[para101]]
            r101 = Table(desc101,colWidths=0.6*inch,rowHeights=1*mm)
            w, h = r101.wrapOn(c, width,height)
            r101.drawOn(c, 3.3*inch, height3)

            para102 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%("N/mm2"), styles['Normal'])
            desc102 = [[para102]]
            r102 = Table(desc102,colWidths=0.6*inch,rowHeights=1*mm)
            r102.wrapOn(c, width,height)
            r102.drawOn(c, 3.3*inch, height4)

            para103 = Paragraph('<para align="center" fontName = FrutigerR fontSize=7 >%s</para>'%("E-Module"), styles['Normal'])
            desc103 = [[para103]]
            r103 = Table(desc103,colWidths=0.6*inch,rowHeights=1*mm)
            r103.wrapOn(c, width,height)
            r103.drawOn(c, 3.3*inch, height5)


            _color = rangeColors(template.color,luminance=.5)
            c.setFillColor(_color.hex)
            c.rect(4.3*inch,height2,0.6*inch,0.6*inch, fill=1)
            c.setFont("Helvetica-Bold", 7)
            c.setFillColor(colors.black)
            k1 = json.loads(template.keyword2)

            k12 =[[k1]]

            r12 = Table(k12,colWidths=5*inch,rowHeights=10*mm)

            para201 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%(k1["value1"]), styles['Normal'])
            desc201 = [[para201]]
            r201 = Table(desc201,colWidths=0.6*inch)
            w,h = r201.wrapOn(c, width,height)

            r201.drawOn(c, 4.3*inch, height3)

            para202 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%("%"), styles['Normal'])
            desc202 = [[para202]]
            r202 = Table(desc202,colWidths=0.6*inch,rowHeights=1*mm)
            r202.wrapOn(c, width,height)
            r202.drawOn(c, 4.3*inch, height4)

            para203 = Paragraph('<para align="center" fontName = FrutigerR fontSize=7 >%s</para>'%("Elastic<br/>Elongation"), styles['Normal'])
            desc203 = [[para203]]
            r203 = Table(desc203,colWidths=0.65*inch,rowHeights=1*mm)
            r203.wrapOn(c, width,height)
            r203.drawOn(c, 4.3*inch, height5 )


            _color = rangeColors(template.color,luminance=.7)
            c.setFillColor(_color.hex)
            c.setStrokeColor(colors.white)

            c.rect(5.3*inch,height2,0.6*inch,0.6*inch, fill=1)
            c.setFont("Helvetica-Bold", 7)
            c.setFillColor(colors.black)
            k2 = json.loads(template.keyword3)

            k13 = [[k2]]

            r13 = Table(k13,colWidths=5*inch,rowHeights=10*mm)

            para301 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%(k2["value1"]), styles['Normal'])
            desc301 = [[para301]]
            r301 = Table(desc301,colWidths=0.6*inch,rowHeights=1*mm)
            r301.wrapOn(c, width,height)
            r301.drawOn(c, 5.3*inch, height3)

            para302 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%("%"), styles['Normal'])
            desc302 = [[para302]]
            r302 = Table(desc302,colWidths=0.6*inch,rowHeights=1*mm)
            r302.wrapOn(c, width,height)
            r302.drawOn(c, 5.3*inch, height4)

            para303 = Paragraph('<para align="center" fontName = FrutigerR fontSize=7 >%s</para>'%("Permanent<br/>Elongation"), styles['Normal'])
            desc303 = [[para303]]
            r303 = Table(desc303,colWidths=0.7*inch,rowHeights=1*mm)
            r303.wrapOn(c, width,height)
            r303.drawOn(c, 5.3*inch, height5)


            _color = rangeColors(template.color,luminance=.9)
            c.setFillColor(_color.hex)
            c.setStrokeColor(colors.white)
            c.rect(6.3*inch,height2,0.6*inch,0.6*inch, fill=1)
            c.setFont("Helvetica-Bold", 7)
            c.setFillColor(colors.black)
            k3 = json.loads(template.keyword4)
            k14 = [[k3]]
            r14 = Table(k14,colWidths=5*inch,rowHeights=10*mm)

            para401 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%(k3["value1"]), styles['Normal'])
            desc401 = [[para401]]
            r401 = Table(desc401,colWidths=0.6*inch,rowHeights=1*mm)
            r401.wrapOn(c, width,height)
            r401.drawOn(c, 6.3*inch, height3)

            para402 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%("m"), styles['Normal'])
            desc402 = [[para402]]
            r402 = Table(desc402,colWidths=0.6*inch,rowHeights=1*mm)
            r402.wrapOn(c, width,height)
            r402.drawOn(c, 6.3*inch, height4)

            para403 = Paragraph('<para align="center" fontName = FrutigerR fontSize=7 >%s</para>'%("Lifting<br/>Height"), styles['Normal'])
            desc403 = [[para403]]
            r403 = Table(desc403,colWidths=0.6*inch,rowHeights=1*mm)
            r403.wrapOn(c, width,height)
            r403.drawOn(c, 6.3*inch, height5)


            height2 = height5

            data = []
            # data2 = []
            dataHeading = ['Item Number']
            dataHeading2 = ['']
            list1 = []
            list2 = []
            for j in prodfield:
                # printprodfield
                if j.inPdf ==True:

                    # printj.name,'kkkkkkkkkkkkk'
                    try:
                        name1, name2 = j.name.split('(')
                        # printname2[:-1]
                        name2 = ''+name2[:-1]
                        # printname2
                    except:
                        name1 = j.name
                        name2 = ''

                    # printname1, ' ' , name2

                    list1.append(name1)
                    list2.append(name2)
            for a in list1:
                dataHeading.append(a)
            for b in list2:
                dataHeading2.append(b)



            for i in prod:
                appendlist = [i.itemNumber]
                for j in prodfield:
                    prodQty = ProductValueMap.objects.filter( field = j.pk,product = i.pk)
                    for k in prodQty:
                        if j.inPdf ==True:
                            if j.type=='Char':
                                appendlist.append(k.char)
                            if j.type=='float':
                                appendlist.append(k.fValue)
                            if j.type=='Integer':
                                appendlist.append(k.iValue)
                            if j.type=='Boolean':
                                appendlist.append(k.bool)
                data.append(appendlist)

            height2 = height2-40
            leftHeight = height2-100
            numberRows = int(leftHeight/20)
            # printheight2, leftHeight, numberRows, "number of rows"

            data.insert(0,dataHeading)
            data.insert(1,dataHeading2)

            if len(data)<= numberRows:
                    t5 = Table(data,rowHeights=[20]*len(data))
                    t5.setStyle(TableStyle([
                                         ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                                         ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                                         ('FONTSIZE', (0, 0), (-1, -1), 7),
                                         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                         ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                                         ]))
                    w5, h5 = t5.wrapOn(c, width, height)
                    height2 = height2 - h5
                    t5.drawOn(c, 200, height2)



                    para2 = Paragraph('<para fontName = Helvetica fontSize=6 >%s</para>'%(template.disclaimer_en), styles['Normal'])
                    tab = [[para2]]
                    r = Table(tab,colWidths=3.25*inch)
                    w,h1 = r.wrapOn(c, width,height)
                    height2 = height2 - h1
                    r.drawOn(c, 200, height2)

                    gm934 = Paragraph('<para></para>',stylesN)
                    gmn934 = Paragraph('<para></para>',stylesN)

                    data =  [[gm934,gmn934]]

                    t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
                    t.setStyle(TableStyle([
                                        ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                                         ]))
                    t.wrapOn(c,width, height)


                    c.setFillColor(colors.black)
                    c.setFont("Helvetica-Bold",10)
                    if pageCount%2==0:
                        t.drawOn(c, -3*inch,0.2*inch)
                        c.drawString(20, 0.15*inch, str(pageCount))
                    else:
                        t.drawOn(c, width-35,0.2*inch)
                        c.drawString(width-30, 0.15*inch, str(pageCount))

                    c.showPage()
                    pageCount +=1
            else:

                data1 = data[:numberRows-1]

                data2 = data[numberRows:-1]

                t5 = Table(data1,rowHeights=[20]*len(data1))
                t5.setStyle(TableStyle([
                                     ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                                     ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                                     ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                                     ('FONTSIZE', (0, 0), (-1, -1), 7),
                                     ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                     ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                                     ]))
                w5, h5 = t5.wrapOn(c, width, height)
                height2 = height2 - h5
                t5.drawOn(c, 200, height2)



                para2 = Paragraph('<para fontName = Helvetica fontSize=6 >%s</para>'%(template.disclaimer_en), styles['Normal'])
                tab = [[para2]]
                r = Table(tab,colWidths=3.25*inch)
                w,h1 = r.wrapOn(c, width,height)
                height2 = height2 - h1
                r.drawOn(c, 200, height2)

                gm934 = Paragraph('<para></para>',stylesN)
                gmn934 = Paragraph('<para></para>',stylesN)

                data =  [[gm934,gmn934]]

                t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
                t.setStyle(TableStyle([
                                    ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                                     ]))
                t.wrapOn(c,width, height)


                c.setFillColor(colors.black)
                c.setFont("Helvetica-Bold",10)
                if pageCount%2==0:
                    t.drawOn(c, -3*inch,0.2*inch)
                    c.drawString(20, 0.15*inch, str(pageCount))
                else:
                    t.drawOn(c, width-35,0.2*inch)
                    c.drawString(width-30, 0.15*inch, str(pageCount))

                c.showPage()
                pageCount +=1
                maxNumberItems = 15

                index = float(len(data2))/maxNumberItems

                index = int(math.ceil(index))

                for i in range(index):
                    if i == index-1:
                        data1 = data2[maxNumberItems*i:-1]
                        data1.insert(0,dataHeading)
                        data1.insert(1,dataHeading2)

                    else:
                        data1 = data2[maxNumberItems*i:maxNumberItems*(i+1)-1]
                        data1.insert(0,dataHeading)
                        data1.insert(1,dataHeading2)

                    pageCount = addElevatorPage(c, data1,template,stylesN,pageCount,lang)


        # sha1 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes','PageShadowRightSide.png')
        # sha = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes','PageShadowLeftSide.png')
        bg1 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes',"page21Img.png")

        c.drawImage(bg1,0*inch,0,width=8.3*inch,height=11.7*inch,mask='auto')

        # c.drawImage(sha,0*inch,0*inch,width=0.5*inch,height=12.5*inch,mask='auto')

        c.setFont("Helvetica-Bold",10)

        tp = Paragraph('<para fontsize=9>Bezeichnungen und Klassifizierungen von Drahtseilen [EN 12385-2]</para>',stylesN)
        tpt=[[tp]]
        tptab=Table(tpt)
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,3.6*inch,7*inch)

        c.setFillColor('#D0D0D0')
        c.rect(4*inch,6.35*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
        c.setFont("Helvetica-Bold",8)

        c.setFillColor('#000000')
        c.drawCentredString(4.07*inch,6.37*inch,"A")

        tr = Paragraph('<para fontSize=8 ><b >Seilnenndurchmesser in mm</b><br/>(siehe jeweils in zugehöriger Tabelle)</para>',stylesN)
        trt=[[tr]]
        trtab=Table(trt)
        trtab.wrapOn(c,width,height)
        trtab.drawOn(c,4.25*inch,6.1*inch)


        c.setFillColor('#D8D8D8')
        c.rect(4*inch,5.9*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
        c.setFont("Helvetica-Bold",8)
        c.setFillColor('#3C434B')
        c.drawCentredString(4.07*inch,5.93*inch,"B")
        tr = Paragraph('<para fontSize=8 ><b >Seilkonstruktion</b><br/></para>',stylesN)
        trt=[[tr]]
        trtab=Table(trt)
        trtab.wrapOn(c,width,height)
        trtab.drawOn(c,4.25*inch,5.85*inch)

        tr = Paragraph('<para fontSize=8 ><b >Konstruktionsart der Verseilung</b><br/></para>',stylesN)
        trt=[[tr]]
        trtab=Table(trt)
        trtab.wrapOn(c,width,height)
        trtab.drawOn(c,4.25*inch,5.6*inch)

        c.setFillColor('#DCDCDC')
        c.rect(4*inch,5.65*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
        c.setFont("Helvetica-Bold",8)
        c.setFillColor('#3C434B')
        c.drawCentredString(4.07*inch,5.68*inch,"C")
        data1 = [['-','Einlagige Verseilung',''],
                ['' , 'Bsp. für Litzenkonstruktion:','7 d.h.(1-6)'],
                ['s' , 'Seale Parallelverseilung',''],
                ['' , 'Bsp. für Litzenkonstruktion:','19S d.h. (1-9-9)'],
                ['W','Warrington Parallelverseilung',''],
                ['' , 'Bsp. für Litzenkonstruktion:','19W d.h. (1-6-6+6)'],
                ['F' , 'Filler Parrallelverseilung',''],
                ['' , 'sp. für Litzenkonstruktion:','21F d.h. (1-5-5F-10)'],
                ['' , '','25F d.h. (1-6-6F-12)'],
                ['WS' , 'Kombinierte (Warrington Seale) Parallelverseilung',''],
                ['' , 'Bsp. für Litzenkonstruktion:','31WS d.h. (1-6-6+6-12)'],
        ]

        r = Table(data1,colWidths=[0.75*cm,3.25*cm,2*cm],rowHeights=3.25*mm)
        r.setStyle(TableStyle([
                            ('FONTSIZE',(0,0),(-1,-1),7),
                                    ('LEFTPADDING',(1,0),(-1,-1),7),
                                     ('LEFTPADDING',(2,0),(-1,-1),50),
                                     ('VALIGN',(0,0),(-1,-1),'TOP')
                               ]))
        r.wrapOn(c,width,height)
        r.drawOn(c,4.15*inch,4.25*inch)

        c.setFillColor('#DCDCDC')
        c.rect(4*inch,3.9*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
        c.setFont("Helvetica-Bold",8)
        c.setFillColor('#3C434B')
        c.drawCentredString(4.07*inch,3.93*inch,"D")

        tr = Paragraph('<para fontSize=8 ><b >Konstruktion der Einlage</b><br/></para>',stylesN)
        trt=[[tr]]
        trtab=Table(trt)
        trtab.wrapOn(c,width,height)
        trtab.drawOn(c,4.25*inch,3.85*inch)

        data2 = [['Einlagiges Seil mit Fasereinlage FC',''],
                ['NFC' , 'Naturfasereinlage'],
                ['SFC' , 'Synthetikfasereinlage'],
                ['' , ''],
                ['Einlagiges Seil mit Stahleinlage WC',''],
                ['WSC' , 'Drahtlitzeneinlage'],
                ['IWRC' , 'Drahtseileinlage, gesondert verseilt',''],
                ['' , ''],
                ['Seil mit Parallelverseilung'],
                ['PWRC' , 'Drahtseilkern in Parallelverseilung',''],
        ]

        s = Table(data2,colWidths=17*mm,rowHeights=2.75*mm)
        s.setStyle(TableStyle([
                                    ('FONTSIZE',(0,0),(-1,-1),7),
                                    ('LEFTPADDING',(1,0),(-1,-1),7),
                                    ('LEFTPADDING',(2,0),(-1,-1),20),('VALIGN',(0,0),(-1,-1),'TOP')
                               ]))
        s.wrapOn(c,width,height)
        s.drawOn(c,4.2*inch,2.85*inch)

        c.setFillColor('#DCDCDC')
        c.rect(4*inch,2.4*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
        c.setFont("Helvetica-Bold",8)
        c.setFillColor('#3C434B')
        c.drawCentredString(4.07*inch,2.43*inch,"E")

        tr = Paragraph('<para fontSize=8 ><b >Nennfestigkeit der Drähte in N/mm 2</b><br/></para>',stylesN)
        trt=[[tr]]
        trtab=Table(trt)
        trtab.wrapOn(c,width,height)
        trtab.drawOn(c,4.25*inch,2.35*inch)


        c.setFillColor('#DCDCDC')
        c.rect(4*inch,2.1*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
        c.setFont("Helvetica-Bold",8)
        c.setFillColor('#3C434B')
        c.drawCentredString(4.07*inch,2.12*inch,"F")
        tr = Paragraph('<para fontSize=8 ><b >Oberflächenausführung der Drähte</b><br/></para>',stylesN)
        trt=[[tr]]
        trtab=Table(trt)
        trtab.wrapOn(c,width,height)
        trtab.drawOn(c,4.25*inch,2.05*inch)

        data3 = [['U','blank'],
                ['B' , 'verzinkt gezogen'],
        ]

        u = Table(data3,colWidths=17*mm,rowHeights=3*mm)
        u.setStyle(TableStyle([
                            ('FONTSIZE',(0,0),(-1,-1),7),
                            ('LEFTPADDING',(1,0),(-1,-1),7),
                            ('VALIGN',(0,0),(-1,-1),'TOP')
                               ]))
        u.wrapOn(c,width,height)
        u.drawOn(c,4.25*inch,1.75*inch)

        c.setFillColor('#DCDCDC')
        c.rect(4*inch,1.5*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
        c.setFont("Helvetica-Bold",8)
        c.setFillColor('#3C434B')
        c.drawCentredString(4.07*inch,1.53*inch,"G")
        tr = Paragraph('<para fontSize=8 ><b >Schlagart und Schlagrichtung</b><br/></para>',stylesN)
        trt=[[tr]]
        trtab=Table(trt)
        trtab.wrapOn(c,width,height)
        trtab.drawOn(c,4.35*inch,1.43*inch)

        data3 = [['z','rechtsgängig (Litze)'],
                ['s','linksgängig (Litze)'],
                ['Z','rechtsgängig (Seil)'],
                ['S','linksgängig (Seil)'],
                ['sZ(RRL)','Kreuzschlag rechtsgängig'],
                ['zS(RLL)','Kreuzschlag linksgängig'],
        ]

        u = Table(data3,colWidths=17*mm,rowHeights=3.5*mm)
        u.setStyle(TableStyle([
                            ('FONTSIZE',(0,0),(-1,-1),7),
                                    ('LEFTPADDING',(1,0),(-1,-1),7),
                                     ('VALIGN',(0,0),(-1,-1),'TOP')
                               ]))
        u.wrapOn(c,width,height)
        u.drawOn(c,4.25*inch,0.6*inch)

        c.setFont("Helvetica",12)
        c.setFillColor('#ffffff')
        c.drawString(250, 7.65*inch, "KURZBEZEICHNUNGEN")

        c.setFont("Helvetica",10)
        c.setFillColor('#000000')
        c.drawString(30, 7*inch, "Beispiel")

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        for accessorie in accessoriesCat:
            accessObjects = AccessoriesSection.objects.filter(accessories=accessorie,lang = "de")
            # printaccessObjects,'accessObjects'

            for access in accessObjects:
                # printaccess.productName, "product name"
                prodfield = AccessoriesField.objects.filter(productBaseName = access.basicProductName)
                # printprodfield, "product fields "
                itemNumbers = AccessoriesData.objects.filter(productBaseName = access.basicProductName)
                # printitemNumbers, "item numbers"
                itemNumberValues = AccessoriesValueMap.objects.filter(productBaseName = access.basicProductName)
                # printitemNumberValues, "itemNumberValues"
                # addAccessoriePage(c,access, prodfield,itemNumbers, itemNumberValues, stylesN)
                # width,height = A4

                if access.image2:
                    productImage = access.image2.path
                else:
                    productImage = os.path.join(globalSettings.BASE_DIR , 'static_shared/images',"stars.jpeg")


                if pageCount%2 == 0:
                    if access.catalogBG1:
                        background = access.catalogBG1.path
                    else:
                        background = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes',"page22a.jpg")
                    c.drawImage(background,0,0,width=width, height=height, mask = 'auto')

                    # name = Paragraph('<para fontName = FrutigerB fontSize=30>%s</para>'%(access.productName), stylesN)
                    # nd =[[name]]
                    # w = pdfmetrics.stringWidth(access.productName, "FrutigerB", 30)
                    # # printw, "text width "
                    # ndt = Table(nd)
                    # w1,h1 = ndt.wrapOn(c, width,height)
                    # width2 = width - w -50
                    # ndt.drawOn(c, width2,570)



                else:
                    if access.catalogBG2:
                        background = access.catalogBG2.path
                    else:
                        background = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/elevatorRopes',"page22a.jpg")
                    c.drawImage(background,0,0,width=width, height=height, mask = 'auto')
                    # name = Paragraph('<para fontName = FrutigerB fontSize=30>%s</para>'%(access.productName), stylesN)
                    # nd =[[name]]
                    # w = pdfmetrics.stringWidth(access.productName, "FrutigerB", 30)
                    # # printw, "text width "
                    # ndt = Table(nd)
                    # w1,h1 = ndt.wrapOn(c, width,height)
                    # width2 = 50
                    # ndt.drawOn(c, width2,570)



                accessoriesPK = access.accessories
                # printaccessoriesPK.name, "accessory name"


                name = Paragraph('<para fontName = FrutigerB fontSize=25>%s</para>'%(access.productName), stylesN)
                nd =[[name]]
                w = pdfmetrics.stringWidth(access.productName, "FrutigerB", 30)
                # printw, "text width "
                ndt = Table(nd)
                w1,h1 = ndt.wrapOn(c, width,height)
                width2 = 50
                ndt.drawOn(c, width2,570)
                name = Paragraph('<para  fontName = FrutigerB fontSize=15>%s</para>'%((access.categoryName).upper()), stylesN)
                des =[[name]]
                dest = Table(des,colWidths=8*cm)
                w2, h3 = dest.wrapOn(c, width,height)
                # # printw2,w1, "tag width"
                w2 = pdfmetrics.stringWidth((access.categoryName).upper(), "FrutigerB", 15)
                print w, "tagline width"
                width2 = width - w2 - 20
                dest.drawOn(c, width2,560)

                # name = Paragraph('<para  fontName = FrutigerB fontSize=15>%s</para>'%((access.categoryName).upper()), stylesN)
                # des =[[name]]
                # dest = Table(des,colWidths=8*cm)
                # w2, h3 = dest.wrapOn(c, width,height)
                # # # printw2,w1, "tag width"
                # # width2 = width2 + w +10
                # # # printwidth2, "tagline width"
                # dest.drawOn(c, 200,555)


                height2 = 550

                img = utils.ImageReader(productImage)
                iw, ih = img.getSize()
                height3 = height2 - ih
                c.drawImage(productImage,50,height3,width=150,preserveAspectRatio=True,mask='auto')



                name = Paragraph('<para fontName = FrutigerB fontSize=15>%s</para>'%(access.title1), stylesN)
                nd =[[name]]
                ndt = Table(nd,colWidths=10*cm)
                w1,h1 = ndt.wrapOn(c, width,height)
                height2 = height2-h1 -20
                ndt.drawOn(c, 200,height2)

                name = Paragraph('<para fontName = FrutigerR fontSize=12>%s</para>'%(access.desc1), stylesN)
                des =[[name]]
                dest = Table(des,colWidths=10*cm)
                w2, h2 = dest.wrapOn(c, width,height)
                # printw2, h2, "height of para1"
                height2 = height2 -h2
                dest.drawOn(c, 200,height2)

                name = Paragraph('<para fontName = FrutigerB fontSize=15>%s</para>'%(access.title2), stylesN)
                nd =[[name]]
                ndt = Table(nd,colWidths=10*cm)
                w3,h3 = ndt.wrapOn(c, width,height)
                height2 = height2 -h3-30
                ndt.drawOn(c, 200,height2)


                name = Paragraph('<para fontName = FrutigerR fontSize=12>%s</para>'%(access.desc2), stylesN)
                des =[[name]]
                dest = Table(des,colWidths=10*cm)
                w4, h4 = dest.wrapOn(c, width,height)
                height2 = height2 -h4
                dest.drawOn(c, 200,height2)




                data = []
                # data2 = []
                dataHeading = ['Item Number']
                dataHeading2 = ['']
                list1 = []
                list2 = []
                for j in prodfield:
                    # printprodfield
                    if j.inPdf ==True:

                        # printj.name,'kkkkkkkkkkkkk'
                        try:
                            name1, name2 = j.name.split('(')
                            # printname2[:-1]
                            name2 = ''+name2[:-1]
                            # printname2
                        except:
                            name1 = j.name
                            name2 = ''

                        # printname1, ' ' , name2

                        list1.append(name1)
                        list2.append(name2)
                for a in list1:
                    dataHeading.append(a)
                for b in list2:
                    dataHeading2.append(b)


                # printdataHeading, dataHeading2, "fields  "


                for i in itemNumbers:
                    appendlist = [i.itemNumber]
                    for j in prodfield:
                        prodQty = itemNumberValues.filter( field = j.pk,product = i.pk)
                        for k in prodQty:
                            if j.inPdf ==True:
                                if j.type=='Char':
                                    appendlist.append(k.char)
                                if j.type=='float':
                                    appendlist.append(k.fValue)
                                if j.type=='Integer':
                                    appendlist.append(k.iValue)
                                if j.type=='Boolean':
                                    appendlist.append(k.bool)
                    data.append(appendlist)

                # printlen(data), "data length"
                # printdata , "item number data"


                data.insert(0,dataHeading)
                # printdata,len(data), "final data"

                # # printheight2, "height2"
                height2 = height2-40
                leftHeight = height2-120
                numberRows = int(leftHeight/20)
                # printheight2, leftHeight, numberRows, "number of rows"

                if len(data)<= numberRows:
                        t5 = Table(data,rowHeights=[20]*len(data))
                        t5.setStyle(TableStyle([
                                             ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                                             ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                                             ('FONTSIZE', (0, 0), (-1, -1), 7),
                                             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                             ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                                             ]))
                        w5, h5 = t5.wrapOn(c, width, height)
                        height2 = height2 - h5
                        t5.drawOn(c, 200, height2)


                        gm934 = Paragraph('<para></para>',stylesN)
                        gmn934 = Paragraph('<para></para>',stylesN)

                        data =  [[gm934,gmn934]]

                        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
                        t.setStyle(TableStyle([
                                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                                             ]))
                        t.wrapOn(c,width, height)


                        c.setFillColor(colors.black)
                        c.setFont("Helvetica-Bold",10)
                        if pageCount%2==0:
                            t.drawOn(c, -3*inch,0.2*inch)
                            c.drawString(20, 0.15*inch, str(pageCount))
                        else:
                            t.drawOn(c, width-35,0.2*inch)
                            c.drawString(width-30, 0.15*inch, str(pageCount))

                        c.showPage()
                        pageCount +=1
                else:
                    # print"in else"
                    data1 = data[:numberRows-1]
                    # printdata1, "data1"
                    data2 = data[numberRows:-1]
                    # printdata2, "data2"
                    t5 = Table(data1,rowHeights=[20]*len(data1))
                    t5.setStyle(TableStyle([
                                         ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                                         ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                                         ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                                         ('FONTSIZE', (0, 0), (-1, -1), 7),
                                         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                         ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                                         ]))
                    w5, h5 = t5.wrapOn(c, width, height)
                    height2 = height2 - h5
                    t5.drawOn(c, 200, height2)

                    gm934 = Paragraph('<para></para>',stylesN)
                    gmn934 = Paragraph('<para></para>',stylesN)

                    data =  [[gm934,gmn934]]

                    t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
                    t.setStyle(TableStyle([
                                        ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                                         ]))
                    t.wrapOn(c,width, height)


                    c.setFillColor(colors.black)
                    c.setFont("Helvetica-Bold",10)
                    if pageCount%2==0:
                        t.drawOn(c, -3*inch,0.2*inch)
                        c.drawString(20, 0.15*inch, str(pageCount))
                    else:
                        t.drawOn(c, width-35,0.2*inch)
                        c.drawString(width-30, 0.15*inch, str(pageCount))

                    c.showPage()
                    pageCount +=1

                    maxNumberItems = 20

                    index = float(len(data2))/maxNumberItems
                    # printindex
                    index = int(math.ceil(index))
                    # printindex, range(index),"index ...."
                    for i in range(index):
                        if i == index-1:
                            data1 = data2[maxNumberItems*i:-1]
                            data1.insert(0,dataHeading)
                            # printlen(data1), i , "if loop"
                        else:
                            data1 = data2[maxNumberItems*i:maxNumberItems*(i+1)-1]
                            data1.insert(0,dataHeading)
                            # printlen(data1), i, "else loop"
                        # printdata1, "datapass "
                        pageCount = addAccessoriePageExtra(c, data1, access,stylesN,productImage,pageCount,lang)

    return pageCount

def elevatorCode1(request,response,styles,stylesN,stylesH,width,height,c,lang,templatesTractionRopes2,accessoriesCat,productTemplatesObjects):
    pageCount = 1

    width, height = A4
    # printlang , 'language'
    pageCount = initialPages(request,response,styles,stylesN,stylesH,width,height,c,productTemplatesObjects,pageCount,lang)
    print pageCount, "pageCountpageCountpageCountpageCountpageCountpageCountpageCountpageCountpageCount"

    pageCount = templateAndAccess(request,response,styles,stylesN,stylesH,width,height,c,lang,templatesTractionRopes2,accessoriesCat,pageCount)
    endPagesElevatorRope(request,response,styles,stylesN,stylesH,width,height,c,pageCount,lang)
    c.save()



def addCTPPage(c, data1,template,stylesN,pageCount,lang):
    if lang == 'en':
        width, height = A4

        if pageCount%2 == 1:
            if template.catalogBG1:
                background = template.catalogBG1.path
            else:
                background = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/ctpCatalog',"page4.jpg")
            c.drawImage(background,0,0,width=width, height=height, mask = 'auto')
            name = Paragraph('<para fontName = FrutigerB fontSize=30>%s</para>'%(template.name), stylesN)
            nd =[[name]]
            w = pdfmetrics.stringWidth(template.name, "FrutigerB", 30)
            # printw, "text width "
            ndt = Table(nd)
            w1,h1 = ndt.wrapOn(c, width,height)
            width2 = width - w -50
            ndt.drawOn(c, width2,570)


        else:
            if template.catalogBG2:
                background = template.catalogBG2.path
            else:
                background = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/ctpCatalog',"page4.jpg")
            c.drawImage(background,0,0,width=width, height=height, mask = 'auto')
            name = Paragraph('<para fontName = FrutigerB fontSize=30>%s</para>'%(template.name), stylesN)
            nd =[[name]]
            w = pdfmetrics.stringWidth(template.name, "FrutigerB", 30)
            # printw, "text width "
            ndt = Table(nd)
            w1,h1 = ndt.wrapOn(c, width,height)
            width2 = 50
            ndt.drawOn(c, width2,570)

        name = Paragraph('<para fontName = FrutigerR fontSize=15>%s</para>'%("COATED TRANSMISSION PRODUCTS"), stylesN)
        nd =[[name]]
        ndt = Table(nd)
        w1,h1 = ndt.wrapOn(c, width,height)

        ndt.drawOn(c, 200,548)

        table = Table(data1,rowHeights=[20]*len(data1))
        table.setStyle(TableStyle([
                             ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                             ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                             ('FONTSIZE', (0, 0), (-1, -1), 7),
                             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                             ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                             ]))
        w5, h5 = table.wrapOn(c, width, height)
        height2 = height - h5-350
        table.drawOn(c, 200, height2)


        para2 = Paragraph('<para fontName = Helvetica fontSize=6 >%s</para>'%(template.disclaimer_en), stylesN)
        tab = [[para2]]
        r = Table(tab,colWidths=3.25*inch)
        w,h1 = r.wrapOn(c, width,height)
        height2 = height2 - h1
        r.drawOn(c, 200, height2)

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1
        return pageCount

    elif lang == 'de':
        width, height = A4

        if pageCount%2 == 1:
            if template.catalogBG1:
                background = template.catalogBG1.path
            else:
                background = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/ctpCatalog',"page4.jpg")
            c.drawImage(background,0,0,width=width, height=height, mask = 'auto')
            name = Paragraph('<para fontName = FrutigerB fontSize=30>%s</para>'%(template.name), stylesN)
            nd =[[name]]
            w = pdfmetrics.stringWidth(template.name, "FrutigerB", 30)
            # printw, "text width "
            ndt = Table(nd)
            w1,h1 = ndt.wrapOn(c, width,height)
            width2 = width - w -50
            ndt.drawOn(c, width2,570)


        else:
            if template.catalogBG2:
                background = template.catalogBG2.path
            else:
                background = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/ctpCatalog',"page4.jpg")
            c.drawImage(background,0,0,width=width, height=height, mask = 'auto')
            name = Paragraph('<para fontName = FrutigerB fontSize=30>%s</para>'%(template.name), stylesN)
            nd =[[name]]
            w = pdfmetrics.stringWidth(template.name, "FrutigerB", 30)
            # printw, "text width "
            ndt = Table(nd)
            w1,h1 = ndt.wrapOn(c, width,height)
            width2 = 50
            ndt.drawOn(c, width2,570)

        name = Paragraph('<para fontName = FrutigerR fontSize=15>%s</para>'%("COATED TRANSMISSION PRODUCTS"), stylesN)
        nd =[[name]]
        ndt = Table(nd)
        w1,h1 = ndt.wrapOn(c, width,height)

        ndt.drawOn(c, 200,548)

        table = Table(data1,rowHeights=[20]*len(data1))
        table.setStyle(TableStyle([
                             ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                             ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                             ('FONTSIZE', (0, 0), (-1, -1), 7),
                             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                             ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                             ]))
        w5, h5 = table.wrapOn(c, width, height)
        height2 = height - h5-350
        table.drawOn(c, 200, height2)


        para2 = Paragraph('<para fontName = Helvetica fontSize=6 >%s</para>'%(template.disclaimer_otl), stylesN)
        tab = [[para2]]
        r = Table(tab,colWidths=3.25*inch)
        w,h1 = r.wrapOn(c, width,height)
        height2 = height2 - h1
        r.drawOn(c, 200, height2)

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1
        return pageCount

    elif lang == 'zh':
        width, height = A4

        if pageCount%2 == 1:
            if template.catalogBG1:
                background = template.catalogBG1.path
            else:
                background = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/ctpCatalog',"page4.jpg")
            c.drawImage(background,0,0,width=width, height=height, mask = 'auto')
            name = Paragraph('<para fontName = FrutigerB fontSize=30>%s</para>'%(template.name), stylesN)
            nd =[[name]]
            w = pdfmetrics.stringWidth(template.name, "FrutigerB", 30)
            # printw, "text width "
            ndt = Table(nd)
            w1,h1 = ndt.wrapOn(c, width,height)
            width2 = width - w -50
            ndt.drawOn(c, width2,570)


        else:
            if template.catalogBG2:
                background = template.catalogBG2.path
            else:
                background = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/ctpCatalog',"page4.jpg")
            c.drawImage(background,0,0,width=width, height=height, mask = 'auto')
            name = Paragraph('<para fontName = FrutigerB fontSize=30>%s</para>'%(template.name), stylesN)
            nd =[[name]]
            w = pdfmetrics.stringWidth(template.name, "FrutigerB", 30)
            # printw, "text width "
            ndt = Table(nd)
            w1,h1 = ndt.wrapOn(c, width,height)
            width2 = 50
            ndt.drawOn(c, width2,570)

        name = Paragraph('<para fontName = FrutigerR fontSize=15>%s</para>'%("COATED TRANSMISSION PRODUCTS"), stylesN)
        nd =[[name]]
        ndt = Table(nd)
        w1,h1 = ndt.wrapOn(c, width,height)

        ndt.drawOn(c, 200,548)

        table = Table(data1,rowHeights=[20]*len(data1))
        table.setStyle(TableStyle([
                             ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                             ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                             ('FONTSIZE', (0, 0), (-1, -1), 7),
                             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                             ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                             ]))
        w5, h5 = table.wrapOn(c, width, height)
        height2 = height - h5-350
        table.drawOn(c, 200, height2)


        para2 = Paragraph('<para fontName = STSong-Light fontSize=6 >%s</para>'%(template.disclaimer_ch), stylesN)
        tab = [[para2]]
        r = Table(tab,colWidths=3.25*inch)
        w,h1 = r.wrapOn(c, width,height)
        height2 = height2 - h1
        r.drawOn(c, 200, height2)

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1
        return pageCount


def ctpCode(request,response,ctpObj,styles,stylesN,stylesH,width,height,c,lang):
    pageCount = 1
    page1BG = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/ctpCatalog','page1.jpg')
    page2BG = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/ctpCatalog','page2.jpg')
    page3BG = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/ctpCatalog','page3.jpg')
    page4BG = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/ctpCatalog','page4.jpg')
    page5BG = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/ctpCatalog','page5.jpg')
    page6BG = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/ctpCatalog','page6.jpg')
    page7BG = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/ctpCatalog','page7a.jpg')
    page8BG = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/ctpCatalog','page8.jpg')
    page9BG = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/ctpCatalog','page9.jpg')
    page10BG = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/ctpCatalog','page10.jpg')
    page11BG = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/ctpCatalog','page11.jpg')
    page12BG = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/ctpCatalog','page12.jpg')


    if lang == 'en':

        #page 1
        c.drawImage(page1BG,0,0,width=width,height=height,mask='auto')
        c.setFont("FrutigerB",50)
        c.setFillColor('#000000')
        c.drawString(185, 5.85*inch, "CTP")

        c.setFont("FrutigerR",15)
        c.setFillColor('#000000')
        c.drawString(300, 5.85*inch, "COATED TRACTION ROPES")

        c.setFont("FrutigerB",20)
        c.setFillColor(colors.white)
        c.drawString(330, 30, ". . . the future starts now!")

        c.showPage()
        pageCount +=1

        #page 2
        c.drawImage(page2BG,0,0,width=width, height=height, mask='auto')

        c.setFillColor(colors.black)
        c.setFont("FrutigerB",25)
        c.drawString(50, 8.3*inch, "SERVICES")
        c.setFillGray(0.5)


        tp = Paragraph('<para fontName = FrutigerB fontsize=12 leftindent=13  ><b>System Provider</b></para>',stylesN)
        tp2 = Paragraph('<para fontName = FrutigerR fontsize=9  align="Justify" leading=15> We offer to you a wide assortment of elevator ropes, accessories and tools to meet all of your requirements. We supply you with complete solutions or individually combined components as individual or pre-assembled parts to suit your needs.</para>',stylesN)
        tpt=[[tp],[tp2]]
        tptab=Table(tpt,colWidths=6*inch)
        tptab.setStyle(TableStyle([
                                    ('LEFTPADDING',(0,1),(-1,-1),20),
                               ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,1.7*inch, 450)

        tp = Paragraph('<para fontName = FrutigerB fontsize=12 leftindent=13  ><b>Customized</b></para>',stylesN)
        tp2 = Paragraph('<para fontName = FrutigerR fontsize=9  align="Justify" leading=15> Our wide assortment of elevator ropes, accessories and tools provides nearly all products required for your applications. If none of the articles depicted in the catalog solvesyour problem, or if your elevator is to meet specific requirements, we will be glad to advise you and to develop customized solutions together with you.</para>',stylesN)
        tpt=[[tp],[tp2]]
        tptab=Table(tpt,colWidths=6*inch)
        tptab.setStyle(TableStyle([
                                    ('LEFTPADDING',(0,1),(-1,-1),20),
                               ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,1.7*inch, 350)


        tp = Paragraph('<para fontName = FrutigerB fontsize=12 leftindent=13  ><b>Availability</b></para>',stylesN)
        tp2 = Paragraph('<para fontName = FrutigerR fontsize=9 align="Justify" leading=15 >Due to our three production facilities located in Switzerland and China, as well as due toour global network of warehouse locations, our products will be delivered to your factory or your construction site within a very short time. Please contact us if you have anyquestions regarding deadlines, individual deliveries and specific projects.</para>',stylesN)
        tpt=[[tp],[tp2]]
        tptab=Table(tpt,colWidths=6*inch)
        tptab.setStyle(TableStyle([
                                    ('LEFTPADDING',(0,1),(-1,-1),20),
                               ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,1.7*inch, 260)


        tp = Paragraph('<para fontName = FrutigerB fontsize=12 leftindent=13  ><b>Express Service</b></para>',stylesN)
        tp2 = Paragraph('<para fontName = FrutigerR fontsize=9 align="Justify" leading=15 >In urgent cases we provide the required materials ex works within the hour and ship it to you as quickly as possible by courier all over the world.</para>',stylesN)
        tpt=[[tp],[tp2]]
        tptab=Table(tpt,colWidths=6*inch)
        tptab.setStyle(TableStyle([

                                    ('LEFTPADDING',(0,1),(-1,-1),20)
                               ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,1.7*inch, 200)

        tp = Paragraph('<para fontName = FrutigerB fontsize=12 leftindent=13  ><b>International Standards</b></para>',stylesN)
        tp2 = Paragraph('<para fontName = FrutigerR fontsize=9 align="Justify" leading=15 >All of our products meet the valid international standards.<br/> BRUGG LIFTING is certified according to ISO 9001:2008 and ISO 14001:2004.</para>',stylesN)
        tpt=[[tp],[tp2]]
        tptab=Table(tpt,colWidths=6*inch)
        tptab.setStyle(TableStyle([

                                    ('LEFTPADDING',(0,1),(-1,-1),20),
                               ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,1.7*inch, 140)

        tp = Paragraph('<para fontName = FrutigerB fontsize=12 leftindent=13  ><b>Training/Specialist Workshops</b></para>',stylesN)
        tp2 = Paragraph('<para fontName = FrutigerR fontsize=9 align="Justify" leading=15 >Our aim is to ensure that you will enjoy an optimal use and an increase service life of your elevator ropes. Make use of our offering of qualified and customized training units for your staff.</para>',stylesN)
        tpt=[[tp],[tp2]]
        tptab=Table(tpt,colWidths=6*inch)
        tptab.setStyle(TableStyle([

                                    ('LEFTPADDING',(0,1),(-1,-1),20),
                               ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,1.7*inch, 70)

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        #page 3

        c.drawImage(page3BG,0,0,width=width,height=height,mask='auto')


        p = Paragraph('''<para fontName= FrutigerR fontsize=10  leading=13 align="justify">Developed as a world s first, CTP combines technological innovations into
        a state of the art plastic coated rope specifically designed for the elevator
        industry.  </para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=4.7*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,50,6.7*inch)

        p = Paragraph('''<para fontName= FrutigerR fontsize=10  leading=13 align="justify">Approved for traction sheaves with a diameter of only 115 mm, CTP  ropes
        have been already installed in 60,000 elevators all over the world.
        Tested by means if simulation In the laboratory and under real-life conditions,
        CTP  meets highest demands on function and efficiency. </para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=4.7*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,50,5.8*inch)


        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)
        t.drawOn(c, 7.75*inch,0.2*inch)

        c.setFillColor(colors.black)
        c.setFont("FrutigerB",10)
        c.drawString(580, 0.15*inch, "3")

        c.showPage()
        pageCount +=1

        #page 4
        for template in ctpObj:
            prodfield = ProductField.objects.filter(template = template.pk)
            # printprodfield
            prod = Product.objects.filter(template = template.pk)
            # printprod



            if pageCount%2 == 1:
                if template.catalogBG1:
                    background = template.catalogBG1.path
                else:
                    background = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/ctpCatalog',"page4.jpg")

                c.drawImage(background,0,0,width=width, height=height, mask = 'auto')
                name = Paragraph('<para fontName = FrutigerB fontSize=30>%s</para>'%(template.name), stylesN)
                nd =[[name]]
                w = pdfmetrics.stringWidth(template.name, "FrutigerB", 30)
                # printw, "text width "
                ndt = Table(nd)
                w1,h1 = ndt.wrapOn(c, width,height)
                width2 = width - w -50
                ndt.drawOn(c, width2,570)



            else:
                if template.catalogBG2:
                    background = template.catalogBG2.path
                else:
                    background = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/ctpCatalog',"page4.jpg")
                c.drawImage(background,0,0,width=width, height=height, mask = 'auto')
                name = Paragraph('<para fontName = FrutigerB fontSize=30>%s</para>'%(template.name), stylesN)
                nd =[[name]]
                w = pdfmetrics.stringWidth(template.name, "FrutigerB", 30)
                # printw, "text width "
                ndt = Table(nd)
                w1,h1 = ndt.wrapOn(c, width,height)
                width2 = 50
                ndt.drawOn(c, width2,570)



            name = Paragraph('<para fontName = FrutigerR fontSize=15>%s</para>'%("COATED TRANSMISSION PRODUCTS"), styles['Normal'])
            nd =[[name]]
            # printw, "text width "
            ndt = Table(nd)
            w1,h1 = ndt.wrapOn(c, width,height)

            ndt.drawOn(c, 200,548)

            c.drawImage(template.defaultImage.path,50,400,width=1.4*inch,height=1.4*inch, mask='auto')

            para2 =  addBRInRichText(template.rteData2_en)
            para22 = Paragraph('<para fontName = FrutigerR>%s</para>'%(para2), styles['Normal'])
            tab1 = [[para22]]
            ps = Table(tab1,colWidths=4.5*inch)
            w2, h2 = ps.wrapOn(c, width,height)
            height2 = height - h2 - 350


            ps.drawOn(c, 200, height2)

            height2 = height2 - 50
            height3 = height2 + 15
            height4 = height2
            height5 = height2 - 30
            c.setFillColor('#81B3EE')
            c.setStrokeColor(colors.white)
            c.rect(4*inch,height2,0.6*inch,0.6*inch, fill=1)
            c.setFont("Helvetica-Bold", 7)
            c.setFillColor(colors.black)
            k = json.loads(template.keyword1)
            k11 =[[k]]
            r11 = Table(k11,colWidths=3.6*inch,rowHeights=4*mm)
            c.setFont("Helvetica", 5)

            para101 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%(k["value1"]), styles['Normal'])
            desc101 = [[para101]]
            r101 = Table(desc101,colWidths=0.6*inch,rowHeights=1*mm)
            w, h = r101.wrapOn(c, width,height)
            r101.drawOn(c, 4*inch, height3)

            para102 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%("N/mm2"), styles['Normal'])
            desc102 = [[para102]]
            r102 = Table(desc102,colWidths=0.6*inch,rowHeights=1*mm)
            r102.wrapOn(c, width,height)
            r102.drawOn(c, 4*inch, height4)

            para103 = Paragraph('<para align="center" fontName = FrutigerR fontSize=7 >%s</para>'%("E-Module"), styles['Normal'])
            desc103 = [[para103]]
            r103 = Table(desc103,colWidths=0.6*inch,rowHeights=1*mm)
            r103.wrapOn(c, width,height)
            r103.drawOn(c, 4*inch, height5)


            c.setFillColor('#9BC7EC')
            c.rect(5*inch,height2,0.6*inch,0.6*inch, fill=1)
            c.setFont("Helvetica-Bold", 7)
            c.setFillColor(colors.black)
            k1 = json.loads(template.keyword2)

            k12 =[[k1]]

            r12 = Table(k12,colWidths=5*inch,rowHeights=10*mm)

            para201 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%(k1["value1"]), styles['Normal'])
            desc201 = [[para201]]
            r201 = Table(desc201,colWidths=0.6*inch)
            w,h = r201.wrapOn(c, width,height)

            r201.drawOn(c, 5*inch, height3)

            para202 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%("%"), styles['Normal'])
            desc202 = [[para202]]
            r202 = Table(desc202,colWidths=0.6*inch,rowHeights=1*mm)
            r202.wrapOn(c, width,height)
            r202.drawOn(c, 5*inch, height4)

            para203 = Paragraph('<para align="center" fontName = FrutigerR fontSize=7 >%s</para>'%("Elastic<br/>Elongation"), styles['Normal'])
            desc203 = [[para203]]
            r203 = Table(desc203,colWidths=0.65*inch,rowHeights=1*mm)
            r203.wrapOn(c, width,height)
            r203.drawOn(c, 5*inch, height5 )


            c.setFillColor(	'#BBD5F0')
            c.setStrokeColor(colors.white)

            c.rect(6*inch,height2,0.6*inch,0.6*inch, fill=1)
            c.setFont("Helvetica-Bold", 7)
            c.setFillColor(colors.black)
            k2 = json.loads(template.keyword3)

            k13 = [[k2]]

            r13 = Table(k13,colWidths=5*inch,rowHeights=10*mm)

            para301 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%(k2["value1"]), styles['Normal'])
            desc301 = [[para301]]
            r301 = Table(desc301,colWidths=0.6*inch,rowHeights=1*mm)
            r301.wrapOn(c, width,height)
            r301.drawOn(c, 6*inch, height3)

            para302 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%("%"), styles['Normal'])
            desc302 = [[para302]]
            r302 = Table(desc302,colWidths=0.6*inch,rowHeights=1*mm)
            r302.wrapOn(c, width,height)
            r302.drawOn(c, 6*inch, height4)

            para303 = Paragraph('<para align="center" fontName = FrutigerR fontSize=7 >%s</para>'%("Permanent<br/>Elongation"), styles['Normal'])
            desc303 = [[para303]]
            r303 = Table(desc303,colWidths=0.7*inch,rowHeights=1*mm)
            r303.wrapOn(c, width,height)
            r303.drawOn(c, 6*inch, height5)


            c.setFillColor('#D5E5F5')
            c.setStrokeColor(colors.white)
            c.rect(7*inch,height2,0.6*inch,0.6*inch, fill=1)
            c.setFont("Helvetica-Bold", 7)
            c.setFillColor(colors.black)
            k3 = json.loads(template.keyword4)
            k14 = [[k3]]
            r14 = Table(k14,colWidths=5*inch,rowHeights=10*mm)

            para401 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%(k3["value1"]), styles['Normal'])
            desc401 = [[para401]]
            r401 = Table(desc401,colWidths=0.6*inch,rowHeights=1*mm)
            r401.wrapOn(c, width,height)
            r401.drawOn(c, 7*inch, height3)

            para402 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%("m"), styles['Normal'])
            desc402 = [[para402]]
            r402 = Table(desc402,colWidths=0.6*inch,rowHeights=1*mm)
            r402.wrapOn(c, width,height)
            r402.drawOn(c, 7*inch, height4)

            para403 = Paragraph('<para align="center" fontName = FrutigerR fontSize=7 >%s</para>'%("Lifting<br/>Height"), styles['Normal'])
            desc403 = [[para403]]
            r403 = Table(desc403,colWidths=0.6*inch,rowHeights=1*mm)
            r403.wrapOn(c, width,height)
            r403.drawOn(c, 7*inch, height5)


            height2 = height5

            data = []
            # data2 = []
            dataHeading = ['Item Number']
            dataHeading2 = ['']
            list1 = []
            list2 = []
            for j in prodfield:
                # printprodfield
                if j.inPdf ==True:

                    # printj.name,'kkkkkkkkkkkkk'
                    try:
                        name1, name2 = j.name.split('(')
                        # printname2[:-1]
                        name2 = ''+name2[:-1]
                        # printname2
                    except:
                        name1 = j.name
                        name2 = ''

                    # printname1, ' ' , name2

                    list1.append(name1)
                    list2.append(name2)
            for a in list1:
                dataHeading.append(a)
            for b in list2:
                dataHeading2.append(b)



            for i in prod:
                appendlist = [i.itemNumber]
                for j in prodfield:
                    prodQty = ProductValueMap.objects.filter( field = j.pk,product = i.pk)
                    for k in prodQty:
                        if j.inPdf ==True:
                            if j.type=='Char':
                                appendlist.append(k.char)
                            if j.type=='float':
                                appendlist.append(k.fValue)
                            if j.type=='Integer':
                                appendlist.append(k.iValue)
                            if j.type=='Boolean':
                                appendlist.append(k.bool)
                data.append(appendlist)

            height2 = height2-40
            leftHeight = height2-100
            numberRows = int(leftHeight/20)
            # printheight2, leftHeight, numberRows, "number of rows"

            data.insert(0,dataHeading)
            data.insert(1,dataHeading2)

            if len(data)<= numberRows:
                    t5 = Table(data,rowHeights=[20]*len(data))
                    t5.setStyle(TableStyle([
                                         ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                                         ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                                         ('FONTSIZE', (0, 0), (-1, -1), 7),
                                         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                         ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                                         ]))
                    w5, h5 = t5.wrapOn(c, width, height)
                    height2 = height2 - h5
                    t5.drawOn(c, 200, height2)



                    para2 = Paragraph('<para fontName = Helvetica fontSize=6 >%s</para>'%(template.disclaimer_en), styles['Normal'])
                    tab = [[para2]]
                    r = Table(tab,colWidths=3.25*inch)
                    w,h1 = r.wrapOn(c, width,height)
                    height2 = height2 - h1
                    r.drawOn(c, 200, height2)

                    gm934 = Paragraph('<para></para>',stylesN)
                    gmn934 = Paragraph('<para></para>',stylesN)

                    data =  [[gm934,gmn934]]

                    t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
                    t.setStyle(TableStyle([
                                        ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                                         ]))
                    t.wrapOn(c,width, height)


                    c.setFillColor(colors.black)
                    c.setFont("Helvetica-Bold",10)
                    if pageCount%2==0:
                        t.drawOn(c, -3*inch,0.2*inch)
                        c.drawString(20, 0.15*inch, str(pageCount))
                    else:
                        t.drawOn(c, width-35,0.2*inch)
                        c.drawString(width-30, 0.15*inch, str(pageCount))

                    c.showPage()
                    pageCount +=1
            else:
                # print"in else ctp extra page requiresss"
                data1 = data[:numberRows-1]

                data2 = data[numberRows:-1]

                t5 = Table(data1,rowHeights=[20]*len(data1))
                t5.setStyle(TableStyle([
                                     ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                                     ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                                     ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                                     ('FONTSIZE', (0, 0), (-1, -1), 7),
                                     ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                     ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                                     ]))
                w5, h5 = t5.wrapOn(c, width, height)
                height2 = height2 - h5
                t5.drawOn(c, 200, height2)



                para2 = Paragraph('<para fontName = Helvetica fontSize=6 >%s</para>'%(template.disclaimer_en), styles['Normal'])
                tab = [[para2]]
                r = Table(tab,colWidths=3.25*inch)
                w,h1 = r.wrapOn(c, width,height)
                height2 = height2 - h1
                r.drawOn(c, 200, height2)

                gm934 = Paragraph('<para></para>',stylesN)
                gmn934 = Paragraph('<para></para>',stylesN)

                data =  [[gm934,gmn934]]

                t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
                t.setStyle(TableStyle([
                                    ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                                     ]))
                t.wrapOn(c,width, height)


                c.setFillColor(colors.black)
                c.setFont("Helvetica-Bold",10)
                if pageCount%2==0:
                    t.drawOn(c, -3*inch,0.2*inch)
                    c.drawString(20, 0.15*inch, str(pageCount))
                else:
                    t.drawOn(c, width-35,0.2*inch)
                    c.drawString(width-30, 0.15*inch, str(pageCount))

                c.showPage()
                pageCount +=1
                maxNumberItems = 15

                index = float(len(data2))/maxNumberItems

                index = int(math.ceil(index))

                for i in range(index):
                    if i == index-1:
                        data1 = data2[maxNumberItems*i:-1]
                        data1.insert(0,dataHeading)
                        data1.insert(1,dataHeading2)

                    else:
                        data1 = data2[maxNumberItems*i:maxNumberItems*(i+1)-1]
                        data1.insert(0,dataHeading)
                        data1.insert(1,dataHeading2)

                    pageCount = addCTPPage(c, data1,template,stylesN,pageCount,lang)



        # new page

        c.drawImage(page5BG, 0,0, width=width, height=height, mask='auto')
        textobject = c.beginText()
        textobject.setTextOrigin(0.75*inch, 7.25*inch)
        textobject.setFont("STSong-Light", 10)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                                A world first, CTP ® unites technological innovation for the highest demands.
                                This high-end rope is unbeatable in terms of function and efficiency.''')
        c.drawText(textobject)

        textobject = c.beginText()
        textobject.setTextOrigin(0.75*inch, 6.8*inch)
        textobject.setFont("FrutigerB", 10)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            Reduce your total cost by up to 40%.
                            ''')
        c.drawText(textobject)
        c.drawText(textobject)
        textobject = c.beginText()
        textobject.setTextOrigin(0.75*inch, 6.6*inch)
        textobject.setFont("FrutigerR", 10)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            A smaller rope diameter and a smaller drive allow for a reduction of capital and operating cost.
                            ''')
        c.drawText(textobject)
        textobject = c.beginText()
        textobject.setTextOrigin(0.75*inch,6.3*inch)
        textobject.setFont("Helvetica-Bold", 10)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            Reduce your maintenance cost by up to 100%.
                            ''')
        c.drawText(textobject)
        c.drawText(textobject)
        textobject = c.beginText()
        textobject.setTextOrigin(0.75*inch, 6.1*inch)
        textobject.setFont("FrutigerR", 10)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            CTP is a self-contained system which requires neither lubrication and minimal maintenance.
                            ''')
        c.drawText(textobject)
        textobject = c.beginText()
        textobject.setTextOrigin(0.75*inch, 5.8*inch)
        textobject.setFont("FrutigerB", 10)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            Enjoy a clearly improved travelling comfort
                            ''')
        c.drawText(textobject)
        c.drawText(textobject)
        textobject = c.beginText()
        textobject.setTextOrigin(0.75*inch, 5.6*inch)
        textobject.setFont("Helvetica", 10)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            The polymer coating eliminates or strongly absorbs vibrations, which significantly contributes to a smooth running.
                            ''')
        c.drawText(textobject)
        textobject = c.beginText()
        textobject.setTextOrigin(0.75*inch, 5.3*inch)
        textobject.setFont("FrutigerB", 10)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            Increase the service life
                            ''')
        c.drawText(textobject)

        textobject = c.beginText()
        textobject.setTextOrigin(0.75*inch, 5.1*inch)
        textobject.setFont("FrutigerR", 10)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            As there is negligible wear between the traction sheave and the rope, the frequency of rope replacement is much reduced.
                            ''')
        c.drawText(textobject)
        # c.drawText(textobject1)
        c.setFont("FrutigerR",9)





        # c.drawImage(l1,130,170,width=2.5*inch,height=2.15*inch,mask='auto')
        c.setFont("FrutigerB", 5)

        c.drawString(2.15*inch, 2.25*inch, "Diagramm der festgelegten")
        c.drawString(2.15*inch, 2.1*inch, "Rillen fur CTP 6.5mm")

        # c.drawImage(l2,300,170, width=2.5*inch,height=2.15*inch,mask='auto')
        c.drawString(4*inch, 2.25*inch, "Diagramm der festgelegten")
        c.drawString(4*inch, 2.1*inch, "Rillen fur CTP 8.1mm")

        textobject = c.beginText()
        textobject.setTextOrigin(0.75*inch, 1.75*inch)
        textobject.setFont("FrutigerR", 8)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            Main data of traction sheave / deflection
                            ''')
        c.drawText(textobject)


        data = [
            ['FUR', 'Seil-@', 'Stahlseil-@',  'Reibungs-' , "Seilgeschwindigkeit","scheiben-@","Treibscheibe","Rillenform","Abelenkscheibe"],
           ['Art.-Nr', '', '',  'Koeffzient' , "max","","Material","","Material"],
           ['',   'mm',  'mm','','m/s'   ,'mm'   '',         'hulbrund@mm',     ' ',     ],
           ['10982',   '6.5', '4,9','0,6-0,3','3,5*','>115','C45,c45 gehartet,42CrMo4','3,4-3,65','Stahl,Gusseisen,PA,PU.'],
           ['73106',   '6.5', '4,9','0,6-0,3','3,5*','>115','C45,c45 gehartet,42CrMo4','3,4-3,65','Stahl,Gusseisen,PA,PU.'],


           ]

        t5 = Table(data, colWidths=[0.75* cm, 1* cm, 1 * cm,
                                    2.5* cm, 2.5* cm,2.5* cm,2.5* cm,2.5* cm, ],rowHeights=5.5*mm)
        t5.setStyle(TableStyle([
                             ('LINEABOVE',(0,2),(-1,-1),0.25,colors.black),
                             ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                            ('FONTSIZE', (0, 0), (-1, -1), 5),

                            ('FONTNAME', (0, 0), (1,0), "FrutigerB"),
                            ('FONTNAME', (2, 0), (3,0), "FrutigerB"),
                            ('FONTNAME', (4,0), (5,0), "FrutigerB"),
                            ('FONTNAME', (6, 0), (7,0), "FrutigerB"),
                            ('FONTNAME', (0,0),(8, 0), "FrutigerB"),
                            ('FONTNAME', (0,0),(0, 1), "FrutigerB"),
                            ('FONTNAME', (1,0),(3,1), "FrutigerB"),
                            ('FONTNAME', (4,1),(6,1), "FrutigerB"),
                            ('FONTNAME', (0,0),(8,1), "FrutigerB"),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
                            ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                            # ('ALIGN', (1, 0), (1, 7), 'CENTER'),
                            # ('ALIGN', (2, 0), (-1, 7), 'CENTER'),
                            # ('ALIGN', (3, 0), (-1, 7), 'LEFT'),
                            # ('ALIGN', (4, 0), (-1, 7), 'LEFT'),
                            # ('ALIGN', (5, 0), (-1, 7), 'CENTER'),
                            # ('VALIGN', (5, 0), (-1, 7), 'BOTTOM'),
                            # ('LEFTPADDING', (0, 0), (-1, -1), -20),
                            #  ('LEFTPADDING', (1, 0), (-1, -1),10),
                            #  ('LEFTPADDING', (2, 0), (-1, -1), -30),
                            #  ('LEFTPADDING', (3, 0), (-1, -1), -30),
                            #  ('LEFTPADDING', (5, 0), (-1, -1), -30),
                            # ('LEFTPADDING', (4, 0), (-1, 9), -30),
                            #  ('LEFTPADDING', (5, 0), (-1, 9), -70),
                            ('BACKGROUND', (1,0), (1, 1), '#DCDCDC'),
                            ('BACKGROUND', (1,2), (1, 3), '#DCDCDC'),
                            ('BACKGROUND', (1,4), (1, 5), '#DCDCDC'),
                            # ('BACKGROUND', (1,6), (1, 7), '#DCDCDC'),
                             ]))

        t5.wrapOn(c, 20, 170)
        t5.drawOn(c, 0.75*inch,0.6*inch)


        textobject1 = c.beginText()
        textobject1.setTextOrigin(0.72*inch, 0.49*inch)
        c.setFillColor(colors.black)
        textobject1.setFont("FrutigerR", 5)
        textobject1.textLines('''* Higher speeds must be tested..
                                   ''')
        c.drawText(textobject1)

        textobject1 = c.beginText()
        textobject1.setTextOrigin(0.75*inch, 0.38*inch)
        c.setFillColor(colors.black)
        textobject1.setFont("FrutigerR", 5)
        textobject1.textLines('''Tolerances according to ISO 2768-1 class m (middle).
                                   ''')
        c.drawText(textobject1)

        textobject1 = c.beginText()
        textobject1.setTextOrigin(0.8*inch, 0.27*inch)
        c.setFillColor(colors.black)
        textobject1.setFont("FrutigerR", 5)
        textobject1.textLines(''' The CTP  rope is only certified for usage on traction and deflector sheaves that meet the requirements outlined above.''')
        c.drawText(textobject1)


        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        #page 6
        c.drawImage(page6BG, 0,0, width=width, height=height, mask='auto')
        c.setFont('FrutigerB', 25)
        c.drawString(50, 7.8*inch, "APAG")

        c.setFont('FrutigerR', 13)
        c.drawString(125, 7.8*inch, "Threaded Swaged Sockets")


        textobject = c.beginText()
        textobject.setTextOrigin(3.2*inch, 6.5*inch)
        textobject.setFont("FrutigerB", 12)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            Product Data''')
        c.drawText(textobject)
        # textobject = c.beginText()
        # textobject.setTextOrigin(3*inch, 6.25*inch)
        # textobject.setFont("FrutigerR", 9)
        # lyrics = [' APAG-end connections are TUV tested and approved according to ENB1',
        #           ' APAG-end connections transmits 80 of minimal breaking load of traction rope',
        #
        #           ]
        # for line in lyrics:
        #     textobject.textLine(". %s" %(line))

        list = '''<ul>
                    <li> APAG-end connections are TUV tested and approved according to ENB1</li>
                    <li> APAG-end connections transmits 80 of minimal breaking load of traction rope</li>
                  </ul>
               '''
        height2 = htmlRMLCanvvas(list,c,4.75*inch,3*inch, 6.45*inch,styles['Normal'],colors.black,lang)

        c.drawText(textobject)
        textobject = c.beginText()
        textobject.setTextOrigin(3.2*inch, 5.5*inch)
        textobject.setFont("FrutigerB", 12)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            				 Advantages''')
        c.drawText(textobject)
        # textobject = c.beginText()
        # textobject.setTextOrigin(3*inch, 5.475*inch)
        # textobject.setFont("FrutigerR", 9)
        # lyrics = [' simple, fast and safe end terminations ',
        #           ' shortened installation time, since no mounting of end connections by customers ',
        #           ' no special tools required ',
        #           ' the compact type enables a very tight arrangement of ropes ',
        #           '  and parallel running ropes ',
        #           ' simple securing against rotation ',
        #           ' position of pilot hole for rope end ',
        #           ' quiet operation because there are no individual parts ',
        #
        #           ]
        # for line in lyrics:
        #     textobject.textLine(". %s" %(line))

        list = '''<ul>
                    <li> simple, fast and safe end termination</li>
                    <li> shortened installation time, since no mounting of end connections by customers</li>
                    <li> no special tools required</li>
                    <li> the compact type enables a very tight arrangement of ropes</li>
                    <li> and parallel running ropes</li>
                    <li> simple securing against rotation</li>
                    <li> position of pilot hole for rope end</li>
                    <li> quiet operation because there are no individual parts</li>
                  </ul>
               '''
        height2 = htmlRMLCanvvas(list,c,3.75*inch,3*inch, 5.45*inch,styles['Normal'],colors.black,lang)


        c.drawText(textobject)
        c.setFont("Helvetica-Bold", 7)

        c.drawString(3.2*inch, 3.1*inch, "For use with CTP  6.5 mm")

        data = [

           ['Art.-Nr', 'd1', 'd2', 'd3' , "d4","L1","L2","L3","L4"],
           ['',   '',  '','',''      'Abmessungen in mm',         '',     ' ',     ],
           ['10209',   'M 10', '13','9','7','240','150','66.0','16.6'],


           ]

        t5 = Table(data, colWidths=[1.25* cm, 1.25* cm, 1.25 * cm,
                                    1.25* cm, 1.25* cm,1.25* cm,1.25* cm,1.25* cm, ],rowHeights=5*mm)
        t5.setStyle(TableStyle([
                             ('LINEABOVE',(0,2),(-1,-1),0.25,colors.black),
                             ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                             ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                            ('FONTSIZE', (0, 0), (-1, -1), 6),
                             ('FONTNAME', (0, 0), (1,0), "Helvetica-Bold"),
                             ('FONTNAME', (2, 0), (3,0), "Helvetica-Bold"),
                             ('FONTNAME', (4,0), (5,0), "Helvetica-Bold"),
                             ('FONTNAME', (6, 0), (7,0), "Helvetica-Bold"),
                            ('FONTNAME', (0,0),(8, 0), "Helvetica-Bold"),

                            # ('BACKGROUND', (1,2), (1, 3), '#DCDCDC'),
                            # ('BACKGROUND', (1,4), (1, 5), '#DCDCDC'),
                             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
                            ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),

                             ]))

        t5.wrapOn(c, 30, 300)
        t5.drawOn(c, 3.2*inch,2.25*inch)
        c.setFont("Helvetica-Bold", 6)
        c.drawString(3.2*inch, 1.7*inch, "Fur den Einsatz mit CTP 8.1mm")

        data = [

           ['Art.-Nr', 'd1', 'd2',  'd3' , "d4","L1","L2","L3","L4"],
           ['',   '',  '','',''      'Abmessungen in mm',         '',     ' ',     ],
           ['10113',   'M 10', '13','9','7','240','150','66.0','16.6'],


           ]

        t5 = Table(data, colWidths=[1.25* cm, 1.25* cm, 1.25 * cm,
                                    1.25* cm, 1.25* cm,1.25* cm,1.25* cm,1.25* cm, ],rowHeights=5*mm)
        t5.setStyle(TableStyle([
                             ('LINEABOVE',(0,2),(-1,-1),0.25,colors.black),
                             ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                             ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                            ('FONTSIZE', (0, 0), (-1, -1), 5),
                             ('FONTNAME', (0, 0), (1,0), "Helvetica-Bold"),
                             ('FONTNAME', (2, 0), (3,0), "Helvetica-Bold"),
                             ('FONTNAME', (4,0), (5,0), "Helvetica-Bold"),
                             ('FONTNAME', (6, 0), (7,0), "Helvetica-Bold"),
                            ('FONTNAME', (0,0),(8, 0), "Helvetica-Bold"),

                             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
                            ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),

                             ]))

        t5.wrapOn(c, 30, 300)
        t5.drawOn(c, 3.2*inch,0.9*inch)


        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("FrutigerB",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        #page 7
        c.drawImage(page7BG, 0,0, width=width, height=height, mask='auto')
        c.setFont('FrutigerB', 18.5)
        c.drawString(50, 7.85*inch, "WEDGE SOCKET")
        c.setFont('FrutigerR', 13)
        c.drawString(210, 7.85*inch, "Symmetrical [EN 13411-7]")


        textobject = c.beginText()
        textobject.setTextOrigin(4.5*inch, 6.65*inch)
        textobject.setFont("FrutigerB", 12)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            Product Data''')
        c.drawText(textobject)
        # textobject = c.beginText()
        # textobject.setTextOrigin(4.4*inch, 6.375*inch)
        # textobject.setFont("FrutigerR", 9)
        # lyrics = [' wedge socket welded, steel zinc-plated',
        #           ' incl. wedge, bolt and safety pins pre-assembled',
        #           ' wedge socket transmits 80 of minimal breaking load',
        #           '  of traction rope or governor rope',
        #           ' eylet bolt welded, steel zinc-plated',
        #           ' in connection with the wedge socket the eyelet bolt transmits',
        #           '  80 of the minimal breaking load of the elevator rope',
        #           ' for mounting and operation the explanations in appendix B',
        #           '  of the norm EN 13411-7 are valid',
        #           ]
        # for line in lyrics:
        #     textobject.textLine(". %s" %(line))


        list = '''<ul>
                        <li> wedge socket welded, steel zinc-plated</li>
                        <li> incl. wedge, bolt and safety pins pre-assembled</li>
                        <li> wedge socket transmits 80 of minimal breaking load of traction rope or governor rope</li>
                        <li> eylet bolt welded, steel zinc-plated</li>
                        <li> in connection with the wedge socket the eyelet bolt transmits 80 of the minimal breaking load of the elevator rope</li>
                        <li> for mounting and operation the explanations in appendix B of the norm EN 13411-7 are valid</li>
                  </ul>
               '''
        height2 = htmlRMLCanvvas(list,c,3.7*inch,4.4*inch, 6.5*inch,styles['Normal'],colors.black,lang)


        c.drawText(textobject)
        textobject = c.beginText()
        textobject.setTextOrigin(4.5*inch, 4.5*inch)
        textobject.setFont("FrutigerB", 12)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            Advantages''')
        c.drawText(textobject)
        # textobject = c.beginText()
        # textobject.setTextOrigin(4.4*inch, 4.3*inch)
        # textobject.setFont("FrutigerR", 9)
        # lyrics = [' can be assembled safely and simply on-site ',
        #           ' springs, buffers and other accessories can',
        #           '  be mounted individually',
        # ]
        # for line in lyrics:
        #     textobject.textLine(". %s" %(line))
        # c.drawText(textobject)


        list = '''<ul>
                        <li> can be assembled safely and simply on-site</li>
                        <li>springs, buffers and other accessories can</li>
                        <li>be mounted individually</li>
                  </ul>
               '''
        height2 = htmlRMLCanvvas(list,c,3.75*inch,4.4*inch, 4.4*inch,styles['Normal'],colors.black,lang)


        c.setFont("FrutigerB", 7)
        c.drawString(4.5*inch, 3.5*inch, "Fur den Einsatz mit CTP 6.5 mm")

        data = [

           ['Art.-Nr','', 'Seil-@', 'd',  'd1',"L1","L2","L3"],
           ['',   '','mm',  '','',''      '',         '',     ' ',     ],
           ['64109',  'A', '5,0-6,5','M 10', '','265','180'],
           ['64140', 'AM', '5,0-6,5','M 10', '','265','180'],
           ['64115',    'D', '5,0-6,5','M 10', '23','265','180','85,5']


           ]

        t5 = Table(data, colWidths=[1* cm, 1* cm, 1 * cm,
                                    1* cm, 1* cm,1* cm,1* cm,1* cm, ],rowHeights=5*mm)
        t5.setStyle(TableStyle([
                             ('LINEABOVE',(0,2),(-1,-1),0.25,colors.black),
                             ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                             ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                            ('FONTSIZE', (0, 0), (-1, -1), 6),
                             ('FONTNAME', (0, 0), (1,0), "FrutigerB"),
                             ('FONTNAME', (2, 0), (3,0), "FrutigerB"),
                             ('FONTNAME', (4,0), (5,0), "FrutigerB"),
                             ('FONTNAME', (6, 0), (7,0), "FrutigerB"),
                             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
                            ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                            ('BACKGROUND', (2,0),(2, 5), '#DCDCDC')
                             ]))

        t5.wrapOn(c, 30, 300)
        t5.drawOn(c, 4.5*inch,2.4*inch)
        textobject1 = c.beginText()
        textobject1.setTextOrigin(4.5*inch, 2.3*inch)
        c.setFillColor(colors.black)
        textobject1.setFont("FrutigerR", 6)
        textobject1.textLines(''' Weitere Nennfestigkeiten und/oder Durchmesser
                                Weitere Nennfestigkeiten und/oder Durchmesser (auch   imperial Masse) auf Anfrage   ''')
        c.drawText(textobject1)
        c.setFont("FrutigerB", 7)

        c.drawString(4.5*inch, 1.9*inch, "Fur den Einsatz mit CTP 8.1mm")

        data = [

           ['Art.-Nr','', 'Seil-@', 'd',  'd1',"L1","L2","L3"],
           ['',   '','mm',  '','',''      '',         '',     ' ',     ],
           ['64109',  'A', '5,0-6,5','M 10', '','265','180'],
           ['64140', 'AM', '5,0-6,5','M 10', '','265','180'],
           ['64115',    'D', '5,0-6,5','M 10', '23','265','180','85,5']
           ]

        t5 = Table(data, colWidths=[1* cm, 1* cm, 1 * cm,
                                    1* cm, 1* cm,1* cm,1* cm,1* cm, ],rowHeights=5*mm)
        t5.setStyle(TableStyle([
                             ('LINEABOVE',(0,2),(-1,-1),0.25,colors.black),
                             ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                             ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                            ('FONTSIZE', (0, 0), (-1, -1), 6),
                             ('FONTNAME', (0, 0), (1,0), "FrutigerB"),
                             ('FONTNAME', (2, 0), (3,0), "FrutigerB"),
                             ('FONTNAME', (4,0), (5,0), "FrutigerB"),
                             ('FONTNAME', (6, 0), (7,0), "FrutigerB"),
                             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
                            ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                            ('BACKGROUND', (2,0),(2, 5), '#DCDCDC'),
                             ]))
        t5.wrapOn(c, 30, 300)
        t5.drawOn(c, 4.5*inch,0.8*inch)

        textobject1 = c.beginText()
        textobject1.setTextOrigin(4.5*inch,0.7*inch)
        c.setFillColor(colors.black)
        textobject1.setFont("FrutigerR", 5)
        textobject1.textLines(''' Weitere Nennfestigkeiten und/oder Durchmesser
                                Weitere Nennfestigkeiten und/oder Durchmesser (auch   imperial Masse) auf Anfrage   ''')
        c.drawText(textobject1)

        d = c.beginPath()
        d.rect(-20, 7.25*inch, 10*inch, 0.6*inch)
        d.rect(700, 7.25*inch, 12.5*inch, 0.2*inch)
        c.clipPath (d, stroke=0)
        # c.linearGradient(100*mm,200*mm,100*mm,60*mm, ('#996515','#DAA520','#996515'),extend=False)
        c.setFont("FrutigerR", 10)
        c.drawString(90,450, "Anpress-Ausssengewinden")
        c.setFont("FrutigerB", 18)
        # c.drawString(30,535, "APAG")
        c.setFont("FrutigerB", 18)
        c.drawString(400,450, "SEILSCHLOSS")
        c.setFont("FrutigerR", 10)
        c.drawString(530,450, "symmetrisch [EN-13411-7]")


        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("FrutigerB",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        #page 8

        # tabImg = "p8table.png"
        tabImg = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/ctpCatalog',"p8table.png")
        c.drawImage(page8BG,0,0,width=width,height=height, mask='auto')

        c.drawImage(tabImg,30,0.6*inch,width=8*inch,height= 3*inch, mask='auto')

        c.setFont('FrutigerB', 20.5)
        c.drawString(50, 7.9*inch, "INSPECTION MANUAL CTP")

        p = Paragraph('''<para fontName= FrutigerR fontsize=10  leading=13 align="justify">This document shall serve as practical guidance for CTP  rope
        inspections out in the field. It covers the official discard crite-
        ria of the CTP   rope as well as specific fields of inspection in
        a running elevator system which are most critical to rope life. </para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,6.3*inch)


        p = Paragraph('''<para fontName= FrutigerB fontsize=10  leading=13 align="justify">1.Discard criteria of the CTP ® rope </para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,5.85*inch)

        p = Paragraph('''<para fontName= FrutigerR fontsize=10  leading=13 align="justify">Brugg Lifting is applying a simple replacement criteria that
        limits the use of the CTP   rope after a defined number of
        cycles or trips (1) . This method of appraisal is therefore based
        on the level of usage.</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,5.05*inch)

        # textobject = c.beginText()
        # textobject.setTextOrigin(0.5*inch,  5.5*inch)
        # c.setFont('FrutigerB', 11)
        # c.setFillColorRGB(0,0,0)
        # textobject.textLines('''
        # 1. Discard criteria of the CTP rope''')
        # c.drawText(textobject)

        p = Paragraph('''<para fontName= FrutigerR fontsize=10  leading=13 align="justify">This discard criterion forms part of all CTP   rope certifications,
        which have been issued by LIFTINSTITUUT  The calculation of
        maximum allowed trips is described under chapter  conditions
        as follows:</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,4.15*inch)


        p = Paragraph('''<para fontName= FrutigerR fontsize=10  leading=13 align="justify"> - The defined maximum number of trips shall be divided by
        the number of pulleys which are passed most often by the
        bended rope</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,3.55*inch)

        p = Paragraph('''<para fontName= FrutigerR fontsize=8  leading=10 align="justify">Intact ropes in elevator shaft. Note
        that there is no color change of
        coating during the entire rope life.
        The rope remains dark black.</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=1.85*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,440,6.25*inch)


        p = Paragraph('''<para fontName= FrutigerR fontsize=9  leading=10 align="justify">During inspection the condition of the ropes should always be
        checked for any abnormal wear or damage (2) . Following is the
        table showing the five typical rope issues which can occur in
        an elevator system and the according actions, which must be
        taken by the elevator maintenance company in such a case.</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.5*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,325,5.2*inch)

        p = Paragraph('''<para fontName= FrutigerR fontsize=9  leading=10 align="justify">(1)
        	Every change of direction will be counted as a trip or cycle by the lift cont-
        roller. Important:  trip  or  cycle  should NOT be confused with  starts .</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.5*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,325,4.6*inch)


        p = Paragraph('''<para fontName= FrutigerR fontsize=9  leading=10 align="justify">(2)
        	The abnormal wear or damages presented below could be caused by
        overloading, unequal rope tension, severe shock, loading, torsional un-
        balance, bad rope alignment, etc. The maximum number of broken wires
        defined in the instructions is based on standards (UNE-EN, ISO, DIN) as
        well as on verification by testing samples.</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.5*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,325,3.6*inch)

        # p1 = ['Beschreibung der Kunststoffummantelung']
        #
        #
        # c.setFillColor('#EEE8AA')
        # c.rect(18, 0.68*inch, 8*inch, 2.4*inch,stroke=0,fill=1)
        #
        # c.drawString(30,150,'Ablegekriterien')


        # textobject = c.beginText()
        # textobject.setTextOrigin(0.4*inch,  2.9*inch)
        # c.setFont('FrutigerB', 9)
        # c.setFillColorRGB(0,0,0)
        # textobject.textLines('''
        # Ablegekriterien''')
        # c.drawText(textobject)
        #
        #
        # # Headers
        # hdescrpcion = Paragraph('''<para align = "RIGHT">|</para>''', stylesN)
        # hpartida = Paragraph('<para fontsize=7 align = "CENTER"><b>A</b></para>', stylesN)
        # h1 = Paragraph('''<para align = "LEFT">|</para>''', stylesN)
        # hcandidad = Paragraph('<para fontsize=7 align = "CENTER" leftindent = -5 align="LEFT"><b>B</b></para>', stylesN)
        # h2 = Paragraph('''|''', stylesN)
        # hprecio_unitario = Paragraph('<para fontsize=7 leftindent = -40 align="LEFT"><b>C</b></para>', stylesN)
        # h3 = Paragraph('''<para  leftindent = -130 align = "CENTER">|</para>''', stylesN)
        # hprecio_total = Paragraph('<para fontsize=7 align="CENTER" leftindent = -140 align="CENTER"><b>D</b></para>', stylesN)
        # h4 = Paragraph('''<para  align = "LEFT" leftindent = -70>|</para>''', stylesN)
        # hprecio_empty1 = Paragraph(''+''' ''', stylesN)
        # hprecio_empty2 = Paragraph(''+''' ''', stylesN)
        #
        #
        # descrpcion = Paragraph('<para fontsize=5><b>Problem</b></para>', styleN)
        # partida = Paragraph('<para fontsize=5>Beschadigung der <br\>Kunststoffummantelung</para>', styleN)
        # candidad = Paragraph('<para fontsize=5>Drahbruch</para>', styleN)
        # precio_unitario = Paragraph('<para fontsize=4>Massive Bruche von Drahten</para>', styleN)
        # precio_total = Paragraph('<para fontsize=4>Litzenbrunch</para>', styleN)
        # precio_empty1 = Paragraph('<para fontsize=4>Seil aus der Rille</para>', styleN)
        # precio_empty2 = Paragraph('<para fontsize=4> Image1 </para>', styleN)
        # # precio_empty3 = Paragraph('<para fontsize=4> Image2 </para>', styleN)
        #
        #
        # descrpcio = Paragraph('<para fontsize=5><b>Beschreibung</b></para>', styleN)
        # partid = Paragraph('<para fontsize=4>Kunststoffummantelung ist so <br/>abgenutzt, dass der mettallische</para>', styleN)
        # candida = Paragraph('<para fontsize=4>Mehr als 10 Drahte ragen<br/>aus dem TPU-Mantel</para>', styleN)
        # precio_unitari = Paragraph('<para fontsize=4>Mehr als 3 Drahte ragen aus   dem</para>', styleN)
        # precio_tota = Paragraph('<para fontsize=4>spezifischer Seilbruch</para>', styleN)
        # precio_empty = Paragraph('<para fontsize=4>Seil ist aus seiner<br/>ursprunglichen Rille</para>', styleN)
        # # precio_empty = Paragraph('<para fontsize=4> Image1 </para>', styleN)
        #
        #
        # descrpci = Paragraph('<para fontsize=5><b>Korrektur-massnahme</b></para>', styleN)
        # parti = Paragraph('<para fontsize=4>Bericht an<br/>Brugg Lifting senden.</para>', styleN)
        # candid = Paragraph('<para fontsize=4>Bericht an<br/>Brugg Lifting senden.</para>', styleN)
        # precio_unitar = Paragraph('<para fontsize=4>Bericht an<br/>Brugg Lifting senden.</para>', styleN)
        # precio_tot = Paragraph('<para fontsize=4>Bericht anBericht an<br/>Brugg Lifting senden.</para>', styleN)
        # precio_empt = Paragraph('<para fontsize=4>Bericht an<br/>Brugg Lifting senden.</para>', styleN)
        # precio_empt = Paragraph('<para fontsize=4> Image1 </para>', styleN)
        #
        #
        # descrpc = Paragraph('<para fontsize=5><b>Zeitskala</b></para>', styleN)
        # part = Paragraph('<para fontsize=4>< 2 Monate</para>', styleN)
        # candi = Paragraph('<para fontsize=4>2 Monate</para>', styleN)
        # precio_unita = Paragraph('<para fontsize=4>umgehend</para>', styleN)
        # precio_to = Paragraph('<para fontsize=4>umgehend</para>', styleN)
        # precio_emp = Paragraph('<para fontsize=4>umgehend</para>', styleN)
        # # precio_emp = Paragraph('<para fontsize=4> Image1 </para>', styleN)
        #
        #
        # data= [[hdescrpcion, hpartida,h1,hcandidad,h2,hprecio_unitario,h3, hprecio_total,h4, hprecio_empty1,hprecio_empty2],
        #        [descrpcion, partida, candidad, precio_unitario, precio_total,precio_empty1],
        #        [descrpcio,partid,candida,precio_unitari,precio_tota,precio_empty],
        #        [descrpci,parti,candid,precio_unitar,precio_tot,precio_empt],
        #        [descrpc,part,candi,precio_unita,precio_to,precio_emp]]
        #
        # table = Table(data, colWidths=[1.6 * cm, 2.5 * cm, 2 * cm,
        #                                2.25* cm, 2.5 * cm, 2*cm,1*cm,1.45*cm],rowHeights =12*mm)
        #
        # table.setStyle(TableStyle([
        #                             ('LINEABOVE',(0,1),(-1,1),0.25,colors.black),
        #                             ('SPAN',(2,0),(2,0)),
        #                             ('LINEBELOW',(0,1),(5,4),0.25,colors.black),
        #                             ('LINEBELOW',(0,4),(-1,-1),0.25,colors.black),
        #                             ('FONTSIZE', (0, 1), (-1, -1), 5),
        #                        ]))
        #
        # table.wrapOn(c, width, height)
        # table.drawOn(c, 17, 60, cm)

        # c.drawImage(logo13,6.15*inch,1.3*inch,width=0.45*inch,height=1.3*inch)
        # c.drawImage(logo14,6.65*inch,1.3*inch,width=0.45*inch,height=1.3*inch)
        # c.drawImage(logo15,7.15*inch,1.3*inch,width=0.45*inch,height=1.3*inch)
        # c.drawImage(logo16,7.65*inch,1.3*inch,width=0.45*inch,height=1.3*inch)




        p = c.beginPath()
        p.rect(-20, 7.25*inch, 4*inch, 0.9*inch)
        p.rect(268, 7.25*inch, 8*inch, 0.2*inch)

        c.clipPath(p, stroke=0)
        # c.linearGradient(100*mm,200*mm,100*mm,60*mm, ('#996515','#DAA520','#996515'),extend=False)
        c.setFont('FrutigerB', 17)
        c.setFillColor(colors.black)
        c.drawString(20,465,"CTP PRUFHANDBUCH")

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("FrutigerB",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        #page9

        # tabImg2 = "p9table.png"
        tabImg2 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/ctpCatalog',"p9table.png")
        c.drawImage(page9BG,0,0,width=width,height=height, mask='auto')

        c.drawImage(tabImg2,0,0.725*inch, width=3.85*inch, height= 3*inch, mask='auto')

        textobject = c.beginText()
        textobject.setTextOrigin(0.6*inch, 7.1*inch)
        c.setFont('FrutigerB', 10)
        c.setFillColorRGB(0,0,0)
        textobject.textLines('''
        2. Elevator specifications''')
        c.drawText(textobject)

        p = Paragraph('''<para fontsize=10  leading=13 align="justify">Only with the help of specific elevator data are we able to
        analyze the rope regarding traction capabilities, bending
        fatigue performance, etc. Therefore in case of support please
        contact your Brugg Lifting representative.  </para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.5*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,6.05*inch)

        # c.setFillColor('#EEE8AA')
        # c.rect(30, 3.35*inch, 3.9*inch, 2.25*inch,stroke=0,fill=1)

        textobject = c.beginText()
        textobject.setTextOrigin(0.6*inch, 5.65*inch)
        c.setFont('Helvetica-Bold', 10)
        c.setFillColorRGB(0,0,0)
        textobject.textLines('''
        Safety Instructions
        ''')
        c.drawText(textobject)

        textobject = c.beginText()
        textobject.setTextOrigin(0.6*inch, 5.5*inch)
        c.setFont('Helvetica', 9)
        c.setFillColorRGB(0,0,0)
        textobject.textLines('''
        Most of these inspections must be performed on a
        running elevator (in maintenance mode) Do never
        perform below listed measurements without trained an
        authorized elevator personnel. Be sure to be secured
        at all times when standing on top of the lift car.
        ''')
        c.drawText(textobject)

        textobject = c.beginText()
        textobject.setTextOrigin(0.6*inch, 4.6*inch)
        c.setFont('Helvetica', 9)
        c.setFillColorRGB(0,0,0)
        textobject.textLines('''
        CTP ropes should not be operated if oil or water is onth
        e surface of the rope. If water or oil is on the surface
        of the rope and then comes into contact with the traction
        sheave,it will reduce traction capability and causeslippage.
        ''')
        c.drawText(textobject)

        textobject = c.beginText()
        textobject.setTextOrigin(4.6*inch, 6.95*inch)
        c.setFont('Helvetica-Bold', 9)
        c.setFillColorRGB(0,0,0)
        textobject.textLines('''
        3. Visual inspection''')
        c.drawText(textobject)

        p = Paragraph('''<para fontsize=10  leading=13 align="justify">In addition external factors that could have a negative impact
        on the rope shall be evaluated. Before doing detailed mea-
        surements we recommend to first visually check the outside
        appearance of the rope. Particular attention must be paid to
        the rope coating: </para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.3*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,325,5.8*inch)


        # textobject = c.beginText()
        # textobject.setTextOrigin(4.5*inch, 5.45*inch)
        # c.setFont('Helvetica', 9)
        # c.setFillColorRGB(0,0,0)
        #
        # dat = [
        # 'Broken wires piercing out of the coating material',
        # 'Irregularities regarding rope coating surface',
        # 'Scratches, tear or fractures on the rope coating',
        # 'Abrasion of the coating',
        # 'Dust, oil, water etc. on the rope coating',
        # 'Rope kinks',
        # ]
        #
        # for i in dat:
        #     textobject.textLines("- %s"%(i))
        #
        # c.drawText(textobject)

        list = '''<ul>
                    <li> Broken wires piercing out of the coating material</li>
                    <li> Irregularities regarding rope coating surface</li>
                    <li> Scratches, tear or fractures on the rope coating</li>
                    <li> Abrasion of the coating</li>
                    <li> Dust, oil, water etc. on the rope coating</li>
                    <li> Rope kinks</li>
                  </ul>
               '''
        height2 = htmlRMLCanvvas(list,c,3.75*inch,4.5*inch, 5.55*inch,styles['Normal'],colors.black,lang)

        textobject = c.beginText()
        textobject.setTextOrigin(4.5*inch, 4.2*inch)
        c.setFont('Helvetica', 9)
        c.setFillColorRGB(0,0,0)
        textobject.textLines('''
        The following points should also be evaluated:
        ''')
        c.drawText(textobject)

        # textobject = c.beginText()
        # textobject.setTextOrigin(4.5*inch, 3.8*inch)
        # c.setFont('Helvetica', 9)
        # c.setFillColorRGB(0,0,0)
        #
        # data = [
        # 'Rope touching elevator parts or shaft',
        # 'Ropes touching each other due to electro-static charge',
        # 'Rope vibration during operation',
        # 'Insufficient alignment of traction sheave',
        # ]
        #
        # for i in data:
        #     textobject.textLines("- %s"%(i))
        #
        # c.drawText(textobject)

        list = '''<ul>
                    <li> Rope touching elevator parts or shaft</li>
                    <li> Ropes touching each other due to electro-static charge</li>
                    <li> Rope vibration during operation</li>
                    <li> Insufficient alignment of traction sheave</li>
                  </ul>
               '''
        height2 = htmlRMLCanvvas(list,c,3.75*inch,4.5*inch, 4*inch,styles['Normal'],colors.black,lang)


        p = Paragraph('''<para fontsize=10  leading=13 align="justify">Whenever possible pictures of the rope should be taken
        during inspection (also in the case of intact ropes). Also
        traction sheave, diverting pulley and end terminations
        should be photographed. </para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.3*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,325,2.3*inch)

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("FrutigerB",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        #page 10
        c.drawImage(page10BG,0,0,width=width,height=height, mask='auto')

        textobject = c.beginText()
        textobject.setTextOrigin(0.5*inch,  6.75*inch)
        c.setFont('FrutigerB', 12)
        c.setFillColorRGB(0,0,0)
        textobject.textLines('''
        4.Inspection of fleet angle''')
        c.drawText(textobject)

        c.setFont('FrutigerB', 21.5)
        c.drawString(50, 7.75*inch, "INSPECTION MANUAL CTP")



        p = Paragraph('''<para fontName=FrutigerR fontsize=10  leading=13 align="justify">The allowable fleet angle is 0.5 . For the CTP   8.1 this angle
        can be increased up to a maximum of 1.0  as long as the
        number of trips is reduced limited to 2 400 000 and divided
        by the number of pulleys passing the most bended part of
        the rope (this does NOT apply for the CTP   6.5). Fleet angle
        allowed (in accordance with our certificate) is 0.5 . If the fleet
        angle is too big it will induce torsion into the rope. This effect
        also applies to conventional ropes but is even more pronounced
        in the CTP   rope.  </para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,5*inch)


        p = Paragraph('''<para fontName=FrutigerR fontsize=10  leading=13 align="justify">The most critical positions are when the cabin is at the top
        floor (maximum fleet angle between cabin and tractions
        sheave deflecting pulley) and when the cabin is at the lowest
        floor (maximum fleet angle between counter weight and
        traction sheave deflecting pulley). It is fairly difficult to directly
        measure the fleet angle between rope and sheave. For this
        reason we recommend an indirect more practical way of
        measuring the fleet angle (please see below).  </para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,3.2*inch)


        p = Paragraph('''<para fontName=FrutigerR fontsize=10  leading=13 align="justify">To get a rough estimate on the fleet angle measure follo-
        wing points(illustratedon an elevator with 1:1 suspension): </para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,2.6*inch)


        p = Paragraph('''<para fontName=FrutigerR fontsize=10  leading=13 align="justify">Distance from traction sheave to end termination on lift
        car (when cabin is at the very top)</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,2.1*inch)


        p = Paragraph('''<para fontName=FrutigerR fontsize=10  leading=13 align="justify">Distance from rope to rope at rope termination on elevator
        cabin and on traction sheave. Distance from rope to rope on
        traction sheave (groove to-groove distance) and on rope
        termination on counter weight </para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,1.2*inch)

        p = Paragraph('''<para fontName=FrutigerR fontsize=10  leading=13 align="justify">Distance from traction sheave to end termination on
        counter weight (when cabin is at the very bottom) </para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,0.7*inch)


        # textobject = c.beginText()
        # textobject.setTextOrigin(4.6*inch, 3.1*inch)
        # c.setFont('FrutigerR', 5)
        # c.setFillColorRGB(0,0,0)
        # textobject.textLines('''
        # Schragzugwinkel zwischen
        # Scheibe und Seil
        # ''')
        # c.drawText(textobject)

        # textobject = c.beginText()
        # textobject.setTextOrigin(6.8*inch, 0.7*inch)
        # c.setFont('FrutigerR', 7)
        # c.setFillColorRGB(0,0,0)
        # textobject.textLines('''
        # Brugg Rillenlehre
        # ''')
        # c.drawText(textobject)

        textobject = c.beginText()
        textobject.setTextOrigin(8.6*inch, 0.7*inch)
        c.setFont('FrutigerR', 7)
        c.setFillColorRGB(0,0,0)
        textobject.textLines('''
        Seilspannungsmessgerat Brugg RPM
        ''')
        c.drawText(textobject)

        p = c.beginPath()
        p.rect(0.3*inch,1.2*inch, 0.1*inch, 0.1*inch)
        p.rect(0.3*inch,1.8*inch,0.1*inch, 0.1*inch)
        p.rect(0.3*inch,2.3*inch, 0.1*inch, 0.1*inch)
        p.rect(-20, 7.25*inch, 4*inch, 0.9*inch)
        p.rect(268, 7.25*inch, 8*inch, 0.2*inch)

        c.clipPath(p, stroke=0)


        c.setFont('FrutigerR', 7)
        c.drawString(23,87,"3")

        c.setFont('FrutigerR', 7)
        c.drawString(23,130,"2")

        c.setFont('FrutigerR', 7)
        c.drawString(23,167,"1")

        c.setFont('FrutigerB', 17)
        c.drawString(20,465,"CTP PRUFHANDBUCH")

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("FrutigerB",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        #page 11
        c.drawImage(page11BG,0,0,width=width,height=height, mask='auto')
        # textobject = c.beginText()
        # textobject.setTextOrigin(0.5*inch,  6.7*inch)
        # c.setFont('FrutigerB', 12)
        # c.setFillColorRGB(0,0,0)
        # textobject.textLines('''5. Inspection of groove shape
        # (traction sheave and diverting pulley)''')
        # c.drawText(textobject)

        p = Paragraph('''<para fontName=FrutigerB fontsize=10 >5. Inspection of groove shape<br/>
        (traction sheave and diverting pulley) </para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.5*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,0.4*inch,  6.8*inch)


        p = Paragraph('''<para fontName=FrutigerR fontsize=10  leading=13 align="justify"> Even if traction sheave and diverting pulley grooves are
        manufactured according to drawing (radius for CTP   6.5 :
        3.4   3.65 mm, radius for CTP   8.1  4.3mm), we strongly
        recommend to check the shape with the specially designed
        Brugg groove gauge Brugg Lifting provides a custom made
        gauge which includes the 45  (30    45  for CTP   6.5)
        opening angle as specified in our CTP   certificate. </para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.5*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,5.3*inch)

        p = Paragraph('''<para fontName=FrutigerB fontsize=10 >5.Rope tension</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.5*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,320,  6.9*inch)



        p = Paragraph('''<para fontName=FrutigerR fontsize=10  leading=13 align="justify">Even though rope tension is often measured by hand (by
        plucking the rope and judging by  feeling ) this method is
        far from accurate. Comparing spring buffers with each other
        is more precise   to a certain extent but not all elevators are
        equipped with such springs. The most reliable way of measuring
        rope tension is by measuring the tension on the rope itself.
        There are various tools for measuring tension commercially
        available. Brugg Lifting recommend our own specialist tool
        the Brugg RPM.  </para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.5*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,320,5.1*inch)

        p = Paragraph('''<para fontName=FrutigerR fontsize=10 >Furthermore check the groove surface for following defects:</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.5*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,0.4*inch,  4.85*inch)

        p = Paragraph('''<para fontName=FrutigerR fontsize=10 >Rust or abrasion of rope coating on or around sheave <br/> Wet surface (water, oil, etc.)</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.5*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,0.4*inch, 4.5*inch)

        p = Paragraph('''<para fontName=FrutigerR fontsize=10 >Finally check, if the bearings of the diverting pulleys still run smoothly, if possible.</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.5*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,0.4*inch, 4*inch)


        p = Paragraph('''<para fontName=FrutigerR fontsize=10 >Brugg groove gauge.</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.5*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,1.5*inch, 1.25*inch)

        p = Paragraph('''<para fontName=FrutigerR fontsize=10 >Rope tension device Brugg RPM</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.5*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,4.75*inch, 1.25*inch)


        p = Paragraph('''<para fontName=FrutigerR fontsize=8 >Creation date 09/2017<br/>
            Subject to changes. Nonbinding indication of measures. No warranty for printing errors or errors.<br/>
            Design, realization: www.schaefer-design.com</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,0.9*inch, 0.5*inch)

        # textobject = c.beginText()
        # textobject.setTextOrigin(0.9*inch, 0.75*inch)
        # c.setFont('FrutigerR', 6)
        # c.setFillColorRGB(0,0,0)
        # textobject.textLines('''
        # Creation date 09/2017
        # Subject to changes. Nonbinding indication of measures. No warranty for printing errors or errors.
        # Design, realization: www.schaefer-design.com
        # ''')

        c.drawText(textobject)

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("FrutigerB",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1
        if pageCount %2 == 0:
            print "dont worry"
        else:
            c.showPage()
            pageCount +=1

        c.drawImage(page12BG,0,0,width=width,height=height, mask='auto')
        textobject = c.beginText()
        textobject.setTextOrigin(250, 40)
        textobject.setFont("FrutigerB", 12)
        # textobject.setFillColorRGB(192,192,192)
        textobject.setFillColor(colors.white)
        textobject.textLines('''
                                brugglifting.com
                              ''')
        c.drawText(textobject)
        c.showPage()
        c.save()



    elif lang == 'zh':

        #page 1
        c.drawImage(page1BG,0,0,width=width,height=height,mask='auto')
        c.setFont("FrutigerB",50)
        c.setFillColor('#000000')
        c.drawString(185, 5.85*inch, "CTP")

        c.setFont("STSong-Light",20)
        c.setFillColor('#000000')
        c.drawString(280, 5.85*inch, "裹塑钢丝绳")

        c.setFont("STSong-Light",25)
        c.setFillColor(colors.white)
        c.drawString(400, 30, ". . .未来,已来!")

        c.showPage()
        pageCount +=1

        #page 2
        c.drawImage(page2BG,0,0,width=width, height=height, mask='auto')

        c.setFillColor(colors.black)
        c.setFont("STSong-Light",28)
        c.drawString(50, 8.15*inch, "服务")
        c.setFillGray(0.5)


        tp = Paragraph('<para fontName = STSong-Light fontsize=13 leftindent=13  ><b>系统供应商</b></para>',stylesN)
        tp2 = Paragraph('<para fontName = STSong-Light fontsize=10  align="Justify" leading=15>我们为您提供各种规格的电梯钢丝绳,配件以及安装工具,可以根据您的具体需求提供完整的解决方案或者定制化的零件组合或者预组装服务。</para>',stylesN)
        tpt=[[tp],[tp2]]
        tptab=Table(tpt,colWidths=5*inch)
        tptab.setStyle(TableStyle([
                                    ('LEFTPADDING',(0,1),(-1,-1),20),
                               ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,1.3*inch, 450)

        tp = Paragraph('<para fontName = STSong-Light fontsize=13 leftindent=13  ><b>定制服务</b></para>',stylesN)
        tp2 = Paragraph('<para fontName = STSong-Light fontsize=10  align="Justify" leading=15>我们可以根据您的需求提供各种型号和规格的电梯钢丝绳,配件以及安装工具;如果您没有在我们的产品目录中找到您需要的产品,或者您的电梯配置需要特殊定制,请直接联系我们,我们非常愿意为您提供咨询服务或者与您共同开发定制的解决方案。</para>',stylesN)
        tpt=[[tp],[tp2]]
        tptab=Table(tpt,colWidths=5*inch)
        tptab.setStyle(TableStyle([
                                    ('LEFTPADDING',(0,1),(-1,-1),20),
                               ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,1.3*inch, 350)


        tp = Paragraph('<para fontName = STSong-Light fontsize=13 leftindent=13  ><b>周期</b></para>',stylesN)
        tp2 = Paragraph('<para fontName = STSong-Light fontsize=10 align="Justify" leading=15 >源于我们在瑞士和中国两大生产基地,以及在全球范围内广泛的仓储网络,我们的产品可以在非常短的时间内派送到您的工厂或者指定的施工现场;如果您对具体的交货期限或者针对具体的项目信息有疑问,欢迎来电垂询。</para>',stylesN)
        tpt=[[tp],[tp2]]
        tptab=Table(tpt,colWidths=5*inch)
        tptab.setStyle(TableStyle([
                                    ('LEFTPADDING',(0,1),(-1,-1),20),
                               ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,1.3*inch, 260)


        tp = Paragraph('<para fontName = STSong-Light fontsize=13 leftindent=13  ><b>快递服务</b></para>',stylesN)
        tp2 = Paragraph('<para fontName = STSong-Light fontsize=10 align="Justify" leading=15 >遇到紧急的情况,我们可以立即为您安排货物的生产及发运</para>',stylesN)
        tpt=[[tp],[tp2]]
        tptab=Table(tpt,colWidths=5*inch)
        tptab.setStyle(TableStyle([

                                    ('LEFTPADDING',(0,1),(-1,-1),20)
                               ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,1.3*inch, 200)

        tp = Paragraph('<para fontName = STSong-Light fontsize=13 leftindent=13  ><b>国际标准</b></para>',stylesN)
        tp2 = Paragraph('<para fontName = STSong-Light fontsize=10 align="Justify" leading=15 >布鲁格通过了 ISO 9001:2015 和 ISO 14001:2015 的认证</para>',stylesN)
        tpt=[[tp],[tp2]]
        tptab=Table(tpt,colWidths=5*inch)
        tptab.setStyle(TableStyle([

                                    ('LEFTPADDING',(0,1),(-1,-1),20),
                               ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,1.3*inch, 140)

        tp = Paragraph('<para fontName = STSong-Light fontsize=13 leftindent=13  ><b>培训 / 专家研讨会</b></para>',stylesN)
        tp2 = Paragraph('<para fontName = STSong-Light fontsize=10 align="Justify" leading=15 >我们的目标是确保您的钢丝绳处于最佳的使用状态,并延长使用寿命,因此我们可以为您以及您的员工提供有关钢丝绳的基础知识和专题培训。</para>',stylesN)
        tpt=[[tp],[tp2]]
        tptab=Table(tpt,colWidths=5*inch)
        tptab.setStyle(TableStyle([

                                    ('LEFTPADDING',(0,1),(-1,-1),20),
                               ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,1.3*inch, 70)

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        #page 3

        c.drawImage(page3BG,0,0,width=width,height=height,mask='auto')


        # p = Paragraph('''<para fontName= FrutigerR fontsize=10  leading=13 align="justify">Developed as a world s first, CTP combines technological innovations into
        # a state of the art plastic coated rope specifically designed for the elevator
        # industry.  </para>''',stylesN)
        # p1 =[[p]]
        # p11 = Table(p1,colWidths=4.7*inch)
        # p11.wrapOn(c,width,height)
        # p11.drawOn(c,50,6.7*inch)

        p = Paragraph('''<para fontName= STSong-Light fontsize=10  leading=13 align="justify">布鲁格CTP,全球首个技术革新裹塑钢丝绳,并且通过认证可以使用在最小直径仅为115 mm的曳引轮上,全球已经有超过9万台的电梯使用布鲁格CTP裹塑钢丝绳;通过在实验室的模拟测试以及现场工地的使用经验,证明CTP可以满足电梯对于钢丝绳使用的高效能的要求。 </para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=4.7*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,50,5.9*inch)


        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)
        t.drawOn(c, 7.75*inch,0.2*inch)

        c.setFillColor(colors.black)
        c.setFont("FrutigerB",10)
        c.drawString(580, 0.15*inch, "3")

        c.showPage()
        pageCount +=1

        #page 4
        for template in ctpObj:
            prodfield = ProductField.objects.filter(template = template.pk)
            # printprodfield
            prod = Product.objects.filter(template = template.pk)
            # printprod



            if pageCount%2 == 1:
                if template.catalogBG1:
                    background = template.catalogBG1.path
                else:
                    background = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/ctpCatalog',"page4.jpg")

                c.drawImage(background,0,0,width=width, height=height, mask = 'auto')
                name = Paragraph('<para fontName = FrutigerB fontSize=30>%s</para>'%(template.name), stylesN)
                nd =[[name]]
                w = pdfmetrics.stringWidth(template.name, "FrutigerB", 30)
                # printw, "text width "
                ndt = Table(nd)
                w1,h1 = ndt.wrapOn(c, width,height)
                width2 = width - w -50
                ndt.drawOn(c, width2,570)



            else:
                if template.catalogBG2:
                    background = template.catalogBG2.path
                else:
                    background = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/ctpCatalog',"page4.jpg")
                c.drawImage(background,0,0,width=width, height=height, mask = 'auto')
                name = Paragraph('<para fontName = FrutigerB fontSize=30>%s</para>'%(template.name), stylesN)
                nd =[[name]]
                w = pdfmetrics.stringWidth(template.name, "FrutigerB", 30)
                # printw, "text width "
                ndt = Table(nd)
                w1,h1 = ndt.wrapOn(c, width,height)
                width2 = 50
                ndt.drawOn(c, width2,570)


            name = Paragraph('<para fontName = FrutigerR fontSize=15>%s</para>'%("COATED TRANSMISSION PRODUCTS"), styles['Normal'])
            nd =[[name]]
            # printw, "text width "
            ndt = Table(nd)
            w1,h1 = ndt.wrapOn(c, width,height)

            ndt.drawOn(c, 200,548)

            c.drawImage(template.defaultImage.path,50,400,width=1.4*inch,height=1.4*inch, mask='auto')

            height2 = height - 350
            height2 = htmlRMLCanvvas(template.rteData2_ch,c,4.5*inch,200,height2,styles['Normal'],colors.black,lang)
            # para2 =  addBRInRichText(template.rteData1_en)
            # para22 = Paragraph('<para fontName = FrutigerR>%s</para>'%(para2), styles['Normal'])
            # tab1 = [[para22]]
            # ps = Table(tab1,colWidths=4.5*inch)
            # w2, h2 = ps.wrapOn(c, width,height)
            # height2 = height - h2 - 350
            #
            #
            # ps.drawOn(c, 200, height2)

            height2 = height2 - 50
            height3 = height2 + 15
            height4 = height2
            height5 = height2 - 30
            c.setFillColor('#81B3EE')
            c.setStrokeColor(colors.white)
            c.rect(4*inch,height2,0.6*inch,0.6*inch, fill=1)
            c.setFont("Helvetica-Bold", 7)
            c.setFillColor(colors.black)
            k = json.loads(template.keyword1)
            k11 =[[k]]
            r11 = Table(k11,colWidths=3.6*inch,rowHeights=4*mm)
            c.setFont("Helvetica", 5)

            para101 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%(k["value1"]), styles['Normal'])
            desc101 = [[para101]]
            r101 = Table(desc101,colWidths=0.6*inch,rowHeights=1*mm)
            w, h = r101.wrapOn(c, width,height)
            r101.drawOn(c, 4*inch, height3)

            para102 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%("N/mm2"), styles['Normal'])
            desc102 = [[para102]]
            r102 = Table(desc102,colWidths=0.6*inch,rowHeights=1*mm)
            r102.wrapOn(c, width,height)
            r102.drawOn(c, 4*inch, height4)

            para103 = Paragraph('<para align="center" fontName = FrutigerR fontSize=7 >%s</para>'%("E-Module"), styles['Normal'])
            desc103 = [[para103]]
            r103 = Table(desc103,colWidths=0.6*inch,rowHeights=1*mm)
            r103.wrapOn(c, width,height)
            r103.drawOn(c, 4*inch, height5)


            c.setFillColor('#9BC7EC')
            c.rect(5*inch,height2,0.6*inch,0.6*inch, fill=1)
            c.setFont("Helvetica-Bold", 7)
            c.setFillColor(colors.black)
            k1 = json.loads(template.keyword2)

            k12 =[[k1]]

            r12 = Table(k12,colWidths=5*inch,rowHeights=10*mm)

            para201 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%(k1["value1"]), styles['Normal'])
            desc201 = [[para201]]
            r201 = Table(desc201,colWidths=0.6*inch)
            w,h = r201.wrapOn(c, width,height)

            r201.drawOn(c, 5*inch, height3)

            para202 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%("%"), styles['Normal'])
            desc202 = [[para202]]
            r202 = Table(desc202,colWidths=0.6*inch,rowHeights=1*mm)
            r202.wrapOn(c, width,height)
            r202.drawOn(c, 5*inch, height4)

            para203 = Paragraph('<para align="center" fontName = FrutigerR fontSize=7 >%s</para>'%("Elastic<br/>Elongation"), styles['Normal'])
            desc203 = [[para203]]
            r203 = Table(desc203,colWidths=0.65*inch,rowHeights=1*mm)
            r203.wrapOn(c, width,height)
            r203.drawOn(c, 5*inch, height5 )


            c.setFillColor(	'#BBD5F0')
            c.setStrokeColor(colors.white)

            c.rect(6*inch,height2,0.6*inch,0.6*inch, fill=1)
            c.setFont("Helvetica-Bold", 7)
            c.setFillColor(colors.black)
            k2 = json.loads(template.keyword3)

            k13 = [[k2]]

            r13 = Table(k13,colWidths=5*inch,rowHeights=10*mm)

            para301 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%(k2["value1"]), styles['Normal'])
            desc301 = [[para301]]
            r301 = Table(desc301,colWidths=0.6*inch,rowHeights=1*mm)
            r301.wrapOn(c, width,height)
            r301.drawOn(c, 6*inch, height3)

            para302 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%("%"), styles['Normal'])
            desc302 = [[para302]]
            r302 = Table(desc302,colWidths=0.6*inch,rowHeights=1*mm)
            r302.wrapOn(c, width,height)
            r302.drawOn(c, 6*inch, height4)

            para303 = Paragraph('<para align="center" fontName = FrutigerR fontSize=7 >%s</para>'%("Permanent<br/>Elongation"), styles['Normal'])
            desc303 = [[para303]]
            r303 = Table(desc303,colWidths=0.7*inch,rowHeights=1*mm)
            r303.wrapOn(c, width,height)
            r303.drawOn(c, 6*inch, height5)


            c.setFillColor('#D5E5F5')
            c.setStrokeColor(colors.white)
            c.rect(7*inch,height2,0.6*inch,0.6*inch, fill=1)
            c.setFont("Helvetica-Bold", 7)
            c.setFillColor(colors.black)
            k3 = json.loads(template.keyword4)
            k14 = [[k3]]
            r14 = Table(k14,colWidths=5*inch,rowHeights=10*mm)

            para401 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%(k3["value1"]), styles['Normal'])
            desc401 = [[para401]]
            r401 = Table(desc401,colWidths=0.6*inch,rowHeights=1*mm)
            r401.wrapOn(c, width,height)
            r401.drawOn(c, 7*inch, height3)

            para402 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%("m"), styles['Normal'])
            desc402 = [[para402]]
            r402 = Table(desc402,colWidths=0.6*inch,rowHeights=1*mm)
            r402.wrapOn(c, width,height)
            r402.drawOn(c, 7*inch, height4)

            para403 = Paragraph('<para align="center" fontName = FrutigerR fontSize=7 >%s</para>'%("Lifting<br/>Height"), styles['Normal'])
            desc403 = [[para403]]
            r403 = Table(desc403,colWidths=0.6*inch,rowHeights=1*mm)
            r403.wrapOn(c, width,height)
            r403.drawOn(c, 7*inch, height5)


            height2 = height5

            data = []
            # data2 = []
            dataHeading = ['Item Number']
            dataHeading2 = ['']
            list1 = []
            list2 = []
            for j in prodfield:
                # printprodfield
                if j.inPdf ==True:

                    # printj.name,'kkkkkkkkkkkkk'
                    try:
                        name1, name2 = j.name.split('(')
                        # printname2[:-1]
                        name2 = ''+name2[:-1]
                        # printname2
                    except:
                        name1 = j.name
                        name2 = ''

                    # printname1, ' ' , name2

                    list1.append(name1)
                    list2.append(name2)
            for a in list1:
                dataHeading.append(a)
            for b in list2:
                dataHeading2.append(b)


            for i in prod:
                appendlist = [i.itemNumber]
                for j in prodfield:
                    prodQty = ProductValueMap.objects.filter( field = j.pk,product = i.pk)
                    for k in prodQty:
                        if j.inPdf ==True:
                            if j.type=='Char':
                                appendlist.append(k.char)
                            if j.type=='float':
                                appendlist.append(k.fValue)
                            if j.type=='Integer':
                                appendlist.append(k.iValue)
                            if j.type=='Boolean':
                                appendlist.append(k.bool)
                data.append(appendlist)

            height2 = height2-40
            leftHeight = height2-100
            numberRows = int(leftHeight/20)
            # printheight2, leftHeight, numberRows, "number of rows"

            data.insert(0,dataHeading)
            data.insert(1,dataHeading2)

            if len(data)<= numberRows:
                    t5 = Table(data,rowHeights=[20]*len(data))
                    t5.setStyle(TableStyle([
                                         ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                                         ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                                         ('FONTSIZE', (0, 0), (-1, -1), 7),
                                         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                         ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                                         ]))
                    w5, h5 = t5.wrapOn(c, width, height)
                    height2 = height2 - h5
                    t5.drawOn(c, 200, height2)


                    para2 = Paragraph('<para fontName = STSong-Light fontSize=6 >%s</para>'%(template.disclaimer_ch), styles['Normal'])
                    tab = [[para2]]
                    r = Table(tab,colWidths=3.25*inch)
                    w,h1 = r.wrapOn(c, width,height)
                    height2 = height2 - h1
                    r.drawOn(c, 200, height2)

                    gm934 = Paragraph('<para></para>',stylesN)
                    gmn934 = Paragraph('<para></para>',stylesN)

                    data =  [[gm934,gmn934]]

                    t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
                    t.setStyle(TableStyle([
                                        ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                                         ]))
                    t.wrapOn(c,width, height)

                    c.setFillColor(colors.black)
                    c.setFont("Helvetica-Bold",10)
                    if pageCount%2==0:
                        t.drawOn(c, -3*inch,0.2*inch)
                        c.drawString(20, 0.15*inch, str(pageCount))
                    else:
                        t.drawOn(c, width-35,0.2*inch)
                        c.drawString(width-30, 0.15*inch, str(pageCount))

                    c.showPage()
                    pageCount +=1
            else:
                # print"in else ctp extra page requiresss"
                data1 = data[:numberRows-1]

                data2 = data[numberRows:-1]

                t5 = Table(data1,rowHeights=[20]*len(data1))
                t5.setStyle(TableStyle([
                                     ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                                     ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                                     ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                                     ('FONTSIZE', (0, 0), (-1, -1), 7),
                                     ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                     ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                                     ]))
                w5, h5 = t5.wrapOn(c, width, height)
                height2 = height2 - h5
                t5.drawOn(c, 200, height2)



                para2 = Paragraph('<para fontName = STSong-Light fontSize=6 >%s</para>'%(template.disclaimer_ch), styles['Normal'])
                tab = [[para2]]
                r = Table(tab,colWidths=3.25*inch)
                w,h1 = r.wrapOn(c, width,height)
                height2 = height2 - h1
                r.drawOn(c, 200, height2)

                gm934 = Paragraph('<para></para>',stylesN)
                gmn934 = Paragraph('<para></para>',stylesN)

                data =  [[gm934,gmn934]]

                t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
                t.setStyle(TableStyle([
                                    ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                                     ]))
                t.wrapOn(c,width, height)


                c.setFillColor(colors.black)
                c.setFont("Helvetica-Bold",10)
                if pageCount%2==0:
                    t.drawOn(c, -3*inch,0.2*inch)
                    c.drawString(20, 0.15*inch, str(pageCount))
                else:
                    t.drawOn(c, width-35,0.2*inch)
                    c.drawString(width-30, 0.15*inch, str(pageCount))

                c.showPage()
                pageCount +=1
                maxNumberItems = 15

                index = float(len(data2))/maxNumberItems

                index = int(math.ceil(index))

                for i in range(index):
                    if i == index-1:
                        data1 = data2[maxNumberItems*i:-1]
                        data1.insert(0,dataHeading)
                        data1.insert(1,dataHeading2)

                    else:
                        data1 = data2[maxNumberItems*i:maxNumberItems*(i+1)-1]
                        data1.insert(0,dataHeading)
                        data1.insert(1,dataHeading2)

                    pageCount = addCTPPage(c, data1,template,stylesN,pageCount,lang)

        # new page

        c.drawImage(page5BG, 0,0, width=width, height=height, mask='auto')
        textobject = c.beginText()
        textobject.setTextOrigin(0.75*inch, 7*inch)
        textobject.setFont("STSong-Light", 10)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                                CTP ® ,全球一流的技术革新产品,满足对于钢丝绳性能的最高要求,这款高端产品在能效方面的表现无与伦比。''')
        c.drawText(textobject)

        textobject = c.beginText()
        textobject.setTextOrigin(0.75*inch, 6.05*inch)
        textobject.setFont("STSong-Light", 10)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            降低成本高达40%。
                            ''')
        c.drawText(textobject)
        c.drawText(textobject)
        textobject = c.beginText()
        textobject.setTextOrigin(0.75*inch, 5.85*inch)
        textobject.setFont("STSong-Light", 10)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            小直径钢丝绳和小直径曳引轮将降低投资成本和运营成本。
                            ''')
        c.drawText(textobject)
        textobject = c.beginText()
        textobject.setTextOrigin(0.75*inch, 5.55*inch)
        textobject.setFont("STSong-Light", 10)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            降低维护成本高达100%。
                            ''')
        c.drawText(textobject)
        c.drawText(textobject)
        textobject = c.beginText()
        textobject.setTextOrigin(0.75*inch, 5.35*inch)
        textobject.setFont("STSong-Light", 10)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            小直径钢丝绳和小直径曳引轮将降低投资成本和运营成本。
                            ''')
        c.drawText(textobject)
        textobject = c.beginText()
        textobject.setTextOrigin(0.75*inch, 5.1*inch)
        textobject.setFont("STSong-Light", 10)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            运行舒适度显著提高。
                            ''')
        c.drawText(textobject)
        c.drawText(textobject)
        textobject = c.beginText()
        textobject.setTextOrigin(0.75*inch, 4.9*inch)
        textobject.setFont("STSong-Light", 10)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            聚合物涂层可以消除或吸收振动,这有助于使电梯运行更加平稳。
                            ''')
        c.drawText(textobject)
        textobject = c.beginText()
        textobject.setTextOrigin(0.75*inch, 4.7*inch)
        textobject.setFont("STSong-Light", 10)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            使用寿命显著提高。
                            ''')
        c.drawText(textobject)
        c.drawText(textobject)
        textobject = c.beginText()
        textobject.setTextOrigin(0.75*inch, 4.7*inch)
        textobject.setFont("STSong-Light", 10)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            由于曳引机的轮槽与电梯钢丝绳不易受磨损,钢丝绳更换的频率和相关的成本将大幅降低
                            ''')

        # c.drawText(textobject1)
        c.setFont("STSong-Light",9)


        # c.drawImage(l1,130,170,width=2.5*inch,height=2.15*inch,mask='auto')
        c.setFont("STSong-Light", 5)

        c.drawString(2.15*inch, 2.25*inch, "适用于绳径6.5的轮槽")

        # c.drawImage(l2,300,170, width=2.5*inch,height=2.15*inch,mask='auto')
        c.drawString(4*inch, 2.25*inch, "适用于绳径8.1的轮槽")

        textobject = c.beginText()
        textobject.setTextOrigin(0.75*inch, 1.75*inch)
        textobject.setFont("STSong-Light", 8)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            曳引轮数据
                            ''')
        c.drawText(textobject)


        data = [
            ['物料号码', '绳径', '金属直径',  '摩擦系数' , "钢丝绳运行","曳引轮直径","曳引轮材质","轮槽形状","导向轮材质"],
           ['', '', '',  '' , "最大速度","","","",""],
           ['',   'mm',  'mm','','m/s'   ,'mm'   '',         'ø mm',     ' ',     ],
           ['10982',   '6.5', '4,9','0,6-0,3','3,5*','>115','C45,c45 gehartet,42CrMo4','3,4-3,65','Stahl,Gusseisen,PA,PU.'],
           ['73106',   '6.5', '4,9','0,6-0,3','3,5*','>115','C45,c45 gehartet,42CrMo4','3,4-3,65','Stahl,Gusseisen,PA,PU.'],


           ]

        t5 = Table(data, colWidths=[0.75* cm, 1* cm, 1 * cm,
                                    2.5* cm, 2.5* cm,2.5* cm,2.5* cm,2.5* cm, ],rowHeights=5.5*mm)
        t5.setStyle(TableStyle([
                             ('LINEABOVE',(0,2),(-1,-1),0.25,colors.black),
                             ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                            ('FONTSIZE', (0, 0), (-1, -1), 5),

                            ('FONTNAME', (0, 0), (1,0), "STSong-Light"),
                            ('FONTNAME', (2, 0), (3,0), "STSong-Light"),
                            ('FONTNAME', (4,0), (5,0), "STSong-Light"),
                            ('FONTNAME', (6, 0), (7,0), "STSong-Light"),
                            ('FONTNAME', (0,0),(8, 0), "STSong-Light"),
                            ('FONTNAME', (0,0),(0, 1), "STSong-Light"),
                            ('FONTNAME', (1,0),(3,1), "STSong-Light"),
                            ('FONTNAME', (4,1),(6,1), "STSong-Light"),
                            ('FONTNAME', (0,0),(8,1), "STSong-Light"),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
                            ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                            # ('ALIGN', (1, 0), (1, 7), 'CENTER'),
                            # ('ALIGN', (2, 0), (-1, 7), 'CENTER'),
                            # ('ALIGN', (3, 0), (-1, 7), 'LEFT'),
                            # ('ALIGN', (4, 0), (-1, 7), 'LEFT'),
                            # ('ALIGN', (5, 0), (-1, 7), 'CENTER'),
                            # ('VALIGN', (5, 0), (-1, 7), 'BOTTOM'),
                            # ('LEFTPADDING', (0, 0), (-1, -1), -20),
                            #  ('LEFTPADDING', (1, 0), (-1, -1),10),
                            #  ('LEFTPADDING', (2, 0), (-1, -1), -30),
                            #  ('LEFTPADDING', (3, 0), (-1, -1), -30),
                            #  ('LEFTPADDING', (5, 0), (-1, -1), -30),
                            # ('LEFTPADDING', (4, 0), (-1, 9), -30),
                            #  ('LEFTPADDING', (5, 0), (-1, 9), -70),
                            ('BACKGROUND', (1,0), (1, 1), '#DCDCDC'),
                            ('BACKGROUND', (1,2), (1, 3), '#DCDCDC'),
                            ('BACKGROUND', (1,4), (1, 5), '#DCDCDC'),
                            # ('BACKGROUND', (1,6), (1, 7), '#DCDCDC'),
                             ]))

        t5.wrapOn(c, 20, 170)
        t5.drawOn(c, 0.75*inch,0.6*inch)


        textobject1 = c.beginText()
        textobject1.setTextOrigin(0.72*inch, 0.49*inch)
        c.setFillColor(colors.black)
        textobject1.setFont("STSong-Light", 5)
        textobject1.textLines('''* 如超过目前规定速度,需要另做测试;
                                   ''')
        c.drawText(textobject1)

        textobject1 = c.beginText()
        textobject1.setTextOrigin(0.75*inch, 0.38*inch)
        c.setFillColor(colors.black)
        textobject1.setFont("STSong-Light", 5)
        textobject1.textLines('''公差标准参照ISO 2768-1 M 级(中级)
                                   ''')
        c.drawText(textobject1)

        textobject1 = c.beginText()
        textobject1.setTextOrigin(0.8*inch, 0.27*inch)
        c.setFillColor(colors.black)
        textobject1.setFont("STSong-Light", 5)
        textobject1.textLines(''' CTP ® 裹塑钢丝绳认证的曳引轮的具体技术参数如上所示''')
        c.drawText(textobject1)


        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)

        c.setFillColor(colors.black)
        c.setFont("STSong-Light",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1


        #page 6
        c.drawImage(page6BG, 0,0, width=width, height=height, mask='auto')
        c.setFont('FrutigerB', 25)
        c.drawString(50, 7.8*inch, "APAG")

        c.setFont('STSong-Light', 13)
        c.drawString(125, 7.8*inch, "螺纹锻造绳头")


        textobject = c.beginText()
        textobject.setTextOrigin(3.2*inch, 6.5*inch)
        textobject.setFont("STSong-Light", 12)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            产品数据''')
        c.drawText(textobject)
        # textobject = c.beginText()
        # textobject.setTextOrigin(3*inch, 6.25*inch)
        # textobject.setFont("STSong-Light", 9)
        # lyrics = ['·APAG绳头获得TÜV认证,测试依据是 TRA / EN81;',
        #           '· APAG绳头可承受曳引绳80%的最小破断载荷;',
        #
        #           ]
        # for line in lyrics:
        #     textobject.textLine(". %s" %(line))
        # c.drawText(textobject)


        list = '''<ul>
                    <li> APAG绳头获得T V认证,测试依据是 TRA / EN81;</li>
                    <li> APAG绳头可承受曳引绳80%的最小破断载荷;</li>
                 </ul>
                '''
        height2 = htmlRMLCanvvas(list,c,3.3*inch,3*inch, 6.35*inch,styles['Normal'],colors.black,lang)


        textobject = c.beginText()
        textobject.setTextOrigin(3.2*inch, 5.7*inch)
        textobject.setFont("STSong-Light", 12)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            	优点''')
        c.drawText(textobject)


        # textobject = c.beginText()
        # textobject.setTextOrigin(3*inch, 5.475*inch)
        # textobject.setFont("STSong-Light", 9)
        # lyrics = [' 简单,快速,安全',
        #           ' 简单,快速,安全',
        #           ' 缩短了安装时间',
        #           ' 无需特殊工具 ',
        #           ' 紧凑型设计使得钢丝绳安装紧密并且运行平稳',
        #           ' 轻松实现防止钢绳安装时的旋转 ',
        #           ' 尾端设计有导向孔',
        #           ' 可实现静音施工',
        #           ]
        #
        # for line in lyrics:
        #     textobject.textLine(". %s" %(line))
        #
        # c.drawText(textobject)

        list = '''<ul>
                    <li> 简单,快速,安全</li>
                    <li> 简单,快速,安全</li>
                    <li> 缩短了安装时间</li>
                    <li> 无需特殊工具</li>
                    <li> 紧凑型设计使得钢丝绳安装紧密并且运行平稳</li>
                    <li> 轻松实现防止钢绳安装时的旋转 </li>
                    <li> 尾端设计有导向孔</li>
                    <li> 可实现静音施工 </li>
                 </ul>
                '''
        height2 = htmlRMLCanvvas(list,c,3.3*inch,3*inch, 5.475*inch,styles['Normal'],colors.black,lang)

        c.setFont("STSong-Light", 7)

        c.drawString(3.2*inch, 3.1*inch, "For use with CTP  6.5 mm")

        data = [
           ['项目', 'd1', 'd2',  'd3' , "d4","L1","L2","L3","L4"],
           ['编号',   '',  '','',''      'mm',         '',     ' ',     ],
           ['10209',   'M 10', '13','9','7','240','150','66.0','16.6'],
           ]

        t5 = Table(data, colWidths=[1.25* cm, 1.25* cm, 1.25 * cm,
                                    1.25* cm, 1.25* cm,1.25* cm,1.25* cm,1.25* cm, ],rowHeights=5*mm)
        t5.setStyle(TableStyle([
                             ('LINEABOVE',(0,2),(-1,-1),0.25,colors.black),
                             ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                             ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                            ('FONTSIZE', (0, 0), (-1, -1), 5),
                             ('FONTNAME', (0, 0), (1,0), "STSong-Light"),
                             ('FONTNAME', (2, 0), (3,0), "STSong-Light"),
                             ('FONTNAME', (4,0), (5,0), "STSong-Light"),
                             ('FONTNAME', (6, 0), (7,0), "STSong-Light"),
                            ('FONTNAME', (0,0),(8, 0), "STSong-Light"),
                            ('FONTNAME', (0,0),(0, 1), "STSong-Light"),
                            # ('FONTNAME', (0,0),(0, 4), "STSong-Light"),
                            # ('BACKGROUND', (1,2), (1, 3), '#DCDCDC'),
                            # ('BACKGROUND', (1,4), (1, 5), '#DCDCDC'),
                             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
                            ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),

                             ]))

        t5.wrapOn(c, 30, 300)
        t5.drawOn(c, 3.2*inch,2.25*inch)
        c.setFont("STSong-Light", 7)
        c.drawString(3.2*inch, 1.7*inch, "此绳头适用CTP ® 8.1毫米裹塑钢丝绳")

        data = [

           ['项目', 'd1', 'd2',  'd3' , "d4","L1","L2","L3","L4"],
           ['编号',   '',  '','',''      'mm',         '',     ' ',     ],
           ['10113',   'M 10', '13','9','7','240','150','66.0','16.6'],


           ]

        t5 = Table(data, colWidths=[1.25* cm, 1.25* cm, 1.25 * cm,
                                    1.25* cm, 1.25* cm,1.25* cm,1.25* cm,1.25* cm, ],rowHeights=5*mm)
        t5.setStyle(TableStyle([
                             ('LINEABOVE',(0,2),(-1,-1),0.25,colors.black),
                             ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                             ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                            ('FONTSIZE', (0, 0), (-1, -1), 5),
                             ('FONTNAME', (0, 0), (1,0), "STSong-Light"),
                             ('FONTNAME', (2, 0), (3,0), "STSong-Light"),
                             ('FONTNAME', (4,0), (5,0), "STSong-Light"),
                             ('FONTNAME', (6, 0), (7,0), "STSong-Light"),
                            ('FONTNAME', (0,0),(8, 0), "STSong-Light"),
                            ('FONTNAME', (0,0),(0, 1), "STSong-Light"),
                             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
                            ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),

                             ]))

        t5.wrapOn(c, 30, 300)
        t5.drawOn(c, 3.2*inch,0.9*inch)


        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("STSong-Light",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1


        #page 7

        c.drawImage(page7BG, 0,0, width=width, height=height, mask='auto')

        c.setFont('STSong-Light', 18.5)
        c.drawString(50, 7.8*inch, "对称楔型连接绳头")

        c.setFont('FrutigerB', 13)
        c.drawString(210, 7.8*inch, "[EN 13411-7]")


        textobject = c.beginText()
        textobject.setTextOrigin(4.5*inch, 6.65*inch)
        textobject.setFont("STSong-Light", 12)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            品参数''')
        c.drawText(textobject)
        textobject = c.beginText()
        textobject.setTextOrigin(4.4*inch, 6.375*inch)
        textobject.setFont("STSong-Light", 9)
        lyrics = ['焊接楔形绳头(镀锌)',
                  '包括楔形绳头、螺栓和安全销(已组装)',
                  '楔形绳头传输曳引绳或限速器绳80%的最小破断载荷',
                  '活节螺栓焊接, 镀锌',
                  '活节螺栓与楔型绳头传输的力可达到钢丝绳最小破断载荷的80%',
                  '安装和操作规范的说明见13411-7',
                  ]

        for line in lyrics:
            textobject.textLine("· %s" %(line))

        c.drawText(textobject)
        textobject = c.beginText()
        textobject.setTextOrigin(4.5*inch, 4.65*inch)
        textobject.setFont("STSong-Light", 12)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            优点''')
        c.drawText(textobject)
        textobject = c.beginText()
        textobject.setTextOrigin(4.4*inch, 4.4*inch)
        textobject.setFont("STSong-Light", 9)
        lyrics = [' 在工地上就能进行简单安全的组装 ',
                  ' 可单独安装弹簧、缓冲垫和其它配件',
        ]

        for line in lyrics:
            textobject.textLine(". %s" %(line))
        c.drawText(textobject)

        c.setFont("STSong-Light", 7)
        c.drawString(4.5*inch, 3.5*inch, "此绳头适用CTP ® 6.5毫米裹塑钢丝绳")

        data = [

           ['项目','', '绳 ø', 'd',  'd1',"L1","L2","L3"],
           ['编号',   '','mm',  '','',''      '',         '',     ' ',     ],
           ['64109',  'A', '5,0-6,5','M 10', '','265','180'],
           ['64115',    'D', '5,0-6,5','M 10', '23','265','180','85,5']
           ]

        t5 = Table(data, colWidths=[1* cm, 1* cm, 1 * cm,
                                    1* cm, 1* cm,1* cm,1* cm,1* cm, ],rowHeights=5*mm)
        t5.setStyle(TableStyle([
                             ('LINEABOVE',(0,2),(-1,-1),0.25,colors.black),
                             ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                             ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                            ('FONTSIZE', (0, 0), (-1, -1), 5),
                             ('FONTNAME', (0, 0), (1,0), "STSong-Light"),
                             ('FONTNAME', (0, 0), (0,1), "STSong-Light"),
                             ('FONTNAME', (2, 0), (3,0), "STSong-Light"),
                             ('FONTNAME', (4,0), (5,0), "STSong-Light"),
                             ('FONTNAME', (6, 0), (7,0), "STSong-Light"),
                             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
                            ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                            ('BACKGROUND', (2,0),(2, 5), '#DCDCDC')
                             ]))

        t5.wrapOn(c, 30, 300)
        t5.drawOn(c, 4.5*inch,2.4*inch)
        textobject1 = c.beginText()
        textobject1.setTextOrigin(4.5*inch, 2.3*inch)
        c.setFillColor(colors.black)
        textobject1.setFont("STSong-Light", 6)
        textobject1.textLines(''' 其它尺寸要求
                                  如有其他尺寸要求,你可以在我们的主样册中找到所有组合的项目编号  ''')
        c.drawText(textobject1)
        c.setFont("STSong-Light", 7)

        c.drawString(4.5*inch, 1.9*inch, "此绳头适用CTP ® 8.1毫米裹塑钢丝绳")

        data = [

           ['项目','', '绳 ø', 'd',  'd1',"L1","L2","L3"],
           ['编号',   '','mm',  '','',''      '',         '',     ' ',     ],
           ['64109',  'A', '5,0-6,5','M 10', '','265','180'],
           ['64115',    'D', '5,0-6,5','M 10', '23','265','180','85,5']
           ]

        t5 = Table(data, colWidths=[1* cm, 1* cm, 1 * cm,
                                    1* cm, 1* cm,1* cm,1* cm,1* cm, ],rowHeights=5*mm)
        t5.setStyle(TableStyle([
                             ('LINEABOVE',(0,2),(-1,-1),0.25,colors.black),
                             ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                             ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                            ('FONTSIZE', (0, 0), (-1, -1), 5),
                             ('FONTNAME', (0, 0), (1,0), "STSong-Light"),
                             ('FONTNAME', (2, 0), (3,0), "STSong-Light"),
                             ('FONTNAME', (0, 0), (0,1), "STSong-Light"),
                             ('FONTNAME', (4,0), (5,0), "STSong-Light"),
                             ('FONTNAME', (6, 0), (7,0), "STSong-Light"),
                             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
                            ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                            ('BACKGROUND', (2,0),(2, 5), '#DCDCDC'),
                             ]))

        t5.wrapOn(c, 30, 300)
        t5.drawOn(c, 4.5*inch,0.8*inch)

        textobject1 = c.beginText()
        textobject1.setTextOrigin(4.5*inch,0.7*inch)
        c.setFillColor(colors.black)
        textobject1.setFont("STSong-Light", 5)
        textobject1.textLines(''' 其它尺寸要求
                                  如有其他尺寸要求,你可以在我们的主样册中找到所有组合的项目编号 ''')
        c.drawText(textobject1)

        d = c.beginPath()
        d.rect(-20, 7.25*inch, 10*inch, 0.6*inch)
        d.rect(700, 7.25*inch, 12.5*inch, 0.2*inch)
        c.clipPath (d, stroke=0)
        # c.linearGradient(100*mm,200*mm,100*mm,60*mm, ('#996515','#DAA520','#996515'),extend=False)
        c.setFont("FrutigerB", 10)
        c.drawString(90,450, "Anpress-Ausssengewinden")
        c.setFont("FrutigerB", 18)
        # c.drawString(30,535, "APAG")
        c.setFont("FrutigerB", 18)
        c.drawString(400,450, "SEILSCHLOSS")
        c.setFont("FrutigerB", 10)
        c.drawString(530,450, "symmetrisch [EN-13411-7]")


        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("FrutigerB",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        #page 8
        chineseimg = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/ctpCatalog','chineesp8a.png')
        # chineseimg = "chineesp8a.png"

        c.drawImage(page8BG,0,0,width=width,height=height, mask='auto')

        c.drawImage(chineseimg,30,0.725*inch,width=8*inch,height= 3*inch, mask='auto')

        c.setFont('STSong-Light', 23)
        c.drawString(50, 7.8*inch, "检验手册")

        c.setFont('FrutigerB', 23)
        c.drawString(150, 7.8*inch, "CTP")

        p = Paragraph('''<para fontName= STSong-Light fontsize=10  leading=13 align="justify">这份文件主要用于指导CTP ® 裹塑钢丝绳在施工现场的检验,它涵盖了该钢丝绳官方的检验标准,以及在运行的电梯系统中针对CTP ® 裹塑钢丝绳具体细节的检验,这无疑对钢丝绳的寿命是至关重要的。 </para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,6.25*inch)

        # textobject = c.beginText()
        # textobject.setTextOrigin(0.5*inch,  5.5*inch)
        # c.setFont('STSong-Light', 11)
        # c.setFillColorRGB(0,0,0)
        # textobject.textLines('''
        # 1. CTP ® 裹塑钢丝绳的判废标准''')
        # c.drawText(textobject)
        #
        p = Paragraph('''<para fontName= STSong-Light fontsize=10  leading=13 align="justify">1. CTP ® 裹塑钢丝绳的判废标准'</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,5.6*inch)

        p = Paragraph('''<para fontName= STSong-Light fontsize=11  leading=13 align="justify">布鲁格正在使用一个简单的替换件标准,因此这种鉴定的方法是基于使用的程度</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,5.25*inch)


        p = Paragraph('''<para fontName= STSong-Light fontsize=10  leading=13 align="justify">这个判废条件,构成了CTP ® 裹塑钢丝绳认证的一部分(由LIFTINSTITUUT颁发):</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,4.6*inch)


        p = Paragraph('''<para fontName= STSong-Light fontsize=10  leading=13 align="justify"> 最大运行次数的计算在第二章“条件”中所述如下:
·  定义的最大运行次数除以钢丝绳通过的滑轮的数量。</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,4.2*inch)


        p = Paragraph('''<para fontName= STSong-Light fontsize=10  leading=10 align="justify">电梯钢丝绳在井道中是未受损的,在整个使用期间,钢丝绳不会发生颜色的改变,依然保持深黑色。</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=2*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,440,6.25*inch)


        p = Paragraph('''<para fontName= STSong-Light fontsize=10  leading=10 align="justify">在检查过程中通常要看钢丝绳是否有任何异常磨损或损坏以下表显示出了可能发生的钢丝绳的五个典型问题,在这种情况下电梯维保公司必须要采取行动。</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,325,5.4*inch)

        p = Paragraph('''<para fontName= STSong-Light fontsize=10  leading=10 align="justify">(1)每个运行方向的改变被电梯的计数系统当作一次运行。注:不要将电梯的一次启动误当作一次运行。</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,325,4.75*inch)


        p = Paragraph('''<para fontName= STSong-Light fontsize=10  leading=10 align="justify">(2) 图所示的不正常的磨损或损坏可能是由于超载、每根绳的张力不均、严重上震动、扭转过度或钢丝绳安装不到位等造成的。说明中提到的最大允许的断丝数是依据(UNE-EN, ISO, DIN)标准通过测试验证得出。</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,325,4.05*inch)


        # p1 = ['Beschreibung der Kunststoffummantelung']
        #
        #
        # c.setFillColor('#EEE8AA')
        # c.rect(18, 0.68*inch, 8*inch, 2.4*inch,stroke=0,fill=1)
        #
        # c.drawString(30,150,'Ablegekriterien')


        # textobject = c.beginText()
        # textobject.setTextOrigin(0.4*inch,  2.9*inch)
        # c.setFont('FrutigerB', 9)
        # c.setFillColorRGB(0,0,0)
        # textobject.textLines('''
        # Ablegekriterien''')
        # c.drawText(textobject)
        #
        #
        # # Headers
        # hdescrpcion = Paragraph('''<para align = "RIGHT">|</para>''', stylesN)
        # hpartida = Paragraph('<para fontsize=7 align = "CENTER"><b>A</b></para>', stylesN)
        # h1 = Paragraph('''<para align = "LEFT">|</para>''', stylesN)
        # hcandidad = Paragraph('<para fontsize=7 align = "CENTER" leftindent = -5 align="LEFT"><b>B</b></para>', stylesN)
        # h2 = Paragraph('''|''', stylesN)
        # hprecio_unitario = Paragraph('<para fontsize=7 leftindent = -40 align="LEFT"><b>C</b></para>', stylesN)
        # h3 = Paragraph('''<para  leftindent = -130 align = "CENTER">|</para>''', stylesN)
        # hprecio_total = Paragraph('<para fontsize=7 align="CENTER" leftindent = -140 align="CENTER"><b>D</b></para>', stylesN)
        # h4 = Paragraph('''<para  align = "LEFT" leftindent = -70>|</para>''', stylesN)
        # hprecio_empty1 = Paragraph(''+''' ''', stylesN)
        # hprecio_empty2 = Paragraph(''+''' ''', stylesN)
        #
        #
        # descrpcion = Paragraph('<para fontsize=5><b>Problem</b></para>', styleN)
        # partida = Paragraph('<para fontsize=5>Beschadigung der <br\>Kunststoffummantelung</para>', styleN)
        # candidad = Paragraph('<para fontsize=5>Drahbruch</para>', styleN)
        # precio_unitario = Paragraph('<para fontsize=4>Massive Bruche von Drahten</para>', styleN)
        # precio_total = Paragraph('<para fontsize=4>Litzenbrunch</para>', styleN)
        # precio_empty1 = Paragraph('<para fontsize=4>Seil aus der Rille</para>', styleN)
        # precio_empty2 = Paragraph('<para fontsize=4> Image1 </para>', styleN)
        # # precio_empty3 = Paragraph('<para fontsize=4> Image2 </para>', styleN)
        #
        #
        # descrpcio = Paragraph('<para fontsize=5><b>Beschreibung</b></para>', styleN)
        # partid = Paragraph('<para fontsize=4>Kunststoffummantelung ist so <br/>abgenutzt, dass der mettallische</para>', styleN)
        # candida = Paragraph('<para fontsize=4>Mehr als 10 Drahte ragen<br/>aus dem TPU-Mantel</para>', styleN)
        # precio_unitari = Paragraph('<para fontsize=4>Mehr als 3 Drahte ragen aus   dem</para>', styleN)
        # precio_tota = Paragraph('<para fontsize=4>spezifischer Seilbruch</para>', styleN)
        # precio_empty = Paragraph('<para fontsize=4>Seil ist aus seiner<br/>ursprunglichen Rille</para>', styleN)
        # # precio_empty = Paragraph('<para fontsize=4> Image1 </para>', styleN)
        #
        #
        # descrpci = Paragraph('<para fontsize=5><b>Korrektur-massnahme</b></para>', styleN)
        # parti = Paragraph('<para fontsize=4>Bericht an<br/>Brugg Lifting senden.</para>', styleN)
        # candid = Paragraph('<para fontsize=4>Bericht an<br/>Brugg Lifting senden.</para>', styleN)
        # precio_unitar = Paragraph('<para fontsize=4>Bericht an<br/>Brugg Lifting senden.</para>', styleN)
        # precio_tot = Paragraph('<para fontsize=4>Bericht anBericht an<br/>Brugg Lifting senden.</para>', styleN)
        # precio_empt = Paragraph('<para fontsize=4>Bericht an<br/>Brugg Lifting senden.</para>', styleN)
        # precio_empt = Paragraph('<para fontsize=4> Image1 </para>', styleN)
        #
        #
        # descrpc = Paragraph('<para fontsize=5><b>Zeitskala</b></para>', styleN)
        # part = Paragraph('<para fontsize=4>< 2 Monate</para>', styleN)
        # candi = Paragraph('<para fontsize=4>2 Monate</para>', styleN)
        # precio_unita = Paragraph('<para fontsize=4>umgehend</para>', styleN)
        # precio_to = Paragraph('<para fontsize=4>umgehend</para>', styleN)
        # precio_emp = Paragraph('<para fontsize=4>umgehend</para>', styleN)
        # # precio_emp = Paragraph('<para fontsize=4> Image1 </para>', styleN)
        #
        #
        # data= [[hdescrpcion, hpartida,h1,hcandidad,h2,hprecio_unitario,h3, hprecio_total,h4, hprecio_empty1,hprecio_empty2],
        #        [descrpcion, partida, candidad, precio_unitario, precio_total,precio_empty1],
        #        [descrpcio,partid,candida,precio_unitari,precio_tota,precio_empty],
        #        [descrpci,parti,candid,precio_unitar,precio_tot,precio_empt],
        #        [descrpc,part,candi,precio_unita,precio_to,precio_emp]]
        #
        # table = Table(data, colWidths=[1.6 * cm, 2.5 * cm, 2 * cm,
        #                                2.25* cm, 2.5 * cm, 2*cm,1*cm,1.45*cm],rowHeights =12*mm)
        #
        # table.setStyle(TableStyle([
        #                             ('LINEABOVE',(0,1),(-1,1),0.25,colors.black),
        #                             ('SPAN',(2,0),(2,0)),
        #                             ('LINEBELOW',(0,1),(5,4),0.25,colors.black),
        #                             ('LINEBELOW',(0,4),(-1,-1),0.25,colors.black),
        #                             ('FONTSIZE', (0, 1), (-1, -1), 5),
        #                        ]))
        #
        # table.wrapOn(c, width, height)
        # table.drawOn(c, 17, 60, cm)

        # c.drawImage(logo13,6.15*inch,1.3*inch,width=0.45*inch,height=1.3*inch)
        # c.drawImage(logo14,6.65*inch,1.3*inch,width=0.45*inch,height=1.3*inch)
        # c.drawImage(logo15,7.15*inch,1.3*inch,width=0.45*inch,height=1.3*inch)
        # c.drawImage(logo16,7.65*inch,1.3*inch,width=0.45*inch,height=1.3*inch)


        p = c.beginPath()
        p.rect(-20, 7.25*inch, 4*inch, 0.9*inch)
        p.rect(268, 7.25*inch, 8*inch, 0.2*inch)

        c.clipPath(p, stroke=0)
        # c.linearGradient(100*mm,200*mm,100*mm,60*mm, ('#996515','#DAA520','#996515'),extend=False)
        c.setFont('FrutigerB', 17)
        c.setFillColor(colors.black)
        c.drawString(20,465,"CTP PRUFHANDBUCH")

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("FrutigerB",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1


        #page9
        chineseimg1 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/ctpCatalog',"chineesp9b.png")
        # chineseimg1 = "chineesp9b.png"
        c.drawImage(page9BG,0,0,width=width,height=height, mask='auto')

        c.drawImage(chineseimg1,0,0.725*inch, width=3.85*inch, height= 3*inch, mask='auto')
        # textobject = c.beginText()
        # textobject.setTextOrigin(0.5*inch,  6.75*inch)
        # c.setFont('STSong-Light', 10)
        # c.setFillColorRGB(0,0,0)
        # textobject.textLines('''
        # 2. 电梯配置参数''')
        # c.drawText(textobject)

        p = Paragraph('''<para fontsize=10 fontName= STSong-Light leading=13 align="justify"> 2.电梯配置参数 </para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,0.5*inch, 6.75*inch)

        p = Paragraph('''<para fontsize=10 fontName= STSong-Light leading=13 align="justify">我们可以通过电梯配置参数来理论测算出钢丝绳的曳引能力、弯曲测试表现等,如需要这方面的支持,欢迎与我们当地的销售代表联系。 </para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.4*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,6.15*inch)

        # c.setFillColor('#EEE8AA')
        # c.rect(30, 3.35*inch, 3.9*inch, 2.25*inch,stroke=0,fill=1)

        p = Paragraph('''<para fontsize=10 fontName= STSong-Light leading=13 align="justify">安全指示 </para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.4*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,0.5*inch, 5.4*inch)

        p = Paragraph('''<para fontsize=10 fontName= STSong-Light leading=13 align="justify">多数的检查需要在电梯运行中完成(检修模式),未经专业培训的人员,如下检查不能操作。轿顶作业时必须确保安全</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.4*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,0.5*inch, 5.2*inch)

        p = Paragraph('''<para fontsize=10 fontName= STSong-Light leading=13 align="justify">当CTP ® 钢丝绳的表面有油或者水时不要做相关操作,因为表面的油或者水非常容易接触到曳引轮,从而降低曳引能力并导致打滑。</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.4*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,0.5*inch, 4.15*inch)

        # textobject = c.beginText()
        # textobject.setTextOrigin(325, 6.75*inch)
        # c.setFont('STSong-Light', 9)
        # c.setFillColorRGB(0,0,0)
        # textobject.textLines('''
        # 3. 外观检查''')
        # c.drawText(textobject)

        p = Paragraph('''<para fontsize=10 fontName= STSong-Light leading=13 align="justify">3. 外观检查 </para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,325,6.75*inch)

        p = Paragraph('''<para fontsize=10 fontName= STSong-Light leading=13 align="justify">外在的因素可能也会对绳子的使用产生负面的影响,因此这些也需要具体评估;在做具体的检测和评估之前,我们建议先从外观开始做基本的检查,特别要注意钢丝绳外面包裹的涂层: </para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.3*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,325,6*inch)


        # textobject = c.beginText()
        # textobject.setTextOrigin(4.5*inch, 5.75*inch)
        # c.setFont('STSong-Light', 9)
        # c.setFillColorRGB(0,0,0)
        # dat = [
        # '是否有断丝穿透包裹的涂层',
        # '包裹涂层表面是否出现不规则的变化(凸起,凹陷或者类似状况)',
        # '包裹涂层表面是否出现划痕,撕裂',
        # '包裹涂层(TPU)是否在轮槽上磨损并出现粉末',
        # ' 包覆层上是否有灰尘、油、水等杂质',
        # '钢丝绳是否出现打结',
        # ]
        #
        # for i in dat:
        #     textobject.textLines("- %s"%(i))
        #
        # c.drawText(textobject)


        stylesC = ParagraphStyle(            'small',
                                            parent=stylesN,

                                            fontName = 'STSong-Light',
                                            bulletType='-',
                                            bulletFontSize = 5,
                                            bulletIndent = 0,
                                            bulletOffsetY = -3,
                                            leftIndent = 7,

                                            )
        list = '''<ul>
                    <li> 是否有断丝穿透包裹的涂层</li>
                    <li> 包裹涂层表面是否出现不规则的变化(凸起,凹陷或者类似状况)</li>
                    <li> 包裹涂层表面是否出现划痕,撕裂</li>
                    <li> 包裹涂层(TPU)是否在轮槽上磨损并出现粉末</li>
                    <li> 包覆层上是否有灰尘、油、水等杂质</li>
                    <li> 包覆层上是否有灰尘、油、水等杂质<br/>-钢丝绳是否出现打结</li>
                 </ul>
                '''
        # p = Paragraph('''<para fontsize=10 fontName= STSong-Light leading=13 align="justify">- 是否有断丝穿透包裹的涂层<br/>- 包裹涂层表面是否出现不规则的变化(凸起,凹陷或者类似状况)<br/>-包裹涂层表面是否出现划痕,撕裂<br/>-包裹涂层(TPU)是否在轮槽上磨损并出现粉末<br/>-包覆层上是否有灰尘、油、水等杂质<br/>-钢丝绳是否出现打结</para>''',stylesC)
        # p1 =[[p]]
        # p11 = Table(p1,colWidths=3.3*inch)
        # p11.wrapOn(c,width,height)
        # p11.drawOn(c,325,4.5*inch)
        height2 = htmlRMLCanvvas(list,c,3.3*inch,325,6*inch,styles['Normal'],colors.black,lang)
        p = Paragraph('''<para fontsize=10 fontName= STSong-Light leading=13 align="justify">同时还要检查</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.3*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,4.5*inch, 4.15*inch)

        # p = Paragraph('''<para fontsize=10 fontName= STSong-Light leading=13 align="justify">-钢丝绳是否与电梯其他部件之间接触或触碰到井道壁<br/>-钢丝绳之间是否相互碰撞产生静电<br/>-曳引轮与转向轮是否充分对准<br/>-曳引轮与转向轮是否充分对准</para>''',stylesN)
        # p1 =[[p]]
        # p11 = Table(p1,colWidths=3.5*inch)
        # p11.wrapOn(c,width,height)
        # p11.drawOn(c,4.5*inch, 3.3*inch)


        # textobject = c.beginText()
        # textobject.setTextOrigin(4.5*inch, 4.3*inch)
        # c.setFont('STSong-Light', 9)
        # c.setFillColorRGB(0,0,0)
        #
        # data = [
        # '钢丝绳是否与电梯其他部件之间接触或触碰到井道壁',
        # '钢丝绳之间是否相互碰撞产生静电',
        # '钢丝绳是否在运行中震动',
        # '曳引轮与转向轮是否充分对准',
        # ]
        # for i in data:
        #     textobject.textLines("- %s"%(i))
        # c.drawText(textobject)


        list = '''<ul>
                <li> 钢丝绳是否与电梯其他部件之间接触或触碰到井道壁</li>
                <li> 钢丝绳之间是否相互碰撞产生静电</li>
                <li> 钢丝绳是否在运行中震动</li>
                <li> 曳引轮与转向轮是否充分对准</li>
             </ul>
            '''
        height2 = htmlRMLCanvvas(list,c,3.3*inch,325,4*inch,styles['Normal'],colors.black,lang)

        p = Paragraph('''<para fontsize=10  fontName= STSong-Light leading=13 align="justify">在检查过程中,需要通过拍摄照片来记录这些信息,包括钢丝绳,曳引轮,转向轮和绳头等等。 </para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.3*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,325,2.55*inch)

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("FrutigerB",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1



        #page 10

        c.drawImage(page10BG,0,0,width=width,height=height, mask='auto')

        p = Paragraph('''<para fontName=STSong-Light fontsize=13  leading=13 align="justify">4. 偏离角的检查</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,0.425*inch,  6.65*inch)

        c.setFont('STSong-Light', 23)
        c.drawString(50, 7.75*inch, "检验手册 ")

        c.setFont('FrutigerB', 23)
        c.drawString(150, 7.75*inch, "CTP")

        p = Paragraph('''<para fontName=STSong-Light fontsize=10  leading=13 align="justify">允许的偏离角是0.5°, CTP8.1的最大的偏离角可以提高到1°,这基于钢丝绳运行次数不大于2, 400, 000除以通过滑轮的个数(不适用CTP6.5);偏离角允许的数值(依据证书)是0.5°;如果偏离角太大,会导致钢丝绳发生扭转,这种检测方法同样适用于传统钢丝绳,但在CTP钢丝绳中的影响更加显著; </para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.6*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,5.5*inch)

        p = Paragraph('''<para fontName=STSong-Light fontsize=10  leading=13 align="justify">最重要的位置是当电梯位于最顶层(最大的偏离角在轿厢与曳引轮/转向轮之间)以及当电梯位于最低层(最大的偏离角在对重与曳引轮/转向轮之间);测量钢丝绳与轮槽之间的偏离角是非常困难的;因此我们建议通过一种间接的但更实用的方法来测量(请参照下文)</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.6*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,4.4*inch)

        p = Paragraph('''<para fontName=STSong-Light fontsize=10  leading=13 align="justify">粗略估算偏离角时需要测量如下几点(电梯为1: 1悬挂时):</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.6*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,4.1*inch)

        p = Paragraph('''<para fontName=STSong-Light fontsize=10  leading=13 align="justify">1. 轿厢停在最顶层时,从曳引轮到轿厢侧绳头的距离。</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.6*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,3.8*inch)

        p = Paragraph('''<para fontName= STSong-Light fontsize=10  leading=13 align="justify">2. 测量在曳引轮,在轿厢侧及对重侧3个位置的绳与绳之间的距离</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.6*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,3.25*inch)

        p = Paragraph('''<para fontName = STSong-Light fontsize=10  leading=13 align="justify">3. 轿厢在最底层时,曳引轮到对重侧绳头的距离 </para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.6*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,3.1*inch)

        # textobject = c.beginText()
        # textobject.setTextOrigin(4.6*inch, 3.1*inch)
        # c.setFont('FrutigerR', 5)
        # c.setFillColorRGB(0,0,0)
        # textobject.textLines('''
        # Schragzugwinkel zwischen
        # Scheibe und Seil
        # ''')
        # c.drawText(textobject)
        #
        # textobject = c.beginText()
        # textobject.setTextOrigin(6.8*inch, 0.7*inch)
        # c.setFont('FrutigerR', 7)
        # c.setFillColorRGB(0,0,0)
        # textobject.textLines('''
        # Brugg Rillenlehre
        # ''')
        # c.drawText(textobject)
        #
        # textobject = c.beginText()
        # textobject.setTextOrigin(8.6*inch, 0.7*inch)
        # c.setFont('FrutigerR', 7)
        # c.setFillColorRGB(0,0,0)
        # textobject.textLines('''
        # Seilspannungsmessgerat Brugg RPM
        # ''')
        # c.drawText(textobject)

        p = c.beginPath()
        # p.rect(20,1.2*inch, 0.1*inch, 0.1*inch)
        # p.rect(20,1.8*inch,0.1*inch, 0.1*inch)
        # p.rect(20,2.3*inch, 0.1*inch, 0.1*inch)
        p.rect(-20, 7.25*inch, 4*inch, 0.9*inch)
        p.rect(268, 7.25*inch, 8*inch, 0.2*inch)

        c.clipPath(p, stroke=0)

        # c.setFont('FrutigerR', 7)
        # c.drawString(23,87,"3")
        #
        # c.setFont('FrutigerR', 7)
        # c.drawString(23,130,"2")
        #
        # c.setFont('FrutigerR', 7)
        # c.drawString(23,167,"1")

        c.setFont('FrutigerB', 17)
        c.drawString(20,465,"CTP PRUFHANDBUCH")

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("FrutigerB",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        #page 11
        c.drawImage(page11BG,0,0,width=width,height=height, mask='auto')

        p = Paragraph('''<para fontName=STSong-Light fontsize=10 >5. 轮槽形状的检查<br/>
        (曳引轮和转向滑轮) </para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,0.4*inch,  6.6*inch)

        p = Paragraph('''<para fontName=STSong-Light fontsize=10  leading=13 align="justify">尽管曳引轮和转向滑轮槽是根据图纸制造的(CTP6.5对应的半径: 3.4-3.65毫米, CTP8.1对应的半径: 4.3毫米),我们强烈建议使用布鲁格专门设计的轮槽量规来测量轮槽形状。布鲁格提供一个定制的量规,可测量CTP证书规定的45°(CTP6.5: 30 - 45° )开度角。</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,5.6*inch)

        p = Paragraph('''<para fontName=STSong-Light fontsize=10 >6. 钢丝绳张力</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,320,  6.7*inch)

        p = Paragraph('''<para fontName=STSong-Light fontsize=10  leading=13 align="justify">尽管钢丝绳的张力通常可以用手来判断(通过拉动钢丝绳,凭感觉来判断),但这种测试方法无法做到精确;通过弹簧缓冲器来测量,无疑比手更加精确,但并不是每一台电梯都配有这种弹簧;测量钢丝绳张力的最可靠的方法是通过测量绳本身的张力,有很多的工具可以测量,其中我们推荐布鲁格专有产品:RPM张力测试仪。</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,320,5.6*inch)


        p = Paragraph('''<para fontName=STSong-Light fontsize=10 >此外还要检查轮槽表面是否有如下缺陷</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,0.4*inch,  5.2*inch)


        list = '''<ul>
                    <li> 生锈或绳涂层的磨损或轮槽周边有磨损</li>
                    <li> 潮湿表面(水,油等)</li>
             </ul>
            '''



        height2 = htmlRMLCanvvas(list,c,3.3*inch,0.4*inch, 5.15*inch,styles['Normal'],colors.black,lang)




        # p = Paragraph('''<para fontName=STSong-Light fontsize=10 >生锈或绳涂层的磨损或轮槽周边有磨损 潮湿表面(水,油等)</para>''',stylesN)
        # p1 =[[p]]
        # p11 = Table(p1,colWidths=3.75*inch)
        # p11.wrapOn(c,width,height)
        # p11.drawOn(c,0.4*inch, 4.8*inch)

        p = Paragraph('''<para fontName=STSong-Light fontsize=10 >如果允许还要检查转向滑轮的轴承是否还在流畅运行。</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,0.5*inch,  4.5*inch)

        p = Paragraph('''<para fontName=STSong-Light fontsize=10 >布鲁格绳槽量规</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,1.5*inch, 1.25*inch)

        p = Paragraph('''<para fontName=STSong-Light fontsize=10 >钢丝绳张力测试仪 布鲁格RPM。</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,4.75*inch, 1.25*inch)


        p = Paragraph('''<para fontName=STSong-Light fontsize=8 >版本日期 03/2019我们的产品介绍如有变化,印刷错误或其它问题以及 www.schaefer-design.com 为目录进行设计和印刷</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,0.9*inch, 0.5*inch)


        # c.drawText(textobject)

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data11 =  [[gm934,gmn934]]

        t = Table(data11,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("FrutigerB",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1
        if pageCount %2 == 0:
            print "dont worry"
        else:
            c.showPage()
            pageCount +=1
        c.drawImage(page12BG,0,0,width=width,height=height, mask='auto')
        textobject = c.beginText()
        textobject.setTextOrigin(250, 40)
        textobject.setFont("FrutigerB", 12)
        # textobject.setFillColorRGB(192,192,192)
        textobject.setFillColor(colors.white)
        textobject.textLines('''
                                brugglifting.com
                              ''')
        c.drawText(textobject)
        c.showPage()
        c.save()



    elif lang == 'de':

        #page 1
        c.drawImage(page1BG,0,0,width=width,height=height,mask='auto')
        c.setFont("FrutigerB",50)
        c.setFillColor('#000000')
        c.drawString(185, 5.85*inch, "CTP")

        c.setFont("FrutigerR",15)
        c.setFillColor('#000000')
        c.drawString(300, 5.85*inch, "COATED TRACTION ROPES")

        c.setFont("FrutigerB",20)
        c.setFillColor(colors.white)
        c.drawString(280, 30, ". . . die Zukunft beginnt jetzt!")

        c.showPage()
        pageCount +=1

        #page 2
        c.drawImage(page2BG,0,0,width=width, height=height, mask='auto')

        c.setFillColor(colors.black)
        c.setFont("FrutigerB",25)
        c.drawString(50, 8.25*inch, "SERVICES")
        c.setFillGray(0.5)

        tp = Paragraph('<para fontName = FrutigerB fontsize=13 leftindent=13  ><b>Systemlieferant</b></para>',stylesN)
        tp2 = Paragraph('<para fontName = FrutigerR fontsize=10  align="Justify" leading=15>Sie finden bei uns ein umfassendes Sortiment an Aufzugseilen, Zubehör und Hilfs-mitteln, um Ihre Bedürfnisse vollständig abzudecken. Wir beliefern Sie mit Komplett-lösungen oder individuell zusammengestellten Komponenten, als Einzelteile oder vormontiert, ganz nach Ihren Wünschen</para>',stylesN)
        tpt=[[tp],[tp2]]
        tptab=Table(tpt,colWidths=6*inch)
        tptab.setStyle(TableStyle([
                                    ('LEFTPADDING',(0,1),(-1,-1),20),
                               ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,1.7*inch, 450)

        tp = Paragraph('<para fontName = FrutigerB fontsize=13 leftindent=13  ><b>Kundenspezifisch</b></para>',stylesN)
        tp2 = Paragraph('<para fontName = FrutigerR fontsize=10  align="Justify" leading=15>In unserem breiten Sortiment an Aufzugseilen, Zubehör und Hilfsmitteln finden Siebeinahe alle benötigten Produkte für Ihre Anwendung. Falls keiner der im Katalog abge-bildeten Artikel Ihr Problem löst, oder Ihr Aufzug spezifische Anforderungen erfüllen soll,beraten wir Sie gerne und erarbeiten individuelle Lösungen.</para>',stylesN)
        tpt=[[tp],[tp2]]
        tptab=Table(tpt,colWidths=6*inch)
        tptab.setStyle(TableStyle([
                                    ('LEFTPADDING',(0,1),(-1,-1),20),
                               ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,1.7*inch, 350)


        tp = Paragraph('<para fontName = FrutigerB fontsize=13 leftindent=13  ><b>Verfügbarkeit</b></para>',stylesN)
        tp2 = Paragraph('<para fontName = FrutigerR fontsize=10 align="Justify" leading=15 >Dank unserer zwei Produktionsstätten in der Schweiz und in China sowie einem globalen Netz an Lagerstandorten werden unsere Produkte innert kürzester Zeit in Ihr Werk oder auf Ihre Baustelle geliefert. Kontaktieren Sie uns bei Fragen zu Terminen, individuellen Lieferungen und spezifischen Projekten.</para>',stylesN)
        tpt=[[tp],[tp2]]
        tptab=Table(tpt,colWidths=6*inch)
        tptab.setStyle(TableStyle([
                                    ('LEFTPADDING',(0,1),(-1,-1),20),
                               ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,1.7*inch, 260)


        tp = Paragraph('<para fontName = FrutigerB fontsize=13 leftindent=13  ><b>Expressdienst</b></para>',stylesN)
        tp2 = Paragraph('<para fontName = FrutigerR fontsize=10 align="Justify" leading=15 >In dringenden Fällen stellen wir das benötigte Material in Stundenfrist ab Werk bereitund schicken es Ihnen schnellstmöglich per Kurier weltweit zu</para>',stylesN)
        tpt=[[tp],[tp2]]
        tptab=Table(tpt,colWidths=6*inch)
        tptab.setStyle(TableStyle([

                                    ('LEFTPADDING',(0,1),(-1,-1),20)
                               ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,1.7*inch, 200)

        tp = Paragraph('<para fontName = FrutigerB fontsize=12 leftindent=13  ><b>Internationale Standards</b></para>',stylesN)
        tp2 = Paragraph('<para fontName = FrutigerR fontsize=9 align="Justify" leading=15 >BRUGG LIFTING ist nach ISO 9001:2015 und ISO 14001:2015 zertifiziert.</para>',stylesN)
        tpt=[[tp],[tp2]]
        tptab=Table(tpt,colWidths=6*inch)
        tptab.setStyle(TableStyle([

                                    ('LEFTPADDING',(0,1),(-1,-1),20),
                               ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,1.7*inch, 140)

        tp = Paragraph('<para fontName = FrutigerB fontsize=12 leftindent=13  ><b>Schulungen/Fachseminare</b></para>',stylesN)
        tp2 = Paragraph('<para fontName = FrutigerR fontsize=9 align="Justify" leading=15 >Unser Ziel ist, Sie beim optimalen Einsatz und der Erhöhung der maximalen Lebens-dauer Ihrer Aufzugseile zu unterstützen. Zur Aus- und Weiterbildung Ihrer Mitarbeiter bieten wir Ihnen qualifizierte und individualisierte Schulungen an</para>',stylesN)
        tpt=[[tp],[tp2]]
        tptab=Table(tpt,colWidths=6*inch)
        tptab.setStyle(TableStyle([

                                    ('LEFTPADDING',(0,1),(-1,-1),20),
                               ]))
        tptab.wrapOn(c,width,height)
        tptab.drawOn(c,1.7*inch, 70)

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        #page 3

        c.drawImage(page3BG,0,0,width=width,height=height,mask='auto')


        p = Paragraph('''<para fontName= FrutigerR fontsize=10  leading=13 align="justify">Als Weltneuheit entwickelt, vereint CTP ® technologische Innovationen zu einem hochmodernen kunststoffummantelten Seil, das speziell für die Aufzugsbranche ausgelegt ist.</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=4.7*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,50,6.7*inch)

        p = Paragraph('''<para fontName= FrutigerR fontsize=10  leading=13 align="justify">Zugelassen für Treibscheiben mit einem Durchmesser von nur 115 mm, sind CTP ® Seilebereits in 90.000 Aufzügen weltweit eingebaut.CTP ® Seile, die mittels Simulation im Labor und unter realen Bedingungen getestet worden sind, erfüllen höchste Ansprüche an Funktion und Leistungsfähigkeit. </para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=4.7*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,50,5.8*inch)


        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)
        t.drawOn(c, 7.75*inch,0.2*inch)

        c.setFillColor(colors.black)
        c.setFont("FrutigerB",10)
        c.drawString(580, 0.15*inch, "3")

        c.showPage()
        pageCount +=1

        #page 4
        for template in ctpObj:
            prodfield = ProductField.objects.filter(template = template.pk)
            # printprodfield
            prod = Product.objects.filter(template = template.pk)
            # printprod



            if pageCount%2 == 1:
                if template.catalogBG1:
                    background = template.catalogBG1.path
                else:
                    background = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/ctpCatalog',"page4.jpg")

                c.drawImage(background,0,0,width=width, height=height, mask = 'auto')
                name = Paragraph('<para fontName = FrutigerB fontSize=30>%s</para>'%(template.name), stylesN)
                nd =[[name]]
                w = pdfmetrics.stringWidth(template.name, "FrutigerB", 30)
                # printw, "text width "
                ndt = Table(nd)
                w1,h1 = ndt.wrapOn(c, width,height)
                width2 = width - w -50
                ndt.drawOn(c, width2,570)



            else:
                if template.catalogBG2:
                    background = template.catalogBG2.path
                else:
                    background = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/ctpCatalog',"page4.jpg")
                c.drawImage(background,0,0,width=width, height=height, mask = 'auto')
                name = Paragraph('<para fontName = FrutigerB fontSize=30>%s</para>'%(template.name), stylesN)
                nd =[[name]]
                w = pdfmetrics.stringWidth(template.name, "FrutigerB", 30)
                # printw, "text width "
                ndt = Table(nd)
                w1,h1 = ndt.wrapOn(c, width,height)
                width2 = 50
                ndt.drawOn(c, width2,570)



            name = Paragraph('<para fontName = FrutigerR fontSize=15>%s</para>'%("COATED TRANSMISSION PRODUCTS"), styles['Normal'])
            nd =[[name]]
            # printw, "text width "
            ndt = Table(nd)
            w1,h1 = ndt.wrapOn(c, width,height)

            ndt.drawOn(c, 200,548)

            c.drawImage(template.defaultImage.path,50,400,width=1.4*inch,height=1.4*inch, mask='auto')

            para2 =  addBRInRichText(template.rteData2_otl)
            para22 = Paragraph('<para fontName = FrutigerR>%s</para>'%(para2), styles['Normal'])
            tab1 = [[para22]]
            ps = Table(tab1,colWidths=4.5*inch)
            w2, h2 = ps.wrapOn(c, width,height)
            height2 = height - h2 - 350


            ps.drawOn(c, 200, height2)

            height2 = height2 - 50
            height3 = height2 + 15
            height4 = height2
            height5 = height2 - 30
            c.setFillColor('#81B3EE')
            c.setStrokeColor(colors.white)
            c.rect(4*inch,height2,0.6*inch,0.6*inch, fill=1)
            c.setFont("Helvetica-Bold", 7)
            c.setFillColor(colors.black)
            k = json.loads(template.keyword1)
            k11 =[[k]]
            r11 = Table(k11,colWidths=3.6*inch,rowHeights=4*mm)
            c.setFont("Helvetica", 5)

            para101 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%(k["value1"]), styles['Normal'])
            desc101 = [[para101]]
            r101 = Table(desc101,colWidths=0.6*inch,rowHeights=1*mm)
            w, h = r101.wrapOn(c, width,height)
            r101.drawOn(c, 4*inch, height3)

            para102 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%("N/mm2"), styles['Normal'])
            desc102 = [[para102]]
            r102 = Table(desc102,colWidths=0.6*inch,rowHeights=1*mm)
            r102.wrapOn(c, width,height)
            r102.drawOn(c, 4*inch, height4)

            para103 = Paragraph('<para align="center" fontName = FrutigerR fontSize=7 >%s</para>'%("E-Module"), styles['Normal'])
            desc103 = [[para103]]
            r103 = Table(desc103,colWidths=0.6*inch,rowHeights=1*mm)
            r103.wrapOn(c, width,height)
            r103.drawOn(c, 4*inch, height5)


            c.setFillColor('#9BC7EC')
            c.rect(5*inch,height2,0.6*inch,0.6*inch, fill=1)
            c.setFont("Helvetica-Bold", 7)
            c.setFillColor(colors.black)
            k1 = json.loads(template.keyword2)

            k12 =[[k1]]

            r12 = Table(k12,colWidths=5*inch,rowHeights=10*mm)

            para201 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%(k1["value1"]), styles['Normal'])
            desc201 = [[para201]]
            r201 = Table(desc201,colWidths=0.6*inch)
            w,h = r201.wrapOn(c, width,height)

            r201.drawOn(c, 5*inch, height3)

            para202 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%("%"), styles['Normal'])
            desc202 = [[para202]]
            r202 = Table(desc202,colWidths=0.6*inch,rowHeights=1*mm)
            r202.wrapOn(c, width,height)
            r202.drawOn(c, 5*inch, height4)

            para203 = Paragraph('<para align="center" fontName = FrutigerR fontSize=7 >%s</para>'%("Elastic<br/>Elongation"), styles['Normal'])
            desc203 = [[para203]]
            r203 = Table(desc203,colWidths=0.65*inch,rowHeights=1*mm)
            r203.wrapOn(c, width,height)
            r203.drawOn(c, 5*inch, height5 )


            c.setFillColor(	'#BBD5F0')
            c.setStrokeColor(colors.white)

            c.rect(6*inch,height2,0.6*inch,0.6*inch, fill=1)
            c.setFont("Helvetica-Bold", 7)
            c.setFillColor(colors.black)
            k2 = json.loads(template.keyword3)

            k13 = [[k2]]

            r13 = Table(k13,colWidths=5*inch,rowHeights=10*mm)

            para301 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%(k2["value1"]), styles['Normal'])
            desc301 = [[para301]]
            r301 = Table(desc301,colWidths=0.6*inch,rowHeights=1*mm)
            r301.wrapOn(c, width,height)
            r301.drawOn(c, 6*inch, height3)

            para302 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%("%"), styles['Normal'])
            desc302 = [[para302]]
            r302 = Table(desc302,colWidths=0.6*inch,rowHeights=1*mm)
            r302.wrapOn(c, width,height)
            r302.drawOn(c, 6*inch, height4)

            para303 = Paragraph('<para align="center" fontName = FrutigerR fontSize=7 >%s</para>'%("Permanent<br/>Elongation"), styles['Normal'])
            desc303 = [[para303]]
            r303 = Table(desc303,colWidths=0.7*inch,rowHeights=1*mm)
            r303.wrapOn(c, width,height)
            r303.drawOn(c, 6*inch, height5)


            c.setFillColor('#D5E5F5')
            c.setStrokeColor(colors.white)
            c.rect(7*inch,height2,0.6*inch,0.6*inch, fill=1)
            c.setFont("Helvetica-Bold", 7)
            c.setFillColor(colors.black)
            k3 = json.loads(template.keyword4)
            k14 = [[k3]]
            r14 = Table(k14,colWidths=5*inch,rowHeights=10*mm)

            para401 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%(k3["value1"]), styles['Normal'])
            desc401 = [[para401]]
            r401 = Table(desc401,colWidths=0.6*inch,rowHeights=1*mm)
            r401.wrapOn(c, width,height)
            r401.drawOn(c, 7*inch, height3)

            para402 = Paragraph('<para align="center" fontName = FrutigerB fontSize=8 >%s</para>'%("m"), styles['Normal'])
            desc402 = [[para402]]
            r402 = Table(desc402,colWidths=0.6*inch,rowHeights=1*mm)
            r402.wrapOn(c, width,height)
            r402.drawOn(c, 7*inch, height4)

            para403 = Paragraph('<para align="center" fontName = FrutigerR fontSize=7 >%s</para>'%("Lifting<br/>Height"), styles['Normal'])
            desc403 = [[para403]]
            r403 = Table(desc403,colWidths=0.6*inch,rowHeights=1*mm)
            r403.wrapOn(c, width,height)
            r403.drawOn(c, 7*inch, height5)


            height2 = height5

            data = []
            # data2 = []
            dataHeading = ['Item Number']
            dataHeading2 = ['']
            list1 = []
            list2 = []
            for j in prodfield:
                # printprodfield
                if j.inPdf ==True:

                    # printj.name,'kkkkkkkkkkkkk'
                    try:
                        name1, name2 = j.name.split('(')
                        # printname2[:-1]
                        name2 = ''+name2[:-1]
                        # printname2
                    except:
                        name1 = j.name
                        name2 = ''

                    # printname1, ' ' , name2

                    list1.append(name1)
                    list2.append(name2)
            for a in list1:
                dataHeading.append(a)
            for b in list2:
                dataHeading2.append(b)



            for i in prod:
                appendlist = [i.itemNumber]
                for j in prodfield:
                    prodQty = ProductValueMap.objects.filter( field = j.pk,product = i.pk)
                    for k in prodQty:
                        if j.inPdf ==True:
                            if j.type=='Char':
                                appendlist.append(k.char)
                            if j.type=='float':
                                appendlist.append(k.fValue)
                            if j.type=='Integer':
                                appendlist.append(k.iValue)
                            if j.type=='Boolean':
                                appendlist.append(k.bool)
                data.append(appendlist)

            height2 = height2-40
            leftHeight = height2-100
            numberRows = int(leftHeight/20)
            # printheight2, leftHeight, numberRows, "number of rows"

            data.insert(0,dataHeading)
            data.insert(1,dataHeading2)

            if len(data)<= numberRows:
                    t5 = Table(data,rowHeights=[20]*len(data))
                    t5.setStyle(TableStyle([
                                         ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                                         ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                                         ('FONTSIZE', (0, 0), (-1, -1), 7),
                                         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                         ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                                         ]))
                    w5, h5 = t5.wrapOn(c, width, height)
                    height2 = height2 - h5
                    t5.drawOn(c, 200, height2)



                    para2 = Paragraph('<para fontName = Helvetica fontSize=6 >%s</para>'%(template.disclaimer_en), styles['Normal'])
                    tab = [[para2]]
                    r = Table(tab,colWidths=3.25*inch)
                    w,h1 = r.wrapOn(c, width,height)
                    height2 = height2 - h1
                    r.drawOn(c, 200, height2)

                    gm934 = Paragraph('<para></para>',stylesN)
                    gmn934 = Paragraph('<para></para>',stylesN)

                    data =  [[gm934,gmn934]]

                    t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
                    t.setStyle(TableStyle([
                                        ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                                         ]))
                    t.wrapOn(c,width, height)


                    c.setFillColor(colors.black)
                    c.setFont("Helvetica-Bold",10)
                    if pageCount%2==0:
                        t.drawOn(c, -3*inch,0.2*inch)
                        c.drawString(20, 0.15*inch, str(pageCount))
                    else:
                        t.drawOn(c, width-35,0.2*inch)
                        c.drawString(width-30, 0.15*inch, str(pageCount))

                    c.showPage()
                    pageCount +=1
            else:
                # print"in else ctp extra page requiresss"
                data1 = data[:numberRows-1]

                data2 = data[numberRows:-1]

                t5 = Table(data1,rowHeights=[20]*len(data1))
                t5.setStyle(TableStyle([
                                     ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                                     ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                                     ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                                     ('FONTSIZE', (0, 0), (-1, -1), 7),
                                     ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                     ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                                     ]))
                w5, h5 = t5.wrapOn(c, width, height)
                height2 = height2 - h5
                t5.drawOn(c, 200, height2)



                para2 = Paragraph('<para fontName = Helvetica fontSize=6 >%s</para>'%(template.disclaimer_en), styles['Normal'])
                tab = [[para2]]
                r = Table(tab,colWidths=3.25*inch)
                w,h1 = r.wrapOn(c, width,height)
                height2 = height2 - h1
                r.drawOn(c, 200, height2)

                gm934 = Paragraph('<para></para>',stylesN)
                gmn934 = Paragraph('<para></para>',stylesN)

                data =  [[gm934,gmn934]]

                t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
                t.setStyle(TableStyle([
                                    ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                                     ]))
                t.wrapOn(c,width, height)


                c.setFillColor(colors.black)
                c.setFont("Helvetica-Bold",10)
                if pageCount%2==0:
                    t.drawOn(c, -3*inch,0.2*inch)
                    c.drawString(20, 0.15*inch, str(pageCount))
                else:
                    t.drawOn(c, width-35,0.2*inch)
                    c.drawString(width-30, 0.15*inch, str(pageCount))

                c.showPage()
                pageCount +=1
                maxNumberItems = 15

                index = float(len(data2))/maxNumberItems

                index = int(math.ceil(index))

                for i in range(index):
                    if i == index-1:
                        data1 = data2[maxNumberItems*i:-1]
                        data1.insert(0,dataHeading)
                        data1.insert(1,dataHeading2)

                    else:
                        data1 = data2[maxNumberItems*i:maxNumberItems*(i+1)-1]
                        data1.insert(0,dataHeading)
                        data1.insert(1,dataHeading2)

                    pageCount = addCTPPage(c, data1,template,stylesN,pageCount,lang)



        # new page

        c.drawImage(page5BG, 0,0, width=width, height=height, mask='auto')
        textobject = c.beginText()
        textobject.setTextOrigin(0.65*inch, 7*inch)
        textobject.setFont("FrutigerR", 10)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                                Als Weltneuheit vereint CTP ® technologische Innovationen für die höchsten Ansprüche.
                                Dieses hochwertige Seil ist unschlagbar hinsichtlich Funktion und Leistungsfähigkeit''')
        c.drawText(textobject)

        textobject = c.beginText()
        textobject.setTextOrigin(0.65*inch, 6.4*inch)
        textobject.setFont("FrutigerB", 10)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            Reduzieren Sie Ihre Gesamtkosten um bis zu 40%.
                            ''')
        c.drawText(textobject)
        c.drawText(textobject)
        textobject = c.beginText()
        textobject.setTextOrigin(0.65*inch, 6.2*inch)
        textobject.setFont("FrutigerR", 10)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            Kleinere Seildurchmesser und kleinerer Antrieb reduzieren Investitions- und Betriebskosten
                            ''')
        c.drawText(textobject)
        textobject = c.beginText()
        textobject.setTextOrigin(0.65*inch, 5.9*inch)
        textobject.setFont("Helvetica-Bold", 10)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            Senken Sie Ihre Wartungskosten um bis zu 100%
                            ''')
        c.drawText(textobject)
        c.drawText(textobject)
        textobject = c.beginText()
        textobject.setTextOrigin(0.65*inch, 5.7*inch)
        textobject.setFont("FrutigerR", 10)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            CTP ® ist in sich ein geschlossenes System, es muss weder geschmiert noch gewartet werden.
                            ''')
        c.drawText(textobject)
        textobject = c.beginText()
        textobject.setTextOrigin(0.65*inch, 5.4*inch)
        textobject.setFont("FrutigerB", 10)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            Geniessen Sie einen deutlich verbesserten Fahrkomfort
                            ''')
        c.drawText(textobject)
        c.drawText(textobject)
        textobject = c.beginText()
        textobject.setTextOrigin(0.65*inch, 5.2*inch)
        textobject.setFont("Helvetica", 10)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            Durch die Polymerummantelung werden Vibrationen beseitigt bzw. stark gedämpft und somit die Laufruhe merklich verbessert.
                            ''')
        c.drawText(textobject)
        textobject = c.beginText()
        textobject.setTextOrigin(0.65*inch, 4.9*inch)
        textobject.setFont("FrutigerB", 10)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            Erhöhen Sie die Lebensdauer
                            ''')
        c.drawText(textobject)
        c.drawText(textobject)
        textobject = c.beginText()
        textobject.setTextOrigin(0.65*inch, 4.7*inch)
        textobject.setFont("FrutigerR", 10)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            Aufgrund des sehr geringen Verschleisses zwischen der Treibscheibe und dem Seil ist die Häufigkeit der Seilwechsel stark reduziert.
                            ''')
        c.drawText(textobject)

        # c.drawText(textobject1)
        c.setFont("FrutigerR",9)

        # c.drawImage(l1,130,170,width=2.5*inch,height=2.15*inch,mask='auto')
        c.setFont("FrutigerB", 5)

        c.drawString(2.15*inch, 2.25*inch, "Diagramm der festgelegten")
        c.drawString(2.15*inch, 2.1*inch, "Rillen für CTP ® 6.5 mm")

        # c.drawImage(l2,300,170, width=2.5*inch,height=2.15*inch,mask='auto')
        c.drawString(4*inch, 2.25*inch, "Diagramm der festgelegten")
        c.drawString(4*inch, 2.1*inch, "Rillen für CTP ® 8.1 mm")

        textobject = c.beginText()
        textobject.setTextOrigin(0.75*inch, 1.75*inch)
        textobject.setFont("FrutigerR", 8)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            Produktdaten der Treibscheibe / Ablenkung
                            ''')
        c.drawText(textobject)


        data = [
            ['für', 'Seil-ø', 'Stahlseil-ø',  'Seilgeschwindigkeit-' , "Scheiben-ø","scheiben-@","Treibscheibe","Rillenform","Ablenkscheibe"],
           ['Art.-Nr', '', '',  'koeffizient' , "max.","","Material","","Material"],
           ['',   'mm',  'mm','','m/s'   ,'mm'   '',         'halbrund ø mm',     ' ',     ],
           ['10982',   '6.5', '4,9','0,6-0,3','3,5*','>115','C45,c45 gehartet,42CrMo4','3,4-3,65','Stahl,Gusseisen,PA,PU.'],
           ['73106',   '6.5', '4,9','0,6-0,3','3,5*','>115','C45,c45 gehartet,42CrMo4','3,4-3,65','Stahl,Gusseisen,PA,PU.'],


           ]

        t5 = Table(data, colWidths=[0.75* cm, 1* cm, 1 * cm,
                                    2.5* cm, 2.5* cm,2.5* cm,2.5* cm,2.5* cm, ],rowHeights=5.5*mm)
        t5.setStyle(TableStyle([
                             ('LINEABOVE',(0,2),(-1,-1),0.25,colors.black),
                             ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                            ('FONTSIZE', (0, 0), (-1, -1), 5),

                            ('FONTNAME', (0, 0), (1,0), "FrutigerB"),
                            ('FONTNAME', (2, 0), (3,0), "FrutigerB"),
                            ('FONTNAME', (4,0), (5,0), "FrutigerB"),
                            ('FONTNAME', (6, 0), (7,0), "FrutigerB"),
                            ('FONTNAME', (0,0),(8, 0), "FrutigerB"),
                            ('FONTNAME', (0,0),(0, 1), "FrutigerB"),
                            ('FONTNAME', (1,0),(3,1), "FrutigerB"),
                            ('FONTNAME', (4,1),(6,1), "FrutigerB"),
                            ('FONTNAME', (0,0),(8,1), "FrutigerB"),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
                            ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                            # ('ALIGN', (1, 0), (1, 7), 'CENTER'),
                            # ('ALIGN', (2, 0), (-1, 7), 'CENTER'),
                            # ('ALIGN', (3, 0), (-1, 7), 'LEFT'),
                            # ('ALIGN', (4, 0), (-1, 7), 'LEFT'),
                            # ('ALIGN', (5, 0), (-1, 7), 'CENTER'),
                            # ('VALIGN', (5, 0), (-1, 7), 'BOTTOM'),
                            # ('LEFTPADDING', (0, 0), (-1, -1), -20),
                            #  ('LEFTPADDING', (1, 0), (-1, -1),10),
                            #  ('LEFTPADDING', (2, 0), (-1, -1), -30),
                            #  ('LEFTPADDING', (3, 0), (-1, -1), -30),
                            #  ('LEFTPADDING', (5, 0), (-1, -1), -30),
                            # ('LEFTPADDING', (4, 0), (-1, 9), -30),
                            #  ('LEFTPADDING', (5, 0), (-1, 9), -70),
                            ('BACKGROUND', (1,0), (1, 1), '#DCDCDC'),
                            ('BACKGROUND', (1,2), (1, 3), '#DCDCDC'),
                            ('BACKGROUND', (1,4), (1, 5), '#DCDCDC'),
                            # ('BACKGROUND', (1,6), (1, 7), '#DCDCDC'),
                             ]))

        t5.wrapOn(c, 20, 170)
        t5.drawOn(c, 0.75*inch,0.6*inch)


        textobject1 = c.beginText()
        textobject1.setTextOrigin(0.72*inch, 0.49*inch)
        c.setFillColor(colors.black)
        textobject1.setFont("FrutigerR", 5)
        textobject1.textLines('''* Toleranzen nach ISO 2768-1 Klasse m (mittel).
                                   ''')
        c.drawText(textobject1)

        # textobject1 = c.beginText()
        # textobject1.setTextOrigin(0.75*inch, 0.38*inch)
        # c.setFillColor(colors.black)
        # textobject1.setFont("FrutigerR", 5)
        # textobject1.textLines('''Tolerances according to ISO 2768-1 class m (middle).
        #                            ''')
        # c.drawText(textobject1)
        textobject1 = c.beginText()
        textobject1.setTextOrigin(0.8*inch, 0.27*inch)
        c.setFillColor(colors.black)
        textobject1.setFont("FrutigerR", 5)
        textobject1.textLines('''Das CTP ® Seil ist nur für die Nutzung auf Treib- und Ablenkscheiben, welche die obigen Anforderungen erfüllen, zertifiziert.''')
        c.drawText(textobject1)


        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("Helvetica-Bold",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        #page 6
        c.drawImage(page6BG, 0,0, width=width, height=height, mask='auto')
        c.setFont('FrutigerB', 25)
        c.drawString(50, 7.8*inch, "APAG")

        c.setFont('FrutigerR', 13)
        c.drawString(125, 7.8*inch, "Anpress-Aussengewinde")


        textobject = c.beginText()
        textobject.setTextOrigin(3.1*inch, 6.5*inch)
        textobject.setFont("FrutigerB", 12)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            Produktdaten''')
        c.drawText(textobject)

        # textobject = c.beginText()
        # textobject.setTextOrigin(3*inch, 6.25*inch)
        # textobject.setFont("FrutigerR", 9)
        # lyrics = [' APAG-Seilendverbindungen sind TÜV-getestet und nach EN81 entsprechend zugelassen',
        #           ' APAG-Seilendverbindungen übertragen 80% der Mindestbruchkraft des Tragseils',
        #           ]
        # for line in lyrics:
        #     textobject.textLine(". %s" %(line))
        # c.drawText(textobject)



        list = '''<ul>
                    <li> APAG-Seilendverbindungen sind TÜV-getestet und nach EN81 entsprechend zugelassen</li>
                    <li> PAG-Seilendverbindungen übertragen 80% der Mindestbruchkraft des Tragseils</li>
                  </ul>
               '''
        height2 = htmlRMLCanvvas(list,c,3.75*inch,3*inch, 6.4*inch,styles['Normal'],colors.black,lang)


        textobject = c.beginText()
        textobject.setTextOrigin(3.1*inch, 5.4*inch)
        textobject.setFont("FrutigerB", 12)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            				 		 Vorteile''')
        c.drawText(textobject)
        # textobject = c.beginText()
        # textobject.setTextOrigin(3*inch, 5.475*inch)
        # textobject.setFont("FrutigerR", 9)
        # lyrics = [' einfache, schnelle und sichere Endbefestigungen ',
        #           ' verkürzte Montagezeit, da bauseitige Montage der Endverbindung entfällt',
        #           ' keine Spezialwerkzeuge erforderlich',
        #           ' ie kompakte Bauweise ermöglicht ein sehr enges Lochbild der Seilaufnahme und',
        #           ' parallel laufende Seile',
        #           ' einfache Sicherung gegen Verdrehen',
        #           ' Lage-Kontrollbohrung für Seilende ',
        #           ' keine Geräuschentwicklung, da keine Einzelteile ',
        #
        #           ]
        # for line in lyrics:
        #     textobject.textLine(". %s" %(line))
        #
        # c.drawText(textobject)

        list = '''<ul>
                    <li> einfache, schnelle und sichere Endbefestigungen</li>
                    <li> verkürzte Montagezeit, da bauseitige Montage der Endverbindung entfällt</li>
                    <li> keine Spezialwerkzeuge erforderlich</li>
                    <li> ie kompakte Bauweise ermöglicht ein sehr enges Lochbild der Seilaufnahme und</li>
                    <li> parallel laufende Seile</li>
                    <li> einfache Sicherung gegen Verdrehen</li>
                    <li> Lage-Kontrollbohrung für Seilende</li>
                    <li> keine Geräuschentwicklung, da keine Einzelteile</li>
                  </ul>
               '''
        height2 = htmlRMLCanvvas(list,c,3.75*inch,3*inch, 5.25*inch,styles['Normal'],colors.black,lang)


        c.setFont("Helvetica-Bold", 7)

        c.drawString(3.2*inch, 3.1*inch, "Für den Einsatz mit CTP ® 6.5 mm")

        data = [

           ['Art.-Nr.', 'd1', 'd2',  'd3' , "d4","L1","L2","L3","L4"],
           ['',   '',  '','',''      'Abmessungen in mm',         '',     ' ',     ],
           ['10209',   'M 10', '13','9','7','240','150','66.0','16.6'],


           ]

        t5 = Table(data, colWidths=[1.25* cm, 1.25* cm, 1.25 * cm,
                                    1.25* cm, 1.25* cm,1.25* cm,1.25* cm,1.25* cm, ],rowHeights=5*mm)
        t5.setStyle(TableStyle([
                             ('LINEABOVE',(0,2),(-1,-1),0.25,colors.black),
                             ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                             ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                            ('FONTSIZE', (0, 0), (-1, -1), 6),
                             ('FONTNAME', (0, 0), (1,0), "Helvetica-Bold"),
                             ('FONTNAME', (2, 0), (3,0), "Helvetica-Bold"),
                             ('FONTNAME', (4,0), (5,0), "Helvetica-Bold"),
                             ('FONTNAME', (6, 0), (7,0), "Helvetica-Bold"),
                            ('FONTNAME', (0,0),(8, 0), "Helvetica-Bold"),

                            # ('BACKGROUND', (1,2), (1, 3), '#DCDCDC'),
                            # ('BACKGROUND', (1,4), (1, 5), '#DCDCDC'),
                             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
                            ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),

                             ]))

        t5.wrapOn(c, 30, 300)
        t5.drawOn(c, 3.2*inch,2.25*inch)
        c.setFont("Helvetica-Bold", 7)
        c.drawString(3.2*inch, 1.7*inch, "Fur den Einsatz mit CTP 8.1mm")

        data = [

           ['Art.-Nr', 'd1', 'd2',  'd3' , "d4","L1","L2","L3","L4"],
           ['',   '',  '','',''      'Abmessungen in mm',         '',     ' ',     ],
           ['10113',   'M 10', '13','9','7','240','150','66.0','16.6'],
           ]

        t5 = Table(data, colWidths=[1.25* cm, 1.25* cm, 1.25 * cm,
                                    1.25* cm, 1.25* cm,1.25* cm,1.25* cm,1.25* cm, ],rowHeights=5*mm)
        t5.setStyle(TableStyle([
                             ('LINEABOVE',(0,2),(-1,-1),0.25,colors.black),
                             ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                             ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                            ('FONTSIZE', (0, 0), (-1, -1), 6),
                             ('FONTNAME', (0, 0), (1,0), "Helvetica-Bold"),
                             ('FONTNAME', (2, 0), (3,0), "Helvetica-Bold"),
                             ('FONTNAME', (4,0), (5,0), "Helvetica-Bold"),
                             ('FONTNAME', (6, 0), (7,0), "Helvetica-Bold"),
                            ('FONTNAME', (0,0),(8, 0), "Helvetica-Bold"),

                             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
                            ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),

                             ]))

        t5.wrapOn(c, 30, 300)
        t5.drawOn(c, 3.2*inch,0.9*inch)


        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("FrutigerB",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1


        #page 7

        c.drawImage(page7BG, 0,0, width=width, height=height, mask='auto')

        c.setFont('FrutigerB', 18.5)
        c.drawString(50, 7.6*inch, "SEILSCHLOSS")

        c.setFont('FrutigerR', 13)
        c.drawString(210, 7.6*inch, "asymmetrisch [ähnlich EN 13411-6]")


        textobject = c.beginText()
        textobject.setTextOrigin(4.5*inch, 6.65*inch)
        textobject.setFont("FrutigerB", 12)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            Produktdaten''')
        c.drawText(textobject)
        textobject = c.beginText()
        textobject.setTextOrigin(4.4*inch, 6.375*inch)
        textobject.setFont("FrutigerR", 9)
        lyrics = [' Seilschloss gegossen, Stahl verzinkt',
                  ' nkl. Keil, Sicherungssplinten vormontiert',
                  ' Seilschloss überträgt 80% der Mindestbruchkraft des Seiles',
                  ' Gewindestange, Stahl verzinkt',
                  ' für Montage und Betrieb gelten die Ausführungen in',
		          ' Anhang C der Norm EN 13411-6',
                  ]
        for line in lyrics:
            textobject.textLine(". %s" %(line))

        c.drawText(textobject)
        textobject = c.beginText()
        textobject.setTextOrigin(4.5*inch, 4.65*inch)
        textobject.setFont("FrutigerB", 12)
        textobject.setFillColorRGB(0,0,0)
        textobject.textLines('''
                            Vorteile''')
        c.drawText(textobject)
        textobject = c.beginText()
        textobject.setTextOrigin(4.4*inch, 4.4*inch)
        textobject.setFont("FrutigerR", 9)
        lyrics = [' sicher und einfach vor Ort montierbar ',
                  ' Federn, Puffer oder andere Zubehörteile können',
                  ' individuell aufgebracht werden',
        ]
        for line in lyrics:
            textobject.textLine(". %s" %(line))
        c.drawText(textobject)

        c.setFont("FrutigerB", 7)
        c.drawString(4.5*inch, 3.5*inch, "Für den Einsatz mit CTP ® 6.5 mm")

        data = [

           ['Art.-Nr','', 'Seil-ø', 'd',  'd1',"L1","L2","L3"],
           ['',   '','mm',  '','',''      '',         '',     ' ',     ],
           ['64109',  'A', '5,0-6,5','M 10', '','265','180'],
           ['64115',    'D', '5,0-6,5','M 10', '23','265','180','85,5']


           ]

        t5 = Table(data, colWidths=[1* cm, 1* cm, 1 * cm,
                                    1* cm, 1* cm,1* cm,1* cm,1* cm, ],rowHeights=5*mm)
        t5.setStyle(TableStyle([
                             ('LINEABOVE',(0,2),(-1,-1),0.25,colors.black),
                             ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                             ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                            ('FONTSIZE', (0, 0), (-1, -1), 5),
                             ('FONTNAME', (0, 0), (1,0), "FrutigerB"),
                             ('FONTNAME', (2, 0), (3,0), "FrutigerB"),
                             ('FONTNAME', (4,0), (5,0), "FrutigerB"),
                             ('FONTNAME', (6, 0), (7,0), "FrutigerB"),
                             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
                            ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                            ('BACKGROUND', (2,0),(2, 5), '#DCDCDC')
                             ]))

        t5.wrapOn(c, 30, 300)
        t5.drawOn(c, 4.5*inch,2.5*inch)
        textobject1 = c.beginText()
        textobject1.setTextOrigin(4.5*inch, 2.35*inch)
        c.setFillColor(colors.black)
        textobject1.setFont("FrutigerR", 6)
        textobject1.textLines(''' Weitere Abmessungen auf Anfrage.
                                  Artikelnummern für alle Kombinationsmöglichkeiten entnehmen Sie bitte im Hauptkatalog Aufzugseile.   ''')
        c.drawText(textobject1)
        c.setFont("FrutigerB", 7)

        c.drawString(4.5*inch, 1.9*inch, "Für den Einsatz mit CTP ® 8.1 mm")

        data = [

           ['Art.-Nr.','', 'Seil-@', 'd',  'd1',"L1","L2","L3"],
           ['',   '','mm',  '','',''      '',         '',     ' ',     ],
           ['64109',  'A', '5,0-6,5','M 10', '','265','180'],
           ['64115',    'D', '5,0-6,5','M 10', '23','265','180','85,5']
           ]

        t5 = Table(data, colWidths=[1* cm, 1* cm, 1 * cm,
                                    1* cm, 1* cm,1* cm,1* cm,1* cm, ],rowHeights=5*mm)
        t5.setStyle(TableStyle([
                             ('LINEABOVE',(0,2),(-1,-1),0.25,colors.black),
                             ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                             ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                            ('FONTSIZE', (0, 0), (-1, -1), 5),
                             ('FONTNAME', (0, 0), (1,0), "FrutigerB"),
                             ('FONTNAME', (2, 0), (3,0), "FrutigerB"),
                             ('FONTNAME', (4,0), (5,0), "FrutigerB"),
                             ('FONTNAME', (6, 0), (7,0), "FrutigerB"),
                             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
                            ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                            ('BACKGROUND', (2,0),(2, 5), '#DCDCDC'),


                             ]))

        t5.wrapOn(c, 30, 300)
        t5.drawOn(c, 4.5*inch,0.9*inch)

        textobject1 = c.beginText()
        textobject1.setTextOrigin(4.5*inch,0.75*inch)
        c.setFillColor(colors.black)
        textobject1.setFont("FrutigerR", 5)
        textobject1.textLines('''Weitere Abmessungen auf Anfrage.
                                 Artikelnummern für alle Kombinationsmöglichkeiten entnehmen Sie bitte im Hauptkatalog Aufzugseile.''')
        c.drawText(textobject1)

        d = c.beginPath()
        d.rect(-20, 7.25*inch, 10*inch, 0.6*inch)
        d.rect(700, 7.25*inch, 12.5*inch, 0.2*inch)
        c.clipPath (d, stroke=0)
        # c.linearGradient(100*mm,200*mm,100*mm,60*mm, ('#996515','#DAA520','#996515'),extend=False)
        c.setFont("FrutigerR", 10)
        c.drawString(90,450, "Anpress-Ausssengewinden")
        c.setFont("FrutigerB", 18)
        # c.drawString(30,535, "APAG")
        c.setFont("FrutigerB", 18)
        c.drawString(400,450, "SEILSCHLOSS")
        c.setFont("FrutigerR", 10)
        c.drawString(530,450, "symmetrisch [EN-13411-7]")


        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("FrutigerB",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        #page 8

        # gemImg = "germanp8a.png"
        gemImg = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/ctpCatalog',"germanp8a.png")
        c.drawImage(page8BG,0,0,width=width,height=height, mask='auto')

        c.drawImage(gemImg,30,0.6*inch,width=8*inch,height=3*inch, mask='auto')

        c.setFont('FrutigerB', 20.5)
        c.drawString(40, 7.75*inch, "CTP ® PRÜFHANDBUCH")

        p = Paragraph('''<para fontName= FrutigerR fontsize=10  leading=13 align="justify">Dieses Dokument dient als Leitfaden für Kontrollen von CTP ® Seilen. Es beschreibt die offiziellen Ablegekriterienfür CTP ® -Seile sowie bestimmte Bereiche der Kontrolle bei einem laufenden Aufzugssystem. Diese Prüfungen sind massgeblich für die Lebensdauer und Betriebssicherheit.</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,6.25*inch)

        # textobject = c.beginText()
        # textobject.setTextOrigin(0.5*inch,  5.5*inch)
        # c.setFont('FrutigerB', 11)
        # c.setFillColorRGB(0,0,0)
        # textobject.textLines('''
        # 1. Discard criteria of the CTP rope''')
        # c.drawText(textobject)

        p = Paragraph('''<para fontName= FrutigerB fontsize=10  leading=13 align="justify">1. Ablegekriterien für CTP ® Seile</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,5.85*inch)

        p = Paragraph('''<para fontName= FrutigerR fontsize=10  leading=13 align="justify">Brugg Lifting wendet einfache Ablegekriterien an, durch die der Einsatz des CTP ® Seils auf eine bestimmte Anzahl an Fahrten (1) beschränkt ist. Diese Methode der Bewertung ba- siert damit auf der Nutzungsintensität.</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,5.1*inch)

        p = Paragraph('''<para fontName= FrutigerR fontsize=10  leading=13 align="justify">This discard criterion forms part of all CTP   rope certifications,
        which have been issued by LIFTINSTITUUT  The calculation of
        maximum allowed trips is described under chapter  conditions
        as follows:</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,4.2*inch)


        p = Paragraph('''<para fontName= FrutigerR fontsize=10  leading=13 align="justify">Die festgelegte maximale Anzahl von Biegewechsel wird durch die Anzahl an Rollen, die von dem am stärksten gebogenen Teil des Seils passiert werden, geteilt</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,3.6*inch)


        p = Paragraph('''<para fontName= FrutigerR fontsize=8  leading=10 align="justify">Unbeschädigte Seile im Aufzugs- schaft. Beachten Sie, dass während der gesamten Lebensdauer des Seils keine Farbveränderung der Ummantelung eintritt. Das Seil bleibt tiefschwarz.</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=1.9*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,440,6*inch)


        p = Paragraph('''<para fontName= FrutigerR fontsize=9  leading=10 align="justify">Während der Seil-Kontrolle sollte stets eine Prüfung auf Verschleiss oder Beschädigungen (2) erfolgen. In der Tabelle werden fünf typischen Probleme von beschädigten Seilen dargestellt und die entsprechenden Massnahmen, die von der Wartungsfirma in einem solchen Fall zu ergreifen sind.</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.5*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,325,5*inch)

        p = Paragraph('''<para fontName= FrutigerR fontsize=7  leading=10 align="justify">((1) Jede Richtungsänderung wird von der Aufzugssteuerung als eine Fahrt oder ein Lastwechseln gezählt. Wichtig: „Fahrt“ oder „Lastwechseln“ darf NICHT mit „Starts“ verwechselt werden.</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.5*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,325,4.4*inch)


        p = Paragraph('''<para fontName= FrutigerR fontsize=7  leading=10 align="justify">(2) 	Übermässiger Verschleiss oder Beschädigungen, wie unten dargestellt, können durch Überlast, ungleich verteilte Seilspannung, starke Stösse, unsymmetrische Torsionsspannung, schlechte Ausrichtung des Seils etc. verursacht werden. Die in den Anweisungen festgelegte maximale Anzahl an Drahtbrüchen basiert auf Normen (UNE-EN, ISO, DIN) sowie auf einer Prüfung mittels Stichproben.</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.5*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,325,3.65*inch)


        # p1 = ['Beschreibung der Kunststoffummantelung']
        #
        #
        # c.setFillColor('#EEE8AA')
        # c.rect(18, 0.68*inch, 8*inch, 2.4*inch,stroke=0,fill=1)
        #
        # c.drawString(30,150,'Ablegekriterien')


        # textobject = c.beginText()
        # textobject.setTextOrigin(0.4*inch,  2.9*inch)
        # c.setFont('FrutigerB', 9)
        # c.setFillColorRGB(0,0,0)
        # textobject.textLines('''
        # Ablegekriterien''')
        # c.drawText(textobject)
        #
        #
        # # Headers
        # hdescrpcion = Paragraph('''<para align = "RIGHT">|</para>''', stylesN)
        # hpartida = Paragraph('<para fontsize=7 align = "CENTER"><b>A</b></para>', stylesN)
        # h1 = Paragraph('''<para align = "LEFT">|</para>''', stylesN)
        # hcandidad = Paragraph('<para fontsize=7 align = "CENTER" leftindent = -5 align="LEFT"><b>B</b></para>', stylesN)
        # h2 = Paragraph('''|''', stylesN)
        # hprecio_unitario = Paragraph('<para fontsize=7 leftindent = -40 align="LEFT"><b>C</b></para>', stylesN)
        # h3 = Paragraph('''<para  leftindent = -130 align = "CENTER">|</para>''', stylesN)
        # hprecio_total = Paragraph('<para fontsize=7 align="CENTER" leftindent = -140 align="CENTER"><b>D</b></para>', stylesN)
        # h4 = Paragraph('''<para  align = "LEFT" leftindent = -70>|</para>''', stylesN)
        # hprecio_empty1 = Paragraph(''+''' ''', stylesN)
        # hprecio_empty2 = Paragraph(''+''' ''', stylesN)
        #
        #
        # descrpcion = Paragraph('<para fontsize=5><b>Problem</b></para>', styleN)
        # partida = Paragraph('<para fontsize=5>Beschadigung der <br\>Kunststoffummantelung</para>', styleN)
        # candidad = Paragraph('<para fontsize=5>Drahbruch</para>', styleN)
        # precio_unitario = Paragraph('<para fontsize=4>Massive Bruche von Drahten</para>', styleN)
        # precio_total = Paragraph('<para fontsize=4>Litzenbrunch</para>', styleN)
        # precio_empty1 = Paragraph('<para fontsize=4>Seil aus der Rille</para>', styleN)
        # precio_empty2 = Paragraph('<para fontsize=4> Image1 </para>', styleN)
        # # precio_empty3 = Paragraph('<para fontsize=4> Image2 </para>', styleN)
        #
        #
        # descrpcio = Paragraph('<para fontsize=5><b>Beschreibung</b></para>', styleN)
        # partid = Paragraph('<para fontsize=4>Kunststoffummantelung ist so <br/>abgenutzt, dass der mettallische</para>', styleN)
        # candida = Paragraph('<para fontsize=4>Mehr als 10 Drahte ragen<br/>aus dem TPU-Mantel</para>', styleN)
        # precio_unitari = Paragraph('<para fontsize=4>Mehr als 3 Drahte ragen aus   dem</para>', styleN)
        # precio_tota = Paragraph('<para fontsize=4>spezifischer Seilbruch</para>', styleN)
        # precio_empty = Paragraph('<para fontsize=4>Seil ist aus seiner<br/>ursprunglichen Rille</para>', styleN)
        # # precio_empty = Paragraph('<para fontsize=4> Image1 </para>', styleN)
        #
        #
        # descrpci = Paragraph('<para fontsize=5><b>Korrektur-massnahme</b></para>', styleN)
        # parti = Paragraph('<para fontsize=4>Bericht an<br/>Brugg Lifting senden.</para>', styleN)
        # candid = Paragraph('<para fontsize=4>Bericht an<br/>Brugg Lifting senden.</para>', styleN)
        # precio_unitar = Paragraph('<para fontsize=4>Bericht an<br/>Brugg Lifting senden.</para>', styleN)
        # precio_tot = Paragraph('<para fontsize=4>Bericht anBericht an<br/>Brugg Lifting senden.</para>', styleN)
        # precio_empt = Paragraph('<para fontsize=4>Bericht an<br/>Brugg Lifting senden.</para>', styleN)
        # precio_empt = Paragraph('<para fontsize=4> Image1 </para>', styleN)
        #
        #
        # descrpc = Paragraph('<para fontsize=5><b>Zeitskala</b></para>', styleN)
        # part = Paragraph('<para fontsize=4>< 2 Monate</para>', styleN)
        # candi = Paragraph('<para fontsize=4>2 Monate</para>', styleN)
        # precio_unita = Paragraph('<para fontsize=4>umgehend</para>', styleN)
        # precio_to = Paragraph('<para fontsize=4>umgehend</para>', styleN)
        # precio_emp = Paragraph('<para fontsize=4>umgehend</para>', styleN)
        # # precio_emp = Paragraph('<para fontsize=4> Image1 </para>', styleN)
        #
        #
        # data= [[hdescrpcion, hpartida,h1,hcandidad,h2,hprecio_unitario,h3, hprecio_total,h4, hprecio_empty1,hprecio_empty2],
        #        [descrpcion, partida, candidad, precio_unitario, precio_total,precio_empty1],
        #        [descrpcio,partid,candida,precio_unitari,precio_tota,precio_empty],
        #        [descrpci,parti,candid,precio_unitar,precio_tot,precio_empt],
        #        [descrpc,part,candi,precio_unita,precio_to,precio_emp]]
        #
        # table = Table(data, colWidths=[1.6 * cm, 2.5 * cm, 2 * cm,
        #                                2.25* cm, 2.5 * cm, 2*cm,1*cm,1.45*cm],rowHeights =12*mm)
        #
        # table.setStyle(TableStyle([
        #                             ('LINEABOVE',(0,1),(-1,1),0.25,colors.black),
        #                             ('SPAN',(2,0),(2,0)),
        #                             ('LINEBELOW',(0,1),(5,4),0.25,colors.black),
        #                             ('LINEBELOW',(0,4),(-1,-1),0.25,colors.black),
        #                             ('FONTSIZE', (0, 1), (-1, -1), 5),
        #                        ]))
        #
        # table.wrapOn(c, width, height)
        # table.drawOn(c, 17, 60, cm)

        # c.drawImage(logo13,6.15*inch,1.3*inch,width=0.45*inch,height=1.3*inch)
        # c.drawImage(logo14,6.65*inch,1.3*inch,width=0.45*inch,height=1.3*inch)
        # c.drawImage(logo15,7.15*inch,1.3*inch,width=0.45*inch,height=1.3*inch)
        # c.drawImage(logo16,7.65*inch,1.3*inch,width=0.45*inch,height=1.3*inch)




        p = c.beginPath()
        p.rect(-20, 7.25*inch, 4*inch, 0.9*inch)
        p.rect(268, 7.25*inch, 8*inch, 0.2*inch)

        c.clipPath(p, stroke=0)
        # c.linearGradient(100*mm,200*mm,100*mm,60*mm, ('#996515','#DAA520','#996515'),extend=False)
        c.setFont('FrutigerB', 17)
        c.setFillColor(colors.black)
        c.drawString(20,465,"CTP PRUFHANDBUCH")

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("FrutigerB",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        #page9

        # gemImg2 = "germanp9b.png"
        gemImg2 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images/ctpCatalog',"germanp9b.png")
        c.drawImage(page9BG,0,0,width=width,height=height, mask='auto')

        c.drawImage(gemImg2,0,0.6*inch,width=3.8*inch,height=3*inch, mask='auto')

        p = Paragraph('''<para fontsize=9 fontName=FrutigerB leading=13 align="justify">2.Spezifikationen der Aufzugsanlage </para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.5*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,6.85*inch)

        p = Paragraph('''<para fontsize=9  leading=13 align="justify">Nur an Hand der spezifischen Daten der Aufzugsanlage sind wir in der Lage, das Seil bezüglich Zugkraft,Biegewechsel-festigkeit etc., zu analysieren.Wenden Sie sich daher im Falledes Supports an Ihren Brugg Lifting-Ansprechpartner. </para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.5*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,5.9*inch)

        # c.setFillColor('#EEE8AA')
        # c.rect(30, 3.35*inch, 3.9*inch, 2.25*inch,stroke=0,fill=1)

        p = Paragraph('''<para fontsize=8 fontName=FrutigerB leading=13 align="justify">Sicherheitshinweise</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.5*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,40,5.65*inch)


        p = Paragraph('''<para fontsize=7 leading=13 align="justify">Die meisten dieser Prüfungen sind bei laufendem Aufzug(im Wartungsmodus) durchzuführen! Die unten aufgeführtenMessungen dürfen nur in Anwesenheit von geschultem undautorisiertem Personal durchgeführt werden. Sorgen Sie dafür,dass Sie stets gesichert sind, wenn Sie auf dem Dach des Fahr-korbs stehen.</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.3*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,40,4.75*inch)


        p = Paragraph('''<para fontsize=7 leading=13 align="justify">CTP ® Seile dürfen nicht betrieben werden, wenn sich Öl oderWasser auf der Seiloberfläche befindet. Falls sich Wasser oder Ölauf der Seiloberfläche befindet und dann mit der Treibscheibe inKontakt kommt, wird dadurch die Treibfähigkeit reduziert undeinen Seilschlupf verursachen.</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.3*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,40,3.85*inch)


        p = Paragraph('''<para fontsize=10 fontName=FrutigerB leading=13 align="justify">3. Visual inspection</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.3*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,325,  6.9*inch)


        p = Paragraph('''<para fontsize=10  leading=13 align="justify">Zusätzlich sind externe Faktoren, die sich auf das Seil negativ auswirken können, auszuwerten. Vor detaillierten Messungen sollte zuerst eine Sichtprüfung des Seils erfolgen. Dabei ist ein besonderer Augenmerk auf die Seilummantelung zu legen:</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.5*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,325,5.8*inch)


        # textobject = c.beginText()
        # textobject.setTextOrigin(4.5*inch, 5.45*inch)
        # c.setFont('Helvetica', 9)
        # c.setFillColorRGB(0,0,0)
        #
        # dat = [
        # 'Gebrochene Drähte die, die Ummantelung durchbohren',
        # 'Unregelmässigkeiten auf der Oberflächenbeschichtung',
        # 'des Seils (Dellen, Kerben oder ähnliches)',
        # 'Kratzer, Risse oder Bruchstellen auf der Seilummantelung',
        # 'Abrieb der Beschichtung (TPU-Staub auf dem Seil oder',
        # 'auf der Scheibe)',
        # 'Staub, Öl, Wasser etc. auf dem Seilmantel',
        # 'Seilquetschung, Seilverdrehung, Knick',
        # ]
        #
        # for i in dat:
        #     textobject.textLines("- %s"%(i))
        #
        # c.drawText(textobject)


        list = '''<ul>
                    <li>Gebrochene Drähte die, die Ummantelung durchbohren</li>
                    <li> Unregelmässigkeiten auf der Oberflächenbeschichtung</li>
                    <li> des Seils (Dellen, Kerben oder ähnliches)</li>
                    <li> Kratzer, Risse oder Bruchstellen auf der Seilummantelung</li>
                    <li> Abrieb der Beschichtung (TPU-Staub auf dem Seil oderauf der Scheibe)</li>
                    <li> Staub, Öl, Wasser etc. auf dem Seilmantel</li>
                    <li> Seilquetschung, Seilverdrehung, Knick</li>
                  </ul>
               '''
        height2 = htmlRMLCanvvas(list,c,3.75*inch,4.5*inch, 5.75*inch,styles['Normal'],colors.black,lang)

        # textobject = c.beginText()
        # textobject.setTextOrigin(4.5*inch, 4.2*inch)
        # c.setFont('Helvetica', 9)
        # c.setFillColorRGB(0,0,0)
        # textobject.textLines('''
        # Die folgenden Punkte sind ebenfalls zu überwachen:
        # ''')
        # c.drawText(textobject)


        p = Paragraph('''<para fontsize=10  fontName=FrutigerR leading=13 align="justify">Die folgenden Punkte sind ebenfalls zu überwachen:</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.5*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,4.5*inch, 3.8*inch)


        # textobject = c.beginText()
        # textobject.setTextOrigin(4.5*inch, 3.85*inch)
        # c.setFont('Helvetica', 9)
        # c.setFillColorRGB(0,0,0)
        #
        # data = [
        # 'Kommen Seile mit Teilen des Aufzugs oder dem Schaft in',
        # ' Berührung (Seile müssen frei laufen)',
        # 'Seile berühren einander wegen elektrostatischer Ladung',
        # 'Seilschwingung während des Betriebs',
        # 'Unzureichende Ausrichtung der Treibscheibe und/oder der',
        # 'Umlenkrolle (Schrägzug beachten)',
        # ]
        #
        # for i in data:
        #     textobject.textLines("- %s"%(i))
        #
        # c.drawText(textobject)



        list = '''<ul>
                    <li>Kommen Seile mit Teilen des Aufzugs oder dem Schaft</li>
                    <li> Kommen Seile mit Teilen des Aufzugs oder dem Schaft in Berührung (Seile müssen frei laufen)</li>
                    <li>Seile berühren einander wegen elektrostatischer Ladung</li>
                    <li>Seilschwingung während des Betriebs</li>
                    <li>Unzureichende Ausrichtung der Treibscheibe und/oder der Umlenkrolle (Schrägzug beachten)</li>
                  </ul>
               '''
        height2 = htmlRMLCanvvas(list,c,3.75*inch,4.5*inch, 3.75*inch,styles['Normal'],colors.black,lang)


        p = Paragraph('''<para fontsize=10  leading=13 align="justify">Soweit möglich sollten während der Sichtprüfung Fotos des Seils gemacht werden (auch im Fall von intakten Seilen). Ebenso sollten die Treibscheibe, die Umlenkrolle und die End-befestigungen fotografiert werden.</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.5*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,325,1.5*inch)

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("FrutigerB",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1




        #page 10
        c.drawImage(page10BG,0,0,width=width,height=height, mask='auto')

        textobject = c.beginText()
        textobject.setTextOrigin(0.5*inch,  6.75*inch)
        c.setFont('FrutigerB', 12)
        c.setFillColorRGB(0,0,0)
        textobject.textLines('''
        4. Prüfung des Ablenkwinkels''')
        c.drawText(textobject)

        c.setFont('FrutigerB', 21.5)
        c.drawString(40, 7.85*inch, "CTP ® PRÜFHANDBUCH")



        p = Paragraph('''<para fontName=FrutigerR fontsize=10  leading=13 align="justify">Der(gemäss unserer Zertifizierung)zulässige Schrägzugwinkel beträgt 0,5°. Falls der Schrägzugwinkel zu gross ist, führt dies zu Torsionsmomenten im Seil. Diese Auswirkung gilt auch bei herkömmlichen Seilen, ist jedoch noch ausgeprägter bei dem CTP ® Seil. </para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,5.7*inch)


        p = Paragraph('''<para fontName=FrutigerR fontsize=10  leading=13 align="justify">Die kritischsten Positionen sind, wenn der Fahrkorb sich in derobersten Position befindet (maximaler Schrägzugwinkel zwi- schen Fahrkorb und Treibscheibe/Umlenkrolle) und wenn der Fahrkorb sich in der untersten Position befindet (maximaler Schrägzugwinkel zwischen Gegengewicht und Treibscheibe/ Umlenkrolle). Eine direkte Messung des Schrägzugwinkels zwischen Seil und Scheibe ist in der Praxis sehr schwierig. Aus diesem Grund empfehlen wir eine indirekte Messung des Schrägzugwinkels (siehe unten).</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,3.75*inch)


        p = Paragraph('''<para fontName=FrutigerR fontsize=10  leading=13 align="justify">Für eine grobe Schätzung des Schrägzugwinkels sind die folgenden Punkte zu messen (dargestellt auf einem Aufzug mit 1:1 Aufhängung):</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,3*inch)

        p = Paragraph('''<para fontName=FrutigerR fontsize=10  leading=13 align="justify">Abstand zwischen Treibscheibe und Endbefestigung am Fahrkorb (wenn Fahrkorb sich in der obersten Position befindet</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,2.3*inch)

        p = Paragraph('''<para fontName=FrutigerR fontsize=10  leading=13 align="justify">Abstand zwischen den Seilen an der Seilbefestigung am Fahrkorb und an der Treibscheibe. Abstand zwischen den Seilen an der Treibscheibe (Abstand zwischen Rillen) und an der Seilbefestigung am Gegengewicht </para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,1.5*inch)

        p = Paragraph('''<para fontName=FrutigerR fontsize=10  leading=13 align="justify">Abstand zwischen Treibscheibe und Endbefestigung am Gegengewicht (wenn Korb sich in der untersten Position befindet)</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,0.85*inch)

        textobject = c.beginText()
        textobject.setTextOrigin(8.6*inch, 0.7*inch)
        c.setFont('FrutigerR', 7)
        c.setFillColorRGB(0,0,0)
        textobject.textLines('''
        Seilspannungsmessgerat Brugg RPM
        ''')
        c.drawText(textobject)

        p = c.beginPath()
        p.rect(0.3*inch,1.2*inch, 0.1*inch, 0.1*inch)
        p.rect(0.3*inch,1.8*inch,0.1*inch, 0.1*inch)
        p.rect(0.3*inch,2.3*inch, 0.1*inch, 0.1*inch)
        p.rect(-20, 7.25*inch, 4*inch, 0.9*inch)
        p.rect(268, 7.25*inch, 8*inch, 0.2*inch)

        c.clipPath(p, stroke=0)

        # c.setFont('FrutigerR', 7)
        # c.drawString(23,87,"3")
        #
        # c.setFont('FrutigerR', 7)
        # c.drawString(23,130,"2")
        #
        # c.setFont('FrutigerR', 7)
        # c.drawString(23,167,"1")

        c.setFont('FrutigerB', 17)
        c.drawString(20,465,"CTP PRUFHANDBUCH")

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("FrutigerB",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1

        #page 11
        c.drawImage(page11BG,0,0,width=width,height=height, mask='auto')
        # textobject = c.beginText()
        # textobject.setTextOrigin(0.5*inch,  6.7*inch)
        # c.setFont('FrutigerB', 12)
        # c.setFillColorRGB(0,0,0)
        # textobject.textLines('''5. Inspection of groove shape
        # (traction sheave and diverting pulley)''')
        # c.drawText(textobject)

        p = Paragraph('''<para fontName=FrutigerB fontsize=9 >5. Prüfung der Rillenform<br/>
(Treibscheibe und Umlenkrolle)</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,0.4*inch,  6.75*inch)


        p = Paragraph('''<para fontName=FrutigerR fontsize=10  leading=13 align="justify">Selbst wenn die Rillen der Treibscheibe und der Umlenk-
rolle nach Zeichnung hergestellt werden (Radius für
CTP ® 6.5: 3,4 – 3,65 mm, Radius für CTP ® 8.1: 4,3 mm),
empfehlen wir dringend, die Form mit der speziell konzi-
pierten Brugg Rillenlehre zu prüfen. Brugg Lifting bietet
eine massgeschneiderte Lehre, welche den 45° (30° - 45°
für CTP ® 6.5) Öffnungswinkel, wie in unser CTP ® Zertifi-
zierung angegeben, umfasst.</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,30,5.3*inch)

        p = Paragraph('''<para fontName=FrutigerB fontsize=10 >6. Seilspannung</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,320,  6.9*inch)



        p = Paragraph('''<para fontName=FrutigerR fontsize=10  leading=13 align="justify">Auch wenn die Seilspannung häufig per Hand gemessen
wird (durch Rupfen am Seil und Beurteilung nach „Gefühl“)
ist diese Methode alles andere als genau. Der Vergleich der
Federpuffer miteinander ist häufiger genau – wobei nur ein
Teil der Aufzüge mit solchen Federn ausgestattet ist. Die
zuverlässigste Methode zur Messung der Seilspannung ist
die Messung der Spannung am Seil selbst unter Zuhilfenahme
eines geeigneten Messinstrumentes. Es gibt verschiedene
Tools zur Spannungsmessung im Handel. Brugg Lifting
empfiehlt Brugg RPM, das eigene Spezialwerkzeug.</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,320,4.9*inch)

        p = Paragraph('''<para fontName=FrutigerR fontsize=10 >Darüber hinaus ist die Rillenoberfläche auf die folgenden
Mängel hin zu überprüfen:</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,0.4*inch,  4.85*inch)

        p = Paragraph('''<para fontName=FrutigerR fontsize=10 >Rost oder Abrieb auf dem Seilmantel, auf oder um die
Treibscheiben und Umlenkrollen</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,0.5*inch,  4.5*inch)

        p = Paragraph('''<para fontName=FrutigerR fontsize=10 >Nasse Flächen (Wasser, Öl etc.)
Abschliessend sollte möglichst noch geprüft werden, ob
die Gleitlager der Umlenkrollen noch frei laufen.</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,0.5*inch,  4*inch)


        p = Paragraph('''<para fontName=FrutigerR fontsize=10 >Brugg Rillenlehre</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,1.5*inch, 1.25*inch)

        p = Paragraph('''<para fontName=FrutigerR fontsize=10 >Seilspannungsmessgerät Brugg RPM</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1,colWidths=3.75*inch)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,4.75*inch, 1.25*inch)


        p = Paragraph('''<para fontName=FrutigerR fontsize=8 >Erstellungsdatum 03/2019<br/>
Änderungen vorbehalten. Massangaben unverbindlich. Keine Gewährleistung für Druckfehler oder Irrtümer.<br/>
Gestaltung, Umsetzung: schaefer-design.de</para>''',stylesN)
        p1 =[[p]]
        p11 = Table(p1)
        p11.wrapOn(c,width,height)
        p11.drawOn(c,0.9*inch, 0.5*inch)

        # textobject = c.beginText()
        # textobject.setTextOrigin(0.9*inch, 0.75*inch)
        # c.setFont('FrutigerR', 6)
        # c.setFillColorRGB(0,0,0)
        # textobject.textLines('''
        # Creation date 09/2017
        # Subject to changes. Nonbinding indication of measures. No warranty for printing errors or errors.
        # Design, realization: www.schaefer-design.com
        # ''')

        c.drawText(textobject)

        gm934 = Paragraph('<para></para>',stylesN)
        gmn934 = Paragraph('<para></para>',stylesN)

        data =  [[gm934,gmn934]]

        t = Table(data,colWidths=[7*cm,2*cm],rowHeights=5.25*mm)
        t.setStyle(TableStyle([
                            ('LINEABOVE',(0,0),(-1,-1),0.1,colors.black),
                             ]))
        t.wrapOn(c,width, height)


        c.setFillColor(colors.black)
        c.setFont("FrutigerB",10)
        if pageCount%2==0:
            t.drawOn(c, -3*inch,0.2*inch)
            c.drawString(20, 0.15*inch, str(pageCount))
        else:
            t.drawOn(c, width-35,0.2*inch)
            c.drawString(width-30, 0.15*inch, str(pageCount))

        c.showPage()
        pageCount +=1
        if pageCount %2 == 0:
            print "dont worry"
        else:
            c.showPage()
            pageCount +=1
        c.drawImage(page12BG,0,0,width=width,height=height, mask='auto')
        textobject = c.beginText()
        textobject.setTextOrigin(250, 40)
        textobject.setFont("FrutigerB", 12)
        # textobject.setFillColorRGB(192,192,192)
        textobject.setFillColor(colors.white)
        textobject.textLines('''
                                brugglifting.com
                              ''')
        c.drawText(textobject)
        c.showPage()
        c.save()







def get_image(path, width=1*cm):
    img = utils.ImageReader(path)
    iw, ih = img.getSize()
    aspect = ih / float(iw)
    # print(width * aspect), "image height"
    return LabImage(path, width=width, height=(width * aspect))

def addNewPage(c,data1,bg2,product,stylesN,productImage):

    if product.lang == 'zh':
        width,height = A4
        c.drawImage(bg2,0,0,width=width,height=height,mask=None)

        # printproduct.productName, "product name"

        img = utils.ImageReader(productImage)
        iw, ih = img.getSize()
        c.drawImage(productImage,30,height-ih-100,width=150,preserveAspectRatio=True,mask='auto')
        #
        name = Paragraph('<para fontName = STSong-Light fontSize=20>%s</para>'%(product.productName), stylesN)
        nd =[[name]]
        ndt = Table(nd,colWidths=10*cm)
        w1,h1 = ndt.wrapOn(c, width,height)
        height2 = height-h1-100
        ndt.drawOn(c, 50,800)

        # printdata1, "data1 in new page"

        table = Table(data1,rowHeights=[20]*len(data1))
        table.setStyle(TableStyle([
                             ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                             ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                             ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                             ('FONTSIZE', (0, 0), (-1, -1), 7),
                             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                             ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                             ]))
        w5, h5 = table.wrapOn(c, width, height)
        height2 = height - h5 -100
        table.drawOn(c, 200, height2)


        textobject = c.beginText()
        textobject.setTextOrigin(0.3*inch, 1.3*inch)
        textobject.setFont("Helvetica", 7)
        c.setFillColorRGB(255,255,255)
        textobject.textLines('''
                        Ein Unternehemen der Gruppe BRUGG''')
        c.drawText(textobject)


        textobject = c.beginText()
        textobject.setTextOrigin(0.3*inch, 1.15*inch)
        textobject.setFont("Helvetica", 7)
        c.setFillColorRGB(0,0,0)
        textobject.textLines('''
                        A company of the BRUGG Group''')
        c.drawText(textobject)


        textobject = c.beginText()
        textobject.setTextOrigin(0.3*inch, 0.6*inch)
        textobject.setFont("Helvetica", 7)
        c.setFillColorRGB(255,255,255)
        textobject.textLines('''
                        Anderungen vorbehalten. Massangaben unverbindlich.
                        Keine Gewahrleistung fur Druckfehler oder irrtumer.''')
        c.drawText(textobject)

        textobject = c.beginText()
        textobject.setTextOrigin(0.3*inch, 0.35*inch)
        textobject.setFont("Helvetica", 7)
        c.setFillColorRGB(0,0,0)
        textobject.textLines('''Subject to changes.Nonbinding indication of measures.
                            No warranty for printing errors of errors.''')
        c.drawText(textobject)

        textobject = c.beginText()
        textobject.setTextOrigin(5.9*inch, 0.4*inch)
        textobject.moveCursor(14,14)
        textobject.setFont("Helvetica", 15)
        textobject.setFillColor(colors.white)
        textobject.textLines('''
        www.brugglifting.com''')
        c.drawText(textobject)
        c.showPage()

    else:
        width,height = A4
        c.drawImage(bg2,0,0,width=width,height=height,mask=None)

        # printproduct.productName, "product name"

        img = utils.ImageReader(productImage)
        iw, ih = img.getSize()
        c.drawImage(productImage,30,height-ih-100,width=150,preserveAspectRatio=True,mask='auto')
        #
        name = Paragraph('<para fontName = FrutigerB fontSize=20>%s</para>'%(product.productName), stylesN)
        nd =[[name]]
        ndt = Table(nd,colWidths=10*cm)
        w1,h1 = ndt.wrapOn(c, width,height)
        height2 = height-h1-100
        ndt.drawOn(c, 50,800)

        # printdata1, "data1 in new page"

        table = Table(data1,rowHeights=[20]*len(data1))
        table.setStyle(TableStyle([
                             ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                             ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                             ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                             ('FONTSIZE', (0, 0), (-1, -1), 7),
                             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                             ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                             ]))
        w5, h5 = table.wrapOn(c, width, height)
        height2 = height - h5 -100
        table.drawOn(c, 200, height2)


        textobject = c.beginText()
        textobject.setTextOrigin(0.3*inch, 1.3*inch)
        textobject.setFont("Helvetica", 7)
        c.setFillColorRGB(255,255,255)
        textobject.textLines('''
                        Ein Unternehemen der Gruppe BRUGG''')
        c.drawText(textobject)


        textobject = c.beginText()
        textobject.setTextOrigin(0.3*inch, 1.15*inch)
        textobject.setFont("Helvetica", 7)
        c.setFillColorRGB(0,0,0)
        textobject.textLines('''
                        A company of the BRUGG Group''')
        c.drawText(textobject)


        textobject = c.beginText()
        textobject.setTextOrigin(0.3*inch, 0.6*inch)
        textobject.setFont("Helvetica", 7)
        c.setFillColorRGB(255,255,255)
        textobject.textLines('''
                        Anderungen vorbehalten. Massangaben unverbindlich.
                        Keine Gewahrleistung fur Druckfehler oder irrtumer.''')
        c.drawText(textobject)

        textobject = c.beginText()
        textobject.setTextOrigin(0.3*inch, 0.35*inch)
        textobject.setFont("Helvetica", 7)
        c.setFillColorRGB(0,0,0)
        textobject.textLines('''Subject to changes.Nonbinding indication of measures.
                            No warranty for printing errors of errors.''')
        c.drawText(textobject)

        textobject = c.beginText()
        textobject.setTextOrigin(5.9*inch, 0.4*inch)
        textobject.moveCursor(14,14)
        textobject.setFont("Helvetica", 15)
        textobject.setFillColor(colors.white)
        textobject.textLines('''
        www.brugglifting.com''')
        c.drawText(textobject)
        c.showPage()





def generateAccess(request,response,i,prodfield,itemNumbers,itemNumberValues):

    lang = i.lang

    if lang == 'zh':
        product = i
        styles=getSampleStyleSheet()
        stylesN = styles['Normal']
        stylesH =styles['Heading1']
        width,height = A4
        c = Canvas(response,pagesize=A4)
        c.setTitle("Brugglifting_%s"%i.productName)

        if i.backgroundImage1:
            bg1 = i.backgroundImage1.path
        else:
            bg1 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images',"brugg.jpg")
        # rope = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','ropetech.png')
        if i.image2:
            productImage = i.image2.path
        else:
            productImage = os.path.join(globalSettings.BASE_DIR , 'static_shared/images',"stars.jpeg")

        if i.backgroundImage2:
            bg2 = i.backgroundImage2.path
        else:
            bg2 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images',"cables.jpg")



        c.drawImage(bg1,0,0,width=width, height= height,mask='auto')


        name = Paragraph('<para fontName = STSong-Light fontSize=54>%s</para>'%(i.productName), styles['Normal'])
        nd =[[name]]
        w = pdfmetrics.stringWidth(i.productName, "FrutigerB", 54)
        # printw, "text width "
        ndt = Table(nd)
        w1,h1 = ndt.wrapOn(c, width,height)
        width2 = 50
        ndt.drawOn(c, width2,6.45*inch)

        name = Paragraph('<para  fontName = STSong-Light fontSize=12.5>%s</para>'%(i.tagLine), styles['Normal'])
        des =[[name]]
        dest = Table(des,colWidths=8*cm, rowHeights=30*mm)
        w2, h3 = dest.wrapOn(c, width,height)
        # printw2,w1, "tag width"
        width2 = width2 + w +10
        # printwidth2, "tagline width"
        dest.drawOn(c, width2,height-h3-330)

        c.showPage()

        c.drawImage(bg2,0,0,width=width,height=height,mask=None)

        img = utils.ImageReader(productImage)
        iw, ih = img.getSize()
        c.drawImage(productImage,30,height-ih-100,width=150,preserveAspectRatio=True,mask='auto')

        name = Paragraph('<para fontName = STSong-Light fontSize=20>%s</para>'%(i.productName), styles['Normal'])
        nd =[[name]]
        ndt = Table(nd,colWidths=10*cm)
        w1,h1 = ndt.wrapOn(c, width,height)
        height2 = height-h1-100
        ndt.drawOn(c, 50,800)

        name = Paragraph('<para fontName = STSong-Light fontSize=15>%s</para>'%(i.title1), styles['Normal'])
        nd =[[name]]
        ndt = Table(nd,colWidths=10*cm)
        w1,h1 = ndt.wrapOn(c, width,height)
        height2 = height-h1-100
        ndt.drawOn(c, 200,height2)

        height2 = htmlRMLCanvvas(i.desc1,c,10*cm,200,height2,styles['Normal'],colors.black,lang)

        # name = Paragraph('<para fontName = STSong-Light fontSize=10>%s</para>'%(i.desc1), styles['BodyText'])
        # des =[[name]]
        # dest = Table(des,colWidths=10*cm)
        # w2, h2 = dest.wrapOn(c, width,height)
        # # printw2, h2, "height of para1"
        # height2 = height2 -h2
        # dest.drawOn(c, 200,height2)

        name = Paragraph('<para fontName = STSong-Light fontSize=15>%s</para>'%(i.title2), styles['Normal'])
        nd =[[name]]
        ndt = Table(nd,colWidths=10*cm)
        w3,h3 = ndt.wrapOn(c, width,height)
        height2 = height2 -h3-30
        ndt.drawOn(c, 200,height2)

        # printi.desc2, "description 2"
        height2 = htmlRMLCanvvas(i.desc2,c,10*cm,200,height2,styles['Normal'],colors.black,lang)
        # name = Paragraph('<para fontName = STSong-Light fontSize=10>%s</para>'%(i.desc2), styles['BodyText'])
        # des =[[name]]
        # dest = Table(des,colWidths=10*cm)
        # w4, h4 = dest.wrapOn(c, width,height)
        # height2 = height2 -h4
        # dest.drawOn(c, 200,height2)


        textobject = c.beginText()
        textobject.setTextOrigin(0.3*inch, 1.3*inch)
        textobject.setFont("Helvetica", 7)
        c.setFillColorRGB(255,255,255)
        textobject.textLines('''
                        Ein Unternehemen der Gruppe BRUGG''')
        c.drawText(textobject)


        textobject = c.beginText()
        textobject.setTextOrigin(0.3*inch, 1.15*inch)
        textobject.setFont("Helvetica", 7)
        c.setFillColorRGB(0,0,0)
        textobject.textLines('''
                        A company of the BRUGG Group''')
        c.drawText(textobject)


        textobject = c.beginText()
        textobject.setTextOrigin(0.3*inch, 0.6*inch)
        textobject.setFont("Helvetica", 7)
        c.setFillColorRGB(255,255,255)
        textobject.textLines('''
                        Anderungen vorbehalten. Massangaben unverbindlich.
                        Keine Gewahrleistung fur Druckfehler oder irrtumer.''')
        c.drawText(textobject)

        textobject = c.beginText()
        textobject.setTextOrigin(0.3*inch, 0.35*inch)
        textobject.setFont("Helvetica", 7)
        c.setFillColorRGB(0,0,0)
        textobject.textLines('''Subject to changes.Nonbinding indication of measures.
                            No warranty for printing errors of errors.''')
        c.drawText(textobject)

        textobject = c.beginText()
        textobject.setTextOrigin(5.9*inch, 0.4*inch)
        textobject.moveCursor(14,14)
        textobject.setFont("Helvetica", 15)
        textobject.setFillColor(colors.white)
        textobject.textLines('''
        www.brugglifting.com''')
        c.drawText(textobject)


        data = []
        # data2 = []
        dataHeading = ['Item Number']
        dataHeading2 = ['']
        list1 = []
        list2 = []
        for j in prodfield:
            # printprodfield
            if j.inPdf ==True:

                # printj.name,'kkkkkkkkkkkkk'
                try:
                    name1, name2 = j.name.split('(')
                    # printname2[:-1]
                    name2 = ''+name2[:-1]
                    # printname2
                except:
                    name1 = j.name
                    name2 = ''

                # printname1, ' ' , name2

                list1.append(name1)
                list2.append(name2)
        for a in list1:
            dataHeading.append(a)
        for b in list2:
            dataHeading2.append(b)


        # printdataHeading, dataHeading2, "fields  "


        for i in itemNumbers:
            appendlist = [i.itemNumber]
            for j in prodfield:
                prodQty = itemNumberValues.filter( field = j.pk,product = i.pk)
                for k in prodQty:
                    if j.inPdf ==True:
                        if j.type=='Char':
                            appendlist.append(k.char)
                        if j.type=='float':
                            appendlist.append(k.fValue)
                        if j.type=='Integer':
                            appendlist.append(k.iValue)
                        if j.type=='Boolean':
                            appendlist.append(k.bool)
            data.append(appendlist)

        dataLength = len(data)
        # printlen(data), "data length"
        # printdata , "item number data"


        data.insert(0,dataHeading)
        # printdata,len(data), "final data"

        # # printheight2, "height2"
        height2 = height2-40
        leftHeight = height2-120
        numberRows = int(leftHeight/20)
        # printheight2, leftHeight, numberRows, "number of rows"

        if len(data)<= numberRows:
            if dataLength>0:
                t5 = Table(data,rowHeights=[20]*len(data))
                t5.setStyle(TableStyle([
                                     ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                                     ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                                     ('FONTSIZE', (0, 0), (-1, -1), 7),
                                     ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                     ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                                     ]))
                w5, h5 = t5.wrapOn(c, width, height)
                height2 = height2 - h5
                t5.drawOn(c, 200, height2)
            c.showPage()
        else:
            # print"in else"
            data1 = data[:numberRows-1]
            # printdata1, "data1"
            data2 = data[numberRows:-1]
            # printdata2, "data2"
            t5 = Table(data1,rowHeights=[20]*len(data1))
            t5.setStyle(TableStyle([
                                 ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                                 ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                                 ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                                 ('FONTSIZE', (0, 0), (-1, -1), 7),
                                 ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                 ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                                 ]))
            w5, h5 = t5.wrapOn(c, width, height)
            height2 = height2 - h5
            t5.drawOn(c, 200, height2)

            c.showPage()

            maxNumberItems = 20

            index = float(len(data2))/maxNumberItems
            # printindex
            index = int(math.ceil(index))
            # printindex, range(index),"index ...."
            for i in range(index):
                if i == index-1:
                    data1 = data2[maxNumberItems*i:-1]
                    data1.insert(0,dataHeading)
                    # printlen(data1), i , "if loop"
                else:
                    data1 = data2[maxNumberItems*i:maxNumberItems*(i+1)-1]
                    data1.insert(0,dataHeading)
                    # printlen(data1), i, "else loop"
                # printdata1, "datapass "
                addNewPage(c, data1, bg2,product,stylesN,productImage)

        c.save()



    else:
        product = i
        styles=getSampleStyleSheet()
        stylesN = styles['Normal']
        stylesH =styles['Heading1']
        width,height = A4
        c = Canvas(response,pagesize=A4)
        c.setTitle("Brugglifting_%s"%i.productName)

        if i.backgroundImage1:
            bg1 = i.backgroundImage1.path
        else:
            bg1 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images',"brugg.jpg")
        # rope = os.path.join(globalSettings.BASE_DIR , 'static_shared/images','ropetech.png')
        if i.image2:
            productImage = i.image2.path
        else:
            productImage = os.path.join(globalSettings.BASE_DIR , 'static_shared/images',"stars.jpeg")

        if i.backgroundImage2:
            bg2 = i.backgroundImage2.path
        else:
            bg2 = os.path.join(globalSettings.BASE_DIR , 'static_shared/images',"cables.jpg")



        c.drawImage(bg1,0,0,width=width, height= height,mask='auto')


        name = Paragraph('<para fontName = FrutigerB fontSize=54>%s</para>'%(i.productName), styles['Normal'])
        nd =[[name]]
        w = pdfmetrics.stringWidth(i.productName, "FrutigerB", 54)
        # printw, "text width "
        ndt = Table(nd)
        w1,h1 = ndt.wrapOn(c, width,height)
        width2 = 50
        ndt.drawOn(c, width2,6.45*inch)

        name = Paragraph('<para  fontName = FrutigerR fontSize=12.5>%s</para>'%(i.tagLine), styles['Normal'])
        des =[[name]]
        dest = Table(des,colWidths=8*cm, rowHeights=30*mm)
        w2, h3 = dest.wrapOn(c, width,height)
        # printw2,w1, "tag width"
        width2 = width2 + w +10
        # printwidth2, "tagline width"
        dest.drawOn(c, width2,height-h3-330)

        c.showPage()

        c.drawImage(bg2,0,0,width=width,height=height,mask=None)

        img = utils.ImageReader(productImage)
        iw, ih = img.getSize()
        c.drawImage(productImage,30,height-ih-100,width=150,preserveAspectRatio=True,mask='auto')

        name = Paragraph('<para fontName = FrutigerB fontSize=20>%s</para>'%(i.productName), styles['Normal'])
        nd =[[name]]
        ndt = Table(nd,colWidths=10*cm)
        w1,h1 = ndt.wrapOn(c, width,height)
        height2 = height-h1-100
        ndt.drawOn(c, 50,800)

        name = Paragraph('<para fontName = FrutigerB fontSize=15>%s</para>'%(i.title1), styles['Normal'])
        nd =[[name]]
        ndt = Table(nd,colWidths=10*cm)
        w1,h1 = ndt.wrapOn(c, width,height)
        height2 = height-h1-100
        ndt.drawOn(c, 200,height2)

        height2 = htmlRMLCanvvas(i.desc1,c,10*cm,200,height2,styles['Normal'],colors.black,lang)
        # name = Paragraph('%s'%(i.desc1), styles['BodyText'])
        # des =[[name]]
        # dest = Table(des,colWidths=10*cm)
        # w2, h2 = dest.wrapOn(c, width,height)
        # # printw2, h2, "height of para1"
        # height2 = height2 -h2
        # dest.drawOn(c, 200,height2)

        name = Paragraph('<para fontName = FrutigerB fontSize=15>%s</para>'%(i.title2), styles['Normal'])
        nd =[[name]]
        ndt = Table(nd,colWidths=10*cm)
        w3,h3 = ndt.wrapOn(c, width,height)
        height2 = height2 -h3-30
        ndt.drawOn(c, 200,height2)

        # printi.desc2, "description 2"
        height2 = htmlRMLCanvvas(i.desc2,c,10*cm,200,height2,styles['Normal'],colors.black,lang)
        # name = Paragraph('%s'%(i.desc2), styles['BodyText'])
        # des =[[name]]
        # dest = Table(des,colWidths=10*cm)
        # w4, h4 = dest.wrapOn(c, width,height)
        # height2 = height2 -h4
        # dest.drawOn(c, 200,height2)


        textobject = c.beginText()
        textobject.setTextOrigin(0.3*inch, 1.3*inch)
        textobject.setFont("Helvetica", 7)
        c.setFillColorRGB(255,255,255)
        textobject.textLines('''
                        Ein Unternehemen der Gruppe BRUGG''')
        c.drawText(textobject)


        textobject = c.beginText()
        textobject.setTextOrigin(0.3*inch, 1.15*inch)
        textobject.setFont("Helvetica", 7)
        c.setFillColorRGB(0,0,0)
        textobject.textLines('''
                        A company of the BRUGG Group''')
        c.drawText(textobject)


        textobject = c.beginText()
        textobject.setTextOrigin(0.3*inch, 0.6*inch)
        textobject.setFont("Helvetica", 7)
        c.setFillColorRGB(255,255,255)
        textobject.textLines('''
                        Anderungen vorbehalten. Massangaben unverbindlich.
                        Keine Gewahrleistung fur Druckfehler oder irrtumer.''')
        c.drawText(textobject)

        textobject = c.beginText()
        textobject.setTextOrigin(0.3*inch, 0.35*inch)
        textobject.setFont("Helvetica", 7)
        c.setFillColorRGB(0,0,0)
        textobject.textLines('''Subject to changes.Nonbinding indication of measures.
                            No warranty for printing errors of errors.''')
        c.drawText(textobject)

        textobject = c.beginText()
        textobject.setTextOrigin(5.9*inch, 0.4*inch)
        textobject.moveCursor(14,14)
        textobject.setFont("Helvetica", 15)
        textobject.setFillColor(colors.white)
        textobject.textLines('''
        www.brugglifting.com''')
        c.drawText(textobject)


        data = []
        # data2 = []
        dataHeading = ['Item Number']
        dataHeading2 = ['']
        list1 = []
        list2 = []
        for j in prodfield:
            # printprodfield
            if j.inPdf ==True:

                # printj.name,'kkkkkkkkkkkkk'
                try:
                    name1, name2 = j.name.split('(')
                    # printname2[:-1]
                    name2 = ''+name2[:-1]
                    # printname2
                except:
                    name1 = j.name
                    name2 = ''

                # printname1, ' ' , name2

                list1.append(name1)
                list2.append(name2)
        for a in list1:
            dataHeading.append(a)
        for b in list2:
            dataHeading2.append(b)


        # printdataHeading, dataHeading2, "fields  "


        for i in itemNumbers:
            appendlist = [i.itemNumber]
            for j in prodfield:
                prodQty = itemNumberValues.filter( field = j.pk,product = i.pk)
                for k in prodQty:
                    if j.inPdf ==True:
                        if j.type=='Char':
                            appendlist.append(k.char)
                        if j.type=='float':
                            appendlist.append(k.fValue)
                        if j.type=='Integer':
                            appendlist.append(k.iValue)
                        if j.type=='Boolean':
                            appendlist.append(k.bool)
            data.append(appendlist)
        dataLength = len(data)
        # printlen(data), "data length"
        # printdata , "item number data"


        data.insert(0,dataHeading)
        # printdata,len(data), "final data"

        # # printheight2, "height2"
        height2 = height2-40
        leftHeight = height2-120
        numberRows = int(leftHeight/20)
        # printheight2, leftHeight, numberRows, "number of rows"

        if len(data)<= numberRows:
            if dataLength>0:
                t5 = Table(data,rowHeights=[20]*len(data))
                t5.setStyle(TableStyle([
                                     ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                                     ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                                     ('FONTSIZE', (0, 0), (-1, -1), 7),
                                     ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                     ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                                     ]))
                w5, h5 = t5.wrapOn(c, width, height)
                height2 = height2 - h5
                t5.drawOn(c, 200, height2)
            c.showPage()
        else:
            # print"in else"
            data1 = data[:numberRows-1]
            # printdata1, "data1"
            data2 = data[numberRows:-1]
            # printdata2, "data2"
            t5 = Table(data1,rowHeights=[20]*len(data1))
            t5.setStyle(TableStyle([
                                 ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                                 ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                                 ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                                 ('FONTSIZE', (0, 0), (-1, -1), 7),
                                 ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                 ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                                 ]))
            w5, h5 = t5.wrapOn(c, width, height)
            height2 = height2 - h5
            t5.drawOn(c, 200, height2)

            c.showPage()

            maxNumberItems = 20

            index = float(len(data2))/maxNumberItems
            # printindex
            index = int(math.ceil(index))
            # printindex, range(index),"index ...."
            for i in range(index):
                if i == index-1:
                    data1 = data2[maxNumberItems*i:-1]
                    data1.insert(0,dataHeading)
                    # printlen(data1), i , "if loop"
                else:
                    data1 = data2[maxNumberItems*i:maxNumberItems*(i+1)-1]
                    data1.insert(0,dataHeading)
                    # printlen(data1), i, "else loop"
                # printdata1, "datapass "
                addNewPage(c, data1, bg2,product,stylesN,productImage)

        c.save()



class GeneratePdfAccessories(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny , )

    def get(self, request, format=None):
        access = request.GET['accessories']

        accessObjects = AccessoriesSection.objects.filter(basicProductName=access)
        # print accessObjects,'accessObjects'
        prodfield = AccessoriesField.objects.filter(productBaseName = access)
        # printprodfield, "product fields "
        itemNumbers = AccessoriesData.objects.filter(productBaseName = access)
        # printitemNumbers, "item numbers"
        itemNumberValues = AccessoriesValueMap.objects.filter(productBaseName = access)
        # printitemNumberValues, "itemNumberValues"

        for i in accessObjects:
            name = i.basicProductName +"_" +i.lang
            try:
                f = open(os.path.join(globalSettings.BASE_DIR, 'media_root/%s.pdf'%(name)), 'w')
                os.unlink(f.name)
            except:
                pass
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="%s.pdf"'%(name)

            generateAccess(request,response,i,prodfield,itemNumbers,itemNumberValues)
            f = open(os.path.join(globalSettings.BASE_DIR, 'media_root/%s.pdf'%(name)), 'wb')
            f.write(response.content)
            f.close()

        if 'saveOnly' in request.GET:
            return Response(status=status.HTTP_200_OK)
        return response



class SearchAllAPI(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny , )
    def get(self , request , format = None):
        if 'search' in self.request.GET:
            search = str(self.request.GET['search'])
            lang = renderedLang(request)


            if lang is None or lang is 'en-US' or lang is 'en-GB':
                lang = 'en'

            l = int(self.request.GET['limit'])
            searchFull = []
            product = list(ProductTemplate.objects.filter(Q(name__icontains=search)| Q(productValueTemplates__itemNumber__icontains=search) | Q(description__icontains=search)| Q(parent_name__icontains=search) | Q(rteData1_en__icontains=search) | Q(rteData1_otl__icontains=search) |   Q(rteData2_en__icontains=search) | Q(rteData2_otl__icontains=search) ).distinct().values('pk','name','defaultImage').annotate(typ= Value('prodTemp',output_field=CharField()),url=Value('/products/',output_field=CharField())))

            print "product : " , product

            acc = AccessoriesSection.objects.filter(lang=lang)

            accessories = list(acc.filter(Q(productName__icontains=search) | Q(categoryName__icontains=search)| Q(desc1__icontains=search)|Q(desc2__icontains=search)).distinct().values('pk','productName').annotate(typ= Value('accessories',output_field=CharField()),name=F('productName'),url=Value('/viewProduct/',output_field=CharField()),defaultImage=F('image1')))


            blog = list(blogPost.objects.filter(Q(title__icontains=search) | Q(description__icontains=search)).values('pk','title').annotate(typ= Value('blog',output_field=CharField()),name=F('title'),url=Value('/blog/',output_field=CharField()),defaultImage=F('ogimage')))


            app = Apptips.objects.filter(lang=lang)


            apptips=list(app.filter(Q(tipname__icontains=search) | Q(text__icontains=search)).values('pk','tipname').annotate(typ= Value('apptips',output_field=CharField()),name=F('tipname'),url=Value('/applicationtips',output_field=CharField()),defaultImage=F('image1')))

            print "apptips : " , apptips

            try:
                directory = os.path.join(globalSettings.BASE_DIR +"/homepage/renderedFiles/"+lang)
                pagesList = list_files(directory, "html")
                for f in pagesList:
                    filename = os.path.join(globalSettings.BASE_DIR, 'homepage/renderedFiles/%s'%(lang +'/'+f))
                    fopen = open(filename, 'r')
                    first_line = fopen.readline()
                    if search.lower() in fopen.read().lower():
                        if len(first_line) <= 1:
                            page_name = 'Home - Brugg Lifting'
                        else:
                            page_name = first_line.upper() +' - ' + search
                        print page_name,'jjjjjjjjjjjjj'
                        value = {'url': first_line, 'pk': 1, 'defaultImage': '', 'typ': 'template', 'name': page_name}
                        searchFull.append(value)
            except:
                pass

            print "searchFull : " , searchFull

            tosend = product + accessories + blog + apptips + searchFull

            print tosend

            return Response(tosend[0:l], status = status.HTTP_200_OK)


class AccessoriesTable(APIView):
    renderer_classes = (JSONRenderer,)
    permission_classes = (permissions.AllowAny , )
    def get(self , request , format = None):
        toreturn = []
        product = request.GET['product']
        # sectionObj = AccessoriesSection.objects.filter(basicProductName = product)[0]
        # albumImages = sectionObj.media.all()
        prodfield = AccessoriesField.objects.filter(productBaseName = product)
        prod = AccessoriesData.objects.filter(productBaseName = product)
        data = []
        listData = ['Item Number']
        for i in prodfield:
            listData.append(i.name)
        for i in prod:
            appendlist = [i.itemNumber]
            for j in prodfield:
                prodQty = AccessoriesValueMap.objects.filter( field = j.pk,product = i.pk)
                for k in prodQty:
                    if j.type=='Char':
                        appendlist.append(k.char)
                    if j.type=='float':
                        appendlist.append(k.fValue)
                    if j.type=='Integer':
                        appendlist.append(k.iValue)
                    if j.type=='Boolean':
                        appendlist.append(k.bool)
            data.append(appendlist)
        tosend = {'heading':listData,'data':data}
        return Response(tosend, status = status.HTTP_200_OK)
        # return render(request, 'accessoriesDetail.html', {"home": True ,"lang" : lang, "product":sectionObj,'heading':listData,'data':data,"albumImages":albumImages })


class emailSendApi(APIView):
    permission_classes = (permissions.AllowAny ,)
    def post(self, request, format=None):
        name = request.data['name']
        phone = request.data['phone']
        email = request.data['email']
        cover_letter = request.data['cover_letter']
        if 'cv_file' in request.FILES:
            file = request.FILES['cv_file']
            f = open(os.path.join(globalSettings.BASE_DIR, 'media_root/%s' %(file.name)), 'wb')
            f.write(file.read())
            f.close()
        print 'email send',name,cover_letter,phone,email

        ctx = {
            'logoUrl' : '/static/images/cudabam/title.png',
            'recieverName' : 'Admin',
            'message': 'Distributorship Request',
            'name':name ,
            'phone':phone ,
            'email':email ,
            'cover_letter' : cover_letter,
        }

        email_subject = 'New Applicant'
        email_body = get_template('app.homepage.email.html').render(ctx)

        email_to = []
        for i in globalSettings.G_ADMIN:
            email_to.append(str(i))
        msg = EmailMessage(email_subject, email_body, to= email_to  ,  )
        msg.content_subtype = 'html'
        try:
            msg.attach_file(os.path.join(globalSettings.MEDIA_ROOT,f.name))
        except:
            pass
        msg.send()

        return Response( status = status.HTTP_200_OK)
