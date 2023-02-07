from rest_framework import serializers
from eckard_api.models.listing import Listing
from eckard_api.models.listing_type import ListingType
from eckard_api.models.status import Status
from eckard_api.models.account import Account
from eckard_api.models.project import Project
from eckard_api.models.constraint import Constraint
from eckard_api.models.offer import Offer
from .constraint import ConstraintSerializer
from .status import StatusSerializer
from .listing_type import ListingTypeSerializer
from .account import AccountGetSerializer
from .project import ProjectGetSerializer
from .offer import OfferGetSerializer
from .auction_type import AuctionTypeSerializer

    
class ListingGetSerializer(serializers.ModelSerializer):
  listing_type = ListingTypeSerializer()
  status = StatusSerializer()
  account = AccountGetSerializer()
  project = ProjectGetSerializer()
  auction_type=AuctionTypeSerializer()
  constraints = ConstraintSerializer(many=True, read_only=True)
  offer = OfferGetSerializer(many=True, read_only=True)

  class Meta:
    model = Listing
    fields = (
      'id', 'listing_type', 'status', 'listingName', 'listingStart', 'auction_type',
      'auctionEnd', 'comments', 'account', 'project', 'nma',
      'minimumAsk', 'buyNowPrice', 'directSaleToken', 'constraints', 'offer'
    )
    

class ListingPostSerializer(serializers.ModelSerializer):
  listing_type = serializers.PrimaryKeyRelatedField(queryset=ListingType.objects.all())
  status = serializers.PrimaryKeyRelatedField(queryset=Status.objects.all())
  account = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all())
  project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all(), required=False)
  constraints = serializers.PrimaryKeyRelatedField(many=True, queryset=Constraint.objects.all(), required=False)
  offer = serializers.PrimaryKeyRelatedField(many=True, queryset=Offer.objects.all(), required=False)

  class Meta:
    model = Listing
    fields = (
      'id', 'listing_type', 'status', 'listingName', 'listingStart', 'auction_type',
      'auctionEnd', 'comments', 'account', 'project', 'nma',
      'minimumAsk', 'buyNowPrice', 'directSaleToken', 'constraints', 'offer'
    )
    extra_kwargs = {
      'comments': {'allow_null': True}, 'nma': {'allow_null': True},
      'minimumAsk': {'allow_null': True}, 'buyNowPrice': {'allow_null': True},
      'directSaleToken': {'allow_null': True}
    }
