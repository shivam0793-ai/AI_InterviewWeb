from django.shortcuts import render

def Dashboard_reder(request):
    return render(request,'app/dashboard.html')