from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from property.models import Property, LandProperty
from .forms import PropertyForm, PropertyLandForm, CarForm, CarImagesForm, BrandForm, TypeForm
from cars.models import CarImage, Car, Brand, Type
from .decorators import check_admin
# Create your views here.
def gen_asset_id(moduleName):
    moduleInstance = moduleName.objects.last()
    if moduleInstance is not None:
        return (moduleInstance.id + 1)
    return 1



@login_required
@check_admin
def dashboardPage(request):
    context = {
        'dash_title': 'Dashboard',
    }
    return render(request, 'dashboard/index.html', context)


@login_required
@check_admin
def propertyPage(request):
    prop_list = Property.objects.all()
    context = {
        'dash_title': 'Properties',
        'property_list': prop_list
    }
    return render(request, 'dashboard/property.html', context)



@login_required
@check_admin
def PropertyAddPage(request):
    propertyForm = PropertyForm()
    propertyLandForm = PropertyLandForm()
       
    context = {
        "dash_title": 'Add Property',
        "property_form": propertyForm,
        "propertyland_form": propertyLandForm,
    }
    return render(request, "dashboard/add-property.html", context)




@login_required
@check_admin
def ajaxPropertyLandAdd(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = PropertyForm(request.POST, request.FILES)
        propland_form = PropertyLandForm(request.POST, request.FILES)
        if form.is_valid() and propland_form.is_valid():
            
            locality = propland_form.cleaned_data['locality']
            location = propland_form.cleaned_data['location']

            instance = form.save(request)
            prop = Property.objects.get(pk=instance.id)

            propland_obj = LandProperty.objects.create(
                property=prop,
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



@login_required
@check_admin
def CarPage(request):
    car_lists = Car.objects.order_by('-id')
    context = {
        'dash_title': 'Cars',
        'car_lists': car_lists
    }
    return render(request, 'dashboard/car.html', context)


@login_required
@check_admin
def CarAddPage(request):
    form = CarForm()
    image_form = CarImagesForm()
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        img_form = CarImagesForm(request.POST, request.FILES)
        files = request.FILES.getlist("images")
        if form.is_valid() and img_form.is_valid():
            inst = form.save()
            for imagefile in files:
                file_instance = CarImage(car=inst, images=imagefile)
                file_instance.save()
            messages.success(request, 'Car  been Added succesfully')
            return redirect('dashboard:car')
        else:
            print(form.errors)
    context = {
        "dash_title": 'Add Car',
        "form": form,
        "image_form": image_form
    }
    return render(request, "dashboard/add-car.html", context)





@login_required
@check_admin
def DeleteCar(request, *args, **kwargs):
    get_object_or_404(Car, pk=kwargs["id"]).delete()
    messages.success(request, "Car deleted successfully")
    return redirect(reverse("dashboard:car"))



@login_required
@check_admin
def CarEditPage(request, *args, **kwargs):
    car = get_object_or_404(Car, pk=kwargs["id"])
    images = CarImage.objects.filter(car=car)
    form = CarForm(instance=car)
    image_form = CarImagesForm()
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES, instance=car)
        img_form = CarImagesForm(request.POST, request.FILES)
        files = request.FILES.getlist("images")
        if form.is_valid() and img_form.is_valid():
            inst = form.save()
            for imagefile in files:
                file_instance = CarImage(car=inst, images=imagefile)
                file_instance.save()
            messages.success(request, 'Car  been updated succesfully')
            return redirect('dashboard:car')
        else:
            print(form.errors)
    context = {
        "dash_title": 'Add Car',
        "form": form,
        "image_form": image_form,
        "images": images
    }
    return render(request, "dashboard/edit-car.html", context)

@login_required
@check_admin
def DeleteCarImage(request, *args, **kwargs):
    get_object_or_404(CarImage, pk=kwargs["id"]).delete()
    messages.success(request, "Image deleted successfully")
    return HttpResponseRedirect(request.path_info)


@login_required
@check_admin
def ViewCar(request, *args, **kwargs):
    car = get_object_or_404(Car, pk=kwargs["id"])
    images = CarImage.objects.filter(car=car)
    context = {
        "car": car,
        "images": images
    }
    return render(request, "dashboard/view-car.html", context)



@login_required
@check_admin
def FeaturedCar(request, *args, **kwargs):
    car = get_object_or_404(Car, pk=kwargs["id"])
    car_qs = Car.objects.filter(id=car.id)
    if car.featured == 1:
        car_qs.update(featured=0)
    else:
        car_qs.update(featured=1)
    messages.success(request, "Updated successfully")
    return redirect('dashboard:car')







@login_required
@check_admin
def BrandPage(request):
    brands = Brand.objects.order_by('-id')
    context = {
        'dash_title': 'Brands',
        'brands': brands
    }
    return render(request, 'dashboard/brands.html', context)



@login_required
@check_admin
def FeaturedBrand(request, *args, **kwargs):
    brand = get_object_or_404(Brand, pk=kwargs["id"])
    brand_qs = Brand.objects.filter(id=brand.id)
    if brand.featured == 1:
        brand_qs.update(featured=0)
    else:
        brand_qs.update(featured=1)
    messages.success(request, "updated successfully")
    return redirect('dashboard:brands')


@login_required
@check_admin
def ViewBrand(request, *args, **kwargs):
    brand = get_object_or_404(Brand, pk=kwargs["id"])
    context = {
        "brand": brand,
    }
    return render(request, "dashboard/view-brand.html", context)


@login_required
@check_admin
def DeleteBrand(request, *args, **kwargs):
    get_object_or_404(Brand, pk=kwargs["id"]).delete()
    messages.success(request, "Brand deleted successfully")
    return redirect(reverse("dashboard:brands"))



@login_required
@check_admin
def BrandEditPage(request, *args, **kwargs):
    brand = get_object_or_404(Brand, pk=kwargs["id"])
    form = BrandForm(instance=brand)
    if request.method == "POST":
        form = BrandForm(request.POST, request.FILES, instance=brand)
        if form.is_valid():
            form.save()
            messages.success(request, 'brand  been updated succesfully')
            return redirect('dashboard:brands')
        else:
            print(form.errors)
    context = {
        "dash_title": 'Edit Brand',
        "form": form,
    }
    return render(request, "dashboard/edit-car.html", context)






@login_required
@check_admin
def BrandAddPage(request):
    form = BrandForm()
    if request.method == "POST":
        form = BrandForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Brand  been Added succesfully')
            return redirect('dashboard:brands')
        else:
            print(form.errors)
    context = {
        "dash_title": 'Add Brand',
        "form": form,
    }
    return render(request, "dashboard/add-brand.html", context)



@login_required
@check_admin
def TypePage(request):
    types = Type.objects.order_by('-id')
    context = {
        'dash_title': 'Car Types',
        'types': types
    }
    return render(request, 'dashboard/types.html', context)




@login_required
@check_admin
def TypeAddPage(request):
    form = TypeForm()
    if request.method == "POST":
        form = TypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Type  been Added succesfully')
            return redirect('dashboard:types')
        else:
            print(form.errors)
    context = {
        "dash_title": 'Add Car Type',
        "form": form,
    }
    return render(request, "dashboard/add-brand.html", context)


@login_required
@check_admin
def TypeEditPage(request, *args, **kwargs):
    typ = get_object_or_404(Type, pk=kwargs["id"])
    form = TypeForm(instance=typ)
    if request.method == "POST":
        form = TypeForm(request.POST, instance=typ)
        if form.is_valid():
            form.save()
            messages.success(request, 'Car type  been updated succesfully')
            return redirect('dashboard:types')
        else:
            print(form.errors)
    context = {
        "dash_title": 'Edit Car type',
        "form": form,
    }
    return render(request, "dashboard/edit-car.html", context)


@login_required
@check_admin
def DeleteType(request, *args, **kwargs):
    get_object_or_404(Type, pk=kwargs["id"]).delete()
    messages.success(request, "Car Type deleted successfully")
    return redirect(reverse("dashboard:types"))