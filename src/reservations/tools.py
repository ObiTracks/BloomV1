
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import (Customer, Day, TimeSlot, Reservation)
from datetime import date, time, timedelta

def multipleBookingCheck(request, timeslot, customer):
    timeslot_day = timeslot.day
    res_exists = False
    i = 0

    while i < timeslot_day.timeslot_set.count() and res_exists == False:
        slot = timeslot_day.timeslot_set.all()[i]
        res_exists = slot.reservation_set.filter(customer=customer).exists()
        
        i += 1

    return res_exists

def autoTimeSlots(TIMESLOTS, company, num_days):
    today_date = date.today()
    tomorrow_date = date.today() + timedelta(days=1)

    previous_day = company.day_set.first()

    if previous_day.timeslot_set.count() == 0:
        next_day = previous_day.day
    else:
        next_day = previous_day.day + timedelta(days=1)

    for i in range(0,num_days):
        day_object = Day.objects.create(
            company = company,
            day = next_day
        )
        
        threeTimeslots(TIMESLOTS, day_object)

        next_day = next_day + timedelta(days=1)
    return

def threeTimeslots(TIMESLOTS, day):
    for slot in TIMESLOTS:
            timeslot = TimeSlot.objects.create(day=day, time_slot=slot[0])
            print(timeslot)
    
def t_res(company):
    reservations = company.reservation_set.all()
    t_reservations = reservations.count()

    for reservation in reservations:
        party_size = reservation.party_members.count()
        t_reservations += party_size
    
    return t_reservations
