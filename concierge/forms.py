# -*- coding: utf-8 -

from __future__ import unicode_literals, division, absolute_import

from django.contrib.auth import forms as auth_forms
from django import forms
from django.utils.translation import ugettext_lazy as _

from . import models


class SignupForm(auth_forms.UserCreationForm):
    agreement = forms.BooleanField(
        required=True, initial=True, label=_('Agree the terms and policy'), disabled=True
    )

    class Meta:
        model = models.User
        fields = ['email']

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.username = user.email
        if commit:
            user.save()
        return user


class LoginForm(auth_forms.AuthenticationForm):
    pass
