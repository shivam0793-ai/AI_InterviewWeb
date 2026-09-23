from django.urls import path
from .views import *

urlpatterns=[
    path('',Dashboard_reder,name='home')
]