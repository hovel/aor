from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html'), name='front-page'),
    url(r'^accounts/', include('registration.urls')),
    url(r'^news/', include('dnews.urls', namespace='news')),
    url(r'^blogs/', include('dblog.urls.blog', namespace='blog')),
    url(r'^posts/', include('dblog.urls.post', namespace='post')),
    url(r'^forum/', include('pybb.urls', namespace='pybb')),
    url(r'^comments/', include('django.contrib.comments.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
) 

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('', ) + static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)


