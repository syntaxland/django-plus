from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        # fields = '__all__'
        # fields = ['id', 'username', 'email', 'first_name', 'last_name', 'phone', 'password', 'age']
        fields = ['id', 'username', 'email', 'phone']


