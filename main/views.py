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
        if models.User.objects.filter(username=username).exists():
            return redirect('main:signup')
        else:
            user = models.User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('main:signin')
    return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:cards')
        else:
            return HttpResponse('Invalid username or password')
    return render(request, 'signin.html')


@login_required
def cards(request):
    if request.user.is_authenticated:
        cards = models.Quiz.objects.filter(author=request.user)
        return render(request, 'cards.html', {'cards': cards})
    else:
        return redirect('main:signin')

def sign_out(request):
    logout(request)
    return redirect('main:signin')
