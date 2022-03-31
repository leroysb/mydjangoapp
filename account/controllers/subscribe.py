from django.contrib.auth import authenticate, get_user_model
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from .redirect import get_redirect_if_exists
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from ..admin import UserCreationForm
from ..models import User

class subscribeForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ['email', 'alias', 'password']

    def cleaned_alias(self, *args, **kwargs):
        alias = self.cleaned_data.get("alias")

        if User.objects.filter(alias=alias).exists():
            raise ValidationError ("Username is taken!!")
        return alias

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
            del request.session['alias']
            del request.session['sess_email']
            destination = get_redirect_if_exists(request)

            if destination:
                return redirect('destination')
            return redirect('core:index')

        else:
            context['form'] = form
            alias = request.POST['alias']
            context['alias'] = request.session['alias']

    return render(request, 'registration/subscribe.html', context)