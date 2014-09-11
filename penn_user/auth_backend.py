from django.conf import settings
from django.contrib.auth.backends import RemoteUserBackend
from django.core.exceptions import ImproperlyConfigured
from django.db.models import get_model

class PennUserModelBackend(RemoteUserBackend):
    def authenticate(self, remote_user):
        """
        Attempts to authenticate a user against CoSign.
        If successful, handles both logging in the user, and creating the user's
        account if this is their first time logging in.
        """

        if not remote_user:
            return
        user = None
        username = self.clean_username(remote_user)

        if self.create_unknown_user:
            user, created = self.user_class.objects.get_or_create(username=username)
            if created:
                user = self.configure_user(user)
        else:
            try:
                user = self.user_class.objects.get(username=username)
            except self.user_class.DoesNotExist:
                pass
        return user


    @property
    def user_class(self):
        if not hasattr(self, '_user_class'):
            self._user_class = get_model(*settings.CUSTOM_USER_MODEL.split('.', 2))
            if not self._user_class:
                raise ImproperlyConfigured('Could not get custom user model.')
        return self._user_class
