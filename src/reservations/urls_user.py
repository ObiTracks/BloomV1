from django.urls import path
from .views  import views_user, views_c_login

urlpatterns = [
    # BASE URLS
    path('', views_user.home_page, name='home'),
    path('profile', views_user.profilePage, name='profile'),

    # CRUD URLS
    path('new_reservation/<str:tk>/<str:pk>/', views_user.createReservation,name='new_reservation'),
    path('delete/<int:pk>/', views_user.deleteUserReservation, name='deleteUserReservation'),

    # LOGIN URLS
    # path('register', views_c_login.registerUserPage, name='register'),
    path('login', views_c_login.loginPage, name='login'),
    path('logout', views_c_login.logoutUser, name='logout'),
    path('profile', views_c_login.profilePage, name='profile'),

    # LISTS URLS
    path('reservations', views_user.reservationsPage, name='reservations'),
   

]