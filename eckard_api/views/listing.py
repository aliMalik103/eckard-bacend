from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from eckard_api.models.listing import Listing
from eckard_api.serializers.listing import ListingGetSerializer, ListingPostSerializer
from django.db import connection

class ListingPost(APIView):
 def post(self, request):
    serializer = ListingPostSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListingList(APIView):
  def get(self, request,contactid):
      cursor = connection.cursor()
      cursor.execute('select t."listingId", l."listingName",l."listingStart", l."auctionEnd", a."accountName" || '+"' / '" +'|| p."projectId" as "Account/Project",t."status", a."contact_id",l.nma as "listedNMA", l."minimumAsk", t."highestBid", t.ct as "# Bids", CASE  WHEN l."listingStart" > now() THEN true ELSE false END as "isListingStart", CASE  WHEN l."auctionEnd" < now() THEN true ELSE false END as "isAuctionEnd" from ( select l.id as "listingId", o."highestBid", o."ct",sl."status" from listing l  left join listing_offer lo on lo.listing_id = l.id left join status sl on sl.id = l.status_id left join (	SELECT max(o."offerAmount") as "highestBid", count(o.id) as ct, l.id as "listing_id" from listing l left join listing_offer lo on lo.listing_id = l.id left join status sl on sl.id = l.status_id left join offer o on o.id = lo.offer_id and not o."isDeleted" left join status so on so.id = o."status_id" where not l."isDeleted" and (sl."status"='+"'Active'"+' OR sl."status"='+"'Draft'"+') and so."status" = '+"'Active'"+' group by l.id) o ON l.id = o."listing_id" where not l."isDeleted" and (sl."status"='+"'Active'"+' OR sl."status"='+"'Draft'"+') group by l.id, sl.id, o."highestBid", o."ct" ) t join listing l on l.id = t."listingId" join account a on a.id = l.account_id join project p on p.id = l.project_id where a."contact_id"= '+str(contactid)+' order by l.id desc')
      columns = [col[0] for col in cursor.description]
      data=[
        dict(zip(columns, row))
        for row in cursor.fetchall()
      ]
      return Response(data)
    
    

class ListingDetail(APIView):
  def get(self, request, pk):
    try:
      listing = Listing.objects.get(pk=pk)
      serializer = ListingGetSerializer(listing)
      return Response(serializer.data)
    
    except Listing.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
      
      
  def put(self, request, pk):
    try:
      listing = Listing.objects.get(pk=pk)
    except Listing.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ListingPostSerializer(listing, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  def patch(self, request, pk, format=None):
    try:
      listing = Listing.objects.get(pk=pk)
    except Listing.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ListingPostSerializer(listing, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else: 
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PendingListing(APIView):
  def get(self, request, contactId):
    cursor = connection.cursor()
    cursor.execute('select l.id, l."listingName", sl."status", a."accountName" from listing l join account a on a.id = l."account_id" left join status sl on sl.id = l.status_id where a."contact_id"= '+str(contactId)+' and sl."status"='+"'Accepted'"+' order by l.id desc')
    columns = [col[0] for col in cursor.description]
    data=[
      dict(zip(columns, row))
      for row in cursor.fetchall()
    ]
    return Response(data)
