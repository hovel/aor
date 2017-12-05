from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView
from pybb.views import ProfileEditView
from registration.backends.default.views import RegistrationView
from aor.forms import AORProfileForm, RegistrationFormCaptcha
from aor.sitemaps import sitemaps
from aor.views import Search, MovePostView, AorAddPostView, AorEditPostView, AorTopicView, move_post_processing
from profiles.views import UserTopics, UserPosts, safe_logout

urlpatterns = [
    url(r'^robots.txt$', TemplateView.as_view(template_name='robots.txt')),
    url(r'^yandex_72c667563364196f.html$', TemplateView.as_view(template_name='yandex_72c667563364196f.html')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}),

    url(r'^donate/$', TemplateView.as_view(template_name='donate.html'), name='donate'),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),

    url(r'^accounts/register/$', RegistrationView.as_view(form_class=RegistrationFormCaptcha),
        name="registration_register"),
    url(r'^accounts/logout/$', safe_logout, name='auth_logout'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),

    url(r'^forum/profile/edit/$',
        ProfileEditView.as_view(form_class=AORProfileForm),
        name='pybb:edit_profile'),
    url(r'^forum/users/(?P<username>[^/]+)/topics/$', UserTopics.as_view(),
        name='user_topics'),
    url(r'^forum/users/(?P<username>[^/]+)/posts/$', UserPosts.as_view(),
        name='user_posts'),

    url(r'^forum/topic/(?P<pk>\d+)/$', AorTopicView.as_view(), name='topic'),
    url(r'^forum/topic/(?P<pk>\d+)/move/$', MovePostView.as_view(), name='move_post'),
    url(r'^forum/forum/(?P<forum_id>\d+)/topic/add/$', AorAddPostView.as_view(), name='add_topic'),
    url(r'^forum/topic/(?P<topic_id>\d+)/post/add/$', AorAddPostView.as_view(), name='add_post'),
    url(r'^forum/post/(?P<pk>\d+)/edit/$', AorEditPostView.as_view(), name='edit_post'),
    url(r'^forum/post/move/processing/$', move_post_processing, name='move_post_processing'),
    url(r'^forum/', include('pybb.urls', namespace='pybb')),

#    url(r'^search/$', Search.as_view(), name='search'),
    url(r'^news/', include('pybb4news.urls', namespace='news')),
    url(r'^blogs/', include('pybb4blogs.urls', namespace='blogs')),
    url(r'^ajax_selects/', include('ajax_select.urls')),

    url(r'^messages/', include('aor_messages.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^captcha/', include('captcha.urls')),
    # IRC Mibbit widget
    url(r'^irc/$',
        TemplateView.as_view(template_name='irc_mibbit_widget.html'),
        name='irc'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
