from django.db import models
# from django_counter_field import CounterField
# from django_counter_field import CounterMixin, connect_counter
# from .slotclass import Slot
import datetime, calendar

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    apt_number = models.IntegerField(default=0, blank=False)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    lease_members = models.ManyToManyField('self', blank=True)
    
    def __str__(self):
        return self.name


class Day(models.Model):
    # Time information about today
    today = datetime.date.today()
    today_day = today.day
    today_weekday = calendar.day_name[today.weekday()]
    today_month = calendar.month_name[today.month]

    # Time information about tomorrow
    tomorrow = today + datetime.timedelta(days=1)
    tomorrow_day = tomorrow.day
    tomorrow_weekday = calendar.day_name[tomorrow.weekday()]
    tomorrow_month = calendar.month_name[tomorrow.month]

    # Fields
    date = models.DateField(default=tomorrow)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    string_date = calendar.day_name[datetime.date.today().weekday()]


    def __str__(self):
        return "{} {} {} | Created on {}".format(
            self.tomorrow_weekday,
            self.tomorrow_month,
            self.tomorrow_day,
            self.date_created
            )

class TimeSlot(models.Model):
    time_slot = models.CharField(max_length=10, null=True, default="Choose a time window")
    day = models.ForeignKey(Day, null=True, on_delete= models.SET_NULL)
    pool_status_full = models.BooleanField(default=False, verbose_name='Time slot at capacity')
    capacity = models.IntegerField(blank=True, default=13)
    num_reservations = "Current space: 3 spots left"

    def __str__(self):
        return self.time_slot

class Reservation(models.Model):
    # Basic information
    customer = models.ForeignKey(Customer, related_name="customer", null=True, on_delete= models.SET_NULL)
    timeslot = models.ForeignKey(TimeSlot, null=True, on_delete= models.SET_NULL)

    # Bring alongs
    party_members = models.ManyToManyField(Customer, related_name="party_members", blank=True)


    # Details
    no_show = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return "{} for {} for {} people".format(self.timeslot.time_slot, self.customer, "3")