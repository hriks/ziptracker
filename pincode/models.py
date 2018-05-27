# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pincode.exceptions import PincodeExistsException
from django.db import models
import uuid

# Create your models here.


class Pincode(models.Model):
    """Records Guest details"""
    id = models.UUIDField(default=uuid.uuid4, editable=False)
    pincode = models.CharField(primary_key=True, max_length=128)
    state = models.CharField(max_length=128)
    distict = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    post_office = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        pincodes = Pincode.objects.filter(pincode=self.pincode)
        if pincodes.exists():
            raise PincodeExistsException(
                "Cannot chanage pincode that already Exists : %s" % self.pincode
            )
        super(Pincode, self).save(*args, **kwargs)

    def getCity(self):
        return self.city

    def getDistict(self):
        return self.distict

    def getState(self):
        return self.state

    def getBranch(self):
        return self.post_office_branch


class APIRequest(models.Model):
    """ Stores the API details for every pincode Query
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pincode = models.ForeignKey('Pincode', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    is_ajax = models.BooleanField(default=False)
    ip_address = models.CharField(max_length=16)
    query = models.CharField(max_length=32)
    method = models.CharField(max_length=8)
    request = models.TextField()

    def save(self, *args, **kwargs):
        try:
            pincode = Pincode.objects.get(pincode=self.query)
            self.pincode = pincode
        except Pincode.DoesNotExists:
            self.query += ' | Query pincode not found!'
        super(APIRequest, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s: %s | %s" % (self.ip_address, self.request, self.created)

    @classmethod
    def entry(cls, *args, **kwargs):
        return cls.objects.create(*args, **kwargs)

    def getIPAddress(self, request):
        return
