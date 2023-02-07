from rest_framework import serializers
from eckard_api.models.offer import Offer
from eckard_api.models.listing_offer import ListingOffer
from eckard_api.models.listing import Listing
from .offer import OfferGetSerializer
from .listing import ListingGetSerializer
from .offer import OfferPostSerializer

class ListingOfferGetSerializer(serializers.ModelSerializer):
  offer = OfferGetSerializer()
  listing = ListingGetSerializer()

  class Meta:
    model = ListingOffer
    fields = ('id', 'offer', 'listing', 'acceptedOffer')
    
    
class ListingOfferPostSerializer(serializers.ModelSerializer):
  offer = serializers.PrimaryKeyRelatedField(queryset=Offer.objects.all())
  listing = serializers.PrimaryKeyRelatedField(queryset=Listing.objects.all(), required=False)

  class Meta:
    model = ListingOffer
    fields = ('id', 'offer', 'listing', 'acceptedOffer')
    extra_kwargs = {'acceptedOffer': {'allow_null': True}}
  
