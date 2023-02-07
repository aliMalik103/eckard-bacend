from django.urls import path
from eckard_api.views.offer import OfferList, OfferDetail, ActiveListing, ListingOfferAPI, PendingOffer


urlpatterns = [
  path('', OfferList.as_view()),
  path('contact/<int:contactId>', ActiveListing.as_view()),
  path('<int:pk>/', OfferDetail.as_view()),
  path('list/<int:listid>/', ListingOfferAPI.as_view()),
  path('contact/<int:contactId>/pending_offer', PendingOffer.as_view()),
  
]
