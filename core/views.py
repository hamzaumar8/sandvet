from django.shortcuts import render
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, ListView, DetailView
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import  JsonResponse, HttpResponse
from django.db.models import Q
from property.models import Property, Category, Testimony, Subscription, RealEstate, Hotel, HotelRoom
from property.filters import HomePropertFilter, PropertyFilter, HomeHotelFilter, HomeRealEstateFilter, HotelFilter, HotelRoomFilter, RealEstateFilter, PropertyCategoryFilter
from .forms import SubscriptionForm, ContactForm
from .models import Locality, Region
from cars.filters import CarFilter, SparePartFilter, CarSideFilter, SchoolFilter
from cars.models import Car, Brand, SparePart, School
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
        kwargs['category_list_nav'] = Category.objects.filter((~Q(title="land")))
        kwargs['category_list'] = Category.objects.all()
        kwargs['brands_list'] = Brand.objects.order_by('-views')[:7]
        kwargs['driving_list'] = School.objects.order_by('-views')[:7]
        kwargs['hotels_list'] = Hotel.objects.order_by('-views')[:7]
        kwargs['realestates_list'] = RealEstate.objects.order_by('-views')[:7]
        
        kwargs['partners'] = self.partners
        kwargs['testimonys'] = Testimony.objects.all()
        kwargs['brands'] = Brand.objects.filter(featured=1).order_by('-id')[:12]
        kwargs['cars'] = Car.objects.filter(featured=1).order_by('-id')[:12]
        kwargs['spareparts'] = SparePart.objects.filter(featured=1).order_by('-id')[:12]
        kwargs['hotels'] = Hotel.objects.filter(featured=1).order_by('-id')[:12]
        kwargs['realestate'] = RealEstate.objects.filter(featured=1).order_by('-id')[:12]
        kwargs['hotelrooms'] = HotelRoom.objects.filter(featured=1).order_by('-id')[:12]
        kwargs['schools'] = School.objects.filter(featured=1).order_by('-id')[:12]
        kwargs['carfilter'] = CarFilter(self.request.GET, queryset=Car.objects.all()) 
        kwargs['sparepartfilter'] = SparePartFilter(self.request.GET, queryset=SparePart.objects.all()) 
        kwargs['hotelfilter'] = HomeHotelFilter(self.request.GET, queryset= Hotel.objects.all()) 
        kwargs['realestatefilter'] = HomeRealEstateFilter(self.request.GET, queryset= RealEstate.objects.all()) 
        kwargs['filter'] = HomePropertFilter(self.request.GET, queryset=self.model.objects.all())
        kwargs['subscription_form'] = SubscriptionForm()
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.qs1 = Hotel.objects.values_list('title', 'slug', 'logo', 'rate')
        self.qs2 = RealEstate.objects.values_list('title', 'slug', 'logo', 'url')
        self.partners = self.qs1.union(self.qs2).order_by('title')
        return self.model.objects.order_by('-id')





class CategoryListView(ListView):
    model = Property
    context_object_name = 'lists'
    template_name = 'list.html'
    # paginate_by = 10

    def get_context_data(self, **kwargs):
        kwargs['category_list_nav'] = Category.objects.filter((~Q(title="land")))
        kwargs['category_list'] = Category.objects.all()
        kwargs['brands_list'] = Brand.objects.order_by('-views')[:7]
        kwargs['driving_list'] = School.objects.order_by('-views')[:7]
        kwargs['hotels_list'] = Hotel.objects.order_by('-views')[:7]
        kwargs['realestates_list'] = RealEstate.objects.order_by('-views')[:7]

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
    latest_list = Car.objects.order_by('-id')[:5]
    latest_property = Property.objects.order_by('-id')[:6]
    latest_spareparts = SparePart.objects.order_by('-id')[:5]

    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "We've received your message. We would get back to you soon.")
            return redirect('core:contact')
        else:
            print(form.errors)

    context = {
        'latest_lists': latest_list,
        'property_list': latest_property,
        'latest_spareparts': latest_spareparts,
        'form': form
    }
    context['category_list_nav'] = Category.objects.filter((~Q(title="land")))
    context['category_list'] = Category.objects.all()
    context['brands_list'] = Brand.objects.order_by('-views')[:7]
    context['driving_list'] = School.objects.order_by('-views')[:7]
    context['hotels_list'] = Hotel.objects.order_by('-views')[:7]
    context['realestates_list'] = RealEstate.objects.order_by('-views')[:7] 
    return render(request, 'contact.html', context)

def aboutPage(request):
    latest_list = Car.objects.order_by('-id')[:5]
    latest_property = Property.objects.order_by('-id')[:6]
    latest_spareparts = SparePart.objects.order_by('-id')[:5]
    context = {
        'latest_lists': latest_list,
        'property_list': latest_property,
        'latest_spareparts': latest_spareparts
    }
    context['category_list_nav'] = Category.objects.filter((~Q(title="land")))
    context['category_list'] = Category.objects.all()
    context['brands_list'] = Brand.objects.order_by('-views')[:7]
    context['driving_list'] = School.objects.order_by('-views')[:7]
    context['hotels_list'] = Hotel.objects.order_by('-views')[:7]
    context['realestates_list'] = RealEstate.objects.order_by('-views')[:7] 
    return render(request, 'about.html', context)

