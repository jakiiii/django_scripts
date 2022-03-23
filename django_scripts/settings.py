"""
Django settings for django_scripts project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-pnp_sc!@^pi-)i*+82+o+mac!06db5v_$i0p2jn-i0p4%syql&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
]

THIRD_PARTY_APPS = [
    'widget_tweaks',
    'django_celery_beat',
    'django_celery_results',
    'rest_framework',
    'rest_framework_jwt',
    'django_filters',
    'leaflet',
]

LOCAL_APPS = [
    'apps.home',
    'apps.select_two',
    'apps.celery_task',
    'apps.excelhandling',
    'apps.multiple_image',
    'apps.dfilters',
    'apps.apifilter',
    'apps.generatedocuments',
    'apps.auth_opt',
]

INSTALLED_APPS += THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_scripts.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'django_scripts.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql',
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'djscripts',
        'USER': 'jaki',
        'PASSWORD': '101119',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Message framework
MESSAGE_TAGS = {
    messages.INFO: 'alert alert-info',
    messages.SUCCESS: 'alert alert-success',
    messages.WARNING: 'alert alert-warning',
    messages.ERROR: 'alert alert-danger',
    messages.DEBUG: 'alert alert-info',
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    '/var/www/static/',
)

STATIC_ROOT = os.path.join(
    os.path.dirname(BASE_DIR),
    'django_scripts/static_cdn/', 'static_root/'
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(
    os.path.dirname(BASE_DIR),
    "django_scripts/static_cdn", "media_root"
)

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# G-mail send email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'pakijadjangoproject@gmail.com'
EMAIL_HOST_PASSWORD = 'a$$4u1tpakija'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'jTro | Celery Task Management (pakijadjangoproject@gmail.com)'
# BASE_URL = '127.0.0.1:8000'
#
# MANAGERS = [
#     ('jTro', 'pakijadjangoproject@gmail.com'),
# ]
#
# ADMINS = MANAGERS


# django celery beat
CELERY_BEAT_SCHEDULE = {
    "scheduled_task": {
        "task": "celery_task.tasks.add",
        "schedule": 5.0,
        "args": (10, 10),
    },
    "database": {
        "task": "celery_task.tasks.backup",
        "schedule": 5.0,
    }
}


# Celery Results
CELERY_RESULT_BACKEND = 'django-db'


# Celery Cash
CELERY_CACHE_BACKEND = 'default'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cachedb',
    }
}


# leaflet
LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (23.806220589190477, 90.39348745815941),
    'DEFAULT_ZOOM': 5,
    'MAX_ZOOM': 20,
    'MIN_ZOOM': 3,
    'SCALE': 'both',
    'ATTRIBUTION_PREFIX': 'Inspired by Life in GIS'
}


# install GDAL
# pip install --global-option=build_ext --global-option="-I/usr/include/gdal" GDAL==`gdal-config --version`
if os.name == 'nt':
    VENV_BASE = os.environ('VIRTUAL_ENV')
    os.environ['path'] = os.path.join(
        VENV_BASE,
        '/home/jaki/Dev/django_scripts/venv/lib/python3.8/site-packages/osgeo' + ';' + os.environ['PATH']
    )
    os.environ['PROJ_LIB'] = os.path.join(
        VENV_BASE,
        '/home/jaki/Dev/django_scripts/venv/lib/python3.8/site-packages/osgeo/data/proj' + ';' + os.environ['PATH']
    )

