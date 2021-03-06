from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    points = models.IntegerField()
    ninja_user = models.BooleanField(default=False)
    user_picked_project = models.IntegerField()



    def __str__(self):
        return self.user.email
