# coding=utf-8
"""Project level url handler."""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.http import HttpResponseServerError
from django.template import loader, Context
from django.conf.urls.static import static

admin.autodiscover()
handler404 = 'base.views.error_views.custom_404'


def handler500(request):
    """500 error handler which includes ``request`` in the context.

    See http://raven.readthedocs.org/en/latest/integrations/
        django.html#message-references

    :param request: Django request object.

    Templates: `500.html`
    Context: None
    """
    # You need to create a 500.html template.
    t = loader.get_template('500.html')
    return HttpResponseServerError(t.render(Context({
        'request': request,
    })))

urlpatterns = [
    #url(r'^site-admin/', include(admin.site.urls)),
    url(r'^', include('base.urls')),
    #url(r'^grappelli/', include('grappelli.urls')),
    #url(r'^accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    pass
    #urlpatterns.append(
    #    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
    # urlpatterns.append(
    #     static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # )




