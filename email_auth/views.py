# from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse

from django.shortcuts import redirect, render
# from django.urls import reverse
from django.contrib.auth import get_user_model
from django.http import Http404

def send_email_verification_mail(user):
    subject = 'Verify Your Email Address'
    message = f'Hi {user.email}, Please click the link below to verify your email address'
    link = reverse('verify-email', args=[str(user.email_verification_token)])
    verification_link = settings.FRONTEND_URL + link
    send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False, html_message=verification_link)


User = get_user_model()

def verify_email(request, token):
    try:
        user = User.objects.get(email_verification_token=token)
        user.is_email_verified = True
        user.save()
        return redirect(reverse('login'))
    except User.DoesNotExist:
        raise Http404('Invalid verification token')
