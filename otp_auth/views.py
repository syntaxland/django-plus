from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from twilio.rest import Client
from django.conf import settings
from .utils import generate_otp
from .models import PhoneNumber

class SendOtpView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        if not phone_number:
            return Response({'error': 'Phone number is required.'}, status=status.HTTP_400_BAD_REQUEST)

        user = request.user
        if not user.is_authenticated:
            return Response({'error': 'You must be logged in.'}, status=status.HTTP_401_UNAUTHORIZED)

        otp_code = generate_otp()
        message = f'Your verification code is: {otp_code}'

        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        try:
            message = client.messages.create(
                body=message,
                from_=settings.TWILIO_PHONE_NUMBER,
                to=phone_number
            )
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        phone_obj, created = PhoneNumber.objects.get_or_create(user=user, phone_number=phone_number)
        phone_obj.otp_code = otp_code
        phone_obj.save()

        return Response({'success': 'OTP code sent.'}, status=status.HTTP_200_OK)

# Verify the OTP code
class VerifyOtpView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        otp_code = request.data.get('otp_code')
        if not phone_number or not otp_code:
            return Response({'error': 'Phone number and OTP code are required.'}, status=status.HTTP_400_BAD_REQUEST)

        phone_obj = get_object_or_404(PhoneNumber, phone_number=phone_number, otp_code=otp_code)
        if phone_obj.is_verified:
            return Response({'error': 'Phone number is already verified.'}, status=status.HTTP_400_BAD_REQUEST)

        phone_obj.is_verified = True
        phone_obj.save()

        return Response({'success': 'Phone number verified.'}, status=status.HTTP_200_OK)


# Finally, you can use this backend to authenticate users in your views.
#  For example, if you have a view that requires authentication, 
# you can add the following code:

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class MyView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        ...
        # Your view code here
