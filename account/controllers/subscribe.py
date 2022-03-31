from django import forms
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate, get_user_model, login
from django.shortcuts import redirect, render
from .redirect import get_redirect_if_exists
User = get_user_model()

class subscribeForm(forms.Form):

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

    def clean_alias(self):
        alias = self.cleaned_data.get('alias')

        if not User.objects.filter(alias__iexact=alias).exists():
            raise forms.ValidationError ({'alias': "Username is taken!!"})
        return alias

def SubscribeView (request, *args, **kwargs):
    context= {}
    context['sess_email'] = request.session['sess_email']
    context['form'] = subscribeForm()

    user = request.user
    if user.is_authenticated:
        return redirect("core:index")

    form = subscribeForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data.get('email').lower()
        alias = form.cleaned_data.get('alias')
        password = form.cleaned_data.get('password')

        try: 
            user = authenticate(email=email, alias=alias, password=password)
            user = User.objects.create_user(email, alias, password)
        except:
            user = None

        if user != None:
            login(request, user)
            destination = get_redirect_if_exists(request)
            if destination:
                return redirect('destination')
            return redirect('core:index')
        else:
            alias = request.POST['alias']
            context['alias'] = request.session['alias']
            return render(request, 'account/subscribe.html', context)

    return render(request, "account/subscribe.html", context)