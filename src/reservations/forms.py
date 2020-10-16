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

# RESERVATIONS
class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ('customer','timeslot','notes')
        exclude = ['no_show']

class LeaseMemberReservationForm(ModelForm):
    # full_name = forms.CharField(max_length=100,)
    # set_lease_members = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=None)

    def __init__(self, customer, *args, **kwargs):
        super(LeaseMemberReservationForm, self).__init__(*args, **kwargs)
        self.customer = customer
        self.lease_members = self.customer.lease_member_set.all()
        print("The user for this form is" + str(customer))
        # self.fields.append(set_lease_members)
        self.fields['set_lease_members'] = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=self.lease_members)
        print(self.fields['set_lease_members'])
        
        

    # print(lease_members)
    # set_lease_members = forms.ModelMultipleChoiceField()
    
    class Meta:
        model = LeaseMember
        fields = ()


class CreateCompanyForm(ModelForm):
    first_name = forms.CharField(max_length=60, required=True)
    last_name = forms.CharField(max_length=60, required=True)
    email = forms.CharField(max_length=200, required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Company
        fields = ('company_name','company_email','city','address_line','zip_code','country','pool_capacity','first_name','last_name','email','password')
    
class CreateUserForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Enter a valid email address')
    group = forms.ModelChoiceField(queryset=Group.objects.all(),
                                   required=False)
    class Meta:
        model = Account
        fields = ('first_name','last_name','email','apt','password1','password2','group')

class CreateLeaseMemberForm(ModelForm):
    RELATIONSHIP = (
        ('husband','Husband'),
        ('wife','Wife'),
        ('daughter','Daughter'),
        ('son','Son'),
        ('relative','Relative')
    )
    full_name = forms.CharField(max_length=100,)
    relation = forms.ChoiceField(choices=RELATIONSHIP)
    
    widget=forms.CheckboxSelectMultiple,

    class Meta:
        model = LeaseMember
        fields = ('full_name','relation')

class AddDayForm(ModelForm):
    # day = forms.DateField(widget=DatePickerInput(format='%m/%d/%Y', attrs={'placeholder':'YYYY-MM-DD'}))
    num_days = forms.IntegerField()
    class Meta:
        model = Day
        fields = ('num_days',)