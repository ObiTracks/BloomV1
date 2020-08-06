from django.contrib import admin

# Register your models here.

from .models import Customer, Day, TimeSlot, Reservation

admin.site.register(Customer)
admin.site.register(Day)
admin.site.register(TimeSlot)
admin.site.register(Reservation)