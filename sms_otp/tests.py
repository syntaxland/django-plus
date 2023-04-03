from django.http import HttpResponse
from django.test import TestCase

# Create your tests here.

from django.shortcuts import redirect, render, get_object_or_404
# Create your views here.
import random
from .models import SmsOtp
from twilio.rest import Client
from django.conf import settings

from rest_framework import status
from rest_framework.response import Response

# def send_sms_otp(request):
#     account_sid = settings.TWILIO_ACCOUNT_SID 
#     auth_token = settings.TWILIO_AUTH_TOKEN 
#     client = Client(account_sid, auth_token)

#     if request.method == 'POST':
#         phone = request.POST.get('phone')
#         code = str(random.randint(100000, 999999))

#         try:
#             message = client.messages.create(
#                 body=f'OTP: {code}',
#                 from_=settings.TWILIO_PHONE_NUMBER,
#                 to=phone
#             )
#             print(message.sid)
#             print('SMS verification code sent to:', phone)
            
#             # Save the OTP to the database
#             SmsOtp.objects.create(phone=phone, code=code)
            
#             return redirect('verify_sms_otp', phone=phone)
#         except Exception as e:
#             print(e)
#             return redirect('some_other_target')

#     return render(request, 'sms_auth/verfiy_phone.html')

# def verify_sms_otp(request, phone):
#     if request.method == 'POST':
#         otp = request.POST.get('otp')

#         # Retrieve the SmsOtp instance with the corresponding phone value
#         sms_otp = get_object_or_404(SmsOtp, phone=phone)

#         if sms_otp.code == otp:
#             # OTP is correct
#             sms_otp.delete()
#             return redirect('some_other_target')
#         else:
#             # OTP is incorrect
#             return render(request, 'sms_auth/verify_sms_otp.html', {'error': 'Incorrect OTP'}, {'phone': phone})

#     return render(request, 'sms_auth/verify_sms_otp.html')


def verify_sms_otp(request, phone):
    if request.method == 'POST':
        otp = request.POST.get('otp')

        if SmsOtp.objects.filter(phone=phone, otp=otp).exists():
            # OTP verification successful, do something here
            return HttpResponse('OTP verification successful')
        else:
            # OTP verification failed, do something here
            return HttpResponse('Invalid OTP')

    context = {'phone': phone}
    return render(request, 'sms_auth/verify_sms_otp.html', context)




# if SmsOtp.objects.filter(phone=phone, code=otp).exists():
#     # OTP verification successful, do something here
#     SmsOtp.otp.delete()
#     print("Your phone number", phone, "is verifed with OTP: ", otp) 
#     print(HttpResponse('OTP verification successful'))
#     return redirect('welcome')
# else:
#     # OTP verification failed, do something here
#     print(HttpResponse('Invalid OTP'))
#     return redirect('verify_sms_otp')
#     # return render(request, 'sms_auth/verify_sms_otp.html', {'error': 'Incorrect OTP'}, {'phone': phone})
        