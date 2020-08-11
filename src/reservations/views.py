from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import (Customer, Day, TimeSlot, Reservation)

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

def customer_page(request, pk):
    resident = Customer.objects.get(id=pk)
    reservations = resident.reservation_set.all()
    page_title = "Customer " + resident.name
    context = {"page_title":page_title, 'resident':resident, 'reservations':reservations}
    template_name = 'customer/customer_info.html'
    
    return render(request, template_name, context)
    
def day_page(request):
    context = {}
    template_name = 'day/day_info.html'
    
    return render(request, template_name, context)

def timeslot_page(request):
    context = {}
    template_name = 'timeslot/timeslot_info.html'
    
    return render(request, template_name, context)

def reservation_page(request):
    context = {}
    template_name = 'reservation/reservation_info.html'
    
    return render(request, template_name, context)
