from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from eckard_api.models.constraint import Constraint
from eckard_api.serializers.constraint import ConstraintSerializer

  
class ConstraintList(APIView):
  def get(self, request):
    constraint = Constraint.objects.all()
    if constraint:
      response = ConstraintSerializer(constraint, many=True)
      return Response(response.data)
    
    else:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)


  def post(self, request):
    serializer = ConstraintSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConstraintDetail(APIView):
  def get(self, request, pk):
    try:
      constraint = Constraint.objects.get(pk=pk)
      serializer = ConstraintSerializer(constraint)
      return Response(serializer.data)
    
    except Constraint.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
      
      
  def put(self, request, pk):
    try:
      constraint = Constraint.objects.get(pk=pk)
    except Constraint.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ConstraintSerializer(constraint, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  def patch(self, request, pk, format=None):
    try:
      constraint = Constraint.objects.get(pk=pk)
    except Constraint.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ConstraintSerializer(constraint, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else: 
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConstraintByType(APIView):
   def get(self, request, type):
    try:
      constraint = Constraint.objects.filter(constraintType=type)
      response = ConstraintSerializer(constraint, many=True)
      return Response(response.data)
    
    except Constraint.DoesNotExist:
      return Response([], status=status.HTTP_200_OK)  