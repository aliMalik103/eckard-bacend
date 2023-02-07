from rest_framework import serializers
from eckard_api.models.listing_type import ListingType


class ListingTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = ListingType
    fields = ('id', 'listingType','listingTypeLabel')


