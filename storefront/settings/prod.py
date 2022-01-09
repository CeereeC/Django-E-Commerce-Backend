from storefront.settings.dev import SECRET_KEY
from .common import *
import os
import dj_database_url

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['backend-e-comm.herokuapp.com']

DATABASES = {
    'default': dj_database_url.config()
}