from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from eckard_api.models.investment import Investment
from eckard_api.serializers.investment import InvestmentGetSerializer, InvestmentPostSerializer
from django.db import connection
  
class InvestmentList(APIView):
  def get(self, request):
    investment = Investment.objects.all()
    if investment:
      response = InvestmentGetSerializer(investment, many=True)
      return Response(response.data)
    
    else:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)


  def post(self, request):
    serializer = InvestmentPostSerializer(data=request.data)
    if serializer.is_valid():
      Investment.objects.create(**serializer.validated_data)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InvestmentDetail(APIView):
  def get(self, request, pk):
    try:
      investment = Investment.objects.get(pk=pk)
      serializer = InvestmentGetSerializer(investment)
      return Response(serializer.data)
    
    except Investment.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
      
      
  def put(self, request, pk):
    try:
      investment = Investment.objects.get(pk=pk)
    except Investment.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = InvestmentPostSerializer(investment, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  def patch(self, request, pk, format=None):
    try:
      investment = Investment.objects.get(pk=pk)
    except Investment.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = InvestmentPostSerializer(investment, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else: 
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      
class InvetmentByAccount(APIView):
   def get(self, request, accountid):
    try:
      investmentRecords=Investment.objects.filter(account_id=accountid)
      serializer = InvestmentGetSerializer(investmentRecords,many=True)
      return Response(serializer.data)
    
    except Investment.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)  

class InvetmentListingCost(APIView):
   def get(self, request, accountid,projectid):
    try:
      cursor = connection.cursor()
      cursor.execute('select 	(sum("investmentAmount") / sum("acquiredNma")) as "costPerNma", sum("investmentAmount") as "totalCost", sum("acquiredNma") as "totalNma", count(id) as ct from investment where account_id ='+ str(accountid)+' and project_id ='+ str(projectid)+' and not "isDeleted" and "acquiredNma" > 0')
      row = cursor.fetchone()
      data = {}
      data["costPerNma"] = row[0]
      data["totalCost"] = row[1]
      data["totalNma"] = row[2]
      data["ct"]=row[3]
      return Response(data)
    except Investment.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)       