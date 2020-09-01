from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import inlineformset_factory
from datetime import date
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#View imports here
from ..models import (Customer, Day, TimeSlot, Reservation)
from ..forms import *
from ..filters import CustomerFilter

def createReservation(request, tk, pk, *args, **kwargs):
    customer = Customer.objects.get(id=pk)
    if tk != 'None':
        timeslot = TimeSlot.objects.get(id=tk)
        # print('Path A: tk='+ tk)
    else:
        timeslot = None
        # print('Path B: tk=' + tk)

    if timeslot != None:
        # form = ReservationForm(initial={'customer': customer, 'timeslot':timeslot})
        form = ReservationForm(initial={
            'customer': customer,
            'timeslot': timeslot
        })
    else:
        form = ReservationForm(initial={
            'customer': customer,
        })

    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
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
    num_stats = len(stats)
    test_dict = {'One':'1', 'Two':'2'}
    print('Number of statistics' + str(len(test_dict)))
    print(stats)
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
    return render(request, 'CUD/reservation_form.html', context)

def deletePage(request, pk):
    reservation = Reservation.objects.get(id=pk)
    if request.method == 'POST':
        reservation.delete()
        return redirect('/')

    context = {'item': reservation}
    template_name = 'CUD/delete.html'
    return render(request, template_name, context)