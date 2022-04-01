from urllib import request
from .redirect import get_redirect_if_exists
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from email import message
from django import forms
from django.forms import Form, ModelForm, EmailField, CharField, ValidationError
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

User = get_user_model()

class signinForm(Form):

    email = EmailField(
        widget=forms.EmailInput(),
        max_length=100, 
        label=_("Email"),
    )
    password = CharField(
        widget=forms.PasswordInput(),
        label=_("Password"),
    )
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data['email']
        password = cleaned_data['password']
        user = authenticate(request, email=email, password=password)
        if not user:
            msg = _("Incorrect username, password pairing!!")
            raise ValidationError(msg, code='invalid')

def SigninView(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return redirect("core:index")

    context= {}
    context['sess_email'] = request.session['sess_email']
    context['form'] = signinForm()

    if request.method == 'POST':
        form = signinForm(request.POST)

        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)

            if user:
                login(request, user)
                del request.session['sess_email']
                destination = get_redirect_if_exists(request)

                if destination:
                    return redirect(destination)

                return redirect("core:index")
        else:
            context['form'] = form

    return render(request, 'registration/signin.html', context)        