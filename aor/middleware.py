# coding=utf-8
from __future__ import unicode_literals

from django.conf import settings


class RemoteAddrMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        super(RemoteAddrMiddleware, self).__init__()

    def __call__(self, request):
        REWRITE_CF_HOST = getattr(settings, 'REWRITE_CF_HOST', None)
        CF_HOST = getattr(settings, 'CF_HOST', None)
        if REWRITE_CF_HOST and CF_HOST and request.get_host() == REWRITE_CF_HOST:
            forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if not forwarded_for:
                return
            try:
                remote_addr = forwarded_for.split(',')[0].strip()
                request.META['REMOTE_ADDR'] = remote_addr
            except IndexError as e:
                pass

        response = self.get_response(request)

        return response


class XForwardedHostMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        super(XForwardedHostMiddleware, self).__init__()

    def __call__(self, request):
        REWRITE_CF_HOST = getattr(settings, 'REWRITE_CF_HOST', None)
        CF_HOST = getattr(settings, 'CF_HOST', None)
        if REWRITE_CF_HOST and CF_HOST and request.get_host() == REWRITE_CF_HOST:
            request.META['HTTP_X_FORWARDED_HOST'] = CF_HOST

        response = self.get_response(request)

        return response
