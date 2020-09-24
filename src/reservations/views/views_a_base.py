from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404, HttpResponse
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
from ..decorators import unauthenticated_user, allowed_users

def total_reservations(days):
    count = 0
    for day in days:
        timeslots = day.timeslot_set.all()
        for timeslot in timeslots:
            count += timeslot.reservation_set.count()
    
    return total_reservations

@login_required(login_url='login')
@allowed_users(allowed_roles=['Manager','Staff','SiteAdmin'])
def home_page(request):
    # if Day.objects.all() == None or Day.objects.count() <= 2:
    #     return HttpResponse("<html><h1>There are not enough days available to book</h1></html>")
    # else:
    #     days = Day.objects.all()[:3]
    current_user = request.user
    print(current_user)
    user_company = current_user.customer.company
    print(user_company)
    days = user_company.day_set


    residents = user_company.customer_set.all()[:20]
    total_residents = residents.count()
    total_days = days.count()

    # Dates
    today_date = date.today()
    yesterday_date = date.today() - timedelta(days=1)
    tomorrow_date = date.today() + timedelta(days=1)   

    if days.count() < 3:
        days = days.all()
    else:
        
        today_day = days.get(day=today_date)
        tomorrow_day = days.get(day=tomorrow_date)
        # print(days.filter(day=yesterday_date).exists())
        if days.filter(day=yesterday_date).exists() != False:
            yesterday_day = days.get(day=yesterday_date)
            days = [tomorrow_day, today_day,yesterday_day]
        else:
            days = [tomorrow_day, today_day]
            print(yesterday_date)

    page_title = "Dashboard"
    stats = {
        'stat1': {
            'title': 'Total Days',
            'value': total_days
        },
        'stat2': {
            'title': 'Total Reservations',
            'value': "Some value"
        },
        'stat3': {
            'title': 'Total Residents',
            'value': total_residents
        },
    }

    context = {
        'page_title': page_title,
        'days': days,
        'stats': stats,
        'residents':residents,
        'total_days': total_days,
        'today_date': today_date,
        'yesterday_date':yesterday_date,
        'tomorrow_date':tomorrow_date
    }


    template_name = '../templates/base_templates/home.html'

    return render(request, template_name, context)

    