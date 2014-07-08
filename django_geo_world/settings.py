"""
Django settings for django_geo_world project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from distutils.util import strtobool
import os
import dotenv
from projectutils import ProjectUtils

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))
PROJECT_NAME = 'GEO_WORLD'

projectutils = ProjectUtils(PROJECT_NAME)
projectutils.open_secrets('.secrets/secrets.json', dir_local=PROJECT_PATH)


dotenv.load_dotenv(os.path.join(PROJECT_PATH, "django_geo_world/.env"))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = projectutils.get_project_env('SECRET_KEY', True)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = strtobool(projectutils.get_env_variable('DJANGO_DEBUG'))
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'south',
    'django_geo_world'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'django_geo_world.urls'

WSGI_APPLICATION = 'django_geo_world.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': projectutils.get_project_env('DB_POSTGRE_NAME', True),
        'USER': projectutils.get_project_env('DB_POSTGRE_USER', True),
        'PASSWORD': projectutils.get_project_env('DB_POSTGRE_PASSWORD', True),
        'HOST': projectutils.get_project_env('DB_POSTGRE_HOST', True),
        'PORT': projectutils.get_project_env('DB_POSTGRE_PORT', True),
        'OPTIONS': {
            'autocommit': True,
            },
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
