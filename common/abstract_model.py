from turtle import update
from django.db import models
from django.utils import timezone
from uuid import uuid4

class AbstractModel(models.Model):
    """
    An Abstract Model For All Models
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    createdAt = models.DateTimeField(default = timezone.now())

    updateAt = models.DateTimeField(default = timezone.now())

    class Meta:
        abstract = True