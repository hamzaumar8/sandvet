from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Q
from .models import Category
from property.models import Property

# Create your views here.
class IndexPageView(ListView):
    model = Property
    context_object_name = 'lists'
    template_name = 'index.html'
    # paginate_by = 10

    def get_context_data(self, **kwargs):
        kwargs['category_list_nav'] = self.categoryNav
        kwargs['category_list'] = self.category
    #     kwargs['regions'] = self.region
    #     # kwargs['wishlist'] = self.wishlist
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.categoryNav = Category.objects.filter((~Q(title="land")))
        self.category = Category.objects.filter()
        # self.region = Region.objects.all()
        # if self.request.user.is_authenticated:
        #     self.wishlist = WishList.objects.filter(user=self.request.user)
        # else:
        #     self.wishlist = False
        return self.model.objects.order_by('-id')[:6]





class CategoryListView(ListView):
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
        queryset = self.model.objects.filter(category=self.category)
        return queryset.order_by('-id')
