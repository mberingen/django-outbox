from django.conf.urls import include, url

from .views import OutboxListView, MailTemplateView


urlpatterns = [
    url(r'^$', OutboxListView.as_view(), name='outbox'),
    url(r'^(?P<id>.+)/$', MailTemplateView.as_view(), name='mail'),
]
