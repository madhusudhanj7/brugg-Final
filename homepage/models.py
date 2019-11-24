from django.db import models
from time import time
from django.contrib.auth.models import User

def getERPPictureUploadPath(instance , filename ):
    return 'homepage/images/pictureUploads/%s_%s__%s' % (str(time()).replace('.', '_'), instance.user.username, filename)
def getOGImageAttachment(instance , filename ):
    return 'homepage/images/productImage/%s__%s' % (str(time()).replace('.', '_'), filename)
def getBGImageAttachment(instance , filename ):
    return 'homepage/images/productImage/%s__%s' % (str(time()).replace('.', '_'), filename)
def getPdfImageAttachment(instance , filename ):
    return 'homepage/images/productImage/%s__%s' % (str(time()).replace('.', '_'), filename)
def getAttachmentPath(instance , filename ):
    return 'homepage/images/productImage/%s__%s' % (str(time()).replace('.', '_'), filename)
def getPImageAttachment(instance , filename ):
    return 'homepage/images/productImage/%s__%s' % (str(time()).replace('.', '_'), filename)
def getAImageAttachment(instance , filename ):
    return 'homepage/images/productImag/%s__%s' % (str(time()).replace('.', '_'), filename)
def getAImageAttachment(instance , filename ):
    return 'homepage/images/productImag/%s__%s' % (str(time()).replace('.', '_'), filename)
def getaccessImageAttachment(instance , filename ):
    return 'homepage/images/accessImag/%s__%s' % (str(time()).replace('.', '_'), filename)
def albumImageAttachment(instance , filename ):
    return 'homepage/images/albumImage/%s__%s' % (str(time()).replace('.', '_'), filename)

