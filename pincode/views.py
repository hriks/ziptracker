# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from pincode.models import pincodes

import json

# Create your views here.


def post(
        f, methods={"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0}):
    def wrap(request, *args, **kwargs):
        if request.method != 'POST':
            return bad_request(request)
        return f(request, *args, **kwargs)
    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap


def bad_request():
    return JsonResponse({'Invalid': 'bad_request'}, status=403)


class GetPincodeObject(object):
    """docstring for GetPincodeObjects="""
    def getPincodeDetails(self):
        if self.pincode:
            self.city = pincodes.getCity(self.pincode)
            self.distict = pincodes.getDistict(self.pincode)
            self.state = pincodes.getDistict(self.pincode)
        return self

    def __init__(self, request):
        self.pincode = request.POST.get('picode', '')
        self.city = request.POST.get('city', None)
        self.state = request.POST.get('state', None)
        self.distict = request.POST.get('distict', None)


def jsonParser(ziptracker):
    json_data = {
        'pincode': ziptracker.pincode,
        'city': ziptracker.city,
        'state': ziptracker.state,
        'distict': ziptracker.distict
    }
    return json.dump(json_data)


@csrf_exempt
@post
def ziptracker(request):
    ziptracker = GetPincodeObject(request)
    return jsonParser(ziptracker)
