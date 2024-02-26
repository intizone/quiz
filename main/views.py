from main import models
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        phone = request.POST['phone']
        if models.Avtor.objects.filter(username=username).exists():
            return redirect('main:signup')
        else:
            models.Avtor.objects.create(
                username=username,
                email=email,
                password=password,
                fullname=fullname,
                phone=phone
            )
            return redirect('main:signin')
    return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:quizzes')
        else:
            return HttpResponse('Invalid username or password')
    return render(request, 'signin.html')


@login_required
def quizzes(request):
    if request.user.is_authenticated:
        quizzes = models.Quiz.objects.filter(author=request.user)
        return render(request, 'quizzes.html', {'quizzes': quizzes})
    else:
        return redirect('main:signin')

def sign_out(request):
    logout(request)
    return redirect('main:signin')
