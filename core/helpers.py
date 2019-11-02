import uuid

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text

from .models import User
from .tokens import account_activation_token
from utils.sendgridmail import send_email


def generate_customer_id():
    return str(uuid.uuid4()).split('-')[4]


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
    send_email(recipient=user.email, subject=mail_subject, html_content=message, from_email='BrandShack@brandshack.co')


def _email_design_request(customer=None, purpose=None, brief=None, url=None):
    "an email message for design requests from clients"
    mail_subject = 'Client design request'
    message = render_to_string('core/email/design_request.html', {
        'customer': customer,
        'platform': purpose,
        'brief': brief,
        'URL': url,
    })
    send_email(recipient='design@brandshack.co', subject=mail_subject, html_content=message, from_email='design@brandshack.co')


def _email_contact_us(sender=None, email=None, subject=None, message=None):
    "an email message for conatact form"
    mail_subject = 'Hey, new contact information'
    message = render_to_string('core/email/contact_us.html', {
        'sender': sender,
        'email': email,
        'subject': subject,
        'message': message,
    })
    send_email(recipient='helpdesk@brandshack.co', subject=mail_subject, html_content=message, from_email='helpdesk@brandshack.co')
