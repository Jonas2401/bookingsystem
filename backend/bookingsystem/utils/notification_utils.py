from django.core.mail import send_mail
from django.template.loader import render_to_string

def send_notification(email, subject, template, context):
    message = render_to_string(template, context)
    send_mail(subject, message, 'from@example.com', [email])
