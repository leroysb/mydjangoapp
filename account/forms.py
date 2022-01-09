from django import forms
from django.forms import ModelForm, EmailField, CharField
from django.forms.widgets import TextInput, Textarea

from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from account.models import User
from django.utils.translation import gettext_lazy as _


#####

class authForm(forms.Form):
    email = CharField(max_length=100, label=_("Email"),)

#####

class loginForm(ModelForm):

    email = CharField(max_length=100, required=True, label=_("Email now"))
    password = CharField(widget=forms.PasswordInput(), label=_("Password"))      

#####

class subscribeForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

    email = EmailField(max_length=200, label=_("Email"))
    username = CharField(max_length=200, label=_("Username"))
    password1 = CharField(widget=forms.PasswordInput, label=_("Password"))
    password2 = CharField(widget=forms.PasswordInput, label=_("Password confirmation"))

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        return email