from django.conf import settings
from django.contrib.syndication.views import Feed
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views import generic
from pure_pagination import Paginator
from pybb import defaults
from pybb.models import Forum, Topic


FORUM_ID = getattr(settings, 'PYBB_NEWS_FORUM_ID', 1)


class ForumView(generic.ListView):

    paginate_by = defaults.PYBB_FORUM_PAGE_SIZE
    context_object_name = 'topic_list'
    template_name = 'pybb4news/forum.html'
    paginator_class = Paginator

    def get_context_data(self, **kwargs):
        ctx = super(ForumView, self).get_context_data(**kwargs)
        ctx['forum'] = self.forum
        return ctx

    def get_queryset(self):
        self.forum = get_object_or_404(Forum, pk=FORUM_ID)
        if self.forum.category.hidden and (not self.request.user.is_staff):
            raise Http404()
        qs = self.forum.topics.order_by('-created', '-updated').select_related()
        if not (self.request.user.is_superuser or self.request.user in self.forum.moderators.all()):
            if self.request.user.is_authenticated():
                qs = qs.filter(Q(user=self.request.user)|Q(on_moderation=False))
            else:
                qs = qs.filter(on_moderation=False)
        return qs


class LatestNewsFeed(Feed):
    title = 'News archlinux.org.ru'
    link = '/news/'
    description = 'Latest news'

    def items(self):
        forum = Forum.objects.get(pk=FORUM_ID)
        topics = Topic.objects.filter(forum=forum)[:defaults.PYBB_FORUM_PAGE_SIZE]
        return topics

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return item.head.body_html
