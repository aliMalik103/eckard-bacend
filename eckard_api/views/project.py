from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from eckard_api.models.project import Project
from eckard_api.models.project_production import ProjectProduction
from eckard_api.serializers.project import ProjectGetSerializer, ProjectPostSerializer
from django.db import connection

  
class ProjectList(APIView):
  def get(self, request):
    project = Project.objects.all()
    if project:
      response = ProjectGetSerializer(project, many=True)
      return Response(response.data)
    
    else:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)


  def post(self, request):
    serializer = ProjectPostSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectDetail(APIView):
  def get(self, request, pk):
    try:
      project = Project.objects.get(pk=pk)
      serializer = ProjectGetSerializer(project)
      return Response(serializer.data)
    
    except Project.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    
      
      
  def put(self, request, pk):
    try:
      project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProjectPostSerializer(project, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  def patch(self, request, pk, format=None):
    try:
      project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProjectPostSerializer(project, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else: 
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProjectRecentPrices(APIView):
  def get(self, request, projectId):
    try:
      cursor = connection.cursor()
      cursor.execute('select oil, gas, date, "totalNma" as "totalProjectNma" from project_production as pp join project p on p.id = pp.project_id where not pp."isDeleted" and project_id = '+str(projectId)+' order by date desc limit 1')
      row = cursor.fetchone()
      data = {}
      if row:
        data["oil"] = row[0]
        data["gas"] = row[1]
        data["date"] = row[2]
        data["totalProjectNma"] = row[3]
      return Response(data)
    except ProjectProduction.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)  
      