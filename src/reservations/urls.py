from django.urls import path
from .views import *
urlpatterns = [
    path('', home_page),    
    # path('reserve/', reservation_page),
    # path('confirmation/', confirmation_page),
]
