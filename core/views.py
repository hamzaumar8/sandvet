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
        kwargs['locality'] = self.locality
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.locality = Locality.objects.all() 
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



class LocalityListView(ListView):
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
        self.locality = get_object_or_404(Locality, name=self.kwargs.get('locality'))
        queryset = self.model.objects.filter(locality=self.locality)
        return queryset.order_by('-id')


