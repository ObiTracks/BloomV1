from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import (Customer, Day, TimeSlot, Reservation)

def home_page(request):
    next_day = Day.objects.last()
    days = Day.objects.all().count()
    present_day = None
    if days >= 2:
        present_day = Day.objects.all()[-2]

    timeslots = Day.timeslot_set

    # total_reservations = timeslots.reservation_set.all().count()

    context = {'next_day':next_day, 'present_day':present_day, "timeslots":timeslots}
    template_name = 'home.html'
    
    return render(request, template_name, context)
    
def dayinfo_page(request):
    context = {}
    template_name = 'home.html'
    
    return render(request, template_name, context)

def timeslot_page(request):
    context = {}
    template_name = 'home.html'
    
    return render(request, template_name, context)

def reservation_page(request):
    context = {}
    template_name = 'home.html'
    
    return render(request, template_name, context)
