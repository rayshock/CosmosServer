"""
Definition of models.
"""

from django.db import models
from django.utils import timezone

# Create your models here.

class GameUser(models.Model):
        last_date = models.DateTimeField(
            default=timezone.now)
        coin = models.IntegerField()