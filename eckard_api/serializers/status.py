from rest_framework import serializers
from eckard_api.models.status import Status


class StatusSerializer(serializers.ModelSerializer):
  class Meta:
    model = Status
    fields = ['id', 'status', 'stage', 'explanation','statusLabel']
    extra_kwargs = {'explanation': {'allow_null': True} }

