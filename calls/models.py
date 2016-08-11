from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

class CallLog(models.Model):
    # first generic relation
    #appointment
    caller_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="caller_type")
    caller_id = models.PositiveIntegerField(blank=True, null=True)
    caller_object = GenericForeignKey("caller_type", "caller_id")

    # second generic relation
    #consultation
    receiver_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="receiver_type")
    receiver_id = models.PositiveIntegerField(blank=True, null=True)
    receiver_object = GenericForeignKey("receiver_type", "receiver_id")

    def __str__(self):
        ret = "{0} {1} > {2} {3} ".format(self.caller_id, self.caller_type, self.receiver_id, self.receiver_type)
        return str(ret)