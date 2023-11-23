from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    text = models.TextField() # The text of the question

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE) # Each answer is associated with a question
    text = models.CharField(max_length=255) # The text of the answer

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Each user has one profile



    
