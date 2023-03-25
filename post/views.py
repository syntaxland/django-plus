# from django.shortcuts import render
# from django.http import HttpResponse

# # Create your views here.
# def index(request):
#     return HttpResponse("Welcome!")

# def home(request):
#     return HttpResponse("Welcome!")


from rest_framework import viewsets
from .models import UserPost
from .serializers import UserPostSerializer

class UserPostViewSet(viewsets.ModelViewSet):
    queryset = UserPost.objects.all()
    serializer_class = UserPostSerializer

