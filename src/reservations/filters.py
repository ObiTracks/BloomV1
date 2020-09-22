import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

class CustomerFilter(django_filters.FilterSet):
    first_name = CharFilter(field_name='first_name', lookup_expr='icontains', label='First Name')
    last_name = CharFilter(field_name='last_name', lookup_expr='icontains', label='Last Name')
    apt = CharFilter(field_name='apt', lookup_expr='icontains', label='Apartment')
    email = CharFilter(field_name='email', lookup_expr='icontains', label='Email')

    class Meta:
        model = Customer
        fields = ('first_name','last_name','apt','email')
        exclude = ['user','lease_members','date_created', 'id']
        

class DayFilter(django_filters.FilterSet):
    day = DateFilter(field_name='date_created', label='Day')
    start_date = DateFilter(field_name='date_created', label='Day after (mm/dd/yyyy):', lookup_expr='gte')
    end_date = DateFilter(field_name='date_created', label='Day before (mm/dd/yyyy):', lookup_expr='lte')

    class Meta:
        model = Day
        fields = ['day','start_date','end_date']
        # exclude = ['lease_members','date_created', 'id']