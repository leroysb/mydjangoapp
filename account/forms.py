from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.forms.widgets import TextInput, Textarea
from account.models import User
from django.forms import ModelForm, EmailField, CharField
from django.utils.translation import gettext_lazy as _


#####

class authForm(ModelForm):

    class Meta:
        model = User
        fields = ['email',]

    email = EmailField(max_length=100, required=True, help_text="Enter a valid email address", label=_("Email"),)

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        return email

#####

class loginForm(forms.Form):
    email = EmailField(max_length=200, label=_("Email"))
    password = CharField(widget=forms.PasswordInput, label=_("Password"))

    # class Meta:
    #     model = User
    #     fields = ['email', 'password',]


    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Wrong password!")      

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