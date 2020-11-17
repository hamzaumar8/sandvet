from django.views.generic import View, ListView, DetailView, FormView
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Q
from .models import Property, Category
from .filters import PropertyFilter


# Create your views here.
class PropertyListView(ListView):
    model = Property
    context_object_name = 'lists'
    template_name = 'list.html'
    # paginate_by = 10

    def get_context_data(self, **kwargs):
        kwargs['filter'] = self.filter
        kwargs['category_list_nav'] = self.categoryNav
    #     kwargs['regions'] = self.region
    #     # kwargs['wishlist'] = self.wishlist
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.filter = PropertyFilter(self.request.GET, queryset= self.model.objects.all()) 
        self.categoryNav = Category.objects.filter((~Q(title="land")))
        # self.town = Town.objects.all()
        # self.region = Region.objects.all()
        # if self.request.user.is_authenticated:
        #     self.wishlist = WishList.objects.filter(user=self.request.user)
        # else:
        #     self.wishlist = False
        return self.model.objects.order_by('-id')


class ForSaleListView(ListView):
    model = Property
    context_object_name = 'lists'
    template_name = 'list.html'
    # paginate_by = 10

    def get_context_data(self, **kwargs):
        kwargs['filter'] = self.filter
        kwargs['category_list_nav'] = self.categoryNav
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.filter = PropertyFilter(self.request.GET, queryset= self.model.objects.all()) 
        self.categoryNav = Category.objects.filter((~Q(title="land")))
        # self.town = Town.objects.all()
        # self.region = Region.objects.all()
        # if self.request.user.is_authenticated:
        #     self.wishlist = WishList.objects.filter(user=self.request.user)
        # else:
        #     self.wishlist = False
        self.forsale = self.model.objects.filter(purpose='sale')
        return self.forsale.order_by('-id')


class ForRentListView(ListView):
    model = Property
    context_object_name = 'lists'
    template_name = 'list.html'
    # paginate_by = 10

    def get_context_data(self, **kwargs):
        kwargs['filter'] = self.filter
        kwargs['category_list_nav'] = self.categoryNav
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.filter = PropertyFilter(self.request.GET, queryset= self.model.objects.all()) 
        self.categoryNav = Category.objects.filter((~Q(title="land")))

        self.forrent = self.model.objects.filter(purpose="rent")
        return self.forrent.order_by




def propertyDetail(request, slug):
    lists = get_object_or_404(Property, slug=slug)
    context = {
        'object': lists, 
    }    
    return render(request, 'list-detail.html', context)




class CategoryForSaleListView(ListView):
    model = Property
    context_object_name = 'lists'
    template_name = 'list.html'
    # paginate_by = 10

    def get_context_data(self, **kwargs):
        kwargs['filter'] = self.filter
        kwargs['category_list_nav'] = self.categoryNav
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.filter = PropertyFilter(self.request.GET, queryset= self.model.objects.all()) 
        self.categoryNav = Category.objects.filter((~Q(title="land")))

        self.category = get_object_or_404(Category, title=self.kwargs.get('category'))
        queryset = self.model.objects.filter(category=self.category, purpose="sale")
        return queryset.order_by('-id')


class CategoryForRentListView(ListView):
    model = Property
    context_object_name = 'lists'
    template_name = 'list.html'
    # paginate_by = 10

    def get_context_data(self, **kwargs):
        kwargs['filter'] = self.filter
        kwargs['category_list_nav'] = self.categoryNav
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.filter = PropertyFilter(self.request.GET, queryset= self.model.objects.all()) 
        self.categoryNav = Category.objects.filter((~Q(title="land")))

        self.category = get_object_or_404(Category, title=self.kwargs.get('category'))
        queryset = self.model.objects.filter(category=self.category, purpose="rent")
        return queryset.order_by('-id')





class SearchListView(ListView):
    model = Property
    context_object_name = 'lists'
    template_name = 'list.html'
    # paginate_by = 10

    def get_context_data(self, **kwargs):
        kwargs['filter'] = self.filter
        kwargs['category_list_nav'] = self.categoryNav
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.categoryNav = Category.objects.filter((~Q(title="land")))
        self.filter = PropertyFilter(self.request.GET, queryset= self.model.objects.all()) 
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
