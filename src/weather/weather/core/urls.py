from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin
urlpatterns = patterns('core',
      url(r'^(?P<username>[^/]+)/thanks/$', 'core.views.thanksregister', name='thanksregister'), 
)