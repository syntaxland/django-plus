# from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# Adding .env 
import os
from dotenv import load_dotenv
load_dotenv()

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-o)mv)0z3i%)jd^&l-n8@kor@gd^42mtr*#t*i0&3i=gee786m1'
SECRET_KEY = os.getenv('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', 'localhost:8000', '127.0.0.1', '127.0.0.1:8000']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # required for django allauth
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.github',

    'captcha',

    'djoser',
    
    # restapi
    'rest_framework',
    'corsheaders',

    # started apps
    'captcha_app.apps.CaptchaAppConfig',
    'drf',
    'email_auth.apps.EmailAuthConfig',
    'email_auth_app.apps.EmailAuthAppConfig',
    'email_link_auth.apps.EmailLinkAuthConfig',
    'email_otp.apps.EmailOtpConfig',   
    'otp_auth.apps.OtpAuthConfig',
    'plotly_viz', 
    'chartjs',
    'post.apps.PostConfig',
    'send_mail.apps.SendMailConfig',
    'sms_otp.apps.SmsOtpConfig',
    'two_factor',
    'gpt',
    'weather_api',
    'news_api',
    'users',
    'visualization.apps.VisualizationConfig',
    # 'drf_react_jwt',

    # MongoDB conn 
    'djongo',

    # pip install django-crispy-forms crispy-bootstrap4
    'crispy_forms',  # You will need to pip install crispy-bootstrap4 and add crispy_bootstrap4 to your list of INSTALLED_APPS.
    # 'crispy_bootstrap4', 

    'phonenumber_field',

    
]

# pip install django-crispy-forms crispy-bootstrap4
# 'crispy_forms',  # You will need to pip install crispy-bootstrap4
# and add crispy_bootstrap4 to your list of INSTALLED_APPS.
     
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# LOGIN_URL ='/login/'
# AUTH_USER_MODEL = 'users.CustomUser'
# AUTH_USER_MODEL = 'drf_react_jwt.UserAccount'  

# CORS_ORIGIN_WHITELIST = [
#      'http://localhost:3000',
# ]

# CORS_ALLOWED_ORIGINS = [
#     "https://mcdofglobal.com",
#     "https://store.mcdofglobal.com",
#     "http://localhost:8000",
#     "http://127.0.0.1:3000",
#     "http://localhost:3000",
#     "http://127.0.0.1:8000",
# ]

CORS_ALLOW_ALL_ORIGINS = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # added third-part corsheaders middleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 'django.middleware.locale.LocaleMiddleware', # Added
]

ROOT_URLCONF = 'tiktok.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR / 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # 'django.template.context_processors.i18n',  # trans temp added
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # `allauth` needs this from django
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'tiktok.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': os.getenv('DB_NAME'),
#         'USER': os.getenv('DB_USER'),
#         'PASSWORD': os.getenv('DB_PASSWORD'),
#         'HOST': os.getenv('DB_HOST'),
#         'PORT': int(os.getenv('DB_PORT')),
#     }
# }

DATABASES = {
     'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': int(os.getenv('DB_PORT')),
     }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': os.getenv('MONGODB_NAME'),
#         'ENFORCE_SCHEMA': False,
#         'CLIENT': {
#             'host': os.getenv('MONGODB_HOST'),
#             'port': int(os.getenv('MONGODB_PORT')),
#             'username': os.getenv('MONGODB_USER'),
#             'password': os.getenv('MONGODB_PASS'),
#             'authSource': 'admin',
#             # 'authMechanism': 'SCRAM-SHA-1',
#         },
#     },
# }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'


# MEDIA_ROOT = 'static/images'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

    # 'django.contrib.auth.backends.ModelBackend',
    # 'tiktok.otp_auth.backends.PhoneBackend',

    # for drf_react_jwt
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',

]

SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True,
    }
}


LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'


TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

MY_PHONE_NUMBER  = os.getenv('MY_PHONE_NUMBER')


RECAPTCHA_PUBLIC_KEY = os.getenv('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = os.getenv('RECAPTCHA_PRIVATE_KEY')
RECAPTCHA_REQUIRED_SCORE = os.getenv('RECAPTCHA_REQUIRED_SCORE')


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp-relay.sendinblue.com'
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_SENDER_NAME = os.getenv('EMAIL_SENDER_NAME')

SENDINBLUE_API_KEY = os.getenv('SENDINBLUE_API_KEY')

IPAPI_KEY = os.getenv('IPAPI_KEY')
OPENWEATHERMAP_KEY = os.getenv('OPENWEATHERMAP_KEY')


# for drf_react_jwt
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    # 'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    # 'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_TOKEN_CLASSES': (
        'rest_framework_simplejwt.tokens.AccessToken',
    )
}

DJOSER = {
    'LOGIN_FIELD': 'email',
    'USER_CREATE_PASSWORD_RETYPE': True,
    'USERNAME_CHANGED_EMAIL_CONFIRMATION': True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    'SEND_CONFIRMATION_EMAIL': True,
    'SET_USERNAME_RETYPE': True,
    'SET_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': 'email/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SOCIAL_AUTH_TOKEN_STRATEGY': 'djoser.social.token.jwt.TokenStrategy',
    'SOCIAL_AUTH_ALLOWED_REDIRECT_URIS': ['http://localhost:8000/google', 'http://localhost:8000/facebook'],
    'SERIALIZERS': {
        # 'user_create': 'drf_react_jwt.serializers.CustomUserCreateSerializer',
        # 'user': 'drf_react_jwt.serializers.CustomUserCreateSerializer',
        # 'current_user': 'drf_react_jwt.serializers.CustomUserCreateSerializer',
        # 'user_delete': 'djoser.serializers.UserDeleteSerializer',
    }
}
