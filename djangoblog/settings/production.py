from .base import *
import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
   'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
