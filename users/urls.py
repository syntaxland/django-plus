from django.urls import path, include
from .views import *

urlpatterns = [
    path('', getProile, name='getProile'),
    path('api_users/', getApiUsers, name='api_users'),

    # Using function-based @api_view decorators
    # path('custome-users/', getCustomeUsers, name='custome-users'), 
    # path('mymodel/', mymodel_list, name='mymodel_list'),
    # path('mymodel/<int:pk>/', mymodel_detail, name='mymodel_detail'),
    # path('mymodel/create/', mymodel_create, name='mymodel_create'),
    # path('mymodel/update/<int:pk>/', mymodel_update, name='mymodel_update'),
    # path('mymodel/delete/<int:pk>/', mymodel_delete, name='mymodel_delete'),

    # Using class-based apiview
    # path('serialized_api/', ListSerializedApi.as_view(), name='serialized_api'), 

    # Using class-based generics
    # path('user-list/', UserList.as_view(), name='user-list'),
    # path('user-list/<int:pk>/', UserDetail.as_view(), name='user-list'),
]


# Using viewsets.ModelViewSet - DefaultRouter
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *

router = DefaultRouter()
router.register(r'users', UserViewSet, basename="users")
# router.register(r'products', UserViewSet, basename="product")

urlpatterns = [
    path('', include(router.urls)), 
]

# This will automatically generate the following URL patterns:

# GET /users/
# GET /users/{pk}/
# POST /users/
# PUT /users/{pk}/
# PATCH /users/{pk}/
# DELETE /users/{pk}/
