"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.db import models
from seed.models.model import Model

class Contact(Model):

    business = models.CharField(max_length=255, blank=True)
    comment = models.CharField(max_length=255, blank=True)
    lastname = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    position = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)

    user = models.ForeignKey(
        'models.User', related_name='contacts',
        blank=False, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = '_contact'
        app_label = 'models'