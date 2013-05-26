from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.utils import timezone
from django.views import generic
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


