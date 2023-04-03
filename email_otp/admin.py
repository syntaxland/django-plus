from django.contrib import admin
from .models import EmailOTP
class EmailOTPAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'email', 'code', 'is_verified', 'created_at')

admin.site.register(EmailOTP, EmailOTPAdmin)
