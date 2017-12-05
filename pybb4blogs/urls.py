from django.conf.urls import url
from pybb.views import ForumView
from django.conf import settings

FORUM_ID = getattr(settings, 'PYBB_BLOGS_FORUM_ID', 1)
PAGE_SIZE = getattr(settings, 'PYBB_BLOGS_PAGE_SIZE', 10)

urlpatterns = [
    url(r'^$', ForumView.as_view(template_name='pybb4blogs/forum.html',
        paginate_by=PAGE_SIZE),
        {'pk': FORUM_ID}, name='list'),
]
