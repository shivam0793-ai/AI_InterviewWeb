from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('',api_response,basename='api_response')

urlpatterns=[
     path('createtoken/',createtoken, name='createtoken'),
]
urlpatterns+=router.urls