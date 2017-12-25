import sys
from pincode.models import Pincode
import csv
print sys.argv
input_file = csv.DictReader(open(sys.argv[1]))
data = []
for row in input_file:
    data.append(row)

for row in data:
    pincode = row['pincode']
    distict = row['districtname']
    city = row['taluk']
    state = row['statename']
    pincode, created = Pincode.objects.get_or_create(
        pincode=pincode, state=state, distict=distict,
        city=city)
    if not created:
        print pincode
    print created
