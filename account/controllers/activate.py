from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model as User
from django.shortcuts import redirect, render
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from ..utils import activation_token
from django.contrib.sites.shortcuts import get_current_site
from .redirect import get_redirect_if_exists
import threading

class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()

def activationEmail(request, user):
    template = render_to_string("account/emailActivation.html", {
        'name': user.full_name,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': activation_token.make_token(user),
        'siteURI': get_current_site(request),
    })
    email = EmailMessage(
        'Verify Email - Leroy Buliro',
        template,
        settings.EMAIL_HOST_USER,
        [request.POST['email']],
    )
    email.fail_silently=False
    EmailThread(email).start()

def userActivationView(request, uidcoded, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidcoded))
        user = User.objects.get(pk=uid)
    except Exception as e:
        user = None

    if user and activation_token.check_token(user, token):
        user.is_verified = True
        user.save()
        destination = get_redirect_if_exists(request)
        if destination:
            return redirect('destination')
        return redirect('account:login')

    return render(request, 'account/activationFailed.html', {'user':user})
