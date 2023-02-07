from rest_framework import serializers
from eckard_api.models.tract import Tract


class TractSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tract
    fields = [
      'id', 'tractId', 'township', 'range', 'section', 'country', 'state', 'royalityInterest', 'costPerNma',
      'totalNma'
    ]

