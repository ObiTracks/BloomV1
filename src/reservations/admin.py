from django.contrib import admin

# Register your models here.

from .models import Company, Customer, LeaseMember, Day, TimeSlot, Reservation

admin.site.register(Company)
admin.site.register(Customer)
admin.site.register(LeaseMember)
admin.site.register(Day)
admin.site.register(TimeSlot)
admin.site.register(Reservation)