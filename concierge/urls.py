# -*- coding: utf-8 -

from django.conf.urls import url

from django.contrib.auth import views as django_auth_views

from . import forms
from . import views

urlpatterns = [
    url(r'^signup/$', views.SignupView.as_view(template_name='concierge/signup.html'), name='signup'),
    url(r'^login/$', django_auth_views.login,
        {'authentication_form': forms.LoginForm, 'template_name': 'concierge/login.html'}, name='login'),
    url(r'^logout/$', views.LogoutView.as_view(template_name='concierge/logout.html'), name='logout'),
    url(r'^password_change/$', django_auth_views.password_change, name='password_change'),
    url(r'^password_change/done/$', django_auth_views.password_change_done, name='password_change_done'),
    url(r'^password_reset/$', django_auth_views.password_reset,
        kwargs={
            'template_name': 'concierge/password_reset_form.html',
            'post_reset_redirect': 'concierge:password_reset_done',
            'email_template_name': 'concierge/password_reset_email.html'
        }, name='password_reset'),
    url(r'^password_reset/done/$', django_auth_views.password_reset_done,
        kwargs={
            'template_name': 'concierge/password_reset_done.html',
        },
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        django_auth_views.password_reset_confirm,
        kwargs={
            'template_name': 'concierge/password_reset_confirm.html',
            'post_reset_redirect': 'concierge:password_reset_complete'
        }, name='password_reset_confirm'),
    url(r'^reset/done/$', django_auth_views.password_reset_complete,
        kwargs={
            'template_name': 'concierge/password_reset_complete.html'
        }, name='password_reset_complete'),
]
