from django import template
from django.conf import settings
from pybb.models import Forum, Topic

FORUM_ID = getattr(settings, 'PYBB_NEWS_FORUM_ID', 1)

register = template.Library()

@register.inclusion_tag('last_entries.html')
def last_news(count=5, *args, **kwargs):
    news = Topic.objects.filter(forum_id=FORUM_ID).order_by('-created', '-updated')[:count]
    return dict(object_list=news)
