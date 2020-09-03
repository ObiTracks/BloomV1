from django.db import models
from django.contrib.auth.models import User
# from django_counter_field import CounterField
# from django_counter_field import CounterMixin, connect_counter
# from .slotclass import Slot
import calendar
from datetime import date, time, timedelta

class Customer(models.Model):
    # user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(default='Person Name', max_length=200, null=True)
    apt = models.IntegerField(default='205', blank=False)
    phone = models.CharField(default='805.555.3809', max_length=200, null=True)
    email = models.CharField(default='someemail@gmail.com', max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    id = models.AutoField(primary_key=True, editable=False)
    lease_members = models.ManyToManyField('self', blank=True)
    notes = models.TextField(max_length=2000, null=True, blank=True)
    
    def __str__(self):
        return "{} ID-{}".format(self.name, self.id)


class Day(models.Model):
    today = date.today()
    tomorrow = today + timedelta(days=1)

    # Fields
    day = models.DateField(default=tomorrow, blank=False) 
    date_created = models.DateField(default=today, blank=False, editable=True)
    notes = models.TextField(max_length=2000, null=True, blank=True)

    class Meta:
        ordering = ['-date_created']

    def name_day(self):
        date = self.day
        year = date.year
        # print(year)
        month = calendar.month_abbr[date.month]
        # print(month)
        day_num = date.day
        # print(day_num)
        dayname = calendar.day_name[date.weekday()]
        # print(dayname)

        return '{}. {}, {}'.format(month, day_num, str(year)[-6:])
    
    def __str__(self):
        return self.name_day()

class TimeSlot(models.Model):
    TIMESLOTS = (
        ('9am-11am','9am-11am'),
        ('12pm-2pm','12pm-2pm'),
        ('3pm-5pm','3pm-5pm'),
    )
    time_slot = models.CharField(max_length=10, null=True, choices=TIMESLOTS, default="Choose a time window")
    day = models.ForeignKey(Day, related_name="timeslot_set", default=Day.objects.first(), null=True, on_delete= models.CASCADE)
    capacity = models.IntegerField(blank=True, default=13, editable=False)
    notes = models.TextField(max_length=2000, null=True, blank=True)
    
    # date = day
    # year = date.day.year
    # print(year)
    # month = calendar.month_abbr[date.month]
    # print(month)
    # day_num = date.day
    # print(day_num)
    # dayname = calendar.day_name[date.weekday()]
    # print(dayname)

    def __str__(self):
        return "{} {}".format(self.day, self.time_slot)

class Reservation(models.Model):
    # Foreign relations
    customer = models.ForeignKey(Customer, related_name="reservation_set", null=True, on_delete= models.CASCADE)
    timeslot = models.ForeignKey(TimeSlot, related_name="reservation_set", null=True, on_delete=models.CASCADE)
    # Details
    no_show = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    notes = models.TextField(max_length=2000, null=True, blank=True)
    # Bring alongs
    party_members = models.ManyToManyField(Customer, related_name="party_members", blank=True)

    def __str__(self):
        return "{}".format(self.timeslot)
    
# class Calculations(models.Model):
#     total_customers = Customer.objects.all().count()
#     total_days = Day.objects.all().count()
#     total_reservations = Reservation.objects.all().count()

#     avg_noshows_past_week = 0
#     count = 0
#     for n in Day.objects.all()[:8]:
#         if n.no_show == True:
#             count
#             avg_noshows_past_week = n.