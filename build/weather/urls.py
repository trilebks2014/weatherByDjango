"""weather URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('weather',
    url(r'^$','core.views.home',name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signin/$', 'authentication.views.signin', name='signin'),
    url(r'^signup/$','authentication.views.signup',name='signup'),
    url(r'^signout/$','authentication.views.signout',name='signout'),
    url(r'^reset/$', 'authentication.views.reset', name='reset'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 'authentication.views.reset_confirm', name='password_reset_confirm'),
    url(r'^success/$','authentication.views.success',name='success'),
    url(r'^about/$','about.views.home',name='about'),
    url(r'^sms-api/',include('weather.sms_api.urls',namespace='smsApi')), 
    url(r'^graph/$','graph.views.graph',name='graph'),
    url(r'^(?P<username>[^/]+)/thanks/$', 'core.views.thanksregister', name='thanksregister'),
    url(r'^(?P<username>[^/]+)/$', 'reviews.views.reviews', name='reviews'),
    url(r'^settings/', include('weather.account_settings.urls', namespace="settings")),

    )