from django.urls import path
from eckard_api.views.contact import ContactList, ContactDetail


urlpatterns = [
  path('', ContactList.as_view()),
  path('<int:pk>/', ContactDetail.as_view()),
]
