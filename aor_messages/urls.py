from django.conf.urls import include, url

from aor_messages.views import AorMessageView, AorConversationView, \
    AorReplyView, AorWriteView

merged_patterns = [
    url(r'^reply/(?P<message_id>[\d]+)/$', AorReplyView.as_view(), name='reply'),
    url(r'^view/(?P<message_id>[\d]+)/$', AorMessageView.as_view(), name='view'),
    url(r'^view/t/(?P<thread_id>[\d]+)/$', AorConversationView.as_view(), name='view_conversation'),
    url(r'^write/(?:(?P<recipients>[^/#]+)/)?$', AorWriteView.as_view(), name='write'),
    url(r'^', include('postman.urls')),
]

urlpatterns = [
    url(r'^', include(merged_patterns, namespace='postman', app_name='postman')),
]
