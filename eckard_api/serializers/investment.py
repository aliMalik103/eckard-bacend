from rest_framework import serializers
from eckard_api.models.investment import Investment
from eckard_api.models.account import Account
from eckard_api.models.project import Project
from .account import AccountGetSerializer, AccountPostSerializer
from .project import ProjectGetSerializer


class InvestmentGetSerializer(serializers.ModelSerializer):
  account = AccountGetSerializer()
  project = ProjectGetSerializer()

  class Meta:
    model = Investment
    fields = ('id', 'account', 'project', 'investmentAmount', 'acquiredNma', 'status')


class InvestmentPostSerializer(serializers.ModelSerializer):
  account = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all())
  project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
  
  class Meta:
    model = Investment
    fields = ('id', 'account', 'project', 'investmentAmount', 'acquiredNma', 'status')

