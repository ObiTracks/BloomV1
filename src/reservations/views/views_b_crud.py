from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

#View imports here
from ..models import (Customer, Day, TimeSlot, Reservation)
from ..forms import *
from ..filters import CustomerFilter
from ..logic import reservation_exists

def createReservation(request, tk, pk, *args, **kwargs):
    customer = Customer.objects.get(id=pk)
    current_user = request.user
    current_user_id = current_user.id
    print(current_user)

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
            num_res = timeslot.reservation_set.all().count()
            if timeslot != None:
                if num_res < timeslot.capacity:
                    form.save()
                    return redirect('/')
                else:
                    print("Timeslot at capacity of {}".format(num_res))
    #

    stats = {
        'stat1': {
            'title': 'Total Days',
            'value':'some'
        },
        'stat2': {
            'title': 'Total Reservations',
            'value':''
        },
        'stat3': {
            'title': 'Total Residents',
            'value':''
        },
        'stat4': {
            'title': 'Avg No Shows per Day',
            'value':''
        }
    }

    context = {
        'form': form,
        'page_title': 'New Reservation',
        'customer': customer,
        'time_slot': timeslot
    }
    return render(request, '../templates/crud_templates/reservation_form.html', context)

def updateReservation(request, pk):
    reservation = Reservation.objects.get(id=pk)
    form = ReservationForm(instance=reservation)
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form, 'page_title': 'Update Reservation'}
    return render(request, '../templates/crud_templates/reservation_form.html', context)

def updateResident(request, pk):
    resident = Customer.objects.get(id=pk)
    form = ReservationForm(instance=resident)
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = ReservationForm(request.POST, instance=resident)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form, 'page_title': "Update {}'s ".format(resident.name), 'resident':resident}
    return render(request, '../templates/crud_templates/customer_form.html', context)

def deletePage(request, pk):
    reservation = Reservation.objects.get(id=pk)
    if request.method == 'POST':
        reservation.delete()
        return redirect('/')
        
    context = {'item': reservation}
    template_name = '../templates/crud_templates/delete.html'
    return render(request, template_name, context)