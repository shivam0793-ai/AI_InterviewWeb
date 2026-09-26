from django import forms
from .models import interview

class InterviewForm(forms.ModelForm):
    class Meta:
        model=interview
        fields=[
             "technology",
            "interview_type",
            "difficulty",
            "experience"
        ]
