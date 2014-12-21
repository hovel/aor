# coding=utf-8
from __future__ import unicode_literals
from postman.forms import FullReplyForm
from pybb import util


class AorFullReplyForm(FullReplyForm):
    class Meta(FullReplyForm.Meta):
        widgets = {
            'body': util.get_markup_engine().get_widget_cls(),
        }