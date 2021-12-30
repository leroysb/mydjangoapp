from account.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import subscribeForm, authForm, loginForm
from django.shortcuts import redirect, render
from django.contrib import messages

# from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import get_user_model
# Account = get_user_model()

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import permissions, status


def LogoutView(request, *args, **kwargs):
    logout(request)
    # messages.success(request, 'Successfully logged out!', fail_silently=True)
    destination = get_redirect_if_exists(request)
    if destination:
        return redirect(destination)
    return redirect("core:index")

######    

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

    # if request.POST:
    if request.method == 'POST':
        form = authForm(request.POST)
        email = request.POST['email']
        email = email.lower()

        request.session['sess_email'] = email

        if User.objects.filter(email=email).exists():
            return redirect("account:login")
        else:
            return redirect("account:subscribe")

    return render(request, "account/auth.html", context)

######

def LoginView(request, *args, **kwargs):

    context= {}
    context['sess_email'] = request.session['sess_email']
    context['form'] = loginForm()

    user = request.user
    if user.is_authenticated:
        return redirect("core:index")

    # if request.POST:
    if request.method == 'POST':
        form = loginForm(request.POST)

        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                destination = get_redirect_if_exists(request)

                if destination:
                    return redirect(destination)

                return redirect("core:index")

    return render(request, 'account/registration/login.html', context)

######

def SubscribeView (request, *args, **kwargs):
    
    context= {}
    context['sess_email'] = request.session['sess_email']
    form = subscribeForm()
    context['form'] = form

    user = request.user
    if user.is_authenticated:
        return redirect("core:index")

    # if request.POST:
    if request.method == 'POST':
        form = subscribeForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            username = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, username=username, password=raw_password)
            login(request, account)
            destination = kwargs.get("next")

            if destination:
                return redirect('destination')
                
            return redirect('core:index')

        else:
            context['form'] = form

    return render(request, 'account/subscribe.html', context)

######

def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get("next"):
            redirect = str(request.GET.get("next"))
    return redirect