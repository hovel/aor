from django import template
from django.conf import settings
from pybb.models import Forum, Topic

FORUM_ID = getattr(settings, 'PYBB_BLOGS_FORUM_ID', 1)

register = template.Library()

@register.inclusion_tag('last_entries.html')
def last_blogs(count=5, *args, **kwargs):
    blogs = Topic.objects.filter(forum_id=FORUM_ID)[:count]
    return dict(object_list=blogs)
