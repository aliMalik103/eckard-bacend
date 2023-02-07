from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from eckard_api.models.account import Account
from eckard_api.models.investment import Investment
from eckard_api.serializers.investment import InvestmentGetSerializer
from eckard_api.serializers.account import AccountGetSerializer, AccountPostSerializer

  
class AccountList(APIView):
  def get(self, request):
    account = Account.objects.all()
    if account:
      response = AccountGetSerializer(account, many=True)
      return Response(response.data)
    
    else:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)


  def post(self, request):
    serializer = AccountPostSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AccountDetail(APIView):
  def get(self, request, pk):
    try:
      account = Account.objects.get(pk=pk)
      serializer = AccountGetSerializer(account)
      return Response(serializer.data)
    
    except Account.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
      
      
  def put(self, request, pk):
    try:
      account = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = AccountPostSerializer(account, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  def patch(self, request, pk, format=None):
    try:
      account = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = AccountPostSerializer(account, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else: 
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    


class AccountByContacts(APIView):
   def get(self, request, contactId):
    try:
      accounts = Account.objects.filter(contact_id=contactId)
      serializer = AccountGetSerializer(accounts,many=True)
      return Response(serializer.data)
    
    except Account.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)        