from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    text = models.TextField()  # The text of the question

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)  # Each answer is associated with a question
    text = models.CharField(max_length=255)  # The text of the answer
    is_correct = models.BooleanField(default=False)  # Indicates whether this answer is correct

    def __str__(self):
            return f'{self.text} - {self.question.text}'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Each user has one profile

    def __str__(self):
        return self.user.username
