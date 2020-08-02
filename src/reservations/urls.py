from django.urls import path
from .views import (
    home_page, 
    reservation_page, 
    confirmation_page
)

urlpatterns = [
    path('', home_page),    
    path('reserve/', reservation_page),
    path('confirmation/', confirmation_page),
]
