from django.urls import path
from . import views

urlpatterns = [
    path("", views.interview_setup, name="interview"),
    path("<int:interview_id>/chat/", views.chat_page, name="chat_page"),
]