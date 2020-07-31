from django.contrib import admin

# Register your models here.

from .models import PoolDay, TimeSlot, Reservation

admin.site.register(PoolDay)
admin.site.register(TimeSlot)
admin.site.register(Reservation)