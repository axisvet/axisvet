from django.db import models
from model_utils.models import TimeStampedModel


# Create your models here.

# example:   vet adds medicine to basket (receiver) from inside consultation (caller)


class Object(TimeStampedModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return 'name'


class Call(TimeStampedModel):
    # Example: 1001 for "Counter Sale" or 1005 "Estimate"
    caller_id = models.IntegerField()
    caller_type = models.ForeignKey(Object, related_name='caller_type_object_fk')
    receiver_id = models.IntegerField()
    receiver_type = models.ForeignKey(Object, related_name='receiver_type_object_fk')

    def __str__(self):
        return 'call'
