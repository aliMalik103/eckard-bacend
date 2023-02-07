from django.urls import path
from eckard_api.views.constraint import ConstraintList, ConstraintDetail,ConstraintByType


urlpatterns = [
  path('', ConstraintList.as_view()),
  path('<int:pk>/', ConstraintDetail.as_view()),

  path('type/<str:type>/', ConstraintByType.as_view()),
]
