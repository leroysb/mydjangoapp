from django.urls import path
from .controllers.login import LoginView
from .controllers.subscribe import SubscribeView
from .controllers.signin import SigninView
from .controllers.logout import LogoutView
from .controllers.verification import AuthView

app_name = "account"

urlpatterns = [
    path('auth/', AuthView, name='auth'),
    path('login/', LoginView, name='login'),
    path('signin/', SigninView, name='signin'),
    path('subscribe/', SubscribeView, name='subscribe'),
    path('logout/', LogoutView, name='logout'),
]