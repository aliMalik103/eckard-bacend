from rest_framework import serializers
from eckard_api.models.key_value import KeyValue


class KeyValueGetSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = KeyValue
    fields = ('id', 'key', 'value1', 'value2')