# Create your models here.
class Schedule(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    dated =  models.DateField( null= False )
    slot = models.CharField(max_length = 15 , null= False)
    name  = models.CharField(max_length = 30 , null= True)
    emailId = models.CharField(max_length = 20 , null= False)

MEDIA_TYPE_CHIOCES = (
('onlineVideo','onlineVideo'),
('video','video'),
('image','image'),
('onlineImage','onlineImage'),
('doc','doc'),
)
class Media(models.Model):
    user = models.ForeignKey(User,related_name='serviceDocsUploaded')
    created = models.DateTimeField(auto_now_add = True)
    link = models.TextField(null= True)
    attachment  = models.FileField(upload_to= getERPPictureUploadPath , null = True)
    mediaType = models.CharField(choices=MEDIA_TYPE_CHIOCES , max_length=20,default='image')
    name = models.CharField(max_length = 200,null=True)

ROPE_TYPE_CHOICES=(('Tractionropes','Tractionropes'),
                ('Compensationropes','Compensationropes'),
                ('Governorropes','Governorropes'),
                )

class ProductTemplate(models.Model):
    created = models.DateTimeField(auto_now_add = True,null=True)
    parent_name =  models.CharField(max_length = 200,null=True)
    name = models.CharField(max_length = 200)
    description = models.TextField(max_length = 2000)
    rteData1_en = models.TextField(max_length = 5000 , null = True)
    rteData1_otl = models.TextField(max_length = 5000 , null = True)
    rteData2_en = models.TextField(max_length = 5000 , null = True)
    rteData2_otl = models.TextField(max_length = 5000 , null = True)
    defaultImage = models.ImageField(upload_to= getOGImageAttachment , null = True)
    backgroundImage1 = models.ImageField(upload_to= getBGImageAttachment , null = True)
    backgroundImage2 = models.ImageField(upload_to= getBGImageAttachment , null = True)
    productImage1 = models.ImageField(upload_to= getPImageAttachment , null = True)
    productImage2 = models.ImageField(upload_to= getPImageAttachment , null = True)
    media = models.ManyToManyField(Media,related_name="templateMedia")
    pdfgenerated = models.BooleanField(default = False)
    disclaimer_en = models.TextField( null = True)
    disclaimer_otl = models.TextField( null = True)
    keyword1 = models.TextField( null = True)
    keyword2 = models.TextField( null = True)
    keyword3 = models.TextField( null = True)
    keyword4 = models.TextField( null = True)
    productfields = models.TextField( null = True)
    color =  models.CharField(max_length = 200,null=True)
    catalogBG1 = models.ImageField(upload_to= getPImageAttachment , null = True)
    catalogBG2 = models.ImageField(upload_to= getPImageAttachment , null = True)
    rteDescription = models.TextField(max_length = 5000 , null = True)
    des_ch = models.TextField(max_length = 2000, null = True)
    des_de = models.TextField(max_length = 2000, null = True)
    rteData1_ch = models.TextField(max_length = 5000 , null = True)
    rteData2_ch = models.TextField(max_length = 5000 , null = True)
    disclaimer_ch = models.TextField( null = True)
    rteDescription_de = models.TextField(max_length = 5000 , null = True)
    rteDescription_ch = models.TextField(max_length = 5000 , null = True)

TYPE_CHOICES = (('Boolean', 'Boolean'),
                ('Char','Char'),
                ('float','float'),
                ('Integer','Integer')
                )

class ProductField(models.Model):
    created = models.DateTimeField(auto_now_add = True,null=True)
    name = models.CharField(max_length = 200)
    type = models.CharField(max_length = 50, choices =TYPE_CHOICES ,default = 'Char')
    required = models.BooleanField(default = True)
    dimensions = models.CharField(max_length = 20 , null= True , blank=True)
    inPdf = models.BooleanField(default = True)
    inUI = models.BooleanField(default = True)
    template = models.ForeignKey(ProductTemplate,related_name='productTemplates')

class Product(models.Model):
    created = models.DateTimeField(auto_now_add = True,null=True)
    itemNumber = models.IntegerField(default=0)
    template = models.ForeignKey(ProductTemplate,related_name='productValueTemplates',null=True)

class ProductValueMap(models.Model):
    created = models.DateTimeField(auto_now_add = True,null=True)
    field = models.ForeignKey(ProductField,related_name='productFields')
    bool = models.BooleanField(default=True)
    char = models.CharField(max_length=200)
    fValue = models.FloatField(default=0)
    iValue = models.IntegerField(default=0)
    product= models.ForeignKey(Product,related_name='products')

class PdfDescription(models.Model):
    created = models.DateTimeField(auto_now_add = True,null=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image =  models.ImageField(upload_to= getPdfImageAttachment , null = True)

JOB_TYPES = (('Intern', 'Intern'),
                ('Contract','Contract'),
                ('Fulltime','Fulltime'),
                )
class CareerField(models.Model):
    created = models.DateTimeField(auto_now_add = True,null=True)
    name = models.CharField(max_length = 200)
    jobtype = models.CharField(max_length = 50, choices =JOB_TYPES ,default = 'Char')
    skills = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
    status = models.BooleanField(default = True)
    maxctc = models.FloatField(default=0)

class Apply(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50, null=True)
    mobile = models.IntegerField(default=10)
    coverletter = models.CharField(max_length=2000)
    resume = models.FileField(upload_to = getAttachmentPath ,  null = True)
    forg = models.ForeignKey(CareerField, related_name='CareerField',null=True)

SIZE_TYPES = (('6', '6'),
                ('12','12'),
                )
class Apptips(models.Model):
    text = models.TextField(max_length=40000, null = True)
    image1 =  models.FileField(upload_to= getAImageAttachment , null = True)
    heading = models.ForeignKey('self', blank=True, null=True, related_name='children')
    size = models.IntegerField(choices =SIZE_TYPES ,default = '6')
    tipname = models.CharField(max_length=200,null=True)
    mediaTyp = models.CharField(max_length=200,null=True)
    lang = models.CharField(max_length=200,null=True)

class Accessories(models.Model):
    name = models.CharField(max_length=200,null=True)
    mainImage =  models.ImageField(upload_to= getaccessImageAttachment , null = True)

class AccessoriesSection(models.Model):
    categoryName = models.CharField(max_length=200 )
    basicProductName = models.CharField(max_length=200)
    productName = models.CharField(max_length=200)
    tagLine = models.CharField(max_length=200,null=True)
    title1 = models.CharField(max_length=200,null=True)
    desc1  = models.TextField(max_length=5000,null=True)
    title2 = models.CharField(max_length=200,null=True)
    desc2  = models.TextField(max_length=5000,null=True)
    lang = models.CharField(max_length=200,null=True)
    accessories = models.ForeignKey(Accessories, blank=True, null=True, related_name='accessSections')
    image1 =  models.ImageField(upload_to= getaccessImageAttachment , null = True)
    image2 =  models.ImageField(upload_to= getaccessImageAttachment , null = True)
    backgroundImage1 = models.ImageField(upload_to= getaccessImageAttachment , null = True)
    backgroundImage2 = models.ImageField(upload_to= getaccessImageAttachment , null = True)
    bottomtext =  models.TextField(max_length=5000,null=True)
    catalogBG1 = models.ImageField(upload_to= getPImageAttachment , null = True)
    catalogBG2 = models.ImageField(upload_to= getPImageAttachment , null = True)
    media = models.ManyToManyField(Media,related_name="accessoriesMedia")

class AccessoriesField(models.Model):
    created = models.DateTimeField(auto_now_add = True,null=True)
    name = models.CharField(max_length = 200)
    type = models.CharField(max_length = 50, choices =TYPE_CHOICES ,default = 'Char')
    required = models.BooleanField(default = True)
    dimensions = models.CharField(max_length = 20 , null= True , blank=True)
    inPdf = models.BooleanField(default = True)
    inUI = models.BooleanField(default = True)
    template = models.ForeignKey(AccessoriesSection,related_name='accessoriessectionData')
    productBaseName = models.CharField(max_length = 200)

class AccessoriesData(models.Model):
    created = models.DateTimeField(auto_now_add = True,null=True)
    itemNumber = models.IntegerField(default=0)
    template = models.ForeignKey(AccessoriesSection,related_name='accessoriessectionValue',null=True)
    productBaseName = models.CharField(max_length = 200)

class AccessoriesValueMap(models.Model):
    created = models.DateTimeField(auto_now_add = True,null=True)
    field = models.ForeignKey(AccessoriesField,related_name='accessoriesField')
    bool = models.BooleanField(default=True)
    char = models.CharField(max_length=200)
    fValue = models.FloatField(default=0)
    iValue = models.IntegerField(default=0)
    product= models.ForeignKey(AccessoriesData,related_name='accessoriesData')
    productBaseName = models.CharField(max_length = 200)

class AlbumImages(models.Model):
    created = models.DateTimeField(auto_now_add = True,null=True)
    image =  models.ImageField(upload_to= albumImageAttachment , null = True)

class Locations(models.Model):
    created = models.DateTimeField(auto_now_add = True,null=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    lat = models.FloatField(default=0,null=False)
    long = models.FloatField(default=0,null=False)
    address_en = models.TextField(max_length=40000, null = True,blank=True)
    address_de = models.TextField(max_length=40000, null = True,blank=True)
    address_zh = models.TextField(max_length=40000, null = True,blank=True)
    representation = models.BooleanField(default=False)
    shortUrl = models.CharField(max_length =1000 , null = True,blank=True)
