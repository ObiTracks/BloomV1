from django.forms import ModelForm
from .models import *

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
