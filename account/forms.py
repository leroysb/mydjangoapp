from django import forms
from django.forms import ModelForm, EmailField, CharField, Form
from django.contrib.auth import authenticate, get_user_model
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
        model = get_user_model()
        fields = ['email', 'password']

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        return email

class signinForm(Form):

    email = EmailField(widget=forms.EmailInput(), label=_("Email"))
    password = CharField(widget=forms.PasswordInput(), label=_("Password"))

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        return email

#####

class subscribeForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ['email', 'alias', 'password']

    email = EmailField(max_length=200, label=_("Email"))
    alias = CharField(max_length=14, label=_("Username"))
    password = CharField(widget=forms.PasswordInput, label=_("Password"))

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        return email