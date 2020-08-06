from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404 
from django.urls import reverse 
from django.views import generic

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'videos/index.html'