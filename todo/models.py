from django.db import models
from common.abstract_model import AbstractModel

# Create your models here.
class Todo(AbstractModel):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=200)

    STATUS_TYPE = [
        ('COMPLETED','COMPLETED'),
        ('INCOMPLETE','INCOMPLETE'),
    ]
    status = models.CharField(
        max_length=10,
        default='INCOMPLETE',
        choices=STATUS_TYPE,
        )
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table = 'todo'
    
    
