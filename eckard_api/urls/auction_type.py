from django.urls import path
from eckard_api.views.auction_type import AuctionTypeList, AuctionTypeDetail


urlpatterns = [
  path('', AuctionTypeList.as_view()),
  path('<int:pk>/', AuctionTypeDetail.as_view()),
]
