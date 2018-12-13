from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    points = models.IntegerField()
    ninja_user = models.BooleanField(default=False)



    def __str__(self):
        return self.user.email


# class Rewards(models.Model):
#     user_id = models.IntegerField()
#     points = models.IntegerField(default = 0)
#
#     # def __str__(self):
#     #     return self.username
