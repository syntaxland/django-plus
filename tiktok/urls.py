# from django.contrib import admin
# from django.urls import path, include



# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('post.url')),
#     path('accounts/', include('allauth.urls')),
# ]

# Trying out
from django.contrib import admin
from django.urls import path, include 
from django.views.generic import TemplateView 
from django.contrib.auth.views import LogoutView

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [ 
    path('admin/', admin.site.urls),
    # Started apps
    path('api/', include('post.url')),
    path('', include('captcha_app.urls')),
    path('authentication/', include('email_auth_app.urls')),
    path('mailer/', include('send_mail.urls')),
    path('sendmail/', include('email_auth.urls')),
    path('verify-otp/', include('sms_otp.urls')),
    path('verify-email-otp/', include('email_otp.urls')),
    path('verify-email/', include('email_link_auth.urls')),
    # Others 
    path('', TemplateView.as_view(template_name="account/login.html")), 
    path('accounts/', include('allauth.urls')), 
    path('logout', LogoutView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
