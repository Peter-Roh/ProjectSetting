"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = ["localhost", ".elasticbeanstalk.com"]

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

PROJECT_APPS = [
    "core.apps.CoreConfig",
    "apis.apps.ApisConfig",
    "tests.apps.TestsConfig",
]

THIRD_PARTY_APPS = [
    'corsheaders',
    'rest_framework',
    'storages',
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates"), # react build한 파일
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "templates/static/"),
]

# rest_framework permission settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}

# cors 관련 설정
CORS_ALLOW_ALL_ORIGINS = False

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://localhost:8000',
]

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000',
    'http://localhost:8000',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'content-type',
    'x-csrftoken',
]

CORS_ALLOW_CREDENTIALS = True

# Database and DEBUG
# SECURITY WARNING: don't run with debug turned on in production!

STATE = os.environ.get("STATE")

if STATE == "local":
    DEBUG = True

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

elif STATE == "dev":
    DEBUG = False

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': os.environ.get("RDS_HOST"), # endpoint
            'NAME': os.environ.get("RDS_NAME"), # amazon RDS DB identifier
            'USER': os.environ.get("RDS_USER"),
            'PASSWORD': os.environ.get("RDS_PASSOWRD"),
            'PORT': '5432',
        }
    }

    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = 'Project-Setting-dev-S3' # change name
    AWS_AUTO_CREATE_BUCKET = True
    AWS_BUCKET_ACL = 'public-read'

    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
#    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"

# elif STATE == "production":
#     DEBUG = False

