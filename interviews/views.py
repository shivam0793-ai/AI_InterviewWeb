from django.shortcuts import render, redirect
from .forms import interview_form
from .ai_connection import chat_with_at

def interview(request):

    if request.method == "POST":
        form = interview_form(request.POST)
        if form.is_valid():
            form.cleaned_data[]

    else:
        form = interview_form()

    return render(
        request,
        "interview/Interview_Form.html",
        {"form": form}
    )