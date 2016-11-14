# -*- coding: utf-8 -

from __future__ import unicode_literals, division, absolute_import

import django.dispatch
from django.contrib.auth.signals import user_logged_in, user_logged_out


login = user_logged_in
logout = user_logged_out
signup = django.dispatch.Signal(providing_args=['request', 'user'])
