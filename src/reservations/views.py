from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404

# from .models import PoolDay, TimeSlot, Reservation

def home_page(request):
    context = {
    # "object":obj,
    "home_title":"Pool Reservations",
    "reservations":"5 Reservations"
    }
    template_name = 'home.html'
    
    return render(request, template_name, context)

def reservation_page(request):
    # id = models.IntegerField() #px
    context = {
    "home_title":"Add Reservations for {}".format("12-2"),
    "time_slot":"12-2pm"
    }
    template_name = 'timeslot.html'

    return render(request, template_name, context)

def confirmation_page(request):
    # id = models.IntegerField() #px
    # obj = get_object_or_404(Reservation, slug=id)
    # obj = get_object_or_404(Reservation)
    context = {
    "object":obj,
    "reservation_date":"Pool Reservations",
    "time_slot":"12-2pm",
    "party_size":"5 people",
    "people_in_party": "X person, X person, X person"
    }
    template_name = "confirmation_page.html"
    
    return render(request, template_name, context)

