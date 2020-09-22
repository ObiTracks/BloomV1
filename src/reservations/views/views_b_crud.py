from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import datetime

#View imports here
from ..models import (Customer, Day, TimeSlot, Reservation)
from ..forms import *
from ..filters import CustomerFilter
from ..logic import reservation_exists
from ..decorators import unauthenticated_user, allowed_users

@login_required(login_url='login')
@allowed_users(allowed_roles=['manager','staff','SiteAdmin'])
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
            print(request.POST)
            timeslot_id = request.POST.get('timeslot')
            timeslot = TimeSlot.objects.get(pk=timeslot_id)
            print(timeslot)
            if request.POST.get('timeslot') != None:
                num_res = timeslot.reservation_set.all().count()
                if num_res < timeslot.capacity:
                    form.save()
                    return redirect('/reservations')
                else:
                    print("Timeslot at capacity of {}".format(num_res))
    #

    stats = {}

    context = {
        'form': form,
        'page_title': 'New Reservation',
        'customer': customer,
        'time_slot': timeslot
    }
    return render(request, '../templates/crud_templates/reservation_form.html', context)


def dayValidation(request, form):
    is_valid = False
    cleaned_data = form.cleaned_data
    day = cleaned_data['day']
    day_exists = Day.objects.filter(day=day).exists()
    today = datetime.date.today()

    if day >= today:
        print(day_exists)
        if day_exists == False:
            is_valid = True
            messages.success(request, "New day added {}".format(day))
        else:
            messages.error(request, 'This day already exists: {}'.format(day))
    else:
        messages.error(request, "The selected day must be in the future")

    return is_valid

# def createFollowingDay(request, form):
#     most_recent_day = Day.objects.first()
#     print(most_recent_day)
#     return

@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager','SiteAdmin'])
def createDay(request, *args, **kwargs):
    
    TIMESLOTS = TimeSlot.TIMESLOTS
    print(TIMESLOTS)
    form = AddDayForm()
    if request.method == 'POST':
        form = AddDayForm(request.POST)
        if form.is_valid():
            if dayValidation(request, form) is True:
                day = form.save()
                # createFollowingDay(request, form)
                for slot in TIMESLOTS:
                    timeslot = TimeSlot.objects.create(day=day, time_slot=slot[0])
                    print(timeslot)

            return redirect('days')

    stats = {}

    context = {
        'form': form,
        'page_title': 'New Reservation',
    }
    return render(request, '../templates/crud_templates/day_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['manager','staff','SiteAdmin'])
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['manager','staff','SiteAdmin'])
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager','Staff','SiteAdmin'])
def deleteDay(request, pk):
    day = Day.objects.get(id=pk)
    if request.method == 'POST':
        day.delete()
        return redirect('/staff/')
        
    context = {'item': day}
    template_name = '../templates/crud_templates/delete_day.html'
    return render(request, template_name, context)