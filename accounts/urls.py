from django.urls import path,include
from .views import SingupView
urlpatterns=[
    path('accounts/',include('django.contrib.auth.urls')),
    path('signup/',SingupView,name='signup')

]