from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from property.models import Property, LandProperty
from core.models import Locality
from dashboard.forms import PropertyForm, PropertyLandForm, CarForm, CarImagesForm, BrandForm, TypeForm, SparePartForm, SparePartImagesForm, SchoolForm, SchoolImagesForm, LocalityForm
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
def dashboardPage(request):
    context = {
        'dash_title': 'Dashboard',
    }
    return render(request, 'dashboard/index.html', context)


@login_required
@check_admin
def LocalityPage(request):
    locality = Locality.objects.all()
    context = {
        'dash_title': 'Locality',
        'locality_list': locality
    }
    return render(request, 'dashboard/locality.html', context)


@login_required
@check_admin
def LocalityAddPage(request):
    form = LocalityForm()
    if request.method == "POST":
        form = LocalityForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Locality  been Added succesfully')
            return redirect('dashboard:locality')
        else:
            print(form.errors)
    context = {
        "dash_title": 'Add Locality',
        "form": form,
    }
    return render(request, "dashboard/add-locality.html", context)


@login_required
@check_admin
def DeleteLocality(request, *args, **kwargs):
    get_object_or_404(Locality, pk=kwargs["id"]).delete()
    messages.success(request, "Locality deleted successfully")
    return redirect(reverse("dashboard:locality"))




@login_required
@check_admin
def LocalityEditPage(request, *args, **kwargs):
    locality = get_object_or_404(Locality, pk=kwargs["id"])
    form = CarForm(instance=locality)
    if request.method == "POST":
        form = CarForm(request.POST, instance=locality)
        if form.is_valid():
            form.save()
            messages.success(request, 'Locality  been updated succesfully')
            return redirect('dashboard:locality')
        else:
            print(form.errors)
    context = {
        "dash_title": 'Edit Locality',
        "form": form,
    }
    return render(request, "dashboard/edit-locality.html", context)