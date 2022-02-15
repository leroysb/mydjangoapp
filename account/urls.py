from django.urls import path
from .views import *
from .views import *

app_name = "account"

urlpatterns = [
    path('auth/', AuthView, name='auth'),
    path('login/', LoginView, name='login'),
    path('logout/', LogoutView, name='logout'),
    path('subscribe/', SubscribeView, name='subscribe'),
]