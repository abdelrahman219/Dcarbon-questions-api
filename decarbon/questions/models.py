# models.py
from django.db import models
from user.models import UserModel
from django.conf import settings

class Question(models.Model):
    YES_NO = 'yes_no'
    NUMBER = 'number'
    TEXT = 'text'

    ANSWER_TYPES = [
        (YES_NO, 'Yes/No'),
        (NUMBER, 'Number'),
        (TEXT, 'Text'),
    ]

    content = models.CharField(max_length=255)
    answer_type = models.CharField(max_length=20, choices=ANSWER_TYPES)
    created_by = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    answer = models.TextField(null=False)

    def __str__(self):
        return f"Answer to '{self.question.content}' by {self.user.username}"
