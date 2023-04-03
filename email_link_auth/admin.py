from django.contrib import admin
from .models import EmailVerification

class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'email', 'token', 'verified', 'created_at')

    readonly_fields = ('token_link',)

    def token_link(self, obj):
        return f"<a href='#'>{obj.token}</a>"


admin.site.register(EmailVerification, EmailVerificationAdmin)
