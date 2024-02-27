from django.contrib import admin
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('quizzes/', views.quizzes, name='quizzes'),
    path('quiz_create/', views.quiz_create, name='quiz_create'),
]