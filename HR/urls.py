from django.conf.urls import include, url
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users' , UserViewSet , base_name = 'user')
router.register(r'groups' , GroupViewSet)
router.register(r'usersAdminMode' , userAdminViewSet , base_name = 'userAdminMode')
router.register(r'userSearch' , UserSearchViewSet , base_name = 'userSearch')
router.register(r'profile' , userProfileViewSet , base_name ='profile')
router.register(r'profileAdminMode' , userProfileAdminModeViewSet , base_name ='profileAdminMode')

urlpatterns = [
    url(r'^', include(router.urls)),
]
