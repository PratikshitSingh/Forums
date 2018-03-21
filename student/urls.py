from django.conf.urls import url
from . import views
from django.contrib import admin

app_name = 'student'

urlpatterns = [
    url(r'^notifications/(?P<pk>[0-9]+)/$', views.notify, name='notify'),
    url('^addfile/$', views.AddfileView.as_view(), name='addfile'),
    ]