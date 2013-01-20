from django import template
from django.conf import settings
from pybb.models import Forum, Topic

register = template.Library()

BLOGS_FORUM_ID = getattr(settings, 'PYBB_BLOGS_FORUM_ID', 1)
NEWS_FORUM_ID = getattr(settings, 'PYBB_NEWS_FORUM_ID', 1)

@register.inclusion_tag('last_entries.html')
def last_topics(count=10, *args, **kwargs):
    qs = Topic.objects.filter(forum__hidden=False).filter(forum__category__hidden=False)
    qs = qs.exclude(forum_id__in=[BLOGS_FORUM_ID, NEWS_FORUM_ID, ])
    qs = qs.filter(on_moderation=False)
    qs = qs.order_by('-updated', '-created')
    qs = qs[:count]
    return dict(object_list=qs)