from django.views.generic import TemplateView, ListView

from .outbox import Outbox


class OutboxListView(ListView):
    template_name = 'django_outbox/outbox.html'
    context_object_name = 'mails'

    def get_queryset(self):
        return sorted(Outbox().all(), key=lambda r: r.when)


class MailTemplateView(TemplateView):
    template_name = 'django_outbox/mail.html'

    def get_context_data(self, id, **kwargs):
        context = super(MailTemplateView, self).get_context_data(**kwargs)
        mail = Outbox().get(id)
        context['mail'] = mail
        context['content_type'] = self.request.GET['content_type']
        context['content'] = mail.body[self.request.GET['content_type']]
        return context
