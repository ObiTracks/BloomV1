from django.urls import path
from .views  import views_a_base, views_b_crud, views_c_login, views_d_objects, views_e_lists

urlpatterns = [
    
    # BASE URLS
    path('', views_a_base.home_page, name='staff_dashboard'),

    # CRUD URLS
    path('add_day/',
         views_b_crud.createDay,
         name='create_day'),
    path('create_reservation/<str:tk>/<str:pk>/',
         views_b_crud.createReservation,
         name='create_reservation'),
    path('update_reservation/<str:pk>/',
         views_b_crud.updateReservation,
         name='update_reservation'),
    path('update_customer/<str:pk>/',
         views_b_crud.updateResident,
         name='update_resident'),
    path('delete/<int:pk>/', views_b_crud.deleteDay, name='delete'),

    # LOGIN URLS
    path('register-user/', views_c_login.registerUserPage, name='register_user'),
#     path('login/', views_c_login.loginPage, name='login'),
#     path('logout/', views_c_login.logoutUser, name='logout'),
    path('profile/', views_c_login.profilePage, name='profile'),

    # OBJECT URLS
    path('resident/<str:pk>/', views_d_objects.customer, name='resident'),
    path('days/day/<str:pk>/', views_d_objects.day, name='day'),
    path('timeslot/<str:pk>/', views_d_objects.timeslot, name='timeslot'),
    path('reservation/<str:pk>/', views_d_objects.timeslot,
         name='reservation'),

    # LISTS URLS
    path('residents/<str:tk>/', views_e_lists.customers, name='residents'),
    path('days/', views_e_lists.days, name='days'),
   
]