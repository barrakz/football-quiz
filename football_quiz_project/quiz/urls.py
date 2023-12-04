from django.urls import path
from .views import quiz_view, home_view

app_name = 'quiz'

urlpatterns = [
    path('', home_view, name='home'),
    path('question/', quiz_view, name='quiz_question'),
]

