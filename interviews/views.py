<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 24e5edc (ai-intreget)
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import InterviewForm
from .ai_service import chat_with_ai
from .models import interview as interview,Chatmessage
<<<<<<< HEAD

@login_required
def interview_setup(request):

    if request.method == "POST":

        form = InterviewForm(request.POST)

        if form.is_valid():

            interview_obj = form.save(commit=False)

            interview_obj.user = request.user

            interview_obj.title = f"{interview_obj.technology} Interview"

            interview_obj.save()

            first_question = chat_with_ai(
                [],
                f"Start a {interview_obj.difficulty} {interview_obj.technology} interview for a {interview_obj.experience} candidate. Ask only the first interview question."
            )

            Chatmessage.objects.create(
                interview=interview_obj,
                role="assistant",
                content=first_question
            )

            return redirect("chat_page", interview_id=interview_obj.id)

    else:
        form = InterviewForm()
=======
from django.shortcuts import render, redirect
from .forms import interview_form
from .ai_connection import chat_with_at
=======
>>>>>>> 24e5edc (ai-intreget)

@login_required
def interview_setup(request):

    if request.method == "POST":

        form = InterviewForm(request.POST)

        if form.is_valid():

            interview_obj = form.save(commit=False)

            interview_obj.user = request.user

            interview_obj.title = f"{interview_obj.technology} Interview"

            interview_obj.save()

            first_question = chat_with_ai(
                [],
                f"Start a {interview_obj.difficulty} {interview_obj.technology} interview for a {interview_obj.experience} candidate. Ask only the first interview question."
            )

            Chatmessage.objects.create(
                interview=interview_obj,
                role="assistant",
                content=first_question
            )

            return redirect("chat_page", interview_id=interview_obj.id)

    else:
<<<<<<< HEAD
        form = interview_form()
>>>>>>> 1e4d6ea (form and ai_service created)
=======
        form = InterviewForm()
>>>>>>> 24e5edc (ai-intreget)

    return render(
        request,
        "interview/Interview_Form.html",
        {"form": form}
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 24e5edc (ai-intreget)
    )


@login_required
def chat_page(request, interview_id):

    interview_obj = get_object_or_404(
        interview,
        id=interview_id,
        user=request.user
    )

    sidebar = interview.objects.filter(
        user=request.user
    ).order_by("-update_at")

    messages = interview_obj.messages.all()

    if request.method == "POST":

        user_message = request.POST.get("message", "").strip()

        if user_message:

            Chatmessage.objects.create(
                interview=interview_obj,
                role="user",
                content=user_message
            )

            history = []

            for msg in interview_obj.messages.all():

                history.append({
                    "role": msg.role,
                    "text": msg.content
                })

            ai_reply = chat_with_ai(history, user_message)

            Chatmessage.objects.create(
                interview=interview_obj,
                role="assistant",
                content=ai_reply
            )

        return redirect("chat_page", interview_id=interview_obj.id)

    return render(
        request,
        "interview/chat.html",
        {
            "interview": interview_obj,
            "messages": messages,
            "sidebar": sidebar
        }
<<<<<<< HEAD
=======
>>>>>>> 1e4d6ea (form and ai_service created)
=======
>>>>>>> 24e5edc (ai-intreget)
    )