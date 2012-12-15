from django.conf.urls import patterns, url
from news.views import NewsList, NewsCreate, NewsDetail, NewsUpdate, NewsDelete

urlpatterns = patterns('',
    url(r'^$', NewsList.as_view(), name='list'),
    url(r'^create/$', NewsCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', NewsDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', NewsUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', NewsDelete.as_view(), name='delete'),
)
