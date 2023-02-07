from django.urls import path
from eckard_api.views.project import ProjectList, ProjectDetail,ProjectRecentPrices


urlpatterns = [
  path('', ProjectList.as_view()),
  path('<int:pk>/', ProjectDetail.as_view()),
  path('<int:projectId>/recent_prices', ProjectRecentPrices.as_view()),
]
