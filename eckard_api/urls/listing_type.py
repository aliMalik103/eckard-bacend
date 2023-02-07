from django.urls import path
from eckard_api.views.listing_type import ListingTypeList, ListingTypeDetail


urlpatterns = [
  path('', ListingTypeList.as_view()),
  path('<int:pk>/', ListingTypeDetail.as_view()),
]
