from rest_framework import serializers
from eckard_api.models.account import Account
from eckard_api.models.contact import Contact
from .contact import ContactSerializer


class AccountGetSerializer(serializers.ModelSerializer):
  contact = ContactSerializer()
  class Meta:
    model = Account
    fields = ('id', 'accountId', 'accountName', 'notes', 'accountStatus', 'mpName', 'contact')

   
class AccountPostSerializer(serializers.ModelSerializer):
  contact = serializers.PrimaryKeyRelatedField(queryset=Contact.objects.all())

  class Meta:
    model = Account
    fields = ('id', 'accountId', 'accountName', 'notes', 'accountStatus', 'mpName', 'contact')
    extra_kwargs = {'notes': {'allow_null': True}}

