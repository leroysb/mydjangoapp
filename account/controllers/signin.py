from ..models import User
from .redirect import get_redirect_if_exists
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.http import HttpResponse, request

from email import message
from django import forms
from django.forms import Form, ModelForm, EmailField, CharField
from django.contrib.auth import authenticate, get_user_model
# from django.contrib.auth.forms import UserCreationForm
from account.models import User
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

class signinForm(Form):

    email = EmailField(
        widget=forms.EmailInput(),
        max_length=100, 
        label=_("Email"),
        validators=[RegexValidator(r'^[a-z0-9]+(\.?[a-z0-9])*[a-z0-9]+@[a-z0-9\-]*\.[a-z]{2,3}$', message=_("Please enter a valid email"))],
    )
    password = CharField(
        widget=forms.PasswordInput(),
        label=_("Password"),
        validators=[RegexValidator(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%]).{8,24}$', message=_(" Password should be 8 to 24 characters. Must include uppercase and lowercase letters, a number and a special character."))],
    )

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        return email

def SigninView(request, *args, **kwargs):

    context= {}
    context['sess_email'] = request.session['sess_email']
    form = signinForm()
    context['form'] = form

    user = request.user
    if user.is_authenticated:
        return redirect("core:index")

    if request.method == 'POST':
        form = signinForm(request.POST)

        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)

            if user:
                login(request, user)
                destination = get_redirect_if_exists(request)

                if destination:
                    return redirect(destination)

                return redirect("core:index")

    return render(request, 'registration/signin.html', context)        