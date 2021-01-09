from django.views.generic import View, ListView, DetailView, FormView
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Q, Count
from .models import Property, Category, LandProperty, RealEstate, Hotel, HotelRoom, PropertyBooking, HotelBooking, RealEstateBooking, HotelRoomBooking
from .filters import PropertyFilter, PropertyCategoryFilter, RealEstateFilter, HotelFilter, HotelRoomFilter
from core.models import Locality, Region
from core.forms import BookingForm, HotelBookingForm
from cars.models import Car, SparePart, School, Brand

# Create your views here.
class PropertyListView(ListView):
    model = Property
    context_object_name = 'lists'
    template_name = 'property/list.html'
    paginate_by = 24

    def get_context_data(self, **kwargs):
        kwargs['category_list_nav'] = Category.objects.filter((~Q(title="land")))
        kwargs['category_list'] = Category.objects.all()
        kwargs['brands_list'] = Brand.objects.order_by('-views')[:7]
        kwargs['driving_list'] = School.objects.order_by('-views')[:7]
        kwargs['hotels_list'] = Hotel.objects.order_by('-views')[:7]
        kwargs['realestates_list'] = RealEstate.objects.order_by('-views')[:7]

        kwargs['page_title'] = 'All Properties'
        kwargs['filter'] = self.filter
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
        kwargs['category_list_nav'] = Category.objects.filter((~Q(title="land")))
        kwargs['category_list'] = Category.objects.all()
        kwargs['brands_list'] = Brand.objects.order_by('-views')[:7]
        kwargs['driving_list'] = School.objects.order_by('-views')[:7]
        kwargs['hotels_list'] = Hotel.objects.order_by('-views')[:7]
        kwargs['realestates_list'] = RealEstate.objects.order_by('-views')[:7]

        kwargs['page_title'] = 'For Sale'
        kwargs['filter'] = self.filter

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
        kwargs['category_list_nav'] = Category.objects.filter((~Q(title="land")))
        kwargs['category_list'] = Category.objects.all()
        kwargs['brands_list'] = Brand.objects.order_by('-views')[:7]
        kwargs['driving_list'] = School.objects.order_by('-views')[:7]
        kwargs['hotels_list'] = Hotel.objects.order_by('-views')[:7]
        kwargs['realestates_list'] = RealEstate.objects.order_by('-views')[:7]

        kwargs['page_title'] = 'For Sale'
        kwargs['filter'] = self.filter

        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.forsale = self.model.objects.filter(purpose='rent')
        self.filter = PropertyFilter(self.request.GET, queryset=self.forsale.order_by('-id')) 
        return self.filter.qs




def propertyDetail(request, slug):
    lists = get_object_or_404(Property, slug=slug)
    session_key = 'viewed_property_{}'.format(lists.pk) 
    if not request.session.get(session_key, False):
        lists.views += 1
        lists.save()
        request.session[session_key] = True

    school_list = School.objects.order_by('-id')[:3]
    cars_list = Car.objects.filter(region=lists.region).order_by('-id')[:3]
    region_list = RealEstate.objects.filter((~Q(id=lists.id)), region=lists.region).order_by('-id')[:3]
    latest_list = Car.objects.order_by('-id')[:6]
    latest_property = Property.objects.filter(~Q(id=lists.id)).order_by('-id')[:6]
    latest_spareparts = SparePart.objects.filter(~Q(id=lists.id)).order_by('-id')[:6]


    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            inst = form.save()
            PropertyBooking.objects.create(booking=inst, property=lists)
            messages.success(request, "We've received your message. We would get back to you soon.")
            return redirect('property:property-detail', slug=lists.slug)
        else:
            print(form.errors)

    context = {
        'page_title': 'Properties',
        'object': lists, 
        'latest_lists': latest_list,
        'region_list': region_list,
        'latest_property': latest_property,
        'form': form
    } 
    context['category_list_nav'] = Category.objects.filter((~Q(title="land")))
    context['category_list'] = Category.objects.all()
    context['brands_list'] = Brand.objects.order_by('-views')[:7]
    context['driving_list'] = School.objects.order_by('-views')[:7]
    context['hotels_list'] = Hotel.objects.order_by('-views')[:7]
    context['realestates_list'] = RealEstate.objects.order_by('-views')[:7]    
    return render(request, 'list-detail.html', context)




