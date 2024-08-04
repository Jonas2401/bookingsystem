import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')  # ;)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DATABASE_NAME'),  # ;)
        'USER': os.getenv('DATABASE_USER'),  # ;)
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),  # ;)
        'HOST': os.getenv('DATABASE_HOST'),  # ;)
        'PORT': '5432',
    }
}

INSTALLED_APPS = [
    ...
    'rest_framework',
    'bookingsystem',
]

ANYMAIL = {
    "SENDGRID_API_KEY": os.getenv('SENDGRID_API_KEY'),  # ;)
}
EMAIL_BACKEND = "anymail.backends.sendgrid.EmailBackend"

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
