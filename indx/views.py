from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404 
from django.urls import reverse 
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .decorators import *
from .models import *

@login_required(login_url='indx:login')
def index(request):
    return render(request, 'indx/index.html')

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
def shopSearch(request):
    search = request.POST.get('search')
    obj = str(search)
    try:
        all_products = []
        found_products = []
        for i in Product.objects.all():
            all_products.append(i.product_name)
        for i in all_products:
            if obj in i:
                found_products.append(Product.objects.filter(product_name=i)[0])
        context = {'objects': found_products, 'search': search}
    except IndexError: 
        return render(request, 'indx/shop.html', {
            'message': 'No products found, but u can add them if u want',
            'search': search,
        })
    else:
        return render(request, 'indx/shop.html', context)