class CategoryForSaleListView(ListView):
    model = Property
    context_object_name = 'lists'
    template_name = 'list.html'
    template_name = 'property/list.html'
    paginate_by = 24

    def get_context_data(self, **kwargs):
        kwargs['category_list_nav'] = Category.objects.filter((~Q(title="land")))
        kwargs['category_list'] = Category.objects.all()
        kwargs['brands_list'] = Brand.objects.order_by('-views')[:7]
        kwargs['driving_list'] = School.objects.order_by('-views')[:7]
        kwargs['hotels_list'] = Hotel.objects.order_by('-views')[:7]
        kwargs['realestates_list'] = RealEstate.objects.order_by('-views')[:7]

        kwargs['page_title'] = f'{self.slug} For Sale'
        kwargs['filter'] = self.filter

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
        kwargs['category_list_nav'] = Category.objects.filter((~Q(title="land")))
        kwargs['category_list'] = Category.objects.all()
        kwargs['brands_list'] = Brand.objects.order_by('-views')[:7]
        kwargs['driving_list'] = School.objects.order_by('-views')[:7]
        kwargs['hotels_list'] = Hotel.objects.order_by('-views')[:7]
        kwargs['realestates_list'] = RealEstate.objects.order_by('-views')[:7]

        kwargs['page_title'] = f'{self.slug} For Rent'
        kwargs['filter'] = self.filter

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
        kwargs['category_list_nav'] = Category.objects.filter((~Q(title="land")))
        kwargs['category_list'] = Category.objects.all()
        kwargs['brands_list'] = Brand.objects.order_by('-views')[:7]
        kwargs['driving_list'] = School.objects.order_by('-views')[:7]
        kwargs['hotels_list'] = Hotel.objects.order_by('-views')[:7]
        kwargs['realestates_list'] = RealEstate.objects.order_by('-views')[:7]

        kwargs['filter'] = self.filter
        
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.filter = PropertyFilter(self.request.GET, queryset= self.model.objects.all()) 
        
        self.query = self.filter.qs
        return self.query



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
        kwargs['category_list_nav'] = Category.objects.filter((~Q(title="land")))
        kwargs['category_list'] = Category.objects.all()
        kwargs['brands_list'] = Brand.objects.order_by('-views')[:7]
        kwargs['driving_list'] = School.objects.order_by('-views')[:7]
        kwargs['hotels_list'] = Hotel.objects.order_by('-views')[:7]
        kwargs['realestates_list'] = RealEstate.objects.order_by('-views')[:7]

        kwargs['page_title'] = "Land"
        kwargs['filter'] = self.filter

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
        kwargs['category_list_nav'] = Category.objects.filter((~Q(title="land")))
        kwargs['category_list'] = Category.objects.all()
        kwargs['brands_list'] = Brand.objects.order_by('-views')[:7]
        kwargs['driving_list'] = School.objects.order_by('-views')[:7]
        kwargs['hotels_list'] = Hotel.objects.order_by('-views')[:7]
        kwargs['realestates_list'] = RealEstate.objects.order_by('-views')[:7]

        kwargs['page_title'] = "RealEstate"
        kwargs['filter'] = self.filter

        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.filter = RealEstateFilter(self.request.GET, queryset=self.model.objects.order_by('-id')) 
        return self.filter.qs.annotate(num_props=Count('realestate', distinct=True))



def RealestateDetail(request, slug):
    lists = get_object_or_404(RealEstate, slug=slug)

    session_key = 'viewed_estate_{}'.format(lists.pk) 
    if not request.session.get(session_key, False):
        lists.views += 1
        lists.save()
        request.session[session_key] = True

    school_list = School.objects.order_by('-id')[:3]
    cars_list = Car.objects.filter(region=lists.region).order_by('-id')[:3]
    property_list = Property.objects.filter(region=lists.region).order_by('-id')[:3]
    region_list = RealEstate.objects.filter((~Q(id=lists.id)), region=lists.region).order_by('-id')[:3]
    realestate_list = RealEstate.objects.filter(~Q(id=lists.id), region=lists.region).order_by('-id')[:4]
    latest_list = Car.objects.order_by('-id')[:6]
    latest_property = Property.objects.order_by('-id')[:6]
    latest_spareparts = SparePart.objects.filter(~Q(id=lists.id)).order_by('-id')[:6]

    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            inst = form.save()
            RealEstateBooking.objects.create(booking=inst, realestate=lists)
            messages.success(request, "We've received your message. We would get back to you soon.")
            return redirect('property:realestate-detail', slug=lists.slug)
        else:
            print(form.errors)
    context = {
        'object': lists, 
        'latest_lists': latest_list,
        'realestate_lists': realestate_list,
        'region_list': region_list,
        'latest_spareparts': latest_spareparts,
        'latest_property': latest_property,
        'property_list': property_list,
        'school_list': school_list,
        'form': form,
    }  
    context['category_list_nav'] = Category.objects.filter((~Q(title="land")))
    context['category_list'] = Category.objects.all()
    context['brands_list'] = Brand.objects.order_by('-views')[:7]
    context['driving_list'] = School.objects.order_by('-views')[:7]
    context['hotels_list'] = Hotel.objects.order_by('-views')[:7]
    context['realestates_list'] = RealEstate.objects.order_by('-views')[:7]   
    return render(request, 'list-detail.html', context)



