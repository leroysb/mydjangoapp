from email import message
from django import forms
from django.forms import ModelForm, EmailField, CharField, Form
from django.contrib.auth import authenticate, get_user_model
# from django.contrib.auth.forms import UserCreationForm
from account.models import User
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

from ..models import User
from .redirect import get_redirect_if_exists
from django.contrib.auth import authenticate
from django.shortcuts import redirect, render
from django.http import HttpResponse, request

#####

class authForm(Form):
    email = CharField(
        widget=forms.EmailInput(), 
        max_length=100, 
        label=_("Email"),
        validators=[RegexValidator(r'^[a-z0-9]+(\.?[a-z0-9])*[a-z0-9]+@[a-z0-9\-]*\.[a-z]{2,3}$', message=_("Please enter a valid email"))],
    )

def AuthView(request, *args, **kwargs):

    context = {}
    form = authForm()
    context['form'] = form

    user = request.user
    if user.is_authenticated:
        destination = get_redirect_if_exists(request)
        if destination:
            return redirect(destination)
        return redirect("core:index")

    if request.method == 'POST':
        form = authForm(request.POST)

        if form.is_valid():
            email = request.POST['email']
            request.session['sess_email'] = email.lower()

            if User.objects.filter(email__iexact=email).exists():
                return redirect("account:signin")
            else:
                return redirect("account:subscribe")

        else:
            context['form'] = authForm(request.POST, initial=form)

    return render(request, "account/auth.html", context)
