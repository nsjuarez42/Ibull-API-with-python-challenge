from gzip import READ
from django.conf.urls import url

from trades.views import tradesAPI,tradesById

urlpatterns = [
    url(r'^trades/$',tradesAPI),
    url(r'^trades/(?P<id>[0-9]+)$',tradesById)
]