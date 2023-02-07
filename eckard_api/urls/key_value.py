from django.urls import path
from eckard_api.views.key_value import KeyConfigView 


urlpatterns = [
  path('', KeyConfigView.as_view()),
 
]
