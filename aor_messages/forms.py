# coding=utf-8
from __future__ import unicode_literals
from postman.forms import FullReplyForm, WriteForm
from pybb import util


class AorWriteForm(WriteForm):
    class Meta(WriteForm.Meta):
        widgets = {
            'body': util.get_markup_engine().get_widget_cls(),
        }


class AorFullReplyForm(FullReplyForm):
    class Meta(FullReplyForm.Meta):
        widgets = {
            'body': util.get_markup_engine().get_widget_cls(),
        }