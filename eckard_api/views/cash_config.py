from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from eckard_api.models.cashcalculator import CashCalculator
from eckard_api.serializers.cash_config import CashConfigPostSerializer, CashConfigGetSerializer
from django.db import connection

class Cash_Config(APIView):
  def get(self, request):
    investment = CashCalculator.objects.all()
    if investment:
      response = CashConfigGetSerializer(investment, many=True)
      return Response(response.data)
    
    else:
      return Response([], status=status.HTTP_200_OK)


  def post(self, request):
    serializer = CashConfigPostSerializer(data=request.data)
    if serializer.is_valid():
      CashCalculator.objects.create(**serializer.validated_data)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    else:
       return Response([], status=status.HTTP_200_OK)

  


class ProjectCashConfig(APIView):
  def get(self, request, contactid):
    investment = CashCalculator.objects.filter(contact_id = contactid)
    if investment:
      response = CashConfigGetSerializer(investment, many=True)
      return Response(response.data)
    
    else:
       return Response([], status=status.HTTP_200_OK)  


class ProjectCashUpdate(APIView):
  
 def patch(self, request, pk, format=None):
    try:
      cashconfig = CashCalculator.objects.get(pk=pk)
    except CashCalculator.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = CashConfigPostSerializer(cashconfig, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else: 
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)