class HotelListView(ListView):
    model = Hotel
    context_object_name = 'lists'
    template_name = 'property/list.html'
    paginate_by = 24

    def get_context_data(self, **kwargs):
        kwargs['category_list_nav'] = Category.objects.filter((~Q(title="land")))
        kwargs['category_list'] = Category.objects.all()
        kwargs['brands_list'] = Brand.objects.order_by('-views')[:7]
        kwargs['driving_list'] = School.objects.order_by('-views')[:7]
        kwargs['hotels_list'] = Hotel.objects.order_by('-views')[:7]
        kwargs['realestates_list'] = RealEstate.objects.order_by('-views')[:7]

        kwargs['page_title'] = "Hotels"
        kwargs['filter'] = self.filter

        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.filter = HotelFilter(self.request.GET, queryset=self.model.objects.order_by('-id')) 
        return self.filter.qs





def HotelDetail(request, slug):
    lists = get_object_or_404(Hotel, slug=slug)
    hotelimages = lists.hotelimages.order_by('-id')
    session_key = 'viewed_hotel_{}'.format(lists.pk) 
    if not request.session.get(session_key, False):
        lists.views += 1
        lists.save()
        request.session[session_key] = True

    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            inst = form.save()
            HotelBooking.objects.create(booking=inst, hotel=lists)
            messages.success(request, "We've received your message. We would get back to you soon.")
            return redirect('property:hotel-detail', slug=lists.slug)
        else:
            print(form.errors)

    context = {
        'object': lists, 
        'objectimages': hotelimages,
        'form': form
    }    
    return render(request, 'list-detail.html', context)

def HotelRoomDetail(request, slug):
    lists = get_object_or_404(HotelRoom, slug=slug)
    roomimages = lists.hotelroomimages.order_by('-id')

    session_key = 'viewed_room_{}'.format(lists.pk) 
    if not request.session.get(session_key, False):
        lists.views += 1
        lists.save()
        request.session[session_key] = True

    form = BookingForm()
    hotelForm = HotelBookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        hotelForm = HotelBookingForm(request.POST)
        if form.is_valid() and hotelForm.is_valid():
            inst = form.save()
            room = hotelForm.save()
            room.booking = inst
            room.hotelroom = lists
            room.save()
            # HotelRoomBooking.objects.create(booking=inst, hotelroom=lists)
            messages.success(request, "We've received your message. We would get back to you soon.")
            return redirect('property:hotel-room-detail', slug=lists.slug)
        else:
            print(form.errors)

    context = {
        'object': lists, 
        'objectimages': roomimages,
        "form": form,
        "hotelform": hotelForm
    }   
    context['category_list_nav'] = Category.objects.filter((~Q(title="land")))
    context['category_list'] = Category.objects.all()
    context['brands_list'] = Brand.objects.order_by('-views')[:7]
    context['driving_list'] = School.objects.order_by('-views')[:7]
    context['hotels_list'] = Hotel.objects.order_by('-views')[:7]
    context['realestates_list'] = RealEstate.objects.order_by('-views')[:7] 
    return render(request, 'list-detail.html', context)





class HotelRoomListView(ListView):
    model = HotelRoom
    context_object_name = 'lists'
    template_name = 'property/list.html'
    paginate_by = 24

    def get_context_data(self, **kwargs):
        kwargs['category_list_nav'] = Category.objects.filter((~Q(title="land")))
        kwargs['category_list'] = Category.objects.all()
        kwargs['brands_list'] = Brand.objects.order_by('-views')[:7]
        kwargs['driving_list'] = School.objects.order_by('-views')[:7]
        kwargs['hotels_list'] = Hotel.objects.order_by('-views')[:7]
        kwargs['realestates_list'] = RealEstate.objects.order_by('-views')[:7]

        kwargs['page_title'] = "Hotel Rooms"
        kwargs['filter'] = self.filter

        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.filter = HotelRoomFilter(self.request.GET, queryset=self.model.objects.order_by('-id')) 
        return self.filter.qs