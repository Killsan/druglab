from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404 
from django.urls import reverse 
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required

from .models import *

@login_required(login_url='indx:login')
def index(request):
    return render(request, 'indx/index.html')

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

def shop(request):
    return render(request, 'indx/shop.html')