from django.conf.urls import include, url

urlpatterns = [
    url(r'^HR/', include('HR.urls')),
    url(r'^homepage/', include('homepage.urls')),
    url(r'^ERP/', include('ERP.urls')),
    url(r'^mail/', include('mail.urls')),
    url(r'^PIM/', include('PIM.urls')),
]
