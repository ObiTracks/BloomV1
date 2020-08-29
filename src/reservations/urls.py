from django.urls import path
from .views  import views_a_base, views_b_crud, views_c_login, views_d_objects, views_e_lists

urlpatterns = [
    # BASE URLS
    path('', views_a_base.home_page, name='home'),

    # CRUD URLS
    path('create_reservation/<str:tk>/<str:pk>/',
         views_b_crud.createReservation,
         name='create_reservation'),
    path('update_reservation/<str:pk>/',
         views_b_crud.updateReservation,
         name='update_reservation'),
    path('delete/<str:pk>/', views_b_crud.deletePage, name='delete_page'),

    # LOGIN URLS
    path('register', views_c_login.registerPage, name='register'),
    path('login', views_c_login.loginPage, name='login'),
    path('logout', views_c_login.logoutUser, name='logout'),

    # OBJECT URLS
    path('resident/<str:pk>/', views_d_objects.customer, name='resident'),
    path('days/day/<str:pk>/', views_d_objects.day, name='day'),
    path('timeslot/<str:pk>/', views_d_objects.timeslot, name='timeslot'),
    path('reservation/<str:pk>/', views_d_objects.timeslot,
         name='reservation'),

    # LISTS URLS
    path('residents/<str:tk>/', views_e_lists.customers, name='residents'),
    path('days/', views_e_lists.days, name='days'),
    path('timeslots/', views_e_lists.timeslots, name='timeslots'),
]
