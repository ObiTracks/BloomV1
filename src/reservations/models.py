from django.db import models
# from .slotclass import Slot
import datetime

class PoolDay(models.Model):
    # date = models.DateField()
    # status = "Pool Reservations on {}".format(date)
    title = models.CharField(max_length=120)

# class Time_Slot(models.Model):
#     pool_date = models.ForeignKey(Pool_Day, on_delete=models.CASCADE)
#     time_window = models.DateTime()

# class Reservation(models.Model):
#     time_slot = ForeignKey(Time_Slot, on_delete=models.CASCADE)
#     date = datetime.date.tomorrow()
#     party = models.TextField(blank=True)
#     party_size = models.IntegerField(blank=True)
