from django.contrib import admin
from .models import SmsOtp

class SmsOtpAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'code', 'is_verified', 'created_at')


# Register your models here.
admin.site.register(SmsOtp, SmsOtpAdmin)
