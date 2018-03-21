from django.conf.urls import url
from . import views
from django.contrib import admin

app_name = 'student'

urlpatterns = [
    url(r'^notifications/$', views.notify, name='notify'),
    url('^addfile/$', views.AddfileView.as_view(), name='addfile'),
    ]