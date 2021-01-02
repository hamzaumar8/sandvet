from django.views.generic import View, ListView, DetailView, FormView
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Q, Count
from .models import Property, Category, LandProperty, RealEstate, Hotel, HotelRoom
from .filters import PropertyFilter, PropertyCategoryFilter, RealEstateFilter, HotelFilter
from core.models import Locality, Region
from cars.models import Car, SparePart, School

# Create your views here.
class PropertyListView(ListView):
    model = Property
    context_object_name = 'lists'
    template_name = 'property/list.html'
    paginate_by = 24

    def get_context_data(self, **kwargs):
        kwargs['page_title'] = 'All Properties'
        kwargs['filter'] = self.filter
        kwargs['locality'] = Locality.objects.all() 
        kwargs['category_list_nav'] = Category.objects.filter((~Q(title="land")))
        kwargs['category_list'] = Category.objects.all()
        kwargs['region_list'] = Region.objects.all()

        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.filter = PropertyFilter(self.request.GET, queryset= self.model.objects.order_by('-id')) 
        return self.filter.qs


class ForSaleListView(ListView):
    model = Property
    context_object_name = 'lists'
    template_name = 'property/list.html'
    paginate_by = 24

    def get_context_data(self, **kwargs):
        kwargs['page_title'] = 'For Sale'
        kwargs['filter'] = self.filter
        kwargs['locality'] = Locality.objects.all() 
        kwargs['category_list_nav'] = Category.objects.filter((~Q(title="land")))
        kwargs['category_list'] = Category.objects.all()
        kwargs['region_list'] = Region.objects.all()

        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.forsale = self.model.objects.filter(purpose='sale')
        self.filter = PropertyFilter(self.request.GET, queryset=self.forsale.order_by('-id')) 
        return self.filter.qs


class ForRentListView(ListView):
    model = Property
    context_object_name = 'lists'
    template_name = 'property/list.html'
    paginate_by = 24

    def get_context_data(self, **kwargs):
        kwargs['page_title'] = 'For Sale'
        kwargs['filter'] = self.filter
        kwargs['locality'] = Locality.objects.all() 
        kwargs['category_list_nav'] = Category.objects.filter((~Q(title="land")))
        kwargs['category_list'] = Category.objects.all()
        kwargs['region_list'] = Region.objects.all()

        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.forsale = self.model.objects.filter(purpose='rent')
        self.filter = PropertyFilter(self.request.GET, queryset=self.forsale.order_by('-id')) 
        return self.filter.qs




def propertyDetail(request, slug):
    lists = get_object_or_404(Property, slug=slug)
    latest_list = Property.objects.filter(~Q(id=lists.id)).order_by('-id')[:10]

    region = Region.objects.all()
    context = {
        'object': lists, 
        'latest_lists': latest_list,
        'region_list': region,
    }    
    return render(request, 'list-detail.html', context)




class CategoryForSaleListView(ListView):
    model = Property
    context_object_name = 'lists'
    template_name = 'list.html'
    template_name = 'property/list.html'
    paginate_by = 24

    def get_context_data(self, **kwargs):
        kwargs['page_title'] = f'{self.slug} For Sale'
        kwargs['filter'] = self.filter
        kwargs['locality'] = Locality.objects.all() 
        kwargs['category_list_nav'] = Category.objects.filter((~Q(title="land")))
        kwargs['category_list'] = Category.objects.all()
        kwargs['region_list'] = Region.objects.all()

        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.slug = self.kwargs.get('slug')
        self.cate = get_object_or_404(Category, slug=self.slug)
        self.forsalecate = self.model.objects.filter(category=self.cate, purpose='sale')
        self.filter = PropertyCategoryFilter(self.request.GET, queryset=self.forsalecate.order_by('-id')) 
        return self.filter.qs


class CategoryForRentListView(ListView):
    model = Property
    context_object_name = 'lists'
    template_name = 'list.html'
    template_name = 'property/list.html'
    paginate_by = 24

    def get_context_data(self, **kwargs):
        kwargs['page_title'] = f'{self.slug} For Rent'
        kwargs['filter'] = self.filter
        kwargs['locality'] = Locality.objects.all() 
        kwargs['category_list_nav'] = Category.objects.filter((~Q(title="land")))
        kwargs['category_list'] = Category.objects.all()
        kwargs['region_list'] = Region.objects.all()

        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.slug = self.kwargs.get('slug')
        self.cate = get_object_or_404(Category, slug=self.slug)
        self.forsalecate = self.model.objects.filter(category=self.cate, purpose='rent')
        self.filter = PropertyCategoryFilter(self.request.GET, queryset=self.forsalecate.order_by('-id')) 
        return self.filter.qs