class LocalityListView(ListView):
    model = Property
    context_object_name = 'lists'
    template_name = 'list.html'
    # paginate_by = 1

    def get_context_data(self, **kwargs):
        kwargs['category_list_nav'] = Category.objects.filter((~Q(title="land")))
        kwargs['category_list'] = Category.objects.all()
        kwargs['brands_list'] = Brand.objects.order_by('-views')[:7]
        kwargs['driving_list'] = School.objects.order_by('-views')[:7]
        kwargs['hotels_list'] = Hotel.objects.order_by('-views')[:7]
        kwargs['realestates_list'] = RealEstate.objects.order_by('-views')[:7]

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
        kwargs['category_list_nav'] = Category.objects.filter((~Q(title="land")))
        kwargs['category_list'] = Category.objects.all()
        kwargs['brands_list'] = Brand.objects.order_by('-views')[:7]
        kwargs['driving_list'] = School.objects.order_by('-views')[:7]
        kwargs['hotels_list'] = Hotel.objects.order_by('-views')[:7]
        kwargs['realestates_list'] = RealEstate.objects.order_by('-views')[:7]

        return super().get_context_data(**kwargs)

    def get_queryset(self):

        self.locality = Locality.objects.all() 
        self.categoryNav = Category.objects.filter((~Q(title="land")))
        self.category = Category.objects.all()



        self.reg = get_object_or_404(Region, name=self.kwargs.get('region'))
        queryset = self.model.objects.filter(region=self.reg)
        return queryset.order_by('-id')












def PrivacyPolicyPage(request):
    context = {
        'category_list_nav': Category.objects.filter((~Q(title="land"))),
        'category_list': Category.objects.all(),
        'brands_list': Brand.objects.order_by('-views')[:7],
        'driving_list': School.objects.order_by('-views')[:7],
        'hotels_list': Hotel.objects.order_by('-views')[:7],
        'realestates_list': RealEstate.objects.order_by('-views')[:7],
    }
    return render(request, 'privacy-policy.html', context)




def ReturnPolicyPage(request):
    context = {
        'category_list_nav': Category.objects.filter((~Q(title="land"))),
        'category_list': Category.objects.all(),
        'brands_list': Brand.objects.order_by('-views')[:7],
        'driving_list': School.objects.order_by('-views')[:7],
        'hotels_list': Hotel.objects.order_by('-views')[:7],
        'realestates_list': RealEstate.objects.order_by('-views')[:7],
    }
    return render(request, 'return-policy.html', context)

def FaqsPage(request):
    context = {
        'category_list_nav': Category.objects.filter((~Q(title="land"))),
        'category_list': Category.objects.all(),
        'brands_list': Brand.objects.order_by('-views')[:7],
        'driving_list': School.objects.order_by('-views')[:7],
        'hotels_list': Hotel.objects.order_by('-views')[:7],
        'realestates_list': RealEstate.objects.order_by('-views')[:7],
    }
    return render(request, 'faqs.html', context)


def SafetyPage(request):
    context = {
        'category_list_nav': Category.objects.filter((~Q(title="land"))),
        'category_list': Category.objects.all(),
        'brands_list': Brand.objects.order_by('-views')[:7],
        'driving_list': School.objects.order_by('-views')[:7],
        'hotels_list': Hotel.objects.order_by('-views')[:7],
        'realestates_list': RealEstate.objects.order_by('-views')[:7],
    }
    return render(request, 'safety-tips.html', context)


def ConditionPage(request):
    context = {
        'category_list_nav': Category.objects.filter((~Q(title="land"))),
        'category_list': Category.objects.all(),
        'brands_list': Brand.objects.order_by('-views')[:7],
        'driving_list': School.objects.order_by('-views')[:7],
        'hotels_list': Hotel.objects.order_by('-views')[:7],
        'realestates_list': RealEstate.objects.order_by('-views')[:7],
    }
    return render(request, 'condition.html', context)






class SearchBarListView(ListView):
    model = Property
    context_object_name = 'lists'
    template_name = 'property/search-list.html'
    paginate_by = 24

    def get_context_data(self, **kwargs):
        kwargs['category_list_nav'] = Category.objects.filter((~Q(title="land")))
        kwargs['category_list'] = Category.objects.all()
        kwargs['brands_list'] = Brand.objects.order_by('-views')[:7]
        kwargs['driving_list'] = School.objects.order_by('-views')[:7]
        kwargs['hotels_list'] = Hotel.objects.order_by('-views')[:7]
        kwargs['realestates_list'] = RealEstate.objects.order_by('-views')[:7]

        kwargs['page_title'] = ''
        kwargs['form_category'] = self.category
        kwargs['filter'] = self.filter
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        query = self.request.GET.get('search-title')
        self.category = self.request.GET.get('categories')
        if self.category == 'property':
            self.filter = PropertyFilter(self.request.GET, queryset= self.model.filter(title__icontains=query).objects.order_by('-id'))
        elif self.category == 'cars':
            self.filter = CarSideFilter(self.request.GET, queryset= Car.objects.filter(title__icontains=query).order_by('-id'))
        elif self.category == 'spareparts':
            self.filter = SparePartFilter(self.request.GET, queryset= SparePart.objects.filter(title__icontains=query).order_by('-id'))
        elif self.category == 'hotels':
            self.filter = HotelFilter(self.request.GET, queryset= Hotel.objects.filter(title__icontains=query).order_by('-id'))
        elif self.category == 'hotelrooms':
            self.filter = HotelRoomFilter(self.request.GET, queryset= HotelRoom.objects.filter(title__icontains=query).order_by('-id'))
        elif self.category == 'realestates':
            self.filter = RealEstateFilter(self.request.GET, queryset= RealEstate.objects.filter(title__icontains=query).order_by('-id'))
        elif self.category == 'schools':
            self.filter = SchoolFilter(self.request.GET, queryset= School.objects.filter(title__icontains=query).order_by('-id'))
        elif self.category == 'lands':
            self.landCategory = get_object_or_404(Category, title='land') 
            self.filter = PropertyCategoryFilter(self.request.GET, queryset=self.model.objects.filter(title__icontains=query, category=self.landCategory)) 
        return self.filter.qs