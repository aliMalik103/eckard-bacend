from django.urls import path
from eckard_api.views.cash_config import Cash_Config,ProjectCashConfig,ProjectCashUpdate


urlpatterns = [
  path('', Cash_Config.as_view()),
  path('contact/<int:contactid>', ProjectCashConfig.as_view()),
  path('<int:pk>', ProjectCashUpdate.as_view()),
]
