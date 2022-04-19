from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect, render
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from ..utils import activation_token
from threading import Thread

User = get_user_model()

class EmailThread(Thread):
    def __init__(self, email):
        self.email = email
        Thread.__init__(self)

    def run(self):
        self.email.send()

def activationEmail(request, user):
    emailTemplate = render_to_string("emails/emailActivation.html", {
        'name': user.full_name,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': activation_token.make_token(user),
        'siteURI': get_current_site(request),
    })
    email = EmailMessage(
        'Verify Email',
        emailTemplate,
        settings.EMAIL_HOST_USER,
        [request.POST['email'],],
    )
    email.fail_silently=False
    EmailThread(email).start()

class changePwdForm(forms.Form):
    email = forms.CharField( label = _("Email"))
    pwd = forms.CharField( widget = forms.PasswordInput(), label = _("New Password"))
    pwd2 = forms.CharField( widget = forms.PasswordInput(), label = _("Re-enter Password"))

    def clean_password(self):
        password = self.cleaned_data('pwd1')
        password2 = self.cleaned_data('pwd2')
        if password != password2:
            msg = _("Passwords do not match!")
            raise forms.ValidationError(msg, code='Invalid')
        return password

def editPwdView(request, uidcoded, token):
    user = request.user
    if user.is_authenticated:
        return redirect("core:index")

    context={}
    context['form'] = changePwdForm()

    try:
        uid = force_str(urlsafe_base64_decode(uidcoded))
        user = User.objects.get(uid=uid)
    except Exception as e:
        user = None

    if user and activation_token.check_token(user, token):
        context['usemail'] = user.email

        if request.POST:
            form = changePwdForm(request.POST)
            if form.is_valid:
                email = form.cleaned_data('email')
                user = User.objects.get(uid=uid)
                user.set_password(form.cleaned_data["password"])
                user.save()
                request.session['msg'] = "Password successfully changed."
                return redirect('account:authmsg')

    return render(request, 'account/authReset.html', context)