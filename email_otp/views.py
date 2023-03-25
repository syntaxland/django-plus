from django.shortcuts import render

# Create your views here.
import random
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from .models import EmailVerification, User
from .serializers import EmailVerificationSerializer

class SendEmailVerificationView(generics.CreateAPIView):
    serializer_class = EmailVerificationSerializer

def post(self, request):
    email = request.data.get('email')
    if not email:
        return Response({'error': 'The Email field must be set'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.filter(email=email).first()
    if not user:
        return Response({'error': 'User with this email does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    code = str(random.randint(100000, 999999))
    email_verification = EmailVerification.objects.create(user=user, code=code)
    send_mail(
        'Verify Your Email',
        f'Your OTP verification code is: {code}',
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
    return Response({'success': 'Email verification code sent'}, status=status.HTTP_200_OK)
