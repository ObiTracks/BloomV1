from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import inlineformset_factory

from .models import (Customer, Day, TimeSlot, Reservation)
from .forms import *
#****************************************************
# CRUD Views
#****************************************************
# def createReservation(request, pk):
#     ReservationFormSet = inlineformset_factory(Customer, Reservation, fields=('customer','timeslot', 'notes', 'partymembers'), extra=4)
#     customer = Customer.objects.get(id=pk)
#     formset = ReservationFormSet(queryset=Order.objects.none(),instance=customer)
#     # form = OrderForm(initial={'customer':customer})
#     if request.method == 'POST':
#         # print('Printing POST:', request.POST)
#         # form = OrderForm(request.POST)
#         # formset = ReservationFor
#         if formset.is_valid():
#             formset.save()
#             return redirect('/')
            
#     context = {'formset':formset}
#     return render(request, 'accounts/reservation_form.html', context)

def createReservation(request, pk):
	ReservationFormSet = inlineformset_factory(Customer, Reservation, fields=('timeslot','notes'), max_num=1)
	customer = Customer.objects.get(id=pk)
	formset = ReservationFormSet(queryset=Reservation.objects.none(),instance=customer)
	# form = OrderForm(initial={'customer':customer})
	if request.method == 'POST':
		# print('Printing POST:', request.POST)
		# form = OrderForm(request.POST)
		formset = ReservationFormSet(request.POST, instance=customer)
		if formset.is_valid():
			formset.save()
			return redirect('/')

	context = {'formset':formset, 'page_title':'Create Reservation - {}'.format(customer.name), 'customer':customer}
	return render(request, 'CUD/reservation_form.html', context)

def updateReservation(request, pk):
    reservation = Reservation.objects.get(id=pk)
    form = ReservationForm(instance=reservation)
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form,  'page_title':'Update Reservation'}
    return render(request, 'CUD/reservation_form.html', context)


def deletePage(request, pk):
    reservation = Reservation.objects.get(id=pk)
    if request.method == 'POST':
        reservation.delete()
        return redirect('/')

    context = {'item':reservation}
    template_name = 'CUD/delete.html'
    return render(request, template_name, context)

#****************************************************
# Main views
#****************************************************
def home_page(request):
    days = Day.objects.all()
    residents = Customer.objects.all()
    #Next day Information
    next_day = days.last()
    next_day_slots = next_day.timeslot_set.all()
    print(days)
    print(next_day_slots)
    # slot_reservations 
    # timeslots_tomorrow = next_day.timeslot_set()

    #Present day information
    present_day = days[0]
    present_day_slots = present_day.timeslot_set.all()
    total_days = days.count()


    page_title = "Dashboard"
    # total_reservations = timeslots.reservation_set.all().count()

    context = {'days':days, 'next_day':next_day, 'next_day_slots':next_day_slots, 'present_day':present_day, 'present_day_slots':present_day_slots, 'total_days':total_days, "residents":residents, "page_title":page_title}
    template_name = 'home.html'
    
    return render(request, template_name, context)

#****************************************************
# Customer views
#****************************************************
def customer(request, pk):
    resident = Customer.objects.get(id=pk)
    reservations = resident.reservation_set.all()
    page_title = "Customer " + resident.name
    context = {"page_title":page_title, 'resident':resident, 'reservations':reservations}
    template_name = 'customer/customer_info.html'
    
    return render(request, template_name, context)

def customers_all(request):
    residents = Customer.objects.all()
    page_title = "All Customers"
    context = {"page_title":page_title, 'residents':residents}
    template_name = 'customer/customers_all.html'
    
    return render(request, template_name, context)

#****************************************************
# Day views
#****************************************************
def day(request, pk):
    day = Day.objects.get(id=pk)
    stats = {'stat1':{'name':'Total Reservations','value':day}}
    page_title = "Day "+ str(day.day)
    context = {"page_title":page_title,'day':day, 'stats':stats}
    template_name = 'day/day_info.html'
    
    return render(request, template_name, context)

def days_all(request):
    days = Day.objects.all()
    page_title = "All Days"
    context = {"page_title":page_title, 'days':days}
    template_name = 'day/days_all.html'
    
    return render(request, template_name, context)

#****************************************************
# Timeslot views
#****************************************************
def timeslot(request):
    context = {}
    template_name = 'timeslot/timeslot_info.html'
    
    return render(request, template_name, context)

def timeslots_all(request):
    timeslots = TimeSlot.objects.all()
    page_title = "All TimeSlots"
    context = {"page_title":page_title, 'timeslots':timeslots}
    template_name = 'timeslot/timeslots_all.html'
    
    return render(request, template_name, context)

#****************************************************
# Reservation views
#****************************************************
def reservation(request):
    context = {}
    template_name = 'reservation/reservation_info.html'
    
    return render(request, template_name, context)
