# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid

# Create your models here.


class Pincodes(models.Model):
    """Records Guest details"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pincode = models.CharField(max_length=128)
    state = models.CharField(max_length=128, blank=True)
    distict = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=128, blank=True)

    def getCity(self):
        return self.city

    def getDistict(self):
        return self.distict

    def getState(self):
        return self.state
