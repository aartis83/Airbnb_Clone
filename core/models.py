from django.db import models
from . import managers


class TimeStampedModel(models.Model):

    """Create a Time Stamp Model common to all the models"""

    # auto_now_add, the time when the model is created.
    # auto_now, the time when the model is updated
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = managers.CustomModelManager()

    class Meta:
        abstract = True
