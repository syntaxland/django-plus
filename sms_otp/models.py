from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.utils import timezone

# # Create your models here.

# # Install as: pip install django-phonenumber-field[phonenumber]
# from phonenumber_field.modelfields import PhoneNumberField
# class SmsOtp(models.Model):

#     phone_otp = models.PositiveIntegerField()
#     phone = PhoneNumberField(null=False, blank=False, unique=True)

#     def __str__(self):
#         return str(self.phone_otp)



class SmsOtp(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    # myuser = models.CharField(max_length=50, null=True, default=None)
    # email = models.EmailField()
    phone = models.CharField(max_length=20)
    code = models.CharField(max_length=6)

    # GENDER_CHOICES = (
    # ('M', 'Male'),
    # ('F', 'Female'),
    # (None, 'Prefer not to say')
    # ) 
    # gender = models.CharField(max_length=1, 
    #                           choices=GENDER_CHOICES, 
    #                           null=True, blank=True, default=None)

    # age = models.IntegerField(validators=[MaxValueValidator(200)], default=None)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # created_at = models.DateTimeField(default=timezone.now)


    class Meta:
    #     db_table = 'sms otp db'
        ordering = ['-created_at']
        verbose_name = 'SMS OTP'

    def __str__(self):
        return 'OTP: '+ str(self.code) +' | '+ (self.phone)

    # def __str__(self):
    #     return 'OTP: %s - %s' % self.phone, str(self.code)
    
