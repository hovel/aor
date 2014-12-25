# coding=utf-8
from __future__ import unicode_literals
from pybb.markup.bbcode import BBCodeParser, BBCodeWidget


class AorBBCodeWidget(BBCodeWidget):
    class Media:
        extend = False
        css = {
            'all': (
                'markitup/skins/aor/style.css',
                'markitup/sets/bbcode/style.css',
            ),
        }
        js = (
            'markitup/ajax_csrf.js',
            'markitup/jquery.markitup.js',
            'markitup/sets/bbcode/set.js',
            'pybb/js/markitup.js',
        )


class AorBBCodeParser(BBCodeParser):

    widget_class = AorBBCodeWidget

    def __init__(self):
        super(AorBBCodeParser, self).__init__()
        self._parser.replace_cosmetic = False

    def format(self, text):
        return self._parser.format(text)