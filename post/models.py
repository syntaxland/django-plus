# Create your models here.
from django.db import models

from twilio.rest import Client
from django.conf import settings


class UserPost(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    description = models.TextField()
    
    def __str__(self):
        return self.name

# pip install twilio pyotp 

class Score(models.Model):
    result = models.PositiveIntegerField()
       
    def __str__(self):
        return str(self.result)
    
    def save(self, *args, **kwargs):
        account_sid = settings.TWILIO_ACCOUNT_SID 
        auth_token = settings.TWILIO_AUTH_TOKEN 
        client = Client(account_sid, auth_token)
        
        if 100000 <= self.result <= 999999:           
            message = client.messages.create(
                    body=f'Correct OTP: {self.result}',
                    from_=settings.TWILIO_PHONE_NUMBER,
                    to='+2349066167293'
                )
            print(message.sid)
            print("Correct OTP sent successfully!")
        else:
            message = client.messages.create(
                    body=f'Wrong OTP: {self.result}',
                    from_=settings.TWILIO_PHONE_NUMBER,
                    to=settings.MY_PHONE_NUMBER
                )
            print(message.sid)
            print("Wrong OTP sent successfully!")

        return super().save(*args, **kwargs)
