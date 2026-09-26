from django.db import models
from django.contrib.auth.models import User


class interview(models.Model):
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='interviews'
    )

    title=models.CharField(max_length=250)
    technology=models.CharField(max_length=100)
    interview_type=models.CharField(max_length=50)
    difficulty=models.CharField(max_length=50)
    experience=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.title}"



class Chatmessage(models.Model):
    ROLE_CHOICES=[
        ('user','user'),
        ('assistant','assistant')
    ]

    interview=models.ForeignKey(interview,on_delete=models.CASCADE,related_name='messages')

    role=models.CharField(
        max_length=30,
        choices=ROLE_CHOICES
    )

    content=models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.role} - Interview {self.interview.id}"

