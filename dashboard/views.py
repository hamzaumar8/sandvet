from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from property.models import Property, LandProperty
from .forms import PropertyForm, PropertyLandForm
# Create your views here.
def gen_asset_id(moduleName):
    moduleInstance = moduleName.objects.last()
    if moduleInstance is not None:
        return (moduleInstance.id + 1)
    return 1




def dashboardPage(request):
    context = {
        'dash_title': 'Dashboard',
    }
    return render(request, 'dashboard/index.html', context)


def propertyPage(request):
    prop_list = Property.objects.all()
    context = {
        'dash_title': 'Properties',
        'property_list': prop_list
    }
    return render(request, 'dashboard/property.html', context)




def PropertAddPage(request):

    propertyForm = PropertyForm()
    propertyLandForm = PropertyLandForm()
       
    context = {
        "dash_title": 'Add Property',
        "property_form": propertyForm,
        "propertyland_form": propertyLandForm,
    }
    return render(request, "dashboard/add-property.html", context)





def ajaxPropertyLandAdd(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = PropertyForm(request.POST, request.FILES)
        propland_form = PropertyLandForm(request.POST, request.FILES)
        if form.is_valid() and propland_form.is_valid():
            
            region = propland_form.cleaned_data['region']
            locality = propland_form.cleaned_data['locality']
            location = propland_form.cleaned_data['location']

            instance = form.save(request)
            prop = Property.objects.get(pk=instance.id)

            propland_obj = LandProperty.objects.create(
                property=prop,
                region=region, 
                locality=locality, 
                location=location, 
            )

            propland_obj.save()
            return JsonResponse({'error': False, 'message': 'Uploaded Successfully'}, status=200)
        else:
            # some form errors occured.
            print(propland_form.errors)
            print(form.errors)
            return JsonResponse({'error': True, 'errors': form.errors}, status=400)

    # some error occured
    return JsonResponse({}, status=400)


