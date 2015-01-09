from django.contrib.auth.backends import RemoteUserBackend
from django.contrib.auth import get_user_model


class PennUserModelBackend(RemoteUserBackend):
    def authenticate(self, remote_user):
        """Cosign will handle password, we just need REMOTE_USER set."""
        if not remote_user:
            return
        user = None
        user_model = get_user_model()
        username = self.clean_username(remote_user)

        if self.create_unknown_user:
            user, created = user_model.objects.get_or_create(username=username)
            if created:
                user = self.configure_user(user)
        else:
            try:
                user = user_model.objects.get(username=username)
            except self.user_model.DoesNotExist:
                pass
        return user
