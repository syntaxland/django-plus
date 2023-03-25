from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from .models import PhoneNumber

class PhoneBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            phone_obj = PhoneNumber.objects.get(phone_number=username, is_verified=True)
        except PhoneNumber.DoesNotExist:
            return None

        user = phone_obj.user
        return user if user.is_active else None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
