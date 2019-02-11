# coding=utf-8
"""Urls for djp application."""
from django.conf.urls import url

from .views import Home, custom_404

urlpatterns = [
    # basic app views
    url(regex='^$',
        view=Home.as_view(),
        name='home'),
]

# Prevent cloudflare from showing an ad laden 404 with no context
handler404 = custom_404

