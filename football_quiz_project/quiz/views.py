from django.shortcuts import render
from .models import Question, Answer

# View for the quiz - displays a question and its answers.
def quiz_view(request):
    question = Question.objects.first()
    answers = question.answers.all()
    is_correct = None
    user_answer = None

    if request.method == 'POST':
        user_answer_id = request.POST.get('answer')
        user_answer = Answer.objects.get(id=user_answer_id)
        is_correct = user_answer.is_correct


    return render(request, 'quiz/question.html', {
        'question': question, 
        'answers': answers,
        'is_correct': is_correct,
        'user_answer': user_answer
    })




