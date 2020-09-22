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
from ..filters import CustomerFilter, DayFilter


def customers(request, tk):
    residents = Customer.objects.all().order_by('-date_created')
    myFilter = CustomerFilter(request.GET, queryset=residents)
    residents = myFilter.qs

    paginator = Paginator(residents, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if tk != 'None':
        timeslot = TimeSlot.objects.get(id=tk)
        time_id = tk
    else:
        timeslot = None
        time_id = tk

    stats = {
        'stat1': {
            'title': 'Total Residents',
            'value': Customer.objects.all().count()
        },
    }

    page_title = "All Residents"
    context = {
        "page_title": page_title,
        'residents': residents,
        'time_id': time_id,
        'stats':stats,
        'myFilter':myFilter,
        'page_obj':page_obj
    }
    template_name = 'list_templates/customers.html'

    return render(request, template_name, context)

def days(request):
    days = Day.objects.all().order_by('-day')
    myFilter = DayFilter(request.GET, queryset=days)
    days = myFilter.qs

    paginator = Paginator(days, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    stats = {
        'stat1': {
            'title': 'Total Days',
            'value': days.count
        },
        'stat2': {
            'title': 'Total Reservations',
            'value': 'some_value'
        },
        'stat3': {
            'title': 'Total Residents',
            'value': 'some_value'
        },
        'stat4': {
            'title': 'Avg No Shows per Day',
            'value': 'some_value'
        }
    }

    page_title = "All Days"
    context = {
        'page_title': page_title,
        'days': days,
        'stats': stats,
        'myFilter':myFilter,
        'page_obj':page_obj
    }
    template_name = 'list_templates/days.html'

    return render(request, template_name, context)

