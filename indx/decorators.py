from django.http import HttpResponse
from django.shortcuts import redirect
from .models import *

def unauth_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('indx:index')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not allowed to be on this page")
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'customer':
            return redirect('indx:index')
        
        if group == 'admin':
            return view_func(request, *args, **kwargs)
    return wrapper_func

def bot_owner(view_func):
    def wrapper_func(request, bot, *args, **kwargs):
        bots = Bot.objects.filter(owner=request.user)
        access = False
        for i in bots:
            if i.name == bot:
                access = True
        if access == True:
            return view_func(request, bot, *args, **kwargs)
        else:
            return HttpResponse("You don't have an access to this bot")
    return wrapper_func
        