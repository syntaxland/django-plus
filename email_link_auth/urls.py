from django.urls import path
from . import views

urlpatterns = [
    # path('', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    # path('verify-email-link/', views.verify_email, name='verify_email'),
    path('verify-email/<uuid:token>/', views.verify_email, name='verify_email'),
    path('resend-verification/', views.resend_verification, name='resend_verification'),
    
    path('login/', views.login, name='login'), 

    path('welcome/', views.welcome, name='welcome'),
    path('welcome/<int:user_id>/', views.welcome, name='welcome'), 
    # path('delete-user/', views.delete_user, name='delete_user'), 
    # path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
]


