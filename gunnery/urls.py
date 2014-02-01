from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('core.urls')),
    url(r'^', include('task.urls')),
    url(r'^', include('account.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)