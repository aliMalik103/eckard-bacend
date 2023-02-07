from rest_framework import serializers
from eckard_api.models.project import Project

class ProjectGetSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields = ('id', 'projectId', 'totalNma', 'totalRevenue')
    extra_kwargs = {
      'totalNma': {'allow_null': True}, 'totalRevenue': {'allow_null': True}
    }


class ProjectPostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields = ('id', 'projectId', 'totalNma', 'totalRevenue')
    extra_kwargs = {
      'totalNma': {'allow_null': True}, 'totalRevenue': {'allow_null': True}
    }
