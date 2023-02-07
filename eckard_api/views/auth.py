
import json
from eckard_api.models.contact import Contact

from eckard_api.serializers import ContactSerializer
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


@api_view(['POST'])
def add_contact(request):
    item = ContactSerializer(data=request.data)
  
    # validating for already existing data
    if Contact.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_items(request):
    
    # checking for the parameters from the URL
   #  if request.query_params:
   #      items = Contact.objects.filter(**request.query_param.dict())
   #  else:

    items = Contact.objects.all()
    serializer = ContactSerializer(items,many=True)
    # if there is something in items else raise error
    if items:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
def login(request):
     data = {}
     reqBody = json.loads(request.body)
     email1 = reqBody['email']
     password=reqBody['password']

     contact = Contact.objects.get(email=email1)
    # checking for the parameters from the URL
   #  if request.query_params:
   #      items = Contact.objects.filter(**request.query_param.dict())
   #  else:
     if contact.email==email1:
         if contact.password==password:
            data["message"] = "user logged in"
            data["email"] = contact.email
            data["status"] = contact.mpStatus
            data["id"]=contact.id
            data["name"] = contact.firstName[:1]+"."+contact.lastName
            data["valid"] = True
            Res = {"data": data}

            return Response(Res)
         else:
          data["message"] = "user logged in"
          data["email"] = contact.email
          data["status"] = contact.mpStatus
          data["valid"] = False
          Res = {"data": data}

          return Response(Res)    