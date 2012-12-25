from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views import generic
from pure_pagination import Paginator
from pybb import defaults
from pybb.models import Post, Topic


class UserPosts(generic.ListView):
    model = Post
    paginate_by = defaults.PYBB_TOPIC_PAGE_SIZE
    paginator_class = Paginator
    template_name = 'pybb/user_posts.html'

    def dispatch(self, request, username, *args, **kwargs):
        self.user = get_object_or_404(User, username=username)
        return super(UserPosts, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        qs = super(UserPosts, self).get_queryset()
        qs = qs.filter(user=self.user)
        qs = qs.filter(on_moderation=False)
        qs = qs.filter(topic__forum__hidden=False)
        qs = qs.order_by('-created', '-updated')
        return qs

    def get_context_data(self, **kwargs):
        context = super(UserPosts, self).get_context_data(**kwargs)
        context['target'] = self.user
        return context


class UserTopics(generic.ListView):
    model = Topic
    paginate_by = defaults.PYBB_FORUM_PAGE_SIZE
    paginator_class = Paginator
    template_name = 'pybb/user_topics.html'

    def dispatch(self, request, username, *args, **kwargs):
        self.user = get_object_or_404(User, username=username)
        return super(UserTopics, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        qs = super(UserTopics, self).get_queryset()
        qs = qs.filter(user=self.user)
        qs = qs.filter(on_moderation=False)
        qs = qs.filter(forum__hidden=False)
        qs = qs.order_by('-updated', '-created')
        return qs

    def get_context_data(self, **kwargs):
        context = super(UserTopics, self).get_context_data(**kwargs)
        context['target'] = self.user
        return context

