from django.urls import path
from eckard_api.views.investment import InvestmentList, InvestmentDetail,InvetmentByAccount,InvetmentListingCost


urlpatterns = [
  path('', InvestmentList.as_view()),
  path('<int:pk>/', InvestmentDetail.as_view()),
  path('getbyaccount/<int:accountid>/', InvetmentByAccount.as_view()),
  path('account/<int:accountid>/project/<int:projectid>', InvetmentListingCost.as_view()),
]
