from django.shortcuts import render
from .models import Question

# View for the quiz - displays a question and its answers.
def quiz_view(request):
    question = Question.objects.first()
    answers = question.answers.all()

    return render(request, 'quiz/question.html', {'question': question, 'answers': answers})




