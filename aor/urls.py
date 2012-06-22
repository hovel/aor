from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from aor.forms import  AuthenticationFormCaptcha
from django.contrib.auth.views import login

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='/news/'), name='front-page'),
    url(r'^accounts/login/$', login, name="auth_login",
        kwargs=dict(authentication_form=AuthenticationFormCaptcha)),
    url(r'^accounts/register/$', RedirectView.as_view(), name="registration"),
    #    url(r'^accounts/register/$', register, name="registration",
    #        kwargs=dict(form_class=RegistrationFormCaptcha)),
    url(r'^accounts/', include('registration.urls')),
    url(r'^news/', include('dnews.urls', namespace='news')),
    #    url(r'^blogs/', include('dblog.urls.blog', namespace='blog')),
    #    url(r'^posts/', include('dblog.urls.post', namespace='post')),
    #    url(r'^forum/', include('pybb.urls', namespace='pybb')),
    url(r'^comments/', include('django.contrib.comments.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^robots.txt$', include('robots.urls')),
    url(r'^captcha/', include('captcha.urls')),
)

urlpatterns += staticfiles_urlpatterns()
