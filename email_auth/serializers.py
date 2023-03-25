# Step 4: Allow the user to login only if their email is verified.
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)
            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise ValidationError(msg, code='authorization')
            if not user.is_email_verified:
                msg = 'Email is not verified.'
                raise ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "email" and "password".'
            raise ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
