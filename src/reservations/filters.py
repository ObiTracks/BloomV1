import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

class CustomerFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date_created', lookup_expr='gte')
    end_date = DateFilter(field_name='date_created', lookup_expr='lte')

    name = CharFilter(field_name='name', lookup_expr='icontains')
    apt = CharFilter(field_name='apt', lookup_expr='icontains')
    phone = CharFilter(field_name='phone', lookup_expr='icontains')
    email = CharFilter(field_name='email', lookup_expr='icontains')
    notes = CharFilter(field_name='notes', lookup_expr='icontains')

    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['lease_members','date_created', 'id']