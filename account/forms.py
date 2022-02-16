from django import forms
from django.forms import ModelForm, EmailField, CharField, Form
from django.forms.widgets import TextInput, Textarea

from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from account.models import User
from django.utils.translation import gettext_lazy as _


#####

class authForm(Form):
    email = CharField(widget=forms.EmailInput(), max_length=100, label=_("Email"),)

#####

class loginForm(ModelForm):

    email = CharField(widget=forms.EmailInput(), label=_("Re-enter Email"))
    password = CharField(widget=forms.PasswordInput(), label=_("Password"))

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        return email

#####

class subscribeForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    email = EmailField(max_length=200, label=_("Email"))
    username = CharField(max_length=14, label=_("Username"))
    password = CharField(widget=forms.PasswordInput, label=_("Password"))

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        return email