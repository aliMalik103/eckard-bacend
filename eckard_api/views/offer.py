from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from eckard_api.models.offer import Offer
from eckard_api.models.listing import Listing
from eckard_api.models.status import Status
from eckard_api.models.listing_offer import ListingOffer
from eckard_api.serializers.offer import OfferGetSerializer, OfferPostSerializer
from eckard_api.serializers.listing_offer import ListingOfferPostSerializer,ListingOfferGetSerializer

from django.db import connection
  
class OfferList(APIView):
  def get(self, request):
    offer = Offer.objects.all()
    if offer:
      response = OfferGetSerializer(offer, many=True)
      return Response(response.data)
    
    else:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        

  def post(self, request):
    offer_data = request.data.pop("offer")
    serializer_offer = OfferPostSerializer(data = offer_data)
    if serializer_offer.is_valid():
      serializer_offer.save()
      listing_id = request.data.pop("listing_id")
      acceptedOffer = request.data.pop("acceptedOffer")
      
      if acceptedOffer:
        listing = Listing.objects.get(pk=listing_id)
        listing.status = Status.objects.get(status = "Accepted")
        listing.save()
      
      offer = Offer.objects.latest('id').id
      serializer_listing_offer = ListingOfferPostSerializer(data = { "offer": offer, "listing": listing_id, "acceptedOffer":acceptedOffer} )
      if serializer_listing_offer.is_valid():
        serializer_listing_offer.save()
        return Response(serializer_listing_offer.data, status=status.HTTP_201_CREATED)
      else:
        return Response(serializer_listing_offer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer_offer.errors, status=status.HTTP_400_BAD_REQUEST)


