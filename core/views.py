from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Q
from property.models import Property, Category
from property.filters import HomePropertFilter

# Create your views here.
class IndexPageView(ListView):
    model = Property
    context_object_name = 'lists'
    template_name = 'index.html'
    # paginate_by = 10

    def get_context_data(self, **kwargs):
        kwargs['category_list_nav'] = self.categoryNav
        kwargs['category_list'] = self.category
        kwargs['filter'] = self.filter
        # kwargs['property'] = self.property
    #     kwargs['regions'] = self.region
    #     # kwargs['wishlist'] = self.wishlist
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.categoryNav = Category.objects.filter((~Q(title="land")))
        self.category = Category.objects.all()
        self.property = Property.objects.all()
        self.filter = HomePropertFilter(self.request.GET, queryset=self.model.objects.all())
        return self.model.objects.order_by('-id')





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
