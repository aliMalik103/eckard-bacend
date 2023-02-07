from django.urls import path
from eckard_api.views.listing import ListingList, ListingDetail, ListingPost, PendingListing


urlpatterns = [
  path('',ListingPost.as_view()),
  path('contact/<int:contactid>', ListingList.as_view()),
  path('<int:pk>/', ListingDetail.as_view()),
  path('contact/<int:contactId>/pending_list', PendingListing.as_view()),
]
