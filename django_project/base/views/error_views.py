# coding=utf-8
"""Our custom error views."""
from django.shortcuts import render_to_response
from django.template import RequestContext


def custom_404(request, template_name='404.html'):
    """Our custom 404 view

    :param template_name: The template to render
    :type template_name: str

    :return: Response obj
    :rtype: HttpResponse

    """
    response = render_to_response(
        template_name, {
            'request_path': request.path,},
        context_instance=RequestContext(request))
    response.status_code = 404
    return response
