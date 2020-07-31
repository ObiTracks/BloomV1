from django.urls import path
from .views import (
    home_page, 
    # reservations_page, 
    # booked_page
)

urlpatterns = [
    path('', home_page),    
    # path('reserve/', reservations_page),
    # path('confirmation/', booked_page),
]
