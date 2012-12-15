from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import generic
from news.forms import NewsForm
from news.models import News


class NewsList(generic.ListView):
    model = News


class NewsCreate(generic.CreateView):
    model = News
    form_class = NewsForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perms('news.add_news'):
            raise Http404
        return super(NewsCreate, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        news = form.save(commit=False)
        news.user = self.request.user
        news.save()
        return redirect(news)


class NewsDetail(generic.DetailView):
    model = News


class NewsUpdate(generic.UpdateView):
    model = News
    form_class = NewsForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perms('news.change_news'):
            raise Http404
        return super(NewsUpdate, self).dispatch(request, *args, **kwargs)


class NewsDelete(generic.DeleteView):
    model = News

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perms('news.delete_news'):
            raise Http404
        return super(NewsDelete, self).dispatch(request, *args, **kwargs)


