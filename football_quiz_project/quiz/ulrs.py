from django.urls import path
from .views import quiz_view

app_name = 'quiz'

urlpatterns = [
    path('question/', quiz_view, name='quiz_question')
]

