from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404 
from django.urls import reverse 
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .decorators import *
from .models import *

@login_required(login_url='indx:login')
def index(request):
    context = {
        'bots': Bot.objects.filter(owner=request.user),
    }
    return render(request, 'indx/index.html', context)

@unauth_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user != None:
            login(request, user)
            return redirect('indx:index')
        else:
            messages.error(request, "Username or password is incorrect")

    context = {}
    return render(request, 'indx/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('indx:login')

@unauth_user
def registrationPage(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('indx:login')
        else:
            for field in form.errors:
                messages.error(request, form.errors[field].as_text())

    context = {'form': form,}
    return render(request, 'indx/registration.html', context)

@login_required(login_url='indx:login')
def userPage(request):
    context = {}
    return render(request, 'indx/user.html', context)

@login_required(login_url='indx:login')
@bot_owner
def botInfo(request, bot):
    context = {
        'bot': Bot.objects.filter(name=bot)[0],
    }
    return render(request, 'indx/botInfo.html', context)

@login_required(login_url='indx:login')
def create_main(request):

    if request.method == 'POST':
        form = CreateBotForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("indx:index")
        else:
            messages.error("Form is not valid")

    context = {
        'bots': Bot.objects.filter(owner=request.user),
        'form': CreateBotForm(initial={'owner': request.user}),
    }
    return render(request, 'indx/creation.html', context)

@login_required(login_url='indx:login')
@bot_owner
def botUpdate(request, bot):
    return HttpResponse('<h1>FUck u</h1>')