from django.urls import path
from eckard_api.views.account import AccountList, AccountDetail, AccountByContacts


urlpatterns = [
  path('', AccountList.as_view()),
  path('<int:pk>/', AccountDetail.as_view()),
  path('getbycontact/<int:contactId>/', AccountByContacts.as_view()),
]
