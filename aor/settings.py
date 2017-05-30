import os
from django.utils.log import DEFAULT_LOGGING
from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True

ADMINS = (
    ('Pavel Zhukov', 'gelios@gmail.com'),
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
        'ATOMIC_REQUESTS': True,
        'TEST': {
            'CHARSET': 'utf8',
            'COLLATION': 'utf8_general_ci'
        }
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

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'aor', 'templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'pybb.context_processors.processor',
                'profiles.context_processor.user_theme',
                'postman.context_processors.inbox'
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'debug': DEBUG
        },
    },
]

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
    'ajax_select',
    'postman',
    'aor_messages',
    'bootstrapform',
    'storages',
    'pure_pagination',
)

CAPTCHA_FONT_PATH = 'fonts/captcha_font.ttf'
CAPTCHA_FONT_SIZE = 28
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'
CAPTCHA_LENGTH = 5
CAPTCHA_LETTER_ROTATION = (-10, 15)
CAPTCHA_TIMEOUT = 1
CAPTCHA_NOISE_FUNCTIONS = ('captcha.helpers.noise_null', 'captcha.helpers.noise_arcs',)
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
PYBB_ALLOW_DELETE_OWN_POST = False

AOR_THEMES = (
    ('default', _('default theme')),
    ('default-flat', _('default flat theme')),
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

LOGGING = DEFAULT_LOGGING
LOGGING.setdefault('formatters', {})
LOGGING['formatters'].update({
    'verbose': {
        'format': '%(levelname)s %(asctime)s %(pathname)s:%(lineno)d\n%(message)s'
    }
})
LOGGING.setdefault('filters', {})
LOGGING['filters'].update({})
LOGGING.setdefault('handlers', {})
LOGGING['handlers'].update({
    'debug_console': {
        'class': 'logging.StreamHandler',
        'level': 'DEBUG',
        'formatter': 'verbose',
        'filters': ['require_debug_true'],
    },
    # This handler will be used mostly for management commands (see below),
    # so the debug level can be useful in production.
    'production_console': {
        'class': 'logging.StreamHandler',
        'level': 'DEBUG',
        'formatter': 'verbose',
        'filters': ['require_debug_false'],
    },
    'production_rotate_file': {
        'class': 'logging.handlers.RotatingFileHandler',
        'level': 'INFO',
        'formatter': 'verbose',
        'filters': ['require_debug_false'],
        'filename': os.path.join(BASE_DIR, '../logs/aor_inner.log'),
        'maxBytes': 1024 * 1024 * 10,
        'backupCount': 3,
    },
    'production_mail_admins': {
        'class': 'django.utils.log.AdminEmailHandler',
        'level': 'ERROR',
        'formatter': 'verbose',
        'filters': ['require_debug_false'],
    },
})
LOGGING.setdefault('loggers', {})
LOGGING['loggers'].update({
    'hovel': {
        'level': 'DEBUG',
        'handlers': ['debug_console',
                     'production_rotate_file',
                     'production_mail_admins'],
    },
})


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
