from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from django.contrib import messages

from rest_framework import generics, viewsets, status, permissions
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import CustomUser
from .serializers import CustomUserSerializer

# Returning data using JsonResponse
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

# Returning data using Response
@api_view(['GET'])
def getProile(request):
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


# Returning data using template rendering
def getApiUsers(request):
    custom_users = CustomUser.objects.all()
    context = {
        'custom_users':custom_users
    }
    return render(request, 'custom_users/users.html', context)


# Using function-based @api_view decorators for serialized data
@api_view(['GET'])
def getCustomeUsers(request):
    queryset = CustomUser.objects.all()
    serializer = CustomUserSerializer(queryset, many=True)
    return Response(serializer.data)



# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .models import MyModel
# from .serializers import MyModelSerializer

# # Retrieve all objects
# @api_view(['GET'])
# def mymodel_list(request):
#     mymodels = MyModel.objects.all()
#     serializer = MyModelSerializer(mymodels, many=True)
#     return Response(serializer.data)

# # Retrieve single object
# @api_view(['GET'])
# def mymodel_detail(request, pk):
#     try:
#         mymodel = MyModel.objects.get(pk=pk)
#     except MyModel.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     serializer = MyModelSerializer(mymodel)
#     return Response(serializer.data)

# # Create new object
# @api_view(['POST'])
# def mymodel_create(request):
#     serializer = MyModelSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # Update existing object
# @api_view(['PUT'])
# def mymodel_update(request, pk):
#     try:
#         mymodel = MyModel.objects.get(pk=pk)
#     except MyModel.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     serializer = MyModelSerializer(mymodel, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # Delete existing object
# @api_view(['DELETE'])
# def mymodel_delete(request, pk):
#     try:
#         mymodel = MyModel.objects.get(pk=pk)
#     except MyModel.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     mymodel.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)



# Using class-based APIView
class ListSerializedApi(APIView):
    def get(self, request, format=None):
        queryset = CustomUser.objects.all()
        serializer = CustomUserSerializer(queryset, many=True)
        return Response(serializer.data)

# class MyModelList(APIView):
#     def get(self, request, format=None):
#         queryset = MyModel.objects.all()
#         serializer = MyModelSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = MyModelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class MyModelDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return MyModel.objects.get(pk=pk)
#         except MyModel.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         my_model = self.get_object(pk)
#         serializer = MyModelSerializer(my_model)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         my_model = self.get_object(pk)
#         serializer = MyModelSerializer(my_model, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         my_model = self.get_object(pk)
#         my_model.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# OR

# class SnippetList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class SnippetDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# Using class-based generics
class UserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


# class SnippetList(generics.ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly,
#                       IsOwnerOrReadOnly]


# class SnippetHighlight(generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     renderer_classes = [renderers.StaticHTMLRenderer]

#     def get(self, request, *args, **kwargs):
#         snippet = self.get_object()
#         return Response(snippet.highlighted)


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer



# Using viewsets.ModelViewSet which automatically provides 
# `list`, `create`, `retrieve`, `update` and `destroy` actions.
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = permissions.IsAuthenticatedOrReadOnly
    

# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer











# CustomUser = get_user_model()

# def signup(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         username = request.POST.get('username')
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         CustomUser.objects.create_user(email=email, password=password, username=username, first_name=first_name, last_name=last_name)
#         return redirect('login')
#     return render(request, 'signup.html')


# def user_login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.error(request, 'Invalid email or password.')
#     return render(request, 'login.html')


# def profile(request):
#     user = request.user
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         username = request.POST.get('username')
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         user.email = email
#         user.username = username
#         user.first_name = first_name
#         user.last_name = last_name
#         user.save()
#         messages.success(request, 'Your profile has been updated.')
#     return render(request, 'profile.html', {'user': user})


# def delete_user(request):
#     user = request.user
#     if request.method == 'POST':
#         user.delete()
#         messages.success(request, 'Your account has been deleted.')
#         return redirect('home')
#     return render(request, 'delete_user.html')
