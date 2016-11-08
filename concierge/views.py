# -*- coding: utf-8 -

from __future__ import unicode_literals, division, absolute_import

from django.conf import settings
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views import generic

from . import forms


class SignupView(generic.FormView):
    form_class = forms.SignupForm
    success_url = reverse_lazy(settings.LOGIN_REDIRECT_URL)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super(SignupView, self).form_valid(form)
