from django.conf.urls import include, url
from .views import *
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'schedule' , scheduleViewSet , base_name = 'schedule')
router.register(r'media' , MediaViewSet , base_name = 'media')
router.register(r'productTemplate' , ProductTemplateViewSet , base_name = 'productTemplate')
router.register(r'productField' , ProductFieldViewSet , base_name = 'productField')
router.register(r'product' , ProductViewSet , base_name = 'product')
router.register(r'productValueMap' , ProductValueMapViewSet , base_name = 'productValueMap')
router.register(r'pdfDescription' , PdfDescriptionViewSet , base_name = 'pdfDescription')
router.register(r'careers' , CareersFieldViewSet , base_name = 'careers')
router.register(r'apply' , ApplySerializer , base_name = 'apply')
router.register(r'apptips' , ApptipsViewSet , base_name = 'apptips')
router.register(r'accessories' , AccessoriesViewSet , base_name = 'accessories')
router.register(r'accessoriesSection' , AccessoriesSectionViewSet , base_name = 'accessoriesSection')
router.register(r'accessoriesField' , AccessoriesFieldViewSet , base_name = 'accessoriesField')
router.register(r'accessoriesData' , AccessoriesDataViewSet , base_name = 'accessoriesData')
router.register(r'albumImages' , AlbumImagesViewSet , base_name = 'albumImages')
router.register(r'locations' , LocationsViewSet , base_name = 'locations')



urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'inviteMail/$' , InvitationMailApi.as_view()),
    url(r'broucherpdf/$' , BroucherApi.as_view()),
    url(r'generatePdfAccessories/$' , GeneratePdfAccessories.as_view()),
    url(r'generatebroucher/$' , GenerateBroucherApi.as_view()),
    url(r'book/$' , views.book,name="book"),
    url(r'contact/$' , ContactApi.as_view()),
    url(r'submitFeedback/$' , SubmitAPIView.as_view()),
    url(r'ctpcatalog/$' , CtpBroucherApi.as_view()),
    url(r'searchAll/$' , SearchAllAPI.as_view()),
    url(r'accessories_table/$' , AccessoriesTable.as_view()),
    url(r'emailSend/$' , emailSendApi.as_view()),


]
