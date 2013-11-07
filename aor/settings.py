from django.utils.translation import ugettext_lazy as _
from markdown import Markdown
from os.path import abspath, join, dirname
from postmarkup import render_bbcode

PROJECT_ROOT = abspath(join(dirname(__file__), '..'))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Pavel Zhukov', 'gelios@gmail.com'),
    ('Sergey Fursov', 'geyser85@gmail.com'),
    )

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'NAME': 'aor',
        'USER': 'root',
        'PASSWORD': '',
        },
    'phpbb3': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'arch_forum',
        'USER': 'root',
        'PASSWORD': '',
    },
    'drupal': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'arch_drupal',
        'USER': 'root',
        'PASSWORD': '',
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
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pybb.middleware.PybbMiddleware',
    )

ROOT_URLCONF = 'aor.urls'

TEMPLATE_DIRS = (join(PROJECT_ROOT, 'aor', 'templates'),)

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
    )

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.comments',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'south',
    'registration',
    'sorl.thumbnail',
    'captcha',
    'gunicorn',
    'pybb',
    'django-field-attributes',
    'aor',
    'pybb4news',
    'pybb4blogs',
    'profiles',
    'mailer',
    )

CAPTCHA_LENGTH = 7
CAPTCHA_LETTER_ROTATION = (-60, 60)
CAPTCHA_TIMEOUT = 1
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

AOR_THEMES = (
    ('default', _('default theme')),
    ('dark', _('dark theme')),
)

ACCOUNT_ACTIVATION_DAYS = 3

PHPBB_TABLE_PREFIX = 'phpbb_'
PHPBB_CAPTCHA_QUESTIONS_MODEL_EXIST = True

PYBB_MARKUP_ENGINES = {
    'bbcode': lambda str:
            render_bbcode(
                str,
                exclude_tags=['size', 'center'],
                cosmetic_replace=False,
                render_unknown_tags=True),
    'markdown': lambda str: Markdown(safe_mode='escape').convert(str)
}


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

try:
    from local import *
except ImportError:
    pass

if DEBUG:
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INSTALLED_APPS += ('debug_toolbar', 'django_phpBB3', 'migration',
                       'drupango')
    INTERNAL_IPS = ('127.0.0.1',)
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DATABASE_ROUTERS = ['aor.routers.PHPBB3', 'aor.routers.Drupal']
    DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}
