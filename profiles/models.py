from annoying.fields import AutoOneToOneField
from django.contrib.auth.models import User, Permission
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from pybb.models import PybbProfile
from aor.settings import AOR_THEMES


class Profile(PybbProfile):
    PROFILE_DATE_SHOW_CLASSIC = 1
    PROFILE_DATE_SHOW_REVERTED = 2

    PROFILE_DATE_SHOW_TYPES = (
        (PROFILE_DATE_SHOW_REVERTED, _(u'Reverted')),
        (PROFILE_DATE_SHOW_CLASSIC, _(u'Classic')),
    )
    user = AutoOneToOneField(User)
    theme = models.CharField(max_length=32, choices=AOR_THEMES, default='default')
    date_show_type = models.IntegerField(verbose_name=_(u'Date show type'), choices=PROFILE_DATE_SHOW_TYPES,
                                         default=PROFILE_DATE_SHOW_REVERTED)

    # personal info
    icq = models.CharField(verbose_name=_('ICQ Number'), max_length=10, null=True, blank=True,
                           validators=[RegexValidator(regex='\d+')])
    skype = models.CharField(verbose_name=_('Skype username'), max_length=100, null=True, blank=True)
    jabber = models.CharField(verbose_name=_('Jabber address'), max_length=100, null=True, blank=True)
    site = models.URLField(verbose_name=_('Personal site'), null=True, blank=True, verify_exists=False)
    interests = models.TextField(verbose_name=_('Interests'), null=True, blank=True)

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
