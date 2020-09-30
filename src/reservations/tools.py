from .models import (Customer, Day, TimeSlot, Reservation)
from datetime import date, time, timedelta

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

def threeTimeslots(TIMESLOTS, day):
    for slot in TIMESLOTS:
            timeslot = TimeSlot.objects.create(day=day, time_slot=slot[0])
            print(timeslot)
    
