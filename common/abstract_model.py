from turtle import update
from django.db import models
from django.utils import timezone

class AbstractModel(models.Model):
    """
    An Abstract Model For All Models
    """
    id = models.AutoField(primary_key=True)

    createdAt = models.DateTimeField(default = timezone.now())

    updateAt = models.DateTimeField(default = timezone.now())

    class Meta:
        abstract = True