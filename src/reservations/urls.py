from django.urls import path
from .views import *

urlpatterns = [
    # Read
    path('', home_page, name='home'),
    # path('customer/', customer_page),
    path('residents/', customers_all, name='residents_all'),
    path('resident/<str:pk>/', customer, name='resident'),

    path('days/', days_all, name='days_all'),
    path('days/day/<str:pk>/', day, name='day'),
    path('timeslots/', timeslots_all, name='timeslots_all'),
    path('timeslot/<str:pk>/', timeslot),
    
    # path('reservation/', reservation),
    # path('timeslot/', timeslot),
    # path('daysummary/', day),
    # path('confirmation/', confirmation_page),


    # CRUD
    # path('create/', create_page),
    path('create_reservation/<str:pk>/', createReservation, name='create_reservation'),
    path('update_reservation/<str:pk>/', updateReservation, name='update_reservation'),
    path('delete/<str:pk>/', deletePage, name='delete_page')
    # path('delete/', delete, name="delete"),
]
