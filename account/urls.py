from django.urls import path
from . import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = "account"

urlpatterns = [
    path('auth/', views.AuthView, name='auth'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('subscribe/', views.SubscribeView, name='subscribe'),
]