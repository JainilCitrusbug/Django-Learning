# -*- coding: utf-8 -*-
from django.urls import include, path

from .. import views
from django.views.generic import TemplateView
from . import urls, urls_auth

urlpatterns = [
    path("", views.IndexView.as_view(), name="dashboard"),
    path("", include(urls_auth)),
    path("", include(urls)),
]