from django.urls import path
from .controllers.login import LoginView
from .controllers.signup import SubscribeView
from .controllers.signin import SigninView
from .controllers.logout import LogoutView
from .controllers.search import AuthView
from .controllers.activate import userActivationView
from .controllers.pwdreset import resetPwdView, userVerifyView
from .controllers.resMessages import AuthMsgView
from .controllers.editpassword import editPwdView

app_name = "account"

urlpatterns = [
    path('auth/', AuthView, name='auth'),
    path('auth/reply/', AuthMsgView, name='authmsg'),
    path('login/', LoginView, name='login'),
    path('login/dynamic/', SigninView, name='signin'),
    path('login/identifier?state=verify-<uidcoded><token>/', userVerifyView, name='signinauth'),
    path('login/dynamic/resets/', resetPwdView, name='reset1'),
    path('login/dynamic/resets/identifier?state=resets-<uidcoded><token>/', editPwdView, name='reset2'),
    path('subscribe/', SubscribeView, name='subscribe'),
    path('login/identifier?state=activate-<uidcoded><token>/', userActivationView, name='activate'),
    path('logout/', LogoutView, name='logout'),
]
