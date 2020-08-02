from django.db import models
# from django_counter_field import CounterField
# from django_counter_field import CounterMixin, connect_counter
# from .slotclass import Slot
import datetime

class PoolDay(models.Model):
    date = models.CharField(default="July 30th 2020 (Just Text)", max_length=50)
    day_notes = models.TextField(null=True, default="Todays Notes: ")
    # date = models.DateField(default="Friday")
    # date = models.DateField()
    # timeslot_count = CounterField()

class TimeSlot(models.Model):
    PoolDay = models.ForeignKey(PoolDay, on_delete=models.CASCADE)
    time = models.IntegerField()
    pool_status = models.BooleanField(default="Full")
    # time_window = models.DateTime()

class Reservation(models.Model):
    TimeSlot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    # date = datetime.date.tomorrow()
    party = models.TextField(blank=True)
    party_size = models.IntegerField(blank=True)
    condition = models.TextField(default="Not Full")
    # creation_stamp = models.TimeField(auto_now_add=True)
