from django.urls import path
from .views import *
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.http import request

app_name = "account"

urlpatterns = [
    path('auth/', AuthView, name='auth'),
    path('login/', LoginView, name='login'),
    # path('login/', auth_views.LoginView.as_view(template_name = 'account/login.html'), name='login'),
    path('logout/', LogoutView, name='logout'),
    path('subscribe/', SubscribeView, name='subscribe'),
]