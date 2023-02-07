from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from eckard_api.models.listing_type import ListingType
from eckard_api.serializers.listing_type import ListingTypeSerializer
  
class ListingTypeList(APIView):
  def get(self, request):
    listing_type = ListingType.objects.all()
    if listing_type:
      response = ListingTypeSerializer(listing_type, many=True)
      return Response(response.data)
    
    else:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)


  def post(self, request):
    serializer = ListingTypeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListingTypeDetail(APIView):
  def get(self, request, pk):
    try:
      listing_type = ListingType.objects.get(pk=pk)
      serializer = ListingTypeSerializer(listing_type)
      return Response(serializer.data)
    
    except ListingType.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
      
      
  def put(self, request, pk):
    try:
      listing_type = ListingType.objects.get(pk=pk)
    except ListingType.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ListingTypeSerializer(listing_type, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  def patch(self, request, pk, format=None):
    try:
      listing_type = ListingType.objects.get(pk=pk)
    except ListingType.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ListingTypeSerializer(listing_type, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else: 
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      