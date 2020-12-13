from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, ListView, DetailView
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import  JsonResponse, HttpResponse
from django.db.models import Q
from property.models import Property, Category, Testimony, Subscription
from property.filters import HomePropertFilter, PropertyFilter
from .forms import SubscriptionForm
from .models import Locality, Region
from cars.filters import CarFilter
# Create your views here.

def BaseView(request):
    template_name = 'base.html'

    context ={
        "locality" : Locality.objects.all(),
        "category_list_nav" : Category.objects.filter((~Q(title="land"))),
        "category_list" : Category.objects.all(),
        "region_list" : Region.objects.all(),
        "testimonys" : Testimony.objects.all(),
        "subscription_form" : SubscriptionForm(),
    }

    return render(request, template_name, context)
class IndexPageView(ListView):
    model = Property
    context_object_name = 'lists'
    template_name = 'index.html'
    # paginate_by = 10

    def get_context_data(self, **kwargs):

        kwargs['locality'] = self.locality
        kwargs['category_list_nav'] = self.categoryNav
        kwargs['category_list'] = self.category
        kwargs['region_list'] = self.region

        kwargs['testimonys'] = self.testimony
        kwargs['carfilter'] = self.carfilter
        kwargs['filter'] = self.filter
        kwargs['subscription_form'] = self.subscriptionform
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.locality = Locality.objects.all() 
        self.categoryNav = Category.objects.filter((~Q(title="land")))
        self.category = Category.objects.all()
        self.region = Region.objects.all()

        self.testimony = Testimony.objects.all()
        self.subscriptionform = SubscriptionForm()
        self.carfilter = CarFilter(self.request.GET, queryset= self.model.objects.all()) 
        self.filter = HomePropertFilter(self.request.GET, queryset=self.model.objects.all())


        return self.model.objects.order_by('-id')





class CategoryListView(ListView):
    model = Property
    context_object_name = 'lists'
    template_name = 'list.html'
    # paginate_by = 10

    def get_context_data(self, **kwargs):

        kwargs['locality'] = self.locality
        kwargs['category_list_nav'] = self.categoryNav
        kwargs['category_list'] = self.category

        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.locality = Locality.objects.all() 
        self.categoryNav = Category.objects.filter((~Q(title="land")))
        self.category = Category.objects.all()

        self.categoryparam = get_object_or_404(Category, title=self.kwargs.get('category'))
        queryset = self.model.objects.filter(category=self.categoryparam)
        return queryset.order_by('-id')




@csrf_exempt
def subscriptionForm(request):
    if request.method == "POST" and request.is_ajax:

        email = request.POST['email']
        locality = request.POST['locality']
        category = request.POST['category']
        purpose = request.POST['purpose']
        bed = request.POST['bed']
        from_price = request.POST['from_price']
        to_price = request.POST['to_price']
        try:
            subscription = Subscription()
            subscription.email=email
            subscription.purpose=purpose
            subscription.bed=bed
            subscription.from_price=from_price
            subscription.to_price=to_price

            if locality != '' and locality is not None:
                subscription.locality = Locality.objects.get(pk=locality)

            if category  != '' and category  is not None:
                subscription.category = Category.objects.get(id=category)

            subscription.save()
            
        except Exception as e:
            return JsonResponse({"error":str(e)}, status=403)

        # response_data = 'ok'
        return JsonResponse('ok', status=200, safe=False)
    return JsonResponse({}, status=200)




def contactPage(request):
    return render(request, 'contact.html')

def aboutPage(request):
    locality = Locality.objects.all() 
    categoryNav = Category.objects.filter((~Q(title="land")))
    category = Category.objects.all()
    featured = Property.objects.filter(featured=1)[:4]
    region = Region.objects.all()

    context = {
        'locality': locality,
        'category_list': category,
        'category_list_nav': categoryNav,
        'featured_list': featured,
        'region_list' : region,
    }
    return render(request, 'about.html', context)

class LocalityListView(ListView):
    model = Property
    context_object_name = 'lists'
    template_name = 'list.html'
    # paginate_by = 1

    def get_context_data(self, **kwargs):

        kwargs['locality'] = self.locality
        kwargs['category_list_nav'] = self.categoryNav
        kwargs['category_list'] = self.category

        return super().get_context_data(**kwargs)

    def get_queryset(self):

        self.locality = Locality.objects.all() 
        self.categoryNav = Category.objects.filter((~Q(title="land")))
        self.category = Category.objects.all()



        self.local = get_object_or_404(Locality, name=self.kwargs.get('locality'))
        queryset = self.model.objects.filter(locality=self.local)
        return queryset.order_by('-id')





class RegionListView(ListView):
    model = Property
    context_object_name = 'lists'
    template_name = 'list.html'
    # paginate_by = 1

    def get_context_data(self, **kwargs):

        kwargs['locality'] = self.locality
        kwargs['category_list_nav'] = self.categoryNav
        kwargs['category_list'] = self.category

        return super().get_context_data(**kwargs)

    def get_queryset(self):

        self.locality = Locality.objects.all() 
        self.categoryNav = Category.objects.filter((~Q(title="land")))
        self.category = Category.objects.all()



        self.reg = get_object_or_404(Region, name=self.kwargs.get('region'))
        queryset = self.model.objects.filter(region=self.reg)
        return queryset.order_by('-id')





class LandListView(ListView):
    model = Property
    context_object_name = 'lists'
    template_name = 'list.html'
    # paginate_by = 10

    def get_context_data(self, **kwargs):
        kwargs['filter'] = self.filter
        kwargs['locality'] = self.locality
        kwargs['category_list_nav'] = self.categoryNav
        kwargs['category_list'] = self.category

        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.filter = PropertyFilter(self.request.GET, queryset= self.model.objects.all()) 
        self.locality = Locality.objects.all() 
        self.categoryNav = Category.objects.filter((~Q(title="land")))
        self.category = Category.objects.all()

        self.landCategory = Category.objects.get(title='land')
        queryset = self.model.objects.filter(category=self.landCategory)
        return queryset.order_by('-id')

