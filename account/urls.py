from django.urls import path
from .views import *

app_name = "account"

urlpatterns = [
    path('auth/', AuthView, name='auth'),
    path('login/', LoginView, name='login'),
    path('signin/', SigninView, name='signin'),
    path('logout/', LogoutView, name='logout'),
    path('subscribe/', SubscribeView, name='subscribe'),
]