
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from zipcodeSearcher.zipcode.views import AddressViewSet

router = routers.DefaultRouter()
router.register('address', AddressViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
