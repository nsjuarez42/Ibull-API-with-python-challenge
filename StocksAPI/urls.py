# -*- coding: utf-8 -*-
from django.conf.urls import url

from StocksAPI.views import index

urlpatterns = [
    url('', index.index)
]
