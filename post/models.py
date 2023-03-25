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
        account_sid = settings.TWILIO_ACCOUNT_SID # 'AC304ec90f56320d8b1338d59d9f58d18f'
        auth_token = settings.TWILIO_AUTH_TOKEN # 'f9a7c3c1d429b74fcbd5a4627ab8c529'
        client = Client(account_sid, auth_token)
        
        if self.result < 70:           
            message = client.messages.create(
                    body=f'Result not looking good - {self.result}',
                    from_=settings.TWILIO_PHONE_NUMBER,
                    to='+2349066167293'
                )
            print(message.sid)
        else:
            message = client.messages.create(
                    body=f'Good to go at: {self.result}',
                    from_=settings.TWILIO_PHONE_NUMBER,
                    to=settings.MY_PHONE_NUMBER
                )
            print(message.sid)

        return super().save(*args, **kwargs)
