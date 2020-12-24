from django.views.generic import View, ListView, DetailView, FormView
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Q
from property.models import Property, Category
from property.filters import PropertyFilter
from core.models import Locality, Region
from .models import Car, Brand, SparePart, School
from .filters import CarFilter, CarSideFilter, SparePartFilter

# Create your views here.
class CarListView(ListView):
    model = Car
    context_object_name = 'lists'
    template_name = 'cars/index.html'
    paginate_by = 30

    def get_context_data(self, **kwargs):
        kwargs['locality'] = Locality.objects.all()
        kwargs['category_list_nav'] = Category.objects.filter((~Q(title="land")))
        kwargs['category_list'] = Category.objects.all()
        kwargs['region_list'] = Region.objects.all()

        kwargs['sidefilter'] = self.sidefilter
        kwargs['brands']  = Brand.objects.filter(featured=1).order_by('-id')[:12]
        kwargs['property_list']  = Property.objects.order_by('-id')[:3]
        kwargs['car_count'] = self.sidefilter.qs.count()

        return super().get_context_data(**kwargs)

    def get_queryset(self): 
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
        kwargs['car_list']  = Car.objects.order_by('-id')[:4]

        return super().get_context_data(**kwargs)

    def get_queryset(self):
        return self.model.objects.order_by('-id')


class BrandListView(ListView):
    model = Car
    context_object_name = 'lists'
    template_name = 'cars/brands-list.html'
    paginate_by = 36

    def get_context_data(self, **kwargs):
        kwargs['filter'] = self.filter
        kwargs['sidefilter'] = self.sidefilter
        kwargs['locality'] = Locality.objects.all()
        kwargs['category_list_nav'] = Category.objects.filter((~Q(title="land")))
        kwargs['category_list'] = Category.objects.all()
        kwargs['region_list'] = Region.objects.all()
        kwargs['car_count'] =self.brandqueryset.count()
        kwargs['property_list']  = Property.objects.order_by('-id')[:3]
        kwargs['brands']  = Brand.objects.order_by('-id')[:12]
        kwargs['obj_brands']  = self.brand

        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.filter = CarFilter(self.request.GET, queryset= self.model.objects.all()) 
        self.sidefilter = CarSideFilter(self.request.GET, queryset= self.model.objects.order_by('-id'))
        self.brand = get_object_or_404(Brand,  slug=self.kwargs.get('slug'))
        self.brandqueryset = Car.objects.filter(brand=self.brand)
        return self.brandqueryset.order_by('-id')



# def detail_list(model,  fieldname, field, nid):
#     if nid:
#         lists = model.objects.filter((~Q(id=nid)), brand=field).order_by('-id')[:3]
#     else:
#         lists = model.objects.filter(brand=field).order_by('-id')[:3]


def CarDetail(request, slug):
    lists = get_object_or_404(Car, slug=slug)
    carimages = lists.carimages.order_by('-id')

    session_key = 'viewed_car_{}'.format(lists.pk) 
    if not request.session.get(session_key, False):
        lists.views += 1
        lists.save()
        request.session[session_key] = True

    brand_list = Car.objects.filter((~Q(id=lists.id)), brand=lists.brand).order_by('-id')[:3]
    region_list = Car.objects.filter((~Q(id=lists.id)), region=lists.region).order_by('-id')[:3]
    property_list = Property.objects.filter(region=lists.region).order_by('-id')[:3]
    spare_region_list = SparePart.objects.filter(region=lists.region).order_by('-id')[:3]
    latest_list = Car.objects.filter(~Q(id=lists.id)).order_by('-id')[:6]
    latest_property = Property.objects.order_by('-id')[:6]
    latest_spareparts = SparePart.objects.order_by('-id')[:6]

    # region = Region.objects.all()
    context = {
        'object': lists, 
        'objectimages': carimages,
        'brand_lists': brand_list,
        'property_lists': property_list,
        'region_list': region_list,
        'spare_region_list': spare_region_list,
        'latest_lists': latest_list,
        'latest_property': latest_property,
        'latest_spareparts': latest_spareparts,
    }    
    return render(request, 'cars/car-detail.html', context)




class CarListSaleView(ListView):
    model = Car
    context_object_name = 'lists'
    template_name = 'cars/index.html'
    paginate_by = 30

    def get_context_data(self, **kwargs):
        kwargs['locality'] = Locality.objects.all()
        kwargs['category_list_nav'] = Category.objects.filter((~Q(title="land")))
        kwargs['category_list'] = Category.objects.all()
        kwargs['region_list'] = Region.objects.all()

        kwargs['sidefilter'] = CarSideFilter(self.request.GET, queryset=self.model.objects.order_by('-id'))
        kwargs['brands']  = Brand.objects.filter(featured=1).order_by('-id')[:12]
        kwargs['property_list']  = Property.objects.order_by('-id')[:3]
        kwargs['car_count'] = self.model.objects.filter(purpose="sale").count()

        return super().get_context_data(**kwargs)

    def get_queryset(self): 
        return self.model.objects.filter(purpose="sale").order_by('-id')


