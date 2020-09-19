from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from account.models import Account
from django.conf import settings
User = settings.AUTH_USER_MODEL
from django.contrib.auth.models import Group
# from django.contrib.auth.models import User


from .models import *

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
        exclude = ['no_show']

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Enter a valid email address')
    group = forms.ModelChoiceField(queryset=Group.objects.all(),
                                   required=False)
    class Meta:
        model = Account
        fields = ('first_name','last_name','email','apt','password1','password2','group')