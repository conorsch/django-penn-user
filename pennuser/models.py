from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from .validators import validate_pennname, validate_pennid


class PennUserManager(BaseUserManager):
    """
    Custom user manager for PennUser class.
    """

    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have a PennKey')

        user = self.model(username=username)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username, password=password)
        user.is_staff = True
        # Django 1.7 docs don't mention "is_admin" privilege,
        # but let's support it anyway.
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class PennUser(PermissionsMixin, AbstractBaseUser):
    """
    Custom user model for Penn people. Requires valid PennKey for login.
    This model should be used with RemoteUserBackend and Apache mod_cosign.
    """

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=8, unique=True, validators=[validate_pennname])
    pennid = models.CharField(max_length=8, unique=True, validators=[validate_pennid])
    full_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(
        max_length=255,
        blank=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = PennUserManager()

    USERNAME_FIELD = 'username'

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.full_name

    def __str__(self):
        return self.username

