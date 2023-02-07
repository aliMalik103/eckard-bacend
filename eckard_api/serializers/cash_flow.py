from rest_framework import serializers
from eckard_api.models.project import Project
from eckard_api.models.account import Account
from eckard_api.models.cash_flow import CashFlow
from .account import AccountGetSerializer
from .project import ProjectGetSerializer


class CashFlowGetSerializer(serializers.ModelSerializer):
  project = ProjectGetSerializer()
  account = AccountGetSerializer()

  class Meta:
    model = CashFlow
    fields = ('id', 'project', 'account', 'paidDate', 'income', 'noOfMonths', 'decline', 'oilPrice', 'gasPrice')
    
    
class CashFlowPostSerializer(serializers.ModelSerializer):
  project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
  account = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all())

  class Meta:
    model = CashFlow
    fields = ('id', 'project', 'account', 'paidDate', 'income', 'noOfMonths', 'decline', 'oilPrice', 'gasPrice')
    extra_kwargs = {
      'paidDate': {'allow_null': True}, 'income': {'allow_null': True}, 'noOfMonths': {'allow_null': True},
      'decline': {'allow_null': True}, 'oilPrice': {'allow_null': True}, 'gasPrice': {'allow_null': True}
    }

