from django.urls import path
from eckard_api.views import add_contact, view_items, login

urlpatterns = [
    path('create/', add_contact, name='add-items'),
    path('all/', view_items, name='view_items'),
    path('login/', login, name='Login'),
    
]
