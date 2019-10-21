import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from decouple import config

def send_email(recipient=None, subject=None, html_content=None, from_email=None):
    message = Mail(
        from_email=from_email,
        to_emails=recipient,
        subject=subject,
        html_content=html_content,)
    try:
        sg = SendGridAPIClient(config('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)