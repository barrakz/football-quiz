from .models import Question, Answer

# View for the quiz - displays a question and its answers.
from django.shortcuts import render, redirect
from .models import Question, Answer

def quiz_view(request):
    question_index = request.session.get('question_index', 0)
    questions = Question.objects.prefetch_related('answers').all()

    if question_index >= len(questions):
        # Zakończenie quizu
        request.session['question_index'] = 0  # Reset indeksu na następny raz
        return render(request, 'quiz/finish.html')

    question = questions[question_index]
    is_correct = None

    if request.method == 'POST':
        if 'answer' in request.POST:
            user_answer_id = request.POST.get('answer')
            user_answer = question.answers.get(id=user_answer_id)
            is_correct = user_answer.is_correct
        elif 'next' in request.POST:
            request.session['question_index'] = question_index + 1
            return redirect('quiz:quiz_question')

    return render(request, 'quiz/question.html', {
        'question': question,
        'answers': question.answers.all(),
        'is_correct': is_correct
    })
