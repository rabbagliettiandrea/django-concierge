# -*- coding: utf-8 -

from __future__ import unicode_literals, division, absolute_import

from django.contrib.auth.base_user import BaseUserManager
from django.db import models as db_models
from django.contrib.auth import models as auth_models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class AbstractUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    objects = UserManager()
    USERNAME_FIELD = 'email'

    email = db_models.EmailField(unique=True)
    date_joined = db_models.DateTimeField(_('date joined'), default=timezone.now)
    is_staff = db_models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = db_models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    class Meta:
        abstract = True

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email


class User(AbstractUser):
    pass
