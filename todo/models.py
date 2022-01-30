from django.db import models
from common.abstract_model import AbstractModel
from common.status_enum import StatusType


# Create your models here.
class Todo(AbstractModel):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    status = models.CharField(
        max_length=10,
        default=StatusType.INCOMPLETE,
        choices=[(tag,tag.value) for tag in StatusType]
        )

    def __str__(self) -> str:
        return self.title
