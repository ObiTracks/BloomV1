from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import (Customer, Day, TimeSlot, Reservation)

def customers_all_page(request):
    residents = Customer.objects.all()
    page_title = "All Customers"
    context = {"page_title":page_title, 'residents':residents}
    template_name = 'customer/customers_all.html'
    
    return render(request, template_name, context)

def days_all_page(request):
    days = Day.objects.all()
    page_title = "All Days"
    context = {"page_title":page_title, 'days':days}
    template_name = 'day/days_all.html'
    
    return render(request, template_name, context)
    
def timeslots_all_page(request):
    timeslots = TimeSlot.objects.all()
    page_title = "All TimeSlots"
    context = {"page_title":page_title, 'timeslots':timeslots}
    template_name = 'timeslot/timeslots_all.html'
    
    return render(request, template_name, context)

