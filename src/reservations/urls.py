from django.urls import path
from .views import *

urlpatterns = [
    #Login and Registration
    path('register', registerPage, name='register'),
    path('login', loginPage, name='login'),
    path('logout', loginPage, name='logout'),

    # Read
    path('', home_page, name='home'),
    path('residents/<str:tk>/', customers_all, name='residents'),
    path('resident/<str:pk>/', customer, name='resident'),
    path('days/', days_all, name='days'),
    path('days/day/<str:pk>/', day, name='day'),
    path('timeslots/', timeslots_all, name='timeslots_all'),
    path('timeslot/<str:pk>/', timeslot, name='timeslot'),

    # CRUD
    # path('create/', create_page),
    path('create_reservation/<str:tk>/<str:pk>/',
         createReservation,
         name='create_reservation'),
    path('update_reservation/<str:pk>/',
         updateReservation,
         name='update_reservation'),
    path('delete/<str:pk>/', deletePage, name='delete_page')
    # path('delete/', delete, name="delete"),
]
