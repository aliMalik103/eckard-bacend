from django.urls import path
from eckard_api.views.status import StatusList, StatusDetail


urlpatterns = [
  path('', StatusList.as_view()),
  path('<int:pk>/', StatusDetail.as_view()),
]
