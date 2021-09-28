from .base import *
import os
from datetime import timedelta

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-thbtz_f370_2)+v0*aacf8hrn3rx&(43)o%x(unxyscbt!!n2-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_docker',
        'USER': 'django',
        'PASSWORD': 'password',
        'HOST': 'db',
        'PORT': '3306',
    }
}
