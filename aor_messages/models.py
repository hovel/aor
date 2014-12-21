# coding=utf-8
from __future__ import unicode_literals
from annoying.fields import AutoOneToOneField
from django.db import models
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from postman.models import Message
from pybb import util as pybb_util


class AorMessage(models.Model):
    message = AutoOneToOneField(Message, related_name='aor_message')
    body_html = models.TextField()

    def save(self, *args, **kwargs):
        self.body_html = pybb_util.get_markup_engine().format(self.message.body)
        super(AorMessage, self).save(*args, **kwargs)


@receiver(post_save, sender=Message)
def update_message_html_body(sender,  instance, **kwargs):
    instance.aor_message.save()


