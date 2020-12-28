from django.views.generic import View, ListView, DetailView, FormView
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Q
from .models import Property, Category, LandProperty
from .filters import PropertyFilter, PropertyLandFilter
from core.models import Locality, Region

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
        kwargs['page_title'] = 'All Properties'
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
    template_name = 'list.html'
    # paginate_by = 10

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

        self.forrent = self.model.objects.filter(purpose="rent")
        return self.forrent.order_by




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
    # paginate_by = 10

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

        self.cate = get_object_or_404(Category, title=self.kwargs.get('category'))
        return self.model.objects.filter(category=self.cate, purpose="sale").order_by('-id')


class CategoryForRentListView(ListView):
    model = Property
    context_object_name = 'lists'
    template_name = 'list.html'
    # paginate_by = 10

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

        self.cate = get_object_or_404(Category, title=self.kwargs.get('category'))
        queryset = self.model.objects.filter(category=self.cate, purpose="rent")
        return queryset.order_by('-id')





class SearchListView(ListView):
    model = Property
    context_object_name = 'lists'
    template_name = 'list.html'
    # paginate_by = 10

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
    paginate_by = 36

    def get_context_data(self, **kwargs):
        kwargs['filter'] = self.filter
        kwargs['locality'] =  Locality.objects.all() 
        kwargs['category_list_nav'] = Category.objects.filter((~Q(title="land")))
        kwargs['category_list'] = Category.objects.all()
        kwargs['page_title'] = "Land"

        return super().get_context_data(**kwargs)

    def get_queryset(self):

        # self.sidefilter = CarSideFilter(self.request.GET, queryset= self.model.objects.order_by('-id'))
        self.landCategory = Category.objects.get(title='land') 
        self.filter = PropertyLandFilter(self.request.GET, queryset=self.model.objects.filter(category=self.landCategory)) 
        # queryset = self.model.objects.filter(category=self.landCategory)
        return self.filter.qs