from email import message
from django import forms
from django.forms import ModelForm, EmailField, CharField
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

from .redirect import get_redirect_if_exists
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

class subscribeForm(ModelForm):

    class Meta:
        model = get_user_model()
        fields = ['email', 'alias', 'password']

    alias = CharField(
        label=_("Username"),
        validators=[RegexValidator(r'^[A-Za-z0-9-_]{3,18}$', message="Username should be between 3-18 characters, and must contain letters, numbers, or '_' only.")],
    )
    email = EmailField(
        widget=forms.EmailInput(),
        max_length=100, 
        label=_("Email"),
        validators=[RegexValidator(r'^[a-z0-9]+(\.?[a-z0-9])*[a-z0-9]+@[a-z0-9\-]*\.[a-z]{2,3}$', message=_("Please enter a valid email"))],
    )
    password = CharField(
        widget=forms.PasswordInput(),
        label=_("Password"),
        validators=[RegexValidator(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%]).{8,24}$', message=_(" Password should be 8 to 24 characters. Must include uppercase and lowercase letters, a number and a special character."))]
    )

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

def SubscribeView (request, *args, **kwargs):
    
    context= {}
    context['sess_email'] = request.session['sess_email']
    form = subscribeForm()
    context['form'] = form

    user = request.user
    if user.is_authenticated:
        return redirect("core:index")

    if request.POST:
        form = subscribeForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            alias = form.cleaned_data.get('alias')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, alias=alias, password=password)
            login(request, user)
            destination = get_redirect_if_exists(request)

            if destination:
                return redirect('destination')
            return redirect('core:index')

        else:
            context['form'] = form

    return render(request, 'registration/subscribe.html', context)