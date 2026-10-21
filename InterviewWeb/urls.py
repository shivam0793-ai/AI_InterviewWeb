from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('dashboard.urls')),
    path("accounts/",include('accounts.urls')),
    path("singup/",include('accounts.urls')),
    path("interview/",include("interviews.urls")),
    path('api/',include('API.urls'))
]

