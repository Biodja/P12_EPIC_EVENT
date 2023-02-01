from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'usertypes', views.UserTypeViewSet)
router.register(r'profils', views.ProfilViewSet)
router.register(r'clients', views.ClientViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'contracts', views.ContractViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'api-auth/', include('rest_framework.urls' , namespace='rest_framework')),
    

    """path(r'^usertypes/$', views.UserTypeViewSet.as_view({'get': 'list'}), name='usertype-list'),"""
    """path(r'^usertypes/(?P<pk>[0-9]+)/$', views.UserTypeViewSet.as_view({'get': 'retrieve'}), name='usertype-detail'),"""
]
