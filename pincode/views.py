# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def update(filename):
    from pincode.models import Pincode
    import csv
    input_file = csv.DictReader(open(filename))
    data = []
    for row in input_file:
        data.append(row)
    counter = 0
    updated = 0
    for row in data:
        pincode, created = Pincode.objects.get_or_create(
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
