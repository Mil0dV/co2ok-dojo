from django.contrib.auth.models import User
from django.db import models

# class Profil(models.Model):
#     user = models.OneToOneField(User)
#     points = models.IntegerField()
#     uniq_link = models.CharField()
#
#
#     def __str__(self):
#         return self.user.username


class Rewards(models.Model):
    user_id = models.IntegerField()
    points = models.IntegerField(default = 0)

    # def __str__(self):
    #     return self.username
