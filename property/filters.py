import django_filters

from .models import *

class PropertyFilter(django_filters.FilterSet):
    address = django_filters.CharFilter(field_name='address', lookup_expr='icontains')
    price__min = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__max = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    class Meta:
        model = Property
        fields = ['address', 'purpose', 'category', 'region' ,'bed', 'bath']


class HomePropertFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    price__min = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__max = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    class Meta:
        model = Property
        fields = ['title', 'category']

