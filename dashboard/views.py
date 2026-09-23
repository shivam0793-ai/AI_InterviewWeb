from django.shortcuts import render

def Dashboard_reder(request):
    return render(request,'Dashboard/HomePage.html')