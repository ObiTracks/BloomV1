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

@login_required(login_url='login')
def home_page(request):
    days = Day.objects.all().reverse()[:2]
    residents = Customer.objects.all()[:20]
    today_date = date.today()

    total_days = days.count()
    total_residents = Customer.objects.all().count
    total_reservations = Reservation.objects.all().count

    page_title = "Dashboard"
    stats = {
        'stat1': {
            'title': 'Total Days',
            'value': total_days
        },
        'stat2': {
            'title': 'Total Reservations',
            'value': total_reservations
        },
        'stat3': {
            'title': 'Total Residents',
            'value': total_residents
        },
        'stat4': {
            'title': 'Avg No Shows per Day',
            'value': 'some_value'
        }
    }

    context = {
        'page_title': page_title,
        'days': days,
        'today_date': today_date,
        'stats': stats,
        'residents':residents,
        'total_days': total_days
    }


    template_name = '../templates/base_templates/home.html'

    return render(request, template_name, context)

    