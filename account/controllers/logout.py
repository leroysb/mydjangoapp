from ..models import User
from .redirect import get_redirect_if_exists
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.http import HttpResponse, request

# from django.contrib import messages

def LogoutView(request, *args, **kwargs):
    logout(request)
    # messages.success(request, 'Successfully logged out!', fail_silently=True)
    destination = get_redirect_if_exists(request)
    if destination:
        return redirect(destination)
    return redirect("core:index")