class CarListHireView(ListView):
    model = Car
    context_object_name = 'lists'
    template_name = 'cars/index.html'
    paginate_by = 30

    def get_context_data(self, **kwargs):
        kwargs['locality'] = Locality.objects.all()
        kwargs['category_list_nav'] = Category.objects.filter((~Q(title="land")))
        kwargs['category_list'] = Category.objects.all()
        kwargs['region_list'] = Region.objects.all()

        kwargs['sidefilter'] = CarSideFilter(self.request.GET, queryset=self.model.objects.order_by('-id'))
        kwargs['brands']  = Brand.objects.filter(featured=1).order_by('-id')[:12]
        kwargs['property_list']  = Property.objects.order_by('-id')[:3]
        kwargs['car_count'] = self.model.objects.filter(purpose="hire").count()

        return super().get_context_data(**kwargs)

    def get_queryset(self): 
        return self.model.objects.filter(purpose="hire").order_by('-id')




class SparePartListView(ListView):
    model = SparePart
    context_object_name = 'lists'
    template_name = 'cars/spare-parts.html'
    paginate_by = 30

    def get_context_data(self, **kwargs):
        kwargs['locality'] = Locality.objects.all()
        kwargs['category_list_nav'] = Category.objects.filter((~Q(title="land")))
        kwargs['category_list'] = Category.objects.all()
        kwargs['region_list'] = Region.objects.all()

        kwargs['filter'] = self.filter
        kwargs['brands']  = Brand.objects.filter(featured=1).order_by('-id')[:12]
        kwargs['property_list']  = Property.objects.order_by('-id')[:3]

        return super().get_context_data(**kwargs)

    def get_queryset(self): 
        self.filter = SparePartFilter(self.request.GET, queryset= self.model.objects.order_by('-id'))
        return self.filter.qs





def SparePartDetail(request, slug):
    lists = get_object_or_404(SparePart, slug=slug)
    spareimages = lists.sparepartimages.order_by('-id')

    session_key = 'viewed_spareparts_{}'.format(lists.pk) 
    if not request.session.get(session_key, False):
        lists.views += 1
        lists.save()
        request.session[session_key] = True

    latest_spareparts = SparePart.objects.filter(~Q(id=lists.id)).order_by('-id')[:6]
    region_list = SparePart.objects.filter((~Q(id=lists.id)), region=lists.region).order_by('-id')[:3]
    property_list = Property.objects.filter(region=lists.region).order_by('-id')[:3]
    car_list = Car.objects.filter(region=lists.region).order_by('-id')[:3]
    latest_property = Property.objects.order_by('-id')[:10]
    latest_list = Car.objects.order_by('-id')[:10]

    # region = Region.objects.all()
    context = {
        'object': lists, 
        'latest_lists': latest_list,
        'latest_property': latest_property,
        'property_lists': property_list,
        'car_lists': car_list,
        'objectimages': spareimages,
        'region_list': region_list,
        'latest_spareparts': latest_spareparts,
    }    
    return render(request, 'cars/spare-detail.html', context)





class SchoolListView(ListView):
    model = School
    context_object_name = 'lists'
    template_name = 'cars/school.html'
    paginate_by = 30

    def get_context_data(self, **kwargs):
        kwargs['locality'] = Locality.objects.all()
        kwargs['category_list_nav'] = Category.objects.filter((~Q(title="land")))
        kwargs['category_list'] = Category.objects.all()
        kwargs['region_list'] = Region.objects.all()

        kwargs['filter'] = self.filter
        kwargs['brands']  = Brand.objects.filter(featured=1).order_by('-id')[:12]
        kwargs['property_list']  = Property.objects.order_by('-id')[:3]

        return super().get_context_data(**kwargs)

    def get_queryset(self): 
        self.filter = SparePartFilter(self.request.GET, queryset= self.model.objects.order_by('-id'))
        return self.filter.qs


def SchoolDetail(request, slug):
    lists = get_object_or_404(School, slug=slug)
    spareimages = lists.schoolimage.order_by('-id')

    session_key = 'viewed_school_{}'.format(lists.pk) 
    if not request.session.get(session_key, False):
        lists.views += 1
        lists.save()
        request.session[session_key] = True

    spare_list = SparePart.objects.filter(~Q(id=lists.id)).order_by('-id')[:3]
    region_list = SparePart.objects.filter((~Q(id=lists.id)), region=lists.region).order_by('-id')[:3]
    property_list = Property.objects.filter(region=lists.region).order_by('-id')[:3]
    car_list = Car.objects.filter(region=lists.region).order_by('-id')[:3]
    latest_property = Property.objects.order_by('-id')[:10]
    latest_list = Car.objects.order_by('-id')[:10]

    # region = Region.objects.all()
    context = {
        'object': lists, 
        'latest_lists': latest_list,
        'latest_property': latest_property,
        'spare_lists': spare_list,
        'property_lists': property_list,
        'car_lists': car_list,
        # 'spareimages': spareimages,
        'region_list': region_list,
    }    
    return render(request, 'cars/school-detail.html', context)
