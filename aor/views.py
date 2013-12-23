from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.utils import timezone
from django.views import generic
from django.views.generic.base import TemplateView
from postman.views import DisplayMixin, ReplyView
from pure_pagination import Paginator, PaginationMixin
from pybb import defaults
from pybb.models import Post, Topic
from aor.forms import MovePostForm

BLOGS_FORUM_ID = getattr(settings, 'PYBB_BLOGS_FORUM_ID', 1)
NEWS_FORUM_ID = getattr(settings, 'PYBB_NEWS_FORUM_ID', 1)


class Search(PaginationMixin, generic.ListView):
    template_name = 'search/search.html'
    paginate_by = defaults.PYBB_FORUM_PAGE_SIZE
    paginator_class = Paginator

    def dispatch(self, request, *args, **kwargs):
        self.query = request.GET.get('q')
        return super(Search, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        qs = Post.objects.all()
        if not self.query:
            return qs.none()
        for word in self.query.split()[:10]:
            qs = qs.filter(Q(body_text__icontains=word) |
                           Q(topic__name__icontains=word))
        topic_list = qs.values_list('topic', flat=True)
        return Topic.objects.filter(pk__in=topic_list)

    def get_context_data(self, **kwargs):
        context = super(Search, self).get_context_data(**kwargs)
        context['query'] = self.query
        return context


class MovePostView(generic.UpdateView):
    model = Post
    template_name = 'pybb/move_post.html'
    form_class = MovePostForm

    def get_form_kwargs(self):
        kwargs = super(MovePostView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_object(self, queryset=None):
        post = super(MovePostView, self).get_object()
        if post == post.topic.head:
            raise PermissionDenied
        return post

    def form_valid(self, form):
        old_topic = self.object.topic
        old_forum = self.object.topic.forum

        self.object = form.save(commit=False)
        self.object.created = timezone.now()
        self.object.save()

        old_topic.update_counters()
        old_forum.update_counters()

        return super(MovePostView, self).form_valid(form)


class AorReplyView(ReplyView):
    def get_initial(self):
        self.initial = super(AorReplyView, self).get_initial()
        self.initial['body'] = None
        return self.initial


class FixedFormInitialMixin(object):
    def get_context_data(self, **kwargs):
        context = super(FixedFormInitialMixin, self).get_context_data(**kwargs)
        form = context.get('form')
        if form:
            form.initial['body'] = None
        return context


class AorMessageView(FixedFormInitialMixin, DisplayMixin, TemplateView):
    """Display one specific message."""

    def get(self, request, message_id, *args, **kwargs):
        self.filter = Q(pk=message_id)
        return super(AorMessageView, self).get(request, *args, **kwargs)


class AorConversationView(FixedFormInitialMixin, DisplayMixin, TemplateView):
    """Display a conversation."""

    def get(self, request, thread_id, *args, **kwargs):
        self.filter = Q(thread=thread_id)
        return super(AorConversationView, self).get(request, *args, **kwargs)

