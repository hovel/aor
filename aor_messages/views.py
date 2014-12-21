from django.db.models import Q
from django.views.generic.base import TemplateView
from postman.views import DisplayMixin, ReplyView
from aor_messages.forms import AorFullReplyForm


class AorReplyView(ReplyView):
    def get_initial(self):
        self.initial = super(AorReplyView, self).get_initial()
        self.initial['body'] = None
        return self.initial


class FixedFormInitialMixin(object):
    form_class = AorFullReplyForm

    def get_context_data(self, **kwargs):
        context = super(FixedFormInitialMixin, self).get_context_data(**kwargs)
        form = context.get('form')
        if form:
            form.initial['body'] = None
        return context


class AorMessageView(FixedFormInitialMixin, DisplayMixin, TemplateView):
    """Display one specific message."""

    def get(self, request, message_id, *args, **kwargs):
        self.filter = Q(pk=message_id)
        return super(AorMessageView, self).get(request, *args, **kwargs)


class AorConversationView(FixedFormInitialMixin, DisplayMixin, TemplateView):
    """Display a conversation."""

    def get(self, request, thread_id, *args, **kwargs):
        self.filter = Q(thread=thread_id)
        return super(AorConversationView, self).get(request, *args, **kwargs)

