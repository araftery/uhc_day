import os

from path import path

############################################################
##### SETUP ################################################
############################################################

# i.e., where root urlconf is
PROJECT_ROOT = path(__file__).abspath().dirname().dirname()
os.sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))


############################################################
##### DATABASE #############################################
############################################################

ALLOWED_HOSTS = ['*']

############################################################
##### APPS #################################################
############################################################

# Application definition
DEFAULT_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'widget_tweaks',
)

MY_APPS = (
    'poster',
)

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + MY_APPS

############################################################
##### MIDDLEWARE ###########################################
############################################################

DEFAULT_MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

THIRD_PARTY_MIDDLEWARE = (
)

MIDDLEWARE_CLASSES = DEFAULT_MIDDLEWARE + THIRD_PARTY_MIDDLEWARE

############################################################
##### INTERNATIONALIZATION #################################
############################################################

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = False
USE_TZ = True

############################################################
##### TEMPLATES ############################################
############################################################

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates_common').replace('\\', '/'),
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as DEFAULT_TCP

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
) + DEFAULT_TCP


############################################################
##### AUTHENTICATION #######################################
############################################################

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
URL_PATH = ''

############################################################
##### AWS ##################################################
############################################################

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

############################################################
##### EMAIL ################################################
############################################################

EMAIL_USE_TLS = True
FROM_EMAIL = os.environ.get('FROM_EMAIL')
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT'))
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

ADMINS = (
    ('Andrew Raftery', 'andrewraftery@gmail.com'),
)

############################################################
##### STATIC FILES #########################################
############################################################

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static_common').replace('\\', '/'),
)


############################################################
##### OTHER ################################################
############################################################

ROOT_URLCONF = 'uhc_day.urls'
WSGI_APPLICATION = 'uhc_day.wsgi.application'
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
SECRET_KEY = '#1(e2hpbo3xvmz%al6(t3&#k)abu2gsc!$!&map&591ljgx5di'
DATABASES = {}
TIME_ZONE = 'America/New_York'


############################################################
##### PROJECT-SPECIFIC #####################################
############################################################


