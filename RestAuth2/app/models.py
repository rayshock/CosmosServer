"""
Definition of models.
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
# Create your models here.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Unit(models.Model):
    kingdom = models.IntegerField(default = 0)
    name = models.CharField(max_length=32, default = "")
    energy = models.IntegerField(default = 100)
        

class Cx(models.Model):
    name = models.CharField(max_length=32, default = "")
     


class GameUser(AbstractUser):

    cxs = models.ManyToManyField(Cx)
    units = models.ManyToManyField(Unit)
    curCx_id = models.IntegerField(default = 0)
    curUnit_id = models.IntegerField(default = 0)

    last_date = models.DateTimeField(default=timezone.now)
    coin = models.IntegerField(default = 0)

    isNewPlayer = models.BooleanField(default = True)



