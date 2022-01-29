from re import M
from django.db import models
from ..common.Modals import AbstractModel

# Create your models here.
class Todo(AbstractModel):

    def __init__(self) -> None:
        super().__init__('title')

    title = models.fields.CharField(max_length=50)
    description = models.fields.CharField()
    status = models.CharField(default='INCOMPLETE')

    