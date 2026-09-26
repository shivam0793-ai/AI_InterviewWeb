from django import forms
from .models import interview

<<<<<<< HEAD
<<<<<<< HEAD
class InterviewForm(forms.ModelForm):
=======
class interview_form(forms.ModelForm):
>>>>>>> 1e4d6ea (form and ai_service created)
=======
class InterviewForm(forms.ModelForm):
>>>>>>> 24e5edc (ai-intreget)
    class Meta:
        model=interview
        fields=[
             "technology",
            "interview_type",
            "difficulty",
            "experience"
        ]
