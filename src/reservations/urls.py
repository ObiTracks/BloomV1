from django.urls import path
from .views import *
from .views_read import *

urlpatterns = [
    # Read
    path('', home_page),
    # path('customer/', customer_page),
    path('customers/', customers_all),
    path('customer/<str:pk>/', customer),

    path('days/', days_all, name='days_all'),
    path('days/day/<str:pk>/', day, name='day'),
    path('timeslots/', timeslots_all, name='timeslots_all'),
    path('timeslot/<str:pk>/', timeslot, name='timeslot'),
    
    # path('reservation/', reservation),
    # path('timeslot/', timeslot),
    # path('daysummary/', day),
    # path('confirmation/', confirmation_page),

    # Create
    # path('create/', create_page),
    
    # Update
    # path('update/<str:pk>/', delete_page),

    # Delete
    # path('delete/<str:pk>/', delete_page),
]
