from rest_framework import viewsets
from rest_framework.exceptions import ParseError

from zipcodeSearcher.zipcode.serializer import AddressSerializer
from zipcodeSearcher.zipcode.models import Address


class AddressViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        zipcode = self.request.query_params.get('zipcode', None)
        if zipcode:
            zipcode = zipcode.replace('-', '')
            queryset = Address.objects.filter(zipcode=zipcode)
        else:
            raise ParseError('zipcodeが指定されていません')
        return queryset