from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from pybb.views import ProfileEditView
from registration.backends.default.views import RegistrationView
from aor.forms import AORProfileForm, RegistrationFormCaptcha
from aor.sitemaps import sitemaps
from aor.views import Search, MovePostView, AorMessageView, AorConversationView, AorReplyView
from profiles.views import UserTopics, UserPosts

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^robots.txt$', TemplateView.as_view(template_name='robots.txt')),
    url(r'^yandex_72c667563364196f.html$', TemplateView.as_view(template_name='yandex_72c667563364196f.html')),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

    url(r'^donate/$', TemplateView.as_view(template_name='donate.html'), name='donate'),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^accounts/register/$', RegistrationView.as_view(form_class=RegistrationFormCaptcha),
        name="registration_register"),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^forum/profile/edit/$',
        ProfileEditView.as_view(form_class=AORProfileForm),
        name='pybb:edit_profile'),
    url(r'^forum/users/(?P<username>[^/]+)/topics/$', UserTopics.as_view(),
        name='user_topics'),
    url(r'^forum/users/(?P<username>[^/]+)/posts/$', UserPosts.as_view(),
        name='user_posts'),
    url(r'^forum/post/(?P<pk>\d+)/move/$', MovePostView.as_view(), name='move_post'),
    url(r'^forum/', include('pybb.urls', namespace='pybb')),
#    url(r'^search/$', Search.as_view(), name='search'),
    url(r'^news/', include('pybb4news.urls', namespace='news')),
    url(r'^blogs/', include('pybb4blogs.urls', namespace='blogs')),
    url(r'^ajax_selects/', include('ajax_select.urls')),

    url(r'^messages/reply/(?P<message_id>[\d]+)/$', AorReplyView.as_view(), name='postman_reply'),
    url(r'^messages/view/(?P<message_id>[\d]+)/$', AorMessageView.as_view(), name='postman_view'),
    url(r'^messages/view/t/(?P<thread_id>[\d]+)/$', AorConversationView.as_view(), name='postman_view_conversation'),
    url(r'^messages/', include('postman.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^captcha/', include('captcha.urls')),
    # IRC Mibbit widget
    url(r'^irc/$',
        TemplateView.as_view(template_name='irc_mibbit_widget.html'),
        name='irc'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
