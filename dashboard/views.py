from django.shortcuts import render
from property.models import Property, LandProperty, CarProperty
from .forms import PropertyForm
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
    # assetland_form = AssetLandForm()
       
    context = {
        "dash_title": 'Add Property',
        "property_form": propertyForm,
    }
    return render(request, "dashboard/add-property.html", context)
