from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from eckard_api.models.key_value import KeyValue
from eckard_api.serializers.key_value import KeyValueGetSerializer

class KeyConfigView(APIView):
  def get(self, request):
    key_value = KeyValue.objects.all()
    if key_value:
      response = KeyValueGetSerializer(key_value, many=True)
      return Response(response.data)
    
    else:
      return Response([], status=status.HTTP_200_OK)


 