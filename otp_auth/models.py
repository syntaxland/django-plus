from django.db import models
from django.contrib.auth.models import User

class PhoneNumber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    otp_code = models.CharField(max_length=6)
    is_verified = models.BooleanField(default=False)
