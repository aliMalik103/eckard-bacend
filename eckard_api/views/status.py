from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from eckard_api.models.status import Status
from eckard_api.serializers.status import StatusSerializer

  
class StatusList(APIView):
  def get(self, request):
    status = Status.objects.all()
    if status:
      response = StatusSerializer(status, many=True)
      return Response(response.data)
    
    else:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)


  def post(self, request):
    serializer = StatusSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StatusDetail(APIView):
  def get(self, request, pk):
    try:
      status = Status.objects.get(pk=pk)
      serializer = StatusSerializer(status)
      return Response(serializer.data)
    
    except Status.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
      
      
  def put(self, request, pk):
    try:
      status = Status.objects.get(pk=pk)
    except Status.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = StatusSerializer(status, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  def patch(self, request, pk, format=None):
    try:
      status = Status.objects.get(pk=pk)
    except Status.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = StatusSerializer(status, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else: 
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      