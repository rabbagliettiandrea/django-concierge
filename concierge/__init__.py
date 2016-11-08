# -*- coding: utf-8 -

from django.conf import settings

settings.AUTH_USER_MODEL = 'concierge.User'
settings.LOGIN_URL = 'concierge:login'
settings.LOGIN_REDIRECT_URL = '/'
settings.LOGOUT_REDIRECT_URL = '/'
