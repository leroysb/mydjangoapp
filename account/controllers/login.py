from ..models import User
from .redirect import get_redirect_if_exists
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.http import HttpResponse, request

from email import message
from django import forms
from django.forms import ModelForm, EmailField, CharField
from django.contrib.auth import authenticate, get_user_model
# from django.contrib.auth.forms import UserCreationForm
from account.models import User
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

class loginForm(ModelForm):

    email = EmailField(
        widget=forms.EmailInput(),
        max_length=100, 
        label=_("Email / Username"),
        validators=[RegexValidator(r'^[a-z0-9]+(\.?[a-z0-9])*[a-z0-9]+@[a-z0-9\-]*\.[a-z]{1,20}$', message=_("Please enter a valid email"))],
    )
    password = CharField(
        widget=forms.PasswordInput(),
        label=_("Password"),
        validators=[RegexValidator(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%]).{8,24}$', )],
    )

    class Meta:
        model = get_user_model()
        fields = ['email', 'password']

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        return email

def LoginView(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return redirect("core:index")

    context= {}
    form = loginForm()
    context['form'] = form

    if request.method == 'POST':
        form = loginForm(request.POST)

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

    return render(request, 'registration/login.html', context)