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
from calendar import weekday, week
from ..views.views_a_base import total_reservations

#View imports here
from ..models import (Customer, Day, TimeSlot, Reservation)
from ..forms import *
from ..filters import CustomerFilter


def customer(request, pk):
    resident = Customer.objects.get(id=pk)
    reservations = resident.reservation_set.all()
    page_title = "Resident Profile ↓".format(resident.first_name, resident.last_name)

    # Dates
    today_date = date.today()
    yesterday_date = date.today() - timedelta(days=1)
    tomorrow_date = date.today() + timedelta(days=1) 

    stats = {
        'stat1': {
            'title': 'Lifetime Reservations',
            'value': reservations.count()
        },
    }

    context = {
        'stats':stats,
        "page_title": page_title,
        'resident': resident,
        'reservations': reservations,
        'today_date': today_date,
        'yesterday_date':yesterday_date,
        'tomorrow_date':tomorrow_date
    }
    template_name = 'object_templates/customer.html'

    return render(request, template_name, context)

def day(request, pk):
    today = datetime.date.today
    day = Day.objects.get(id=pk)

    # DATE FORMATTING
    date = day.day
    year = date.year
    month = calendar.month_abbr[date.month]
    day_num = date.day
    dayname = calendar.day_name[date.weekday()]

    timeslots = day.timeslot_set.all()
    num_reservations = 0
    num_noshows = 0
    for timeslot in timeslots:
        n = timeslot.reservation_set.all()
        num_reservations += n.count()

        for r in n:
            if r.no_show == True:
                num_noshows += 1

    print(num_reservations)
    
    stats = {
        'stat1': {
            'title': 'Total Reservations',
            'value': num_reservations
        },
        'stat2': {
            'title': 'Notes',
            'value': day.notes
        }
    }


    page_title = '{}, {}. {}'.format(dayname, month, day_num)
    bg_title = 'Day'
    context = {
        'page_title': page_title, 
        'day': day, 'stats': stats, 
        'today':today,
        'bg_title':bg_title
        }
    template_name = 'object_templates/day.html'

    return render(request, template_name, context)

def timeslot(request, pk):
    timeslot = TimeSlot.objects.get(id=pk)
    page_title = "All Days"
    stats = {
        'stat1': {
            'title': 'Total Reservations',
            'value': timeslot.reservation_set.count
        },
        'stat2': {
            'title': 'Total No Shows',
            'value': 'some_value'
        }
    }

    context = {
        'timeslot':timeslot,
        'page_title': page_title,
        'stats': stats
        }
    template_name = 'object_templates/timeslot.html'

    return render(request, template_name, context)

def reservation(request):
    context = {}
    template_name = 'object_templates/reservation.html'

    return render(request, template_name, context)