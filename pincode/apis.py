from pincode.serializers import PincodeSerializer
from rest_framework import generics

from pincode.models import Pincode


class GetPincode(generics.ListAPIView):
    serializer_class = PincodeSerializer
    queryset = Pincode.objects.all()
