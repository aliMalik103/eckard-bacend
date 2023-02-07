from django.urls import path
from eckard_api.views.cash_flow import CashFlowList, CashFlowDetail


urlpatterns = [
  path('', CashFlowList.as_view()),
  path('<int:pk>/', CashFlowDetail.as_view()),
]
