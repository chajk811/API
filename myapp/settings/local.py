from .base import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'NAME': 'test2',
        'USER': 'root',
        'PASSWORD': '',
        'POST': '3306',
    }
}