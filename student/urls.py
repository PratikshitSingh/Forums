from django.conf.urls import url
from . import views
from django.contrib import admin

app_name = 'student'

urlpatterns = [
    url(r'^registration/$', views.reg.as_view(), name='reg'),
    url(r'^profile_(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='prof'),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^notifications/$', views.notify, name='notify'),
    url('^addfile/$', views.AddfileView.as_view(), name='addfile'),
    ]