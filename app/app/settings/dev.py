import dj_database_url

from .base import *  # NOQA

APP_ENV = "dev"
APP_VERSION = "dev"
SECRET_KEY = os.environ["SECRET_KEY"]

DEBUG = True
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS += []

DATABASES = {
    "default": dj_database_url.config(default=os.environ["DJANGO_DATABASE_URL"])
}
