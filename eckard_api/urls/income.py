from django.urls import path
from eckard_api.views.income import IncomeListingCost


urlpatterns = [
  path('account/<int:accountid>/project/<int:projectid>', IncomeListingCost.as_view()),
]
