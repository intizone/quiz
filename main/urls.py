from django.contrib import admin
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('quizzes/', views.quizzes, name='quizzes'),
    path('create_quiz/', views.create_quiz, name='create_quiz'),
]