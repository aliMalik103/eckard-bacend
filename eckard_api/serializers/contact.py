from rest_framework import serializers
from eckard_api.models.contact import Contact


class ContactSerializer(serializers.ModelSerializer):
  class Meta:
    model = Contact
    fields = ('id', 'firstName', 'lastName', 'email', 'mpStatus')

