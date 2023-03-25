from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from .models import EmailVerification
from .serializers import EmailVerificationSerializer
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user
    

class EmailVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailVerification
        fields = ['id', 'code']


class VerifyEmailView(generics.GenericAPIView):
  serializer_class = EmailVerificationSerializer

  def post(self, request):
      code = request.data.get('code')
      if not code:
          return Response({'error': 'The code field must be set'}, status=status.HTTP_400_BAD_REQUEST)

      email_verification = get_object_or_404(EmailVerification, code=code)
      email_verification.user.is_email_verified = True
      email_verification.user.save()
      email_verification.delete()

      return Response({'success': 'Email verified'}, status=status.HTTP_200_OK)
