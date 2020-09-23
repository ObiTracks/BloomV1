from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import inlineformset_factory
from datetime import date
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from time import sleep
#View imports here
from ..models import (Customer, Day, TimeSlot, Reservation)
from ..forms import *
from ..filters import CustomerFilter


@login_required(login_url='login')
def home_page(request):
    if Day.objects.all() == None or Day.objects.count() < 2:
        return HttpResponse("<html>There are not enough days avaialable to book</html>")
    else:
        days = Day.objects.all()[:2]

        today = days[0]
        tomorrow = days[1]

        customer = request.user.customer
        today_date = date.today()
        tomorrow_date = date.today() + timedelta(days=1)

        page_title = "Resident Dashboard"
        context = {
            'days':days,
            'customer':customer,
            'page_title': page_title,
        }
        template_name = '../templates/user_templates/home.html'
    

    return render(request, template_name, context)

@login_required(login_url='login')
def profilePage(request):
    customer = request.user.customer
    total_reservations = customer.reservation_set.count()
    page_title = "Resident Dashboard"

    context = {
        'customer':customer,
        'total_reservations':total_reservations,
        'page_title': page_title,
    }

    template_name = '../templates/user_templates/profile.html'

    return render(request, template_name, context)

    
@login_required(login_url='login')
def createUserReservation(request, tk, *args, **kwargs):
    customer = request.user.customer
    # Check to pass through a prefilled timeslot if it recieves an id for one
    if tk != 'None':
        timeslot = TimeSlot.objects.get(id=tk)
        form = ReservationForm(initial={
            'customer': customer,
            'timeslot': timeslot
        })
        # print('Path A: tk='+ tk)
        form = ReservationForm(initial={
            'customer': customer,
            'timeslot': timeslot
        })
    else:
        timeslot = None
        form = ReservationForm(initial={
            'customer': customer,
        })
        # print('Path B: tk=' + tk)

    # Creating for creating a reservation from post data
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = ReservationForm(request.POST)
        if form.is_valid():
            print(request.POST)
            timeslot_id = request.POST.get('timeslot')
            timeslot = TimeSlot.objects.get(pk=timeslot_id)
            print(timeslot)
            if request.POST.get('timeslot') != None:
                num_res = timeslot.reservation_set.all().count()
                if num_res < timeslot.capacity:
                    form.save()
                    return redirect('/')
                else:
                    messages.error(request, 'Timeslot is at capacity')
                    print("Timeslot at capacity of {}".format(num_res))
    #

    stats = {}

    context = {
        'form': form,
        'page_title': 'New Reservation',
        'customer': customer,
        'time_slot': timeslot
    }
    return render(request, '../templates/user_templates/reservation_form.html', context)

    
# @login_required(login_url='login')
# # @allowed_users(allowed_roles=['manager','staff','SiteAdmin'])
# def deleteReservation(request, pk):
#     reservation = Reservation.objects.get(id=pk)
#     if request.method == 'POST':
#         reservation.delete()
#         return redirect('/')
        
#     context = {'item': reservation}
#     template_name = '../templates/crud_templates/delete_user-v.html'
#     return render(request, template_name, context)

    
@login_required(login_url='login')
def reservationsPage(request):
    customer = request.user.customer
    reservations = customer.reservation_set.all()[:2]
    today_date = date.today()
    tomorrow_date = date.today() + timedelta(days=1)

    page_title = "Upcoming Reservations"

    context = {
        'customer':customer,
        'reservations':reservations,
        'page_title': page_title,
    }


    template_name = '../templates/user_templates/reservations.html'

    return render(request, template_name, context)

    