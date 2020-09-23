from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from account.models import Account
from django.conf import settings
User = settings.AUTH_USER_MODEL
from django.contrib.auth.models import Group
from itertools import chain

# Date picker imports
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})
from bootstrap_datepicker_plus import DatePickerInput
from django import forms

import datetime

from .models import *

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class ReservationForm(ModelForm):
    # def __init__(self, *args, **kwargs): 
    #     self.user = kwargs.pop('user')
        # timeless30 = datetime.datetime.now() - datetime.timedelta(seconds=3610)
        # timeless30 = timeless30.replace(tzinfo=pytz.utc)

        # if date_joined > timeless30:
        #     self.fields['currentCharities'] = forms.ModelChoiceField(queryset=Charity.objects.filter(enabled=1))
        # ...

    class Meta:
        model = Reservation
        fields = ('customer','timeslot','notes')
        exclude = ['no_show']

class CreateCompanyForm(ModelForm):
    first_name = forms.CharField(max_length=60, required=True)
    last_name = forms.CharField(max_length=60, required=True)
    email = forms.CharField(max_length=200, required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Company
        fields = ('company_name','company_email','city','address_line','zip_code','country','first_name','last_name','email','password')
    
class CreateUserForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Enter a valid email address')
    group = forms.ModelChoiceField(queryset=Group.objects.all(),
                                   required=False)
    class Meta:
        model = Account
        fields = ('first_name','last_name','email','apt','password1','password2','group')
    
class AddDayForm(ModelForm):
    # day = forms.DateField(widget=DateInput(), initial=datetime.date.today)
    day = forms.DateField(widget=DatePickerInput(format='%m/%d/%Y', attrs={'placeholder':'YYYY-MM-DD'}))

    class Meta:
        model = Day
        fields = ('day','notes')