from django.utils.html import urlize

from markdown import Markdown
from postmarkup import render_bbcode
import os

BASE_DIR = lambda *x: os.path.abspath(os.path.join(
                     os.path.dirname(__file__), *x))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Pavel Zhukov','gelios@gmail.com'),
    ('Vladimir Korsun', 'korsun.vladimir@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR('database.db'),
    }
}

SITE_ID = 1

TIME_ZONE = 'Europe/Moscow'

LANGUAGE_CODE = 'ru-RU'
USE_I18N = True
USE_L10N = True

MEDIA_ROOT = BASE_DIR('media')
MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/media/static/admin/'

STATIC_ROOT = BASE_DIR('media/static')
STATIC_URL = '/media/static/'
STATICFILES_DIRS = (BASE_DIR('static'),)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
#SECRET_KEY = 'Insert your SECRET_KEY from your local.py'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pybb.middleware.PybbMiddleware',
)

ROOT_URLCONF = 'aor.urls'

TEMPLATE_DIRS = (
    BASE_DIR('templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'pybb.context_processors.processor',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.comments',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'south',
    'registration',
    'sorl.thumbnail',
    'tagging',
    'dnews',
    'dblog',
    'pybb',
)


AUTH_PROFILE_MODULE = 'pybb.Profile'
FILE_UPLOAD_PERMISSIONS = 0644
LOGIN_REDIRECT_URL = '/'
PYBB_TEMPLATE = 'forum.html'
#PYBB_SMILES_PREFIX = STATIC_URL + 'pybb/emoticons/'
PYBB_MARKUP_ENGINES = {
    'bbcode': lambda str: render_bbcode(str,
                    encoding="utf-8",
                    exclude_tags=None,
                    auto_urls=True,
                    paragraphs=True,
                    clean=True,
                    tag_data=None),
}



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

try:
    from local import *
except:
    pass

