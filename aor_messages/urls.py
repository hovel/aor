from django.conf.urls import patterns, include, url
from aor_messages.views import AorMessageView, AorConversationView, AorReplyView

urlpatterns = patterns(
    url(r'^reply/(?P<message_id>[\d]+)/$', AorReplyView.as_view(), name='postman_reply'),
    url(r'^view/(?P<message_id>[\d]+)/$', AorMessageView.as_view(), name='postman_view'),
    url(r'^view/t/(?P<thread_id>[\d]+)/$', AorConversationView.as_view(), name='postman_view_conversation'),
    url(r'^', include('postman.urls')),
)