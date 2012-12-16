from django.contrib.auth.models import User
from django.db import models
from django.utils.html import urlize
from postmarkup import render_bbcode


class News(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=150)
    text = models.TextField()
    source = models.URLField(blank=True)
    author = models.CharField(max_length=75, blank=True)
    date = models.CharField(max_length=32, blank=True)
    text_html = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'News'
        verbose_name = 'News'

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return 'news:detail', [self.pk, ]

    def save(self, force_insert=False, force_update=False, using=None):
        self.text_html = urlize(render_bbcode(self.text,
            exclude_tags=['size', 'center']))
        super(News, self).save(force_insert, force_update, using)