class OfferDetail(APIView):
  def get(self, request, pk):
    try:
      offer = Offer.objects.get(pk=pk)
      serializer = OfferGetSerializer(offer)
      return Response(serializer.data)
    
    except Offer.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
      
      
  def put(self, request, pk):
    try:
      offer = Offer.objects.get(pk=pk)
    except Offer.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    
    offer_data = request.data.pop("offer")
    serializer_offer = OfferPostSerializer(offer, data=offer_data)
    if serializer_offer.is_valid():
        serializer_offer.save()
        listing_id = request.data.pop("listing_id")
        acceptedOffer = request.data.pop("acceptedOffer")

        if acceptedOffer:
          listing = Listing.objects.get(pk=listing_id)
          listing.status = Status.objects.get(status = "Accepted")
          listing.save()

        listing_offer = ListingOffer.objects.filter(listing_id = listing_id, offer_id = pk ).first()
        serializer_listing_offer = ListingOfferPostSerializer(listing_offer, data = { "offer": pk, "listing": listing_id, "acceptedOffer": acceptedOffer} )
        if serializer_listing_offer.is_valid():
          serializer_listing_offer.save()
          return Response(serializer_listing_offer.data, status=status.HTTP_201_CREATED)
        else:
          return Response(serializer_listing_offer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
      return Response(serializer_offer.errors, status=status.HTTP_400_BAD_REQUEST)
    

  def patch(self, request, pk, format=None):
    try:
      offer = Offer.objects.get(pk=pk)
    except Offer.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    
    offer_data = request.data.pop("offer")
    serializer_offer = OfferPostSerializer(offer, data=offer_data, partial=True)
    if serializer_offer.is_valid():
        serializer_offer.save()
        listing_id = request.data.pop("listing_id")
        acceptedOffer = request.data.pop("acceptedOffer")
        if acceptedOffer:
          listing = Listing.objects.get(pk=listing_id)
          listing.status = Status.objects.get(status = "Accepted")
          listing.save()
        
        listing_offer = ListingOffer.objects.filter(listing_id = listing_id, offer_id = pk ).first()
        serializer_listing_offer = ListingOfferPostSerializer(listing_offer, data = { "offer": pk, "listing": listing_id, "acceptedOffer": acceptedOffer}, partial=True)
        if serializer_listing_offer.is_valid():
          serializer_listing_offer.save()
          return Response(serializer_listing_offer.data, status=status.HTTP_201_CREATED)
        else:
          return Response(serializer_listing_offer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
      return Response(serializer_offer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
  def delete(self, request, pk):
    try:
      offer = Offer.objects.get(pk=pk)
      listing_id = request.data.pop("listing_id")
      ListingOffer.objects.get(offer_id = offer.id, listing_id = listing_id).delete()
      offer.delete()
      return Response({"msg": "deleted successfully"})
    except Offer.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

class ActiveListing(APIView):
  def get(self, request, contactId):
    cursor = connection.cursor()
    cursor.execute('select t."listingId", l."listingName", l."directSaleToken", l."listingStart",o."offer_Status", l."auctionEnd", COALESCE(o."offerAmount", null) as "offerAmount", o."id" as "offer_id", a."mpName" as "accountMpName", a."id" as "acccount_id", p."projectId" as "projectId", p."id" as "project_id", t."status",l.nma as "listedNMA", l."minimumAsk", t."highestBid", t.ct as "noOfBids", ac."auctionType", l."buyNowPrice", CASE  WHEN o."offerAmount" = t."highestBid" THEN true ELSE false END as "isHighestOffer", CASE  WHEN l."listingStart" > now() THEN true ELSE false END as "isListingStart", CASE  WHEN l."auctionEnd" < now() THEN true ELSE false END as "isAuctionEnd" from ( select l.id as "listingId", sl."status", o."highestBid", o."ct" from listing l left join listing_offer lo on lo.listing_id = l.id left join status sl on sl.id = l.status_id left join ( SELECT max(o."offerAmount") as "highestBid", count(o.id) as ct, l.id as "listing_id" from listing l left join listing_offer lo on lo.listing_id = l.id left join status sl on sl.id = l.status_id left join offer o on o.id = lo.offer_id and not o."isDeleted" left join status so on so.id = o."status_id" where not l."isDeleted" and (sl."status"='+"'Active'"+' OR sl."status"='+"'Accepted'"+') and so."status" = '+"'Active'"+' group by l.id ) o ON l.id = o."listing_id" where not l."isDeleted" and (sl."status"='+"'Active'"+' OR sl."status"='+"'Accepted'"+') group by l.id, sl.id, o."highestBid", o."ct" ) t join listing l on l.id = t."listingId" join account a on a.id = l.account_id join project p on p.id = l.project_id join auction_type ac on ac.id = l.auction_type_id LEFT JOIN ( SELECT DISTINCT o."id", o."offerAmount",sl."status" as "offer_Status", lo."listing_id" FROM offer o JOIN listing_offer lo ON o.id = lo."offer_id" left join status sl on sl.id = o.status_id WHERE o."contact_id" = '+str(contactId)+') o ON l.id = o."listing_id" where not a."contact_id" = '+str(contactId)+' order by l.id desc')
    
    columns = [col[0] for col in cursor.description]
    data=[
      dict(zip(columns, row))
      for row in cursor.fetchall()
    ]
    return Response(data)    

class ListingOfferAPI(APIView):
  def get(self, request, listid):
    offer=ListingOffer.objects.filter(listing_id = listid, acceptedOffer = True )
    if offer:
      response = ListingOfferGetSerializer(offer, many=True)
      return Response(response.data)
    
    else:
      return Response([], status=status.HTTP_200_OK)


class PendingOffer(APIView):
  def get(self, request, contactId):
    cursor = connection.cursor()
    cursor.execute('select o.id, so."status", o."offerAmount" from offer o left join status so on so.id = o.status_id join contact c on c.id = o."contact_id" where c.id= '+str(contactId)+'  and so."status" = '+"'Accepted'"+'')
    columns = [col[0] for col in cursor.description]
    data=[
      dict(zip(columns, row))
      for row in cursor.fetchall()
    ]
    return Response(data)
