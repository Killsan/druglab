from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404 
from django.urls import reverse 
from django.views import generic
from .models import *

def index(request):
    
    return render(request, 'indx/index.html')

def registration(request):
    nick = request.POST.get('Nickname')
    email = request.POST.get('Email')
    password1 = request.POST.get('password')
    password2 = request.POST.get('rep_pass')

    if nick == "" or email == "" or password1 == "" or password2 == "":
        return render(request, 'indx/registration.html', {
            'error': 'error',
            'nick': nick,
            'email': email,
        })
    elif password1 != password2:
        return render(request, 'indx/registration.html', {
            'error': 'error',
            'nick': nick,
            'email': email,
            'pass_error': 'Passwords are not the same',
        })
    else:
        new_user = App_user(int(App_user.objects.all().count())+1, nick, email, password1)
        new_user.save()
        return render(request, 'indx/registration.html', {
            'message': "User created",
        })

def login(request):
    nickname = request.POST.get('Nickname')
    print(nickname)
    Password = request.POST.get('password')

    try:
        user = App_user.objects.filter(nick=nickname)[0]
    except IndexError:
        user = None

    if user == None:
        return render(request, 'indx/login.html', {
            'error': "User not found",
        })
    elif user.password == Password:
        return render(request, 'indx/account.html', {
            'user': user,
        })
    else:
        return render(request, 'indx/login.html', {
            'error': "Incorrect password",
        })

def account(request):
    user = App_user.objects.filter(nick=request.POST.get('nickname'))
    return render(request, 'indx/account.html', {'user': user})

def shop(request):
    return render(request, 'indx/shop.html')