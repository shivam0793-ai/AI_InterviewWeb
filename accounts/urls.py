from django.urls import path,include
from .views import SignupView
urlpatterns=[
    path('accounts/',include('django.contrib.auth.urls')),
    path('signup/',SignupView,name='signup')

]