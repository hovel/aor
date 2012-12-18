from django.conf.urls import patterns, url
from pybb.views import ForumView
from django.conf import settings

FORUM_ID = getattr(settings, 'PYBB_NEWS_FORUM_ID', 1)

urlpatterns = patterns('',
    url(r'^$', ForumView.as_view(template_name='pybb4news/forum.html'),
        {'pk': FORUM_ID}, name='list'),
)
