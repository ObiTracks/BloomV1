from django.urls import path
from .views import *

urlpatterns = [
     # BASE URLS
     path('',home_page,name='home'),

     # CRUD URLS
     path('create_reservation/<str:tk>/<str:pk>/',createReservation, name='create_reservation'),
     path('update_reservation/<str:pk>/',updateReservation,name='update_reservation'),
     path('delete/<str:pk>/',deletePage,name='delete_page'),

     # LOGIN URLS
     path('register', registerPage, name='register'),
     path('login', loginPage, name='login'),
     path('logout', loginUser, name='logout'),

     # OBJECT URLS
     path('resident/<str:pk>/', customer, name='resident'),
     path('days/day/<str:pk>/', day, name='day'),
     path('timeslot/<str:pk>/', timeslot, name='timeslot'),
     path('reservation/<str:pk>/', timeslot, name='reservation'),

     # LISTS URLS
     path('residents/<str:tk>/', customers, name='residents'),
     path('days/', days, name='days'),
     path('timeslots/', timeslots, name='timeslots_all'),

]
