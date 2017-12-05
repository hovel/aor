from django.conf.urls import include, url

from aor_messages.views import AorMessageView, AorConversationView, \
    AorReplyView, AorWriteView

from postman.urls import urlpatterns as postman_urlpatterns

merged_urlpatterns = ([
    url(r'^reply/(?P<message_id>[\d]+)/$', AorReplyView.as_view(), name='reply'),
    url(r'^view/(?P<message_id>[\d]+)/$', AorMessageView.as_view(), name='view'),
    url(r'^view/t/(?P<thread_id>[\d]+)/$', AorConversationView.as_view(), name='view_conversation'),
    url(r'^write/(?:(?P<recipients>[^/#]+)/)?$', AorWriteView.as_view(), name='write'),
] + [
    u for u in postman_urlpatterns if u.name not in ['reply', 'view', 'view_conversation', 'write']
], 'postman')

urlpatterns = [
    url(r'^', include(merged_urlpatterns))
]
