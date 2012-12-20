from annoying.fields import AutoOneToOneField
from django.contrib.auth.models import User, Permission
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from pybb.models import PybbProfile
from aor.settings import AOR_THEMES

class Profile(PybbProfile):
    user = AutoOneToOneField(User)
    theme = models.CharField(max_length=32, choices=AOR_THEMES,
        default='default')

    def __unicode__(self):
        return self.user.username

    class Meta(object):
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    def get_absolute_url(self):
        return reverse('pybb:user', kwargs={'username': self.user.username})


def user_saved(instance, created, **kwargs):
    if not created:
        return
    try:
        add_post_permission = Permission.objects.get_by_natural_key('add_post', 'pybb', 'post')
        add_topic_permission = Permission.objects.get_by_natural_key('add_topic', 'pybb', 'topic')
    except Permission.DoesNotExist:
        return
    instance.user_permissions.add(add_post_permission, add_topic_permission)
    instance.save()
    Profile.objects.create(user=instance)

post_save.connect(user_saved, sender=User)
