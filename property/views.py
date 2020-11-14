from django.views.generic import View, ListView, DetailView
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Property
from core.models import Category

# Create your views here.
class PropertyListView(ListView):
    model = Property
    context_object_name = 'lists'
    template_name = 'list.html'
    # paginate_by = 10

    # def get_context_data(self, **kwargs):
    #     # kwargs['towns'] = self.town
    #     # kwargs['regions'] = self.region
    #     # kwargs['wishlist'] = self.wishlist
    #     return super().get_context_data(**kwargs)

    def get_queryset(self):
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

    # def get_context_data(self, **kwargs):
    #     # kwargs['towns'] = self.town
    #     # kwargs['regions'] = self.region
    #     # kwargs['wishlist'] = self.wishlist
    #     return super().get_context_data(**kwargs)

    def get_queryset(self):
        # self.town = Town.objects.all()
        # self.region = Region.objects.all()
        # if self.request.user.is_authenticated:
        #     self.wishlist = WishList.objects.filter(user=self.request.user)
        # else:
        #     self.wishlist = False
        self.forsale = self.model.objects.filter(purpose='sale')
        return self.forsale.order_by


class ForRentListView(ListView):
    model = Property
    context_object_name = 'lists'
    template_name = 'list.html'
    # paginate_by = 10

    # def get_context_data(self, **kwargs):
    #     # kwargs['towns'] = self.town
    #     # kwargs['regions'] = self.region
    #     # kwargs['wishlist'] = self.wishlist
    #     return super().get_context_data(**kwargs)

    def get_queryset(self):
        # self.town = Town.objects.all()
        # self.region = Region.objects.all()
        # if self.request.user.is_authenticated:
        #     self.wishlist = WishList.objects.filter(user=self.request.user)
        # else:
        #     self.wishlist = False
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

    # def get_context_data(self, **kwargs):
    #     kwargs['explore_town'] = self.explore_town
    #     kwargs['towns'] = self.town
    #     kwargs['regions'] = self.region
    #     return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.category = get_object_or_404(Category, title=self.kwargs.get('category'))
        queryset = self.model.objects.filter(category=self.category, purpose="sale")
        return queryset.order_by('-id')


class CategoryForRentListView(ListView):
    model = Property
    context_object_name = 'lists'
    template_name = 'list.html'
    # paginate_by = 10

    # def get_context_data(self, **kwargs):
    #     kwargs['explore_town'] = self.explore_town
    #     kwargs['towns'] = self.town
    #     kwargs['regions'] = self.region
    #     return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.category = get_object_or_404(Category, title=self.kwargs.get('category'))
        queryset = self.model.objects.filter(category=self.category, purpose="rent")
        return queryset.order_by('-id')