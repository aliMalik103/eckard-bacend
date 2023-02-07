from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from eckard_api.models.cash_flow import CashFlow
from eckard_api.serializers.cash_flow import CashFlowGetSerializer, CashFlowPostSerializer

  
class CashFlowList(APIView):
  def get(self, request):
    cashFlow = CashFlow.objects.all()
    if cashFlow:
      response = CashFlowGetSerializer(cashFlow, many=True)
      return Response(response.data)
    
    else:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)


  def post(self, request):
    serializer = CashFlowPostSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CashFlowDetail(APIView):
  def get(self, request, pk):
    try:
      cashFlow = CashFlow.objects.get(pk=pk)
      serializer = CashFlowGetSerializer(cashFlow)
      return Response(serializer.data)
    
    except CashFlow.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
      
      
  def put(self, request, pk):
    try:
      cashFlow = CashFlow.objects.get(pk=pk)
    except CashFlow.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = CashFlowPostSerializer(cashFlow, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  def patch(self, request, pk, format=None):
    try:
      cashFlow = CashFlow.objects.get(pk=pk)
    except CashFlow.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = CashFlowPostSerializer(cashFlow, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else: 
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

