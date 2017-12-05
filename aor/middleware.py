# coding=utf-8
from __future__ import unicode_literals

from django.utils.deprecation import MiddlewareMixin


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
