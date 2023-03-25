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

    path('api/', include('post.url')),

    path('', include('captcha_app.urls')),

    path('authentication/', include('email_auth_app.urls')),

    path('mailer/', include('send_mail.urls')),

 
    path('', TemplateView.as_view(template_name="account/login.html")),

    # path('', TemplateView.as_view(template_name="account/verify_sms_otp.html")),
    # path('', TemplateView.as_view(template_name="account/verify_email_otp.html")),

    path('accounts/', include('allauth.urls')), 
    path('logout', LogoutView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
