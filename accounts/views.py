from django.shortcuts import render
from .forms import SignupForm

def SingupView(request):
    if request.method=='POST':
        pass

    else:
        form=SignupForm()

    return render(request,'registration/signup.html')