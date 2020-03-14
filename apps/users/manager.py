from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class UserManager(BaseUserManager):
    def base_create_user(self, email, first_name, last_name, password,
        is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError("Email is required field")
        if not first_name:
            raise ValueError("First anem is required field")
        if not last_name:
            raise ValueError("Last name is required field")
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_login=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_normaluser(self, email, first_name, last_name, password, **extra_fields):
        return self.base_create_user(email, first_name, last_name, password, False, False, **extra_fields)

    def create_superuser(self, email, first_name, last_name, password, **extra_fields):
        user = self.base_create_user(email, first_name, last_name, password, True, True, **extra_fields)
        user.save(using=self._db)
        return user
    