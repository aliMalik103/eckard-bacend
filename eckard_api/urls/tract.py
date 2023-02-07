from django.urls import path
from eckard_api.views.tract import TractList, TractDetail


urlpatterns = [
  path('', TractList.as_view()),
  path('<int:pk>/', TractDetail.as_view()),
]
