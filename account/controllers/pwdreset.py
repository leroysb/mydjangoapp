from email import message
from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from .redirect import get_redirect_if_exists
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from ..utils import activation_token
from django.contrib.sites.shortcuts import get_current_site
from threading import Thread

User = get_user_model()

class pwdResetForm(forms.Form):
    email = forms.CharField(
        max_length=100, 
        label=_("Email"),
        validators=[RegexValidator(r'^[a-z0-9]+(\.?[a-z0-9])*[a-z0-9]+@[a-z0-9\-]*\.[a-z]{2,20}$', message=_("Please enter a valid email"))],
    )

    def clean_email(self):
        email = self.cleaned_data.get("email").lower()
        if not User.objects.filter(email__iexact=email).exists():
            msg = _("Account does not exist")
            raise forms.ValidationError(msg, code="invalid")
        return email

def resetPwdView(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        destination = get_redirect_if_exists(request)
        if destination:
            return redirect(destination)
        return redirect("core:index")

    context = {}
    form = pwdResetForm()
    context['form'] = form

    if request.POST:
        form = pwdResetForm(request.POST)

        if form.is_valid():
            email = request.POST['email']
            user = User.objects.get(email__iexact=email)
            resetPwd(request, user)
            request.session['msg'] = "Check your email for the reset password link."
            return redirect('account:authmsg')

    return render(request, "account/pwdreset.html", context)

class EmailThread(Thread):
    def __init__(self, email):
        self.email = email
        Thread.__init__(self)

    def run(self):
        self.email.send()

def resetPwd(request, user):
    emailTemplate = render_to_string("emails/emailPwdReset.html", {
        'name': user.full_name,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': activation_token.make_token(user),
        'siteURI': get_current_site(request),
    })
    email = EmailMessage(
        'Reset your account password',
        emailTemplate,
        settings.EMAIL_HOST_USER,
        [request.POST['email'],],
    )
    email.fail_silently=False
    EmailThread(email).start()

def userVerifyView(request, uidcoded, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidcoded))
        user = User.objects.get(uid=uid)
    except Exception as e:
        user = None
    if user and activation_token.check_token(user, token):
        email = user['email']
        password = user['password']
        account = authenticate(request, email=email, password=password)
        if account:
            login(request, account)
            return redirect('core:index')

    request.session['msg'] = "Reset failed. Try again later."
    return redirect('account:authmsg')

