from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.conf import settings

User = get_user_model()


def send_warning_email(user, title, description):
    subject = f"Warning: {user.get_full_name} You have been reported!"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]
    context = {
        "user": user,
        "title": title,
        "description": description,
        "site_name": settings.SITE_NAME,
    }
    html_email = render_to_string("emails/warning_email.html", context)
    text_email = strip_tags(html_email)

    email = EmailMultiAlternatives(subject, text_email, from_email, recipient_list)
    email.attach_alternative(html_email, "text/html")
    email.send()


def send_deactivation_email(user, title, description):
    subject = f"Account Deactivation and Eviction Notice! : {user.get_full_name}"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]
    context = {
        "user": user,
        "title": title,
        "description": description,
        "site_name": settings.SITE_NAME,
    }
    html_email = render_to_string("emails/deactivation_email.html", context)
    text_email = strip_tags(html_email)

    email = EmailMultiAlternatives(subject, text_email, from_email, recipient_list)
    email.attach_alternative(html_email, "text/html")
    email.send()
