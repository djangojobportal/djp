# coding=utf-8
"""Views."""
# noinspection PyUnresolvedReferences
import logging
logger = logging.getLogger(__name__)

from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = 'index.html'

