from django import forms
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate, get_user_model, login
from django.shortcuts import redirect, render
from .redirect import get_redirect_if_exists
User = get_user_model()

class subscribeForm(forms.ModelForm):

    alias = forms.CharField(
        label=_("Username"),
        validators=[RegexValidator(r'^[A-Za-z0-9-_]{3,18}$', message="Username should be between 3-18 characters, and must contain letters, numbers, or '_' only.")],
    )
    email = forms.EmailField(
        label=_("Email"),
        widget=forms.EmailInput(),
        max_length=100, 
        validators=[RegexValidator(r'^[a-z0-9]+(\.?[a-z0-9])*[a-z0-9]+@[a-z0-9\-]*\.[a-z]{2,3}$', message=_("Please enter a valid email"))],
    )
    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput,
        validators=[RegexValidator(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%]).{8,24}$', message=_(" Password should be 8 to 24 characters. Must include uppercase and lowercase letters, a number and a special character."))]
    )

    class Meta:
        model = User
        fields = ('email', 'alias', 'password')

    def clean_alias(self):
        cleaned_data = super(subscribeForm, self).clean()
        alias = cleaned_data.get("alias")
        if User.objects.filter(alias__iexact=alias).exists():
            msg = f"{alias} is not available!"
            self.add_error('alias', msg)
        return alias

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

def SubscribeView (request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return redirect("core:index")

    context= {}
    context['sess_email'] = request.session['sess_email']
    context['form'] = subscribeForm()

    if request.method == "POST":
        form = subscribeForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email'].lower()
            alias = form.cleaned_data['alias']
            password = form.cleaned_data['password']
            user = authenticate(email=email, alias=alias, password=password)
            login(request, user)
            del request.session['sess_email']
            destination = get_redirect_if_exists(request)
            if destination:
                return redirect('destination')
            return redirect('core:index')
        else:
            context['form'] = form
            context['sess_email'] = request.session['sess_email']
            context['alias'] = request.POST['alias']

    return render(request, "account/subscribe.html", context)