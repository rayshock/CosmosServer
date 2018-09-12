"""
Definition of models.
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

class GameUser(AbstractUser):
        last_date = models.DateTimeField(
            default=timezone.now)
        coin = models.IntegerField( default = 0)