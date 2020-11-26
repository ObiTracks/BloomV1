from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from account.models import Account
from django.conf import settings
User = settings.AUTH_USER_MODEL
from django.contrib.auth.models import Group
from itertools import chain
import datetime

# Date picker imports
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})
from django import forms

from .models import *

class LeaseMemberReservationForm(ModelForm):
    # full_name = forms.CharField(max_length=100,)
    # set_lease_members = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=None)

    def __init__(self, customer, *args, **kwargs):
        super(LeaseMemberReservationForm, self).__init__(*args, **kwargs)
        self.customer = customer
        self.lease_members = self.customer.lease_member_set.all()
        print("The user for this form is for: " + str(customer))
        # self.fields.append(set_lease_members)
        self.fields['set_lease_members'] = forms.ModelMultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple, queryset=self.lease_members,)
        print(self.fields['set_lease_members'])
    
    class Meta:
        model = LeaseMember
        fields = ()
        # exclude = ('lease_owner','full_name','relation',)

