# -*- coding: utf-8 -

from django.conf.urls import url

from django.contrib.auth import views as django_auth_views

from . import forms
from . import views

urlpatterns = [
    url(r'^signup/$', views.SignupView.as_view(template_name='concierge/signup.html'), name='signup'),
    url(r'^login/$', django_auth_views.login,
        {'authentication_form': forms.LoginForm, 'template_name': 'concierge/login.html'}, name='login'),
    url(r'^logout/$', django_auth_views.logout, name='logout'),
    url(r'^password_change/$', django_auth_views.password_change, name='password_change'),
    url(r'^password_change/done/$', django_auth_views.password_change_done, name='password_change_done'),
    url(r'^password_reset/$', django_auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', django_auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        django_auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', django_auth_views.password_reset_complete, name='password_reset_complete'),
]
