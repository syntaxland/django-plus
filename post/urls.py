from django.urls import path
from .views import *

urlpatterns = [
    path('', getData, name='getData'),
    path('restapi/', getRestApi, name='getRestApi'),
]

# from django.urls import path, include
# from rest_framework import routers
# from .views import UserPostViewSet

# router = routers.DefaultRouter()
# router.register(r'post', UserPostViewSet)
# # router.register(r'account/login', UserPostViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

