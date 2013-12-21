# coding=utf-8
from __future__ import unicode_literals
from django.contrib.sitemaps import GenericSitemap
from pybb.models import Topic, Forum, Post


forums_dict = {
    'queryset': Forum.objects.all(),
    'date_field': 'updated',
}
topics_dict = {
    'queryset': Topic.objects.all(),
    'date_field': 'updated',
}

sitemaps = {
    'forums': GenericSitemap(forums_dict, priority=0.5),
    'topics': GenericSitemap(topics_dict, priority=0.6),
}