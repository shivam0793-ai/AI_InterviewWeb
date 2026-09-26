from django.urls import path
from .views import interview

urlpatterns=[
    path('interview/',interview,name='interview')
]