from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import inlineformset_factory
from datetime import date
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from time import sleep
#View imports here
from ..models import (Customer, Day, TimeSlot, Reservation)
from ..forms_user import *
from ..filters import CustomerFilter
from ..tools import *
from ..decorators import unauthenticated_user, allowed_users


@login_required(login_url='login')
def home_page(request):
    if Day.objects.all() == None or Day.objects.count() < 2:
        return HttpResponse("<html>There are not enough days avaialable to book</html>")
    else:
        customer = request.user.customer
        company = customer.company
        days = company.day_set.all()

        today_date = date.today()
        tomorrow_date = date.today() + timedelta(days=1)

        today_day = days.filter(day=today_date).exists()
        tomorrow_day = days.filter(day=tomorrow_date).exists()
        
        temp_list = []

        if tomorrow_day != False:
            tomorrow_day = days.get(day=tomorrow_date)
            temp_list.append(tomorrow_day)
        if today_day != False:
            today_day = days.get(day=today_date)
            temp_list.append(today_day)
        days = temp_list
        print(days)


        page_title = "Resident Dashboard"
        context = {
            'days':days,
            'customer':customer,
            'page_title': page_title,
            'today_date':today_date,
            'tomorrow_date':tomorrow_date
        }
        template_name = '../templates/user_templates/home.html'
    

    return render(request, template_name, context)

@login_required(login_url='login')
def profilePage(request):
    resident = request.user.customer
    total_reservations = resident.reservation_set.count()
    page_title = "Profile"

    context = {
        'resident':resident,
        'total_reservations':total_reservations,
        'page_title': page_title,
    }

    template_name = '../templates/user_templates/profile.html'

    return render(request, template_name, context)

    
@login_required(login_url='login')
def createReservation(request, tk, pk, *args, **kwargs):
    current_user = request.user
    customer = current_user.customer
    company = current_user.customer.company
    timeslot = TimeSlot.objects.get(id=tk)

    form = LeaseMemberReservationForm(customer)

    # CREATING RESERVATION FROM FORM POST DATA Creating for creating a reservation from post data
    if request.method == 'POST':
        form = LeaseMemberReservationForm(customer, request.POST)
        print(form.data)

        if form.is_valid():
            party_members = form.cleaned_data.get("set_lease_members")
            res_exists = multipleBookingCheck(request, timeslot, customer)
            print("Does this reservation exist? ", res_exists)

            if res_exists == True:
                messages.error(request,"You already have a reservation booked for today".format(customer))
                # return redirect('/user')
            else:
                current_capacity = timeslot.getCurrentCapacity()   
                if current_capacity < timeslot.capacity:
                    reservation = Reservation.objects.create(
                        company=company,
                        customer = customer,
                        timeslot=timeslot,
                    )
                    # reservation.save()
                    # form.save()
                    reservation.company = company
                    print('************RESERVATION**************')
                    if party_members != None:
                        for person in party_members:
                            print(reservation.party_members.add(person))
                            # print(person.fullname)
                            
                    reservation.save()

                    messages.success(request,"Successfully booked your reservation at {}. Remember to show up or delete your reservation to be courteous of attendance".format(timeslot))
                    group = request.user.groups.first().name
                    print(group)

                    # if request.user.groups.first().name == "Resident":
                    return redirect('reservations')
                    # else:
                        # return redirect('/staff')
                else:
                    messages.error(request,"Timeslot at capacity of {}".format(current_capacity))
    #

    stats = {}

    context = {
        'form':form,
        'page_title': 'Create a reservation',
        'customer': customer,
        'time_slot': timeslot
    }
    return render(request, '../templates/user_templates/reservation_form_user.html', context)


    
@login_required(login_url='login')
# @allowed_users(allowed_roles=['Manager','Staff','SiteAdmin','Resident'])
def deleteReservationUser(request, pk):
    reservation = Reservation.objects.get(id=pk)
    day_id = reservation.timeslot.day.id
    if request.method == 'POST':
        reservation.delete()
        messages.success(request,"Reservation successfully deleted (user side) {}".format(reservation))
        # return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        return redirect('home')
        
    context = {'item': reservation}
    template_name = '../templates/user_templates/delete_reservation_user.html'
    return render(request, template_name, context)

    
@login_required(login_url='login')
def reservationsPage(request):
    resident = request.user.customer
    reservations = resident.reservation_set.all()[:2]
    today_date = date.today()
    tomorrow_date = date.today() + timedelta(days=1)

    page_title = "Upcoming Reservations"

    context = {
        'resident':resident,
        'reservations':reservations,
        'page_title': page_title,
        'today_date':today_date,
    }


    template_name = '../templates/user_templates/reservations.html'

    return render(request, template_name, context)

    