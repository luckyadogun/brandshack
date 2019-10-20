from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text

from .models import User
from .tokens import account_activation_token
from utils.sendgridmail import send_email

def _email_activate_acct(request, user_pk=None):
    "an email message sent for account activation."
    user = User.objects.get(id=user_pk)
    URI = request.build_absolute_uri('/activate/')
    mail_subject = 'Activate your account'
    message = render_to_string('core/email/activate_account.html', {
        'user': "{} {}".format(user.first_name, user.last_name),
        'domain': URI,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    })
    send_email(recipient=user.email, subject=mail_subject, html_content=message)