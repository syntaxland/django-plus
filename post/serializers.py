from rest_framework import serializers
from .models import UserPost

class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPost
        # fields = '__all__'
        fields = ['id', 'name', 'image', 'video', 'description']
        
