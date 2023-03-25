from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.send_email, name='send_email'),
]