class SearchListView(ListView):
    model = Property
    context_object_name = 'lists'
    template_name = 'property/list.html'
    paginate_by = 24

    def get_context_data(self, **kwargs):
        kwargs['filter'] = self.filter
        kwargs['locality'] = self.locality
        kwargs['category_list_nav'] = self.categoryNav
        kwargs['category_list'] = self.category
        kwargs['region_list'] = self.region
        
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.filter = PropertyFilter(self.request.GET, queryset= self.model.objects.all()) 
        self.locality = Locality.objects.all() 
        self.categoryNav = Category.objects.filter((~Q(title="land")))
        self.category = Category.objects.all()
        self.region = Region.objects.all()
        
        self.query = self.filter.qs
        return self.query



# def checkPage(request):
#     table1 = Category.objects.all() 
#     table2 = Property.objects.all() 
#     return render(request, 'template_name.html',{'table1':table1, 'table2':table2})

def checkPage(request):
    s = Category.objects.all()
    return_dict = {
        's' :   s        
    }
    return render(request, 'template_name.html', return_dict)







 
class LandListView(ListView):
    model = Property
    context_object_name = 'lists'
    template_name = 'property/list.html'
    paginate_by = 24

    def get_context_data(self, **kwargs):
        kwargs['filter'] = self.filter
        kwargs['locality'] =  Locality.objects.all() 
        kwargs['category_list_nav'] = Category.objects.filter((~Q(title="land")))
        kwargs['category_list'] = Category.objects.all()
        kwargs['page_title'] = "Land"

        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.landCategory = Category.objects.get(title='land') 
        self.filter = PropertyCategoryFilter(self.request.GET, queryset=self.model.objects.filter(category=self.landCategory)) 
        return self.filter.qs






class RealEstateListView(ListView):
    model = RealEstate
    context_object_name = 'lists'
    template_name = 'property/list.html'
    paginate_by = 24

    def get_context_data(self, **kwargs):
        kwargs['page_title'] = "RealEstate"
        kwargs['filter'] = self.filter
        kwargs['locality'] =  Locality.objects.all() 
        kwargs['category_list_nav'] = Category.objects.filter((~Q(title="land")))
        kwargs['category_list'] = Category.objects.all()

        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.filter = RealEstateFilter(self.request.GET, queryset=self.model.objects.order_by('-id')) 
        return self.filter.qs.annotate(num_props=Count('realestate', distinct=True))



def RealestateDetail(request, slug):
    lists = get_object_or_404(RealEstate, slug=slug)
    school_list = School.objects.order_by('-id')[:3]
    cars_list = Car.objects.filter(region=lists.region).order_by('-id')[:3]
    property_list = Property.objects.filter(region=lists.region).order_by('-id')[:3]
    region_list = RealEstate.objects.filter((~Q(id=lists.id)), region=lists.region).order_by('-id')[:3]
    realestate_list = RealEstate.objects.filter(~Q(id=lists.id), region=lists.region).order_by('-id')[:4]
    latest_list = Car.objects.order_by('-id')[:6]
    latest_property = Property.objects.order_by('-id')[:6]
    latest_spareparts = SparePart.objects.filter(~Q(id=lists.id)).order_by('-id')[:6]

    region = Region.objects.all()
    context = {
        'object': lists, 
        'latest_lists': latest_list,
        'realestate_lists': realestate_list,
        'region_list': region_list,
        'latest_spareparts': latest_spareparts,
        'latest_property': latest_property,
        'property_list': property_list,
        'school_list': school_list
    }    
    return render(request, 'list-detail.html', context)



class HotelListView(ListView):
    model = Hotel
    context_object_name = 'lists'
    template_name = 'property/list.html'
    paginate_by = 24

    def get_context_data(self, **kwargs):
        kwargs['page_title'] = "Hotels"
        kwargs['filter'] = self.filter
        kwargs['locality'] =  Locality.objects.all() 
        kwargs['category_list_nav'] = Category.objects.filter((~Q(title="land")))
        kwargs['category_list'] = Category.objects.all()

        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.filter = HotelFilter(self.request.GET, queryset=self.model.objects.order_by('-id')) 
        return self.filter.qs





def HotelDetail(request, slug):
    lists = get_object_or_404(Hotel, slug=slug)
   
    context = {
        'object': lists, 
    }    
    return render(request, 'list-detail.html', context)

def HotelRoomDetail(request, slug):
    lists = get_object_or_404(HotelRoom, slug=slug)
   
    context = {
        'object': lists, 
    }    
    return render(request, 'list-detail.html', context)