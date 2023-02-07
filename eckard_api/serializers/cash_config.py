from rest_framework import serializers
from eckard_api.models.cashcalculator import CashCalculator
from eckard_api.models.account import Account
from eckard_api.models.project import Project
from eckard_api.models.contact import Contact
from .contact import ContactSerializer


class CashConfigGetSerializer(serializers.ModelSerializer):
  contact = ContactSerializer()

  class Meta:
    model = CashCalculator
    fields = ('id', 'contact', 'noOfMonths', 'decline', 'gasPrice','oilPrice')


class CashConfigPostSerializer(serializers.ModelSerializer):
  contact = serializers.PrimaryKeyRelatedField(queryset=Contact.objects.all())
  
  class Meta:
    model = CashCalculator
    fields = ('id','contact', 'noOfMonths', 'decline', 'gasPrice','oilPrice')

