import django_filters
from django import forms
from .models import Car, SparePart

class CarFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    price__min = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__max = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    class Meta:
        model = Car
        fields = [
            'title', 
            'brand', 
        ]

class CarSideFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    price__min = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__max = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
   
    class Meta:
        model = Car
        fields = [
            'title', 
            'brand', 
            'price__min',
            'price__max',
            'car_state', 
            'mileage',
            'year',
            'region'
        ]

class HomePropertFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    price__min = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__max = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    class Meta:
        model = Car
        fields = [
            'title', 
            # 'category'
        ]



class SparePartFilter(django_filters.FilterSet):
    price__min = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__max = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
   
    class Meta:
        model = SparePart
        fields = [
            'title',
            'region'
        ]


