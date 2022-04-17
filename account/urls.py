from django.urls import path
from .controllers.login import LoginView
from .controllers.subscribe import SubscribeView
from .controllers.signin import SigninView
from .controllers.logout import LogoutView
from .controllers.verification import AuthView
from .controllers.activate import userActivationView
from .controllers.signinalt import SignAltView, userVerifyView
from .controllers.messages import AuthMsgView

app_name = "account"

urlpatterns = [
    path('auth/', AuthView, name='auth'),
    path('auth/reply/', AuthMsgView, name='authmsg'),
    path('login/', LoginView, name='login'),
    path('login/verify/', SigninView, name='signin'),
    path('login/alt/', SignAltView, name='signinalt'),
    path('login/identifier?state=<uidcoded><token>/', userVerifyView, name='signinauth'),
    path('subscribe/', SubscribeView, name='subscribe'),
    path('login/identifier?state=activate-<uidcoded><token>/', userActivationView, name='activate'),
    path('logout/', LogoutView, name='logout'),
]
