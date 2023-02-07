from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from eckard_api.models.auction_type import AuctionType
from eckard_api.serializers.auction_type import AuctionTypeSerializer

  
class AuctionTypeList(APIView):
  def get(self, request):
    auctionType = AuctionType.objects.all()
    if auctionType:
      response = AuctionTypeSerializer(auctionType, many=True)
      return Response(response.data)
    
    else:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)


  def post(self, request):
    serializer = AuctionTypeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AuctionTypeDetail(APIView):
  def get(self, request, pk):
    try:
      auctionType = AuctionType.objects.get(pk=pk)
      serializer = AuctionTypeSerializer(auctionType)
      return Response(serializer.data)
    
    except AuctionType.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
      
      
  def put(self, request, pk):
    try:
      auctionType = AuctionType.objects.get(pk=pk)
    except AuctionType.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = AuctionTypeSerializer(auctionType, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  def patch(self, request, pk, format=None):
    try:
      auctionType = AuctionType.objects.get(pk=pk)
    except AuctionType.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = AuctionTypeSerializer(auctionType, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else: 
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      