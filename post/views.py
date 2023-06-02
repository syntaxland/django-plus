from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index(request):
    return HttpResponse("Welcome!") 

def getData(request):
    data = {'username': 'jondebosco',
            'first_name': 'jon',
            'last_name': 'bosco',
            'email': 'jb@gmail.com',
            'password': '',
            'phone': 1234567890,
            'age': 34
            }
    return JsonResponse(data, safe=False)







from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def getRestApi(request):
    data = {'username': 'jondebosco',
            'first_name': 'jon',
            'last_name': 'bosco',
            'email': 'jb@gmail.com',
            'password': '',
            'phone': 1234567890,
            'age': 34,
            'is_active': True,
            'is_admin': False
            }
    return Response(data)



# from rest_framework import viewsets
# from .models import UserPost
# from .serializers import UserPostSerializer

# class UserPostViewSet(viewsets.ModelViewSet):
#     queryset = UserPost.objects.all()
#     serializer_class = UserPostSerializer

