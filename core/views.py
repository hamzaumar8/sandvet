from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, ListView, DetailView
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import  JsonResponse, HttpResponse
from django.db.models import Q
from property.models import Property, Category, Testimony, Subscription
from property.filters import HomePropertFilter
from .forms import SubscriptionForm
from .models import Locality
# Create your views here.
class IndexPageView(ListView):
    model = Property
    context_object_name = 'lists'
    template_name = 'index.html'
    # paginate_by = 10

    def get_context_data(self, **kwargs):
        kwargs['category_list_nav'] = self.categoryNav
        kwargs['category_list'] = self.category
        kwargs['testimonys'] = self.testimony
        kwargs['filter'] = self.filter
        kwargs['subscription_form'] = self.subscriptionform
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.subscriptionform = SubscriptionForm()
        self.categoryNav = Category.objects.filter((~Q(title="land")))
        self.category = Category.objects.all()
        self.property = Property.objects.all()
        self.testimony = Testimony.objects.all()
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




@csrf_exempt
def subscriptionForm(request):
    response_data = {}

    if request.method == "POST" and request.is_ajax:
        
        email = request.POST['email']
        locality = request.POST['locality']
        category = request.POST['category']
        purpose = request.POST['purpose']
        bed = request.POST['bed']
        from_price = request.POST['from_price']
        to_price = request.POST['to_price']

        locality = Locality.objects.get(id=locality)
        category = Category.objects.get(id=category)

        new_subscription = Subscription.objects.create(
            email=email,
            locality=locality,
            category=category,
            purpose=purpose,
            bed=bed,
            from_price=from_price,
            to_price=to_price,
        )

        new_subscription.save()
        response_data['email'] = email
        response_data['locality'] = locality
        response_data['category'] = category
        response_data['purpose'] = purpose
        response_data['bed'] = bed
        response_data['from_price'] = from_price
        response_data['to_price'] = to_price


        return HttpResponse(JsonResponse(response_data))
    return HttpResponse(JsonResponse(response_data))

