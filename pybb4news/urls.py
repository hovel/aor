from django.conf.urls import patterns, url
from views import ForumView
from django.conf import settings

FORUM_ID = getattr(settings, 'PYBB_NEWS_FORUM_ID', 1)
PAGE_SIZE = getattr(settings, 'PYBB_NEWS_PAGE_SIZE', 10)

urlpatterns = patterns('',
    url(r'^$', ForumView.as_view(), {'pk': FORUM_ID}, name='list'),
)
