# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.log import DEFAULT_LOGGING

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
    'production_console': {
        'class': 'logging.StreamHandler',
        'level': 'DEBUG',
        'formatter': 'verbose',
        'filters': ['require_debug_false'],
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
                     'production_console',
                     'production_mail_admins'],
    },
    'management.commands': {
        'level': 'DEBUG',
        'handlers': ['debug_console',
                     'production_console',
                     'production_mail_admins'],
    },
})
