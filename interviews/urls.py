from django.urls import path
<<<<<<< HEAD
<<<<<<< HEAD
from . import views

urlpatterns = [
    path("", views.interview_setup, name="interview"),
    path("<int:interview_id>/chat/", views.chat_page, name="chat_page"),
=======
from .views import interview

urlpatterns=[
    path('interview/',interview,name='interview')
>>>>>>> 1e4d6ea (form and ai_service created)
=======
from . import views

urlpatterns = [
    path("", views.interview_setup, name="interview"),
    path("<int:interview_id>/chat/", views.chat_page, name="chat_page"),
>>>>>>> 24e5edc (ai-intreget)
]