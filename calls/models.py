from django.db import models
from model_utils.models import TimeStampedModel
from appointments.models import Appointment as a

# Create your models here.

# example:   vet adds medicine to basket (receiver) from inside consultation (caller)


class Object(TimeStampedModel):
    name = models.CharField(max_length=50)
    object_id = models.IntegerField(unique=True)
    object_code = models.CharField(max_length=30)
    def __str__(self):
        return self.name


class Call(TimeStampedModel):
    # Example: 1001 for "Counter Sale" or 1005 "Estimate"
    caller_id = models.IntegerField()
    caller_type = models.ForeignKey(Object, to_field='object_id', related_name='caller_type_object_fk')
    receiver_id = models.IntegerField()
    receiver_type = models.ForeignKey(Object, to_field='object_id', related_name='receiver_type_object_fk')

    def __str__(self):
        ret = "{0} ({1}) [{4}] >> {2} ({3}) [{5}]".format(self.caller_type.name,self.caller_id,self.receiver_type.name,self.receiver_id, self.caller_type.object_id, self.receiver_type.object_id   )
        return str(ret)
