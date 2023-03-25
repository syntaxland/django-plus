from django.urls import path
from .views import SendEmailVerificationView, VerifyEmailView, UserCreateView

urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='signup'),
    path('verify-email/', SendEmailVerificationView.as_view(), name='send-email-verification'),
    path('verify-email/<str:code>/', VerifyEmailView.as_view(), name='verify-email'),
]
