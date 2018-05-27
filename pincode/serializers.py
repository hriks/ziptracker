from pincode.models import Pincode
from rest_framework import serializers


class PincodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pincode
        fields = ('pincode', 'state', 'distict', 'city', 'post_office')
