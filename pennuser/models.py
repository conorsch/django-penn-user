from django.db import models
from django.contrib.auth.models import User, UserManager


class PennUser(User):
    penn_id = models.IntegerField()
    join_date = models.DateField()
    last_login_date = models.DateField()
    login_count = models.IntegerField()
    # put additional properties here

    objects = UserManager()

# other models...
