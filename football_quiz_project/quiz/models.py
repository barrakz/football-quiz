from django.db import models

class Question(models.Model):
    text = models.TextField()
    correct_answer = models.CharField(max_length=255)

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)

class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=255)
    is_correct = models.BooleanField()

    