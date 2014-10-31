from django.db import models
from django.contrib.auth.models import User, UserManager


class PennUser(User):
    penn_id = models.IntegerField()
    join_date = models.DateField(default=datetime.now)
    last_login_date = models.DateField()
    login_count = models.IntegerField(default=0)
    # put additional properties here

    objects = UserManager()

# other models...
