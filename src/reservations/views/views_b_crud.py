from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import inlineformset_factory
from django.contrib import messages
import datetime

#View imports here
from ..models import (Customer, Day, TimeSlot, Reservation)
from ..forms import *
from ..filters import CustomerFilter
from ..decorators import unauthenticated_user, allowed_users

@login_required(login_url='login')
@allowed_users(allowed_roles=['manager','staff','SiteAdmin'])
def createReservation(request, tk, pk, *args, **kwargs):
    current_user = request.user
    current_user_id = current_user.id
    print(current_user)

    # Check to pass through a prefilled timeslot if it recieves an id for one
    
    customer = Customer.objects.get(id=pk)
    if tk != 'None':
        print("Path A")
        timeslot = TimeSlot.objects.get(id=tk)
        form = ReservationForm(initial={
            'customer': customer,
            'timeslot': timeslot
        })
    else:
        print("Path B")
        timeslot = None
        form = ReservationForm(initial={
            'customer': customer,
        })
        # print('Path B: tk=' + tk)

    def multipleBookingCheck(timeslot, customer):
        timeslot_day = timeslot.day
        for slot in timeslot_day.timeslot_set.all():
            res_exists = slot.reservation_set.filter(customer=customer).exists()
            if res_exists == True:
                messages.error(request,"{} has already booked a timeslot for this day".format(customer))
                return redirect('/staff')
        return res_exists

    # def capacityCheck(timeslot,customer,lease_member_form):

    lease_member_form = LeaseMemberReservationForm(request.user)
    # CREATING RESERVATION FROM FORM POST DATA Creating for creating a reservation from post data
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        lease_member_form = LeaseMemberReservationForm(request.user, request.POST)
        print(lease_member_form)

        if form.is_valid():
            print(request.POST)
            timeslot_id = request.POST.get('timeslot')
            timeslot = TimeSlot.objects.get(pk=timeslot_id)
            
            if request.POST.get('timeslot') != None:
                res_exists = multipleBookingCheck(timeslot, customer)
                if res_exists == False:
                    num_res = timeslot.reservation_set.all().count()
                    if num_res < timeslot.capacity:
                        form.save()
                        # for person in lease_member_form:
                        #     person_name
                        #     Reservation.objects.create()
                        messages.success(request,"Reservation created for {} at {}".format(customer,timeslot))
                        return redirect('/staff')
                    else:
                        print("Timeslot at capacity of {}".format(num_res))
    #

    stats = {}

    context = {
        'form': form,
        'lease_member_form':lease_member_form,
        'page_title': 'New Reservation',
        'customer': customer,
        'time_slot': timeslot
    }
    return render(request, '../templates/crud_templates/reservation_form.html', context)


def dayValidation(request, form):
    is_valid = False
    cleaned_data = form.cleaned_data
    day = cleaned_data['day']
    
    current_user = request.user
    user_company = current_user.customer.company
    days = user_company.day_set

    day_exists = days.filter(day=day).exists()
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
                user_company = request.user.customer.company
                day = form.save()
                day.company = user_company
                day.save()
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
@allowed_users(allowed_roles=['Manager','Staff','SiteAdmin'])
def deleteDay(request, pk):
    day = Day.objects.get(id=pk)
    if request.method == 'POST':
        day.delete()
        return redirect('/staff/')
        
    context = {'item': day}
    template_name = '../templates/crud_templates/delete_day.html'
    return render(request, template_name, context)

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
            return redirect('/staff')

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

