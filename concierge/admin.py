# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import

from django.contrib import admin
from django.contrib.admin import register
from django.contrib.auth import admin as auth_admin, models as auth_models
from django.contrib.auth.forms import UserChangeForm, AdminPasswordChangeForm
from django.utils.translation import ugettext_lazy as _

from . import models

from . import forms

admin.site.unregister(auth_models.Group)


@register(models.User)
class UserAdmin(auth_admin.UserAdmin):
    ordering = ['email']
    list_display = ['email', 'is_staff', 'is_active']
    fieldsets = [
        (None, {'fields': ('email', 'password')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    ]
    add_fieldsets = [
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    ]
    add_form = forms.SignupForm
    form = UserChangeForm
    change_password_form = AdminPasswordChangeForm
    list_filter = ['is_staff', 'is_superuser', 'is_active']
    search_fields = ['email']
    filter_horizontal = ['user_permissions']
