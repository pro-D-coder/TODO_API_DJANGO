from sre_constants import ANY
from django.db import models
from django.utils import timezone

class AbstractModel(models.Model):
    """
    An Abstract Model Which Can Be Reused Every Where
    """
    _humanName = None
    id = models.AutoField(primary_key=True)
    createdAt = models.DateTimeField(default = timezone.now())
    updatedAt = models.DateTimeField(default= timezone.now())

    def __init__(self, *args, **kwargs) -> None:
        super().__init__()
        self._humanName = args[0]

    def __str__(self) -> str:
        return self._humanName
