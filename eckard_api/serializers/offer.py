from rest_framework import serializers
from eckard_api.models.offer import Offer
from eckard_api.models.status import Status
from eckard_api.models.contact import Contact
from eckard_api.models.constraint import Constraint
from .constraint import ConstraintSerializer
from .status import StatusSerializer
from .contact import ContactSerializer
from django.utils.crypto import get_random_string

class OfferGetSerializer(serializers.ModelSerializer):
  status = StatusSerializer()
  contact = ContactSerializer()
  constraints = ConstraintSerializer(many=True, read_only=True)
  mpName = serializers.SerializerMethodField()

  class Meta:
    model = Offer
    fields = ('id', 'status', 'offerAmount', 'constraints', 'contact', 'comments', 'mpName')
    
  
  def get_mpName(self, model):
    return 'MPX-' + get_random_string(length=3).upper(),
    
class OfferPostSerializer(serializers.ModelSerializer):
  status = serializers.PrimaryKeyRelatedField(queryset=Status.objects.all())
  contact = serializers.PrimaryKeyRelatedField(queryset=Contact.objects.all(), required=False)
  constraints = serializers.PrimaryKeyRelatedField(many=True, queryset=Constraint.objects.all(), required=False)

  class Meta:
    model = Offer
    fields = ('id', 'status', 'offerAmount', 'constraints', 'contact', 'comments')
    extra_kwargs = {'comments': {'allow_null': True}}

