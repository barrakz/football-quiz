from django.shortcuts import render
from .models import Question, Answer

# View for the quiz - displays a question and its answers.
from django.shortcuts import render, redirect
from .models import Question, Answer

def quiz_view(request):
    question = Question.objects.first()
    answers = question.answers.all()
    is_correct = None
    user_answer = None

    # Check if the user has already answered
    if f'answered_{question.id}' in request.session:
        user_answer_id = request.session[f'answered_{question.id}']
        user_answer = Answer.objects.get(id=user_answer_id)
        is_correct = user_answer.is_correct
        return render(request, 'quiz/question.html', {
            'question': question, 
            'answers': answers,
            'is_correct': is_correct,
            'user_answer': user_answer,
            'answered': True  # Add a flag to indicate that the answer has been given
        })

    if request.method == 'POST':
        user_answer_id = request.POST.get('answer')
        user_answer = Answer.objects.get(id=user_answer_id)
        is_correct = user_answer.is_correct
        request.session[f'answered_{question.id}'] = user_answer_id  # Save the answer in the session

        return render(request, 'quiz/question.html', {
            'question': question, 
            'answers': answers,
            'is_correct': is_correct,
            'user_answer': user_answer
        })

    return render(request, 'quiz/question.html', {
        'question': question, 
        'answers': answers
    })
