from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django.contrib.auth.models import User 
from .models import *

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CreateBotForm(ModelForm):
    class Meta:
        model = Bot
        fields = ['name', 'token', 'owner']

    def __init__(self, *args, **kwargs):
        super(CreateBotForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget = TextInput(attrs={'id': 'name_input'})
    # def __init__(self, *args, **kwargs):
    #     super(CreateBotForm, self).__init__(*args, **kwargs)
    #     self.fields['name'].widget.attrs.update({'class' : 'name_class'})
    #     self.fields['token'].widget.attrs.update({'class' : 'token_class'})
    #     self.fields['owner'].widget.attrs.update({'class' : 'owner_class'})