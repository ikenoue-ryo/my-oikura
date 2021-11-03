from .base import *
import os
from pathlib import Path

ALLOWED_HOSTS = ['*']

BASE_DIR = Path(__file__).resolve().parent

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'django_docker',
#         'USER': 'django',
#         'PASSWORD': 'password',
#         'HOST': 'db',
#         'PORT': '3306',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.environ.get('DATABASE_DB', os.path.join(BASE_DIR, 'db.sqlite3')),
        'USER': os.environ.get('DATABASE_USER', 'django'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'password'),
        'HOST': os.environ.get('DATABASE_HOST', 'db'),
        'PORT': os.environ.get('DATABASE_PORT', '3306'),
    }
}
