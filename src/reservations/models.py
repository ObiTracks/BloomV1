from django.db import models
# from django_counter_field import CounterField
# from django_counter_field import CounterMixin, connect_counter
# from .slotclass import Slot
import datetime

class PoolDay(models.Model):
    # date = models.DateField()
    # status = "Pool Reservations on {}".format(date)
    # timeslot_count = CounterField()
    title = models.CharField(max_length=120)

class TimeSlot(models.Model):
    PoolDay = models.ForeignKey(PoolDay, on_delete=models.CASCADE)
    # time_window = models.DateTime()

class Reservation(models.Model):
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    date = datetime.date.tomorrow()
    party = models.TextField(blank=True)
    party_size = models.IntegerField(blank=True)
