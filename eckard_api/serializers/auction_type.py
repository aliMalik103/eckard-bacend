from rest_framework import serializers
from eckard_api.models.auction_type import AuctionType


class AuctionTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = AuctionType
    fields = ('id', 'auctionType',"auctionLabel")

