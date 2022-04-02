from .redirect import get_redirect_if_exists
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from email import message
from django import forms
from django.forms import ValidationError
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

User = get_user_model

class loginForm(forms.Form):

    email = forms.CharField(
        widget=forms.EmailInput(), 
        max_length=100, 
        label=_("Email"),
        validators=[RegexValidator(r'^[a-z0-9]+(\.?[a-z0-9])*[a-z0-9]+@[a-z0-9\-]*\.[a-z]{2,20}$', message=_("Please enter a valid email"))],
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label=_("Password"),
    )

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        return email

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data['email']
        password = cleaned_data['password']
        user = authenticate(request, email=email, password=password)
        if not user:
            msg = _("Incorrect username and password pairing!!")
            raise ValidationError(msg, code='invalid')

def LoginView(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return redirect("core:index")
    context= {}
    context['form'] = loginForm()
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
        else:
            context['form'] = form
    return render(request, 'registration/signin.html', context)