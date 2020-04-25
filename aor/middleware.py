# coding=utf-8
from __future__ import unicode_literals

from django.conf import settings


class RemoteAddrMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        super(RemoteAddrMiddleware, self).__init__()

    def __call__(self, request):
        variants = [request.META.get('REMOTE_ADDR', '')]
        variants.extend(
            addr.strip() for addr in
            request.META.get('HTTP_X_FORWARDED_FOR', '').split(','))
        for v in variants:
            if v and not v.startswith(('127', '172')):  # localhost, docker
                request.META['REMOTE_ADDR'] = v
                break

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
