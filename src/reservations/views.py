from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .models import PoolDay

def home_page(request):
    # id = models.IntegerField() #px
    context = {
    "home_title":"Pool Reservations",
    "reservations":"5 Reservations",
    "my_list":[1,2,3,4,5]
    }
    # qs = Time_Slot.objects.all()
    template_name = 'home.html'
    
    return render(request, template_name, context)

# def reservations_page(request):
#     # id = models.IntegerField() #px
#     context = {
#     "home_title":"Pool Reservations",
#     "time_slot":"12-2pm"
#     }

#     return render(request, "reservations.html", context)

# def booked_page(request):
#     # id = models.IntegerField() #px
#     context = {
#     "home_title":"Pool Reservations",
#     "time_slot":"12-2pm"
#     }
    
    # return render(request, "verified_res.html", context)

