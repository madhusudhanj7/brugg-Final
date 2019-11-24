from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from HR.views import loginView , logoutView , home , registerView , tokenAuthentication , root, generateOTP, documentView

from homepage.views import blog,blogDetails,news,team, career ,policy ,terms ,refund , contacts , registration,index,customerLoginView, customerHomeView, about, main, rope_selection,categoriesView, productsView, productsViewRefresh,locationsView , sitemapView,apptipsView,referenceView, innovation, work_culture, product, book, legalView,AccessoriesView, AccessoriesDetailView,ProductInformationView,TechnicalInformationView,ApplicationView

from ERP.views import serviceRegistration , renderedStatic
# from django.conf.urls.defaults import *

app_name="libreERP"

urlpatterns = [
    url(r'^$', main , name ='root'),
    # url(r'^CRM/', crmHome , name ='CRM'),
    url(r'^ERP/', home , name ='ERP'),
    url(r'^api/', include('API.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login', loginView , name ='login'),
    url(r'^logout/', logoutView , name ='logout'),
    url(r'^api-auth/', include('rest_framework.urls', namespace ='rest_framework')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^robots\.txt', include('robots.urls')),
    url(r'^contacts', contacts , name ='contacts'),
    url(r'^customer/login', customerLoginView , name ='customerLogin'),
    url(r'^customerhome', customerHomeView , name ='customerhome'),
    url(r'^ngTemplates/(?P<filename>[\w|\W]+)', renderedStatic , name ='renderedStatic'),
    url(r'^rope-selection',rope_selection , name ='rope-selection'),
    url(r'^about',about , name ='about'),
    url(r'^productsRefresh',productsViewRefresh , name ='productsViewRefresh'),
    url(r'^categories/(?P<name>[\w|\W]+)',categoriesView , name ='categoriesView'),
    url(r'^products/(?P<product>[\w|\W]+)',productsView , name ='productsView '),
    url(r'^locations',locationsView , name ='locationsView '),
    url(r'^sitemap',sitemapView , name ='sitemapView '),
    url(r'^legal-privacy',legalView , name ='legal'),
    url(r'^product-info',ProductInformationView , name ='ProductInfo'),
    url(r'^technical-information',TechnicalInformationView , name ='TechInfo'),
    url(r'^pdfapplication',ApplicationView , name ='application'),
    url(r'^accessories',AccessoriesView , name ='accessories'),
    url(r'^viewProduct/(?P<product>[\w|\W]+)/',AccessoriesDetailView , name ='viewProduct'),
    url(r'^applicationtips',apptipsView , name ='apptipsView '),
    url(r'^reference',referenceView , name ='referenceView '),
    url(r'^blogs',blog , name ='blog '),
    url(r'^blog/(?P<blogname>[\w|\W]+)/', blogDetails , name ='blogDetails'),
    url(r'^innovation',innovation , name ='innovation'),
    url(r'^work-culture',work_culture , name ='work-culture'),
    url(r'^product',product , name ='product'),
    # url(r'^book',book , name ='book'),
]


if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL , document_root = settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)

urlpatterns.append(url(r'^.*$', index , name='index'))
