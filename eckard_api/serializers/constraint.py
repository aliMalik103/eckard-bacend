from rest_framework import serializers
from eckard_api.models.constraint import Constraint


class ConstraintSerializer(serializers.ModelSerializer):
  class Meta:
    model = Constraint
    fields = ('id', 'constraint','constraintLabel','constraintType')

