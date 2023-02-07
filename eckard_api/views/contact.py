from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from eckard_api.models.contact import Contact
from eckard_api.serializers.contact import ContactSerializer
from django.db import connection

  
class ContactList(APIView):
  def get(self, request):
    constraint = Contact.objects.all()
    if constraint:
      response = ContactSerializer(constraint, many=True)
      return Response(response.data)
    
    else:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)


  def post(self, request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContactDetail(APIView):
  def get(self, request, pk):
    try:
      contact = Contact.objects.get(pk=pk)
      serializer = ContactSerializer(contact)
      return Response(serializer.data)
    
    except Contact.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
  
      
  def put(self, request, pk):
    try:
      constraint = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ContactSerializer(constraint, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  def patch(self, request, pk, format=None):
    try:
      constraint = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ContactSerializer(constraint, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else: 
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

