from django.views.generic import View, ListView, DetailView, FormView
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Q
from property.models import Property, Category
from property.filters import PropertyFilter
from core.models import Locality, Region
from .models import Car, Brand
from .filters import CarFilter, CarSideFilter

# Create your views here.
class CarListView(ListView):
    model = Car
    context_object_name = 'lists'
    template_name = 'cars/index.html'
    paginate_by = 36

    def get_context_data(self, **kwargs):
        kwargs['filter'] = self.filter
        kwargs['sidefilter'] = self.sidefilter
        kwargs['locality'] = Locality.objects.all()
        kwargs['category_list_nav'] = Category.objects.filter((~Q(title="land")))
        kwargs['category_list'] = Category.objects.all()
        kwargs['region_list'] = Region.objects.all()
        kwargs['car_count'] = self.model.objects.count()
        kwargs['property_list']  = Property.objects.order_by('-id')[:3]
        kwargs['brands']  = Brand.objects.order_by('-id')[:12]

        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.filter = CarFilter(self.request.GET, queryset= self.model.objects.all()) 
        self.sidefilter = CarSideFilter(self.request.GET, queryset= self.model.objects.order_by('-id'))
        return self.sidefilter.qs


class BrandsView(ListView):
    model = Brand
    context_object_name = 'lists'
    template_name = 'cars/brands.html'

    def get_context_data(self, **kwargs):
        kwargs['locality'] = Locality.objects.all()
        kwargs['category_list_nav'] = Category.objects.filter((~Q(title="land")))
        kwargs['category_list'] = Category.objects.all()
        kwargs['region_list'] = Region.objects.all()
        kwargs['property_list']  = Property.objects.order_by('-id')[:3]

        return super().get_context_data(**kwargs)

    def get_queryset(self):
        return self.model.objects.order_by('-id')


class BrandListView(ListView):
    model = Car
    context_object_name = 'lists'
    template_name = 'cars/index.html'
    paginate_by = 36

    def get_context_data(self, **kwargs):
        kwargs['filter'] = self.filter
        kwargs['sidefilter'] = self.sidefilter
        kwargs['locality'] = Locality.objects.all()
        kwargs['category_list_nav'] = Category.objects.filter((~Q(title="land")))
        kwargs['category_list'] = Category.objects.all()
        kwargs['region_list'] = Region.objects.all()
        kwargs['car_count'] =self.queryset1.count()
        kwargs['property_list']  = Property.objects.order_by('-id')[:3]
        kwargs['brands']  = Brand.objects.order_by('-id')[:12]
        kwargs['obj_brands']  = self.brand

        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.filter = CarFilter(self.request.GET, queryset= self.model.objects.all()) 
        self.sidefilter = CarSideFilter(self.request.GET, queryset= self.model.objects.order_by('-id'))
        self.brand = get_object_or_404(Brand,  slug=self.kwargs.get('slug'))
        self.queryset1 = Car.objects.filter(brand=self.brand)
        return self.queryset1.order_by('-id')





def CarDetail(request, slug):
    lists = get_object_or_404(Car, slug=slug)
    carimages = lists.carimages.order_by('-id')

    session_key = 'viewed_car_{}'.format(lists.pk) 
    if not request.session.get(session_key, False):
        lists.views += 1
        lists.save()
        request.session[session_key] = True

    latest_list = Car.objects.filter(~Q(id=lists.id)).order_by('-id')[:10]
    brand_list = Car.objects.filter((~Q(id=lists.id)), brand=lists.brand).order_by('-id')[:3]
    region_list = Car.objects.filter((~Q(id=lists.id)), region=lists.region).order_by('-id')[:3]
    property_list = Property.objects.filter(region=lists.region).order_by('-id')[:3]
    latest_property = Property.objects.filter(~Q(id=lists.id)).order_by('-id')[:10]

    # region = Region.objects.all()
    context = {
        'object': lists, 
        'latest_lists': latest_list,
        'latest_property': latest_property,
        'brand_lists': brand_list,
        'property_lists': property_list,
        'carimages': carimages,
        'region_list': region_list,
    }    
    return render(request, 'cars/car-detail.html', context)
