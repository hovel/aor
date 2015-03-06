from django.utils.translation import ugettext_lazy as _
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = DEBUG

ADMINS = (
    ('Pavel Zhukov', 'gelios@gmail.com'),
    ('Sergey Fursov', 'geyser85@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_ENV_MYSQL_DATABASE', 'local_db'),
        'HOST': os.environ.get('DB_PORT_3306_TCP_ADDR', 'localhost'),
        'PORT': os.environ.get('DB_PORT_3306_TCP_PORT', 3306),
        'USER': 'root',
        'PASSWORD': os.environ.get('DB_ENV_MYSQL_ROOT_PASSWORD', 'pass'),
        'TEST_CHARSET': 'UTF8',
        'ATOMIC_REQUESTS': True,
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
USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'Insert your SECRET_KEY from your local.py'

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pybb.middleware.PybbMiddleware',
    'aor.middleware.RemoteAddrMiddleware',
)

ROOT_URLCONF = 'aor.urls'

TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'aor', 'templates'),)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'pybb.context_processors.processor',
    'profiles.context_processor.user_theme',
    'django.core.context_processors.request',
    'postman.context_processors.inbox'
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    # 'django.contrib.comments',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'registration',
    'sorl.thumbnail',
    'captcha',
    'gunicorn',
    'pybb',
    'aor',
    'pybb4news',
    'pybb4blogs',
    'profiles',
    'mailer',
    'ajax_select',
    'postman',
    'aor_messages',
    'bootstrapform',
    'storages'
)

CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
#CAPTCHA_LENGTH = 7
CAPTCHA_LETTER_ROTATION = (-10, 10)
CAPTCHA_TIMEOUT = 1
CAPTCHA_NOISE_FUNCTIONS = ('captcha.helpers.noise_dots',)
#AUTH_PROFILE_MODULE = 'pybb.Profile'
FILE_UPLOAD_PERMISSIONS = 0644
LOGIN_REDIRECT_URL = '/'
PYBB_TEMPLATE = 'forum.html'
# disable pybb smiles
PYBB_SMILES = dict()
# disable auto subscribe
PYBB_DEFAULT_AUTOSUBSCRIBE = False
PYBB_DEFAULT_TITLE = 'Forum'

PYBB_NEWS_FORUM_ID = 1
PYBB_BLOGS_FORUM_ID = 25

PYBB_NEWS_PAGE_SIZE = 10
PYBB_BLOGS_PAGE_SIZE = 10
PYBB_POLL_MAX_ANSWERS = 30

AUTH_PROFILE_MODULE = 'profiles.Profile'
PYBB_PROFILE_RELATED_NAME = 'profile'

PYBB_MARKUP_ENGINES_PATHS = {
    'bbcode': 'aor.markup_parsers.AorBBCodeParser'
}

AOR_THEMES = (
    ('default', _('default theme')),
    ('dark', _('dark theme')),
)

ACCOUNT_ACTIVATION_DAYS = 3

AJAX_LOOKUP_CHANNELS = {
    'postman_users': {'model': 'auth.user', 'search_field': 'username'},
}
POSTMAN_AUTOCOMPLETER_APP = {
    'arg_default': 'postman_users',
}
POSTMAN_DISALLOW_ANONYMOUS = True
POSTMAN_DISABLE_USER_EMAILING = True
POSTMAN_DISALLOW_MULTIRECIPIENTS = True
POSTMAN_DISALLOW_COPIES_ON_REPLY = True
POSTMAN_AUTO_MODERATE_AS = True

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
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


if DEBUG:
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INSTALLED_APPS += ('debug_toolbar', )
    INTERNAL_IPS = ('127.0.0.1',)
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}

try:
    from settings_local import *
except ImportError:
    pass
