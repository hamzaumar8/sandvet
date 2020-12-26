from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Count, Q
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from property.models import Property, LandProperty, Category, RealEstate, RealEstateImage
from dashboard.forms import PropertyForm, PropertyLandForm, CarForm, CarImagesForm, BrandForm, TypeForm, SparePartForm, SparePartImagesForm, SchoolForm, SchoolImagesForm, CategoryForm, RealEstateForm, RealEstateImagesForm, SocialHandleForm
from core.models import Locality
from cars.models import CarImage, Car, Brand, Type, School, SparePart, SparePartImage, School, SchoolImage
from dashboard.decorators import check_admin


# Create your views here.
def gen_asset_id(moduleName):
    moduleInstance = moduleName.objects.last()
    if moduleInstance is not None:
        return (moduleInstance.id + 1)
    return 1



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
            
            # locality = propland_form.cleaned_data['locality']
            location = propland_form.cleaned_data['location']

            instance = form.save(request)
            prop = Property.objects.get(pk=instance.id)

            propland_obj = LandProperty.objects.create(
                property=prop,
                # locality=locality, 
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
def CategoryPage(request):
    category = Category.objects.all()
    context = {
        'dash_title': 'Category',
        'category_list': category
    }
    return render(request, 'dashboard/category.html', context)

@login_required
@check_admin
def CategoryAddPage(request):
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category  been Added succesfully')
            return redirect('dashboard:categories')
        else:
            print(form.errors)
    context = {
        "dash_title": 'Add Category',
        "form": form,
    }
    return render(request, "dashboard/add-locality.html", context)


@login_required
@check_admin
def DeleteCategory(request, *args, **kwargs):
    get_object_or_404(Category, pk=kwargs["id"]).delete()
    messages.success(request, "Category deleted successfully")
    return redirect(reverse("dashboard:categories"))




@login_required
@check_admin
def CategoryEditPage(request, *args, **kwargs):
    category = get_object_or_404(Category, pk=kwargs["id"])
    form = CategoryForm(instance=category)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category  been updated succesfully')
            return redirect('dashboard:categories')
        else:
            print(form.errors)
    context = {
        "dash_title": 'Edit Category',
        "form": form,
    }
    return render(request, "dashboard/edit-locality.html", context)





@login_required
@check_admin
def RealEstatePage(request):
    realestate = RealEstate.objects.all().annotate(num_props=Count('realestates', distinct=True))
    context = {
        'dash_title': 'Real Estate',
        'realestate_list': realestate
    }
    return render(request, 'dashboard/real-estate.html', context)


@login_required
@check_admin
def FeaturedRealEstate(request, *args, **kwargs):
    realestate = get_object_or_404(RealEstate, pk=kwargs["id"])
    realestate_qs = RealEstate.objects.filter(id=realestate.id)
    if realestate.featured == 1:
        realestate_qs.update(featured=0)
    else:
        realestate_qs.update(featured=1)
    messages.success(request, "Updated successfully")
    return redirect('dashboard:realestates')



@login_required
@check_admin
def DeleteRealEstate(request, *args, **kwargs):
    get_object_or_404(RealEstate, pk=kwargs["id"]).delete()
    messages.success(request, "Real Estate deleted successfully")
    return redirect(reverse("dashboard:realestate"))




@login_required
@check_admin
def RealEstateAddPage(request):
    form = RealEstateForm()
    handle_form = SocialHandleForm()
    image_form = RealEstateImagesForm()
    if request.method == "POST":
        form = RealEstateForm(request.POST, request.FILES)
        img_form = RealEstateImagesForm(request.POST, request.FILES)
        handle_form = SocialHandleForm(request.POST, request.FILES)
        files = request.FILES.getlist("images")
        if form.is_valid() and img_form.is_valid() and handle_form.is_valid():
            inst = form.save()
            handle = handle_form.save()
            handle.realestate = inst
            handle.save()
            print(handle.realestate)
            for imagefile in files:
                file_instance = RealEstateImage(realestate=inst, images=imagefile)
                file_instance.save()
            messages.success(request, 'Real Estate  been Added succesfully')
            return redirect('dashboard:realestates')
        else:
            print(form.errors)
    context = {
        "dash_title": 'Add Real Estate',
        "form": form,
        "handle_form": handle_form,
        "image_form": image_form,
    }
    return render(request, "dashboard/add-realestate.html", context)