# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid

# Create your models here.


class Pincode(models.Model):
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

class APIRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pincode = models.ForeignKey('Pincode', null=True, blank=True)
    query = models.CharField(max_length=32)
    ip = models.CharField(max_length=16)
    request = models.TextField()
    method = models.CharField(max_length=8)
    is_ajax = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        try:
            pincode = Pincode.objects.get(pincode=self.query)
            self.pincode = pincode
        except Pincode.DoesNotExists:
            self.query += ' | Query pincode not found!'
        super(APIRequest, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s: %s | %s" % (self.ip, self.request, self.created)
        