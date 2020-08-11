from django.urls import path
from .views import *
from .views_read import customers_all_page, days_all_page, timeslots_all_page

urlpatterns = [
    # Read
    path('', home_page),
    # path('customer/', customer_page),
    path('customers/', customers_all_page),
    path('customer/<str:pk>/', customer_page),

    path('days/', days_all_page),
    # path('days/<str:pk>/', day_page),
    path('timeslots/', timeslots_all_page),
    # path('timeslot/<str:pk>/', timeslot_page),
    
    # path('reservation/', reservation_page),
    # path('timeslot/', timeslot_page),
    # path('daysummary/', day_page),
    # path('confirmation/', confirmation_page),

    # Create
    # path('create/', create_page),
    
    # Update
    # path('update/<str:pk>/', delete_page),

    # Delete
    # path('delete/<str:pk>/', delete_page),
]
