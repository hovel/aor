from os.path import abspath, join, dirname

PROJECT_ROOT = abspath(join(dirname(__file__), '..'))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Pavel Zhukov', 'gelios@gmail.com'),
    ('Vladimir Korsun', 'korsun.vladimir@gmail.com'),
    )

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'NAME': 'aor',
        'USER': 'web',
        'PASSWORD': 'web',
        },
    'phpbb3': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'arch_forum', # Or path to database file if using sqlite3.
        'USER': 'root', # Not used with sqlite3.
        'PASSWORD': '', # Not used with sqlite3.
    }

}

SITE_ID = 1

TIME_ZONE = 'Europe/Moscow'

LANGUAGE_CODE = 'ru-RU'
LANGUAGES = (
    ('ru', 'Russian'),
    ('ua', 'Ukraine'),)

USE_I18N = True
USE_L10N = True

MEDIA_ROOT = join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/media/static/admin/'

STATIC_ROOT = join(MEDIA_ROOT, 'static')
STATIC_URL = '/media/static/'
STATICFILES_DIRS = (join(PROJECT_ROOT, 'static'),)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    )

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'Insert your SECRET_KEY from your local.py'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
    )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
#    'pybb.middleware.PybbMiddleware',
    )

ROOT_URLCONF = 'aor.urls'

TEMPLATE_DIRS = (join(PROJECT_ROOT,'templates'),)

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
    'robots',
    'captcha',
    'gunicorn',
    'pybb',
    'django-field-attributes',
    )

CAPTCHA_LENGTH = 7
CAPTCHA_LETTER_ROTATION = (-60, 60)
CAPTCHA_TIMEOUT = 1
ROBOTS_CACHE_TIMEOUT = 60 * 60 * 24
AUTH_PROFILE_MODULE = 'pybb.Profile'
FILE_UPLOAD_PERMISSIONS = 0644
LOGIN_REDIRECT_URL = '/'
PYBB_TEMPLATE = 'forum.html'
# disable pybb smiles
PYBB_SMILES = dict()
# disable auto subscribe
PYBB_DEFAULT_AUTOSUBSCRIBE = False

PHPBB_TABLE_PREFIX = 'phpbb_'
PHPBB_CAPTCHA_QUESTIONS_MODEL_EXIST = True


#PYBB_SMILES_PREFIX = STATIC_URL + 'pybb/emoticons/'
#PYBB_MARKUP_ENGINES = {
#    'bbcode': lambda str: render_bbcode(str,
#        encoding="utf-8",
#        exclude_tags=['size', 'center'],
#        auto_urls=True,
#        paragraphs=True,
#        clean=True,
#        tag_data=None),
#    }

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
except ImportError:
    pass

if DEBUG:
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INSTALLED_APPS += ('debug_toolbar', 'django_phpBB3', 'migration',)
    INTERNAL_IPS = ('127.0.0.1',)
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DATABASE_ROUTERS = ['aor.routers.PHPBB3',]
