# from django.urls import path
# from .views import SendEmailVerificationView, VerifyEmailView, UserCreateView

# urlpatterns = [
#     path('signup/', UserCreateView.as_view(), name='signup'),
#     path('verify-email/', SendEmailVerificationView.as_view(), name='send-email-verification'),
#     path('verify-email/<str:code>/', VerifyEmailView.as_view(), name='verify-email'),
# ]


from django.urls import path
from . import views

urlpatterns = [
    # path('', views.login, name='login'),
    path('send-email-otp/', views.send_email_otp, name='send_email_otp'),
    path('verify-email-otp/', views.verify_email_otp, name='verify_email_otp'),
    path('verify-email-otp/<str:email>/', views.verify_email_otp, name='verify_email_otp'),
    path('resend-email-otp/', views.resend_otp, name='resend_email_otp'),
    
    path('welcome/', views.welcome, name='welcome'),
    path('welcome/<int:user_id>/', views.welcome, name='welcome'), 
    path('delete-user/', views.delete_user, name='delete_user'), 
    path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
]
