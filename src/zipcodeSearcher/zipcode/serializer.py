from rest_framework import serializers, viewsets

from zipcodeSearcher.zipcode.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

