from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .models import Question
from django.contrib.auth.decorators import login_required

def home_view(request):
    user_name = request.user.username if request.user.is_authenticated else 'Gość'
    return render(request, 'quiz/home.html', {'user_name': user_name})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Możesz dodać tutaj logikę logowania po rejestracji
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def quiz_view(request):
    question_index = request.session.get('question_index', 0)
    questions = Question.objects.prefetch_related('answers').all()

    if question_index >= len(questions):
        # End of the quiz
        request.session['question_index'] = 0  # Reset the index for the next time
        score = request.session.get('score', 0)  # Retrieve the score from the session
        request.session['score'] = 0  # Reset the score in the session
        user_name = request.user.username if request.user.is_authenticated else 'Gość'
        return render(request, 'quiz/finish.html', {'score': score, 'user_name': user_name})

    question = questions[question_index]
    is_correct = None

    if request.method == 'POST':
        if 'answer' in request.POST:
            user_answer_id = request.POST.get('answer')
            user_answer = question.answers.get(id=user_answer_id)
            is_correct = user_answer.is_correct
            if is_correct:
                # Increase user's score if the answer is correct
                request.session['score'] = request.session.get('score', 0) + 1
        elif 'next' in request.POST:
            request.session['question_index'] = question_index + 1
            return redirect('quiz:quiz_question')

    return render(request, 'quiz/question.html', {
        'question': question,
        'answers': question.answers.all(),
        'is_correct': is_correct
    })

