# coding=utf-8
from __future__ import unicode_literals

from django.utils.deprecation import MiddlewareMixin

from django.conf import settings


class RemoteAddrMiddleware(MiddlewareMixin):
    def process_request(self, request):
        remote_addr = request.META.get('REMOTE_ADDR')
        if not remote_addr or remote_addr == '127.0.0.1' or remote_addr.startswith('172.'):
            forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if not forwarded_for:
                return
            try:
                forwarded_for = forwarded_for.split(',')[0].strip()
                request.META['REMOTE_ADDR'] = forwarded_for
            except:
                pass


class XForwardedHostMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        REWRITE_CF_HOST = getattr(settings, 'REWRITE_CF_HOST', None)
        CF_HOST = getattr(settings, 'CF_HOST', None)
        if REWRITE_CF_HOST and CF_HOST and request.get_host() == REWRITE_CF_HOST:
            request.META['HTTP_X_FORWARDED_HOST'] = CF_HOST

        response = self.get_response(request)

        return response
