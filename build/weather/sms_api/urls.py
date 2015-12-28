from django.conf.urls import url
from weather.sms_api import views
from django.conf.urls import patterns, include, url

urlpatterns = [
    url(r'^$', views.smsapi_list),
    url(r'^(?P<service>[^/]+)/(?P<city>[^/]+)/$',views.smsapi_detail),
]