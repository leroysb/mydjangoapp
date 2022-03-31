from django import forms
from django.forms import ModelForm, EmailField, CharField, Form
from django.contrib.auth import authenticate, get_user_model
# from django.contrib.auth.forms import UserCreationForm
from account.models import User
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


#####

class authForm(Form):
    email = CharField(
        widget=forms.EmailInput(), 
        max_length=100, 
        label=_("Email"),
        validators=[RegexValidator(r'^[a-z0-9]+(\.?[a-z0-9])*[a-z0-9]+@[a-z0-9\-]*\.[a-z]{2,3}$', message=_("Please enter a valid email"))],
    )

#####

class loginForm(ModelForm):

    email = CharField(
        widget=forms.EmailInput(),
        max_length=100, 
        label=_("Email"),
        validators=[RegexValidator(r'^[a-z0-9]+(\.?[a-z0-9])*[a-z0-9]+@[a-z0-9\-]*\.[a-z]{2,3}$', message=_("Please enter a valid email"))],
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

class signinForm(Form):

    email = CharField(
        widget=forms.EmailInput(),
        max_length=100, 
        label=_("Email"),
        validators=[RegexValidator(r'^[a-z0-9]+(\.?[a-z0-9])*[a-z0-9]+@[a-z0-9\-]*\.[a-z]{2,3}$', message=_("Please enter a valid email"))],
    )
    password = CharField(
        widget=forms.PasswordInput(),
        label=_("Password"),
        validators=[RegexValidator(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%]).{8,24}$')],
    )

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        return email

#####

class subscribeForm(ModelForm):

    class Meta:
        model = get_user_model()
        fields = ['email', 'alias', 'password']

    alias = CharField(
        label=_("Username"),
        validators=[RegexValidator(r'^[A-Za-z0-9-_]{3,18}$', message="Username should be between 3-18 characters, and must contain letters, numbers, or '_' only.")],
    )
    email = CharField(
        widget=forms.EmailInput(),
        max_length=100, 
        label=_("Email"),
        validators=[RegexValidator(r'^[a-z0-9]+(\.?[a-z0-9])*[a-z0-9]+@[a-z0-9\-]*\.[a-z]{2,3}$', message=_("Please enter a valid email"))],
    )
    password = CharField(
        widget=forms.PasswordInput(),
        label=_("Password"),
        validators=[RegexValidator(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%]).{8,24}$', )],
    )

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user