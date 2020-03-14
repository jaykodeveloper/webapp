from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .manager import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name=_('email address'), max_length=255, unique=True)
    first_name = models.CharField(_('first name'), max_length=255, null=False, blank=False)
    last_name = models.CharField(_('last name'), max_length=255, null=False, blank=False)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_superuser = models.BooleanField(_('superuser status'), default=False)
    is_active = models.BooleanField(_('active status'), default=True)
    last_login = models.DateTimeField(_('last login'), null=True, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)

    object = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'.strip()

    def __str__(self):
        return f'{self.get_full_name()} {self.email}'

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True
    
    def has_module_perm(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True