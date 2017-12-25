# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from pincode.models import Pincodes

import json

# Create your views here.


def post(
        f, methods={"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0}):
    def wrap(request, *args, **kwargs):
        if request.method != 'POST':
            return bad_request()
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
            try:
                pincode = Pincodes.objects.get(pincode=self.pincode)
            except Pincodes.DoesNotExist:
                return {'Error': str(self.pincode) + " NOT FOUND!"}
            self.city = pincode.getCity()
            self.distict = pincode.getDistict()
            self.state = pincode.getDistict()
        return self

    def __init__(self, request):
        self.pincode = request.POST.get('pincode', '')
        self.city = request.POST.get('city', None)
        self.state = request.POST.get('state', None)
        self.distict = request.POST.get('distict', None)


def jsonParser(ziptracker):
    self = ziptracker.getPincodeDetails()
    try:
        return json.dumps({
            'pincode': self.pincode,
            'city': self.city,
            'state': self.state,
            'distict': self.distict
        }), 200
    except Exception:
        return self, 403


@csrf_exempt
@post
def ziptracker(request):
    ziptracker = GetPincodeObject(request)
    respose, status = jsonParser(ziptracker)
    return JsonResponse(
        {'STATE': respose}, status=status)


def update(filename):
    from pincode.models import Pincodes
    import csv
    input_file = csv.DictReader(open(filename))
    data = []
    for row in input_file:
        data.append(row)
    counter = 0
    updated = 0
    for row in data:
        pincode, created = Pincodes.objects.get_or_create(
            pincode=row['pincode'])
        fields = [
            ('state', row['statename']),
            ('distict', row['districtname']),
            ('city', row['taluk'])
        ]
        for field, value in fields:
            setattr(pincode, field, value)
        pincode.save()
        if not created:
            updated += 1
        else:
            counter += 1
        if created and counter % 100 is 0:
            print str(counter) + ' records created inside database till now!'  # noqa
        elif updated % 100 is 0:
            print str(updated) + ' Successfully updated till now!'

    return (
        str(counter) + ' Successfully records created inside database',
        str(updated) + ' Successfully updated!'
    )
