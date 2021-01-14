from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Count, Q
from django.contrib.auth import  logout
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from property.models import Property, LandProperty, HouseProperty, PropertyBooking, HotelBooking, RealEstateBooking, HotelRoomBooking
from core.models import Locality, Booking
from dashboard.forms import PropertyForm, PropertyLandForm, CarForm, CarImagesForm, BrandForm, TypeForm, SparePartForm, SparePartImagesForm, SchoolForm, SchoolImagesForm, LocalityForm
from cars.models import CarImage, Car, Brand, Type, School, SparePart, SparePartImage, School, SchoolImage, CarBooking, SchoolBooking, SparePartBooking
from dashboard.decorators import check_admin
# Create your views here.
def gen_asset_id(moduleName):
    moduleInstance = moduleName.objects.last()
    if moduleInstance is not None:
        return (moduleInstance.id + 1)
    return 1

@login_required
def authLogout(request):
    logout(request)
    messages.success(request, "You have signed out.")
    return redirect('account_login')

def auth(request):
    if request.user.is_superuser:
        return redirect(reverse("dashboard:dashboard"), permanent=True)
    else:
        return redirect(reverse("core:index"), permanent=True)



@login_required
@check_admin
def dashboardPage(request):
    user_count = User.objects.filter(~Q(is_superuser=True)).count()
    bookings = Booking.objects.filter(read=False).order_by('-id')[:10]
    context = {
        'dash_title': 'Dashboard',
        'bookings': bookings,
        "user_count": user_count,
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
    form = LocalityForm(instance=locality)
    if request.method == "POST":
        form = LocalityForm(request.POST, instance=locality)
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




@login_required
@check_admin
def BookingsPage(request):
    bookings = Booking.objects.order_by('-id')
    context = {
        'dash_title': 'Bookings',
        'bookings': bookings
    }
    return render(request, 'dashboard/bookings.html', context)


@login_required
@check_admin
def DeleteBooking(request, *args, **kwargs):
    get_object_or_404(Booking, pk=kwargs["id"]).delete()
    messages.success(request, "Booking deleted successfully")
    return redirect(reverse("dashboard:bookings"))


@login_required
@check_admin
def ViewBooking(request, *args, **kwargs):
    booking = get_object_or_404(Booking, pk=kwargs["id"])

    booking.read = True
    booking.save()

    context = {
        'dash_title': 'View Bookings',
        "booking": booking,
    }
    return render(request, "dashboard/view-booking.html", context)





@login_required
@check_admin
def CarBookingsPage(request):
    bookings = CarBooking.objects.order_by('-id')
    context = {
        'dash_title': 'Car Bookings',
        'bookings': bookings
    }
    return render(request, 'dashboard/ind-bookings.html', context)


@login_required
@check_admin
def SparePartBookingsPage(request):
    bookings = SparePartBooking.objects.order_by('-id')
    context = {
        'dash_title': 'Spare Parts Bookings',
        'bookings': bookings
    }
    return render(request, 'dashboard/ind-bookings.html', context)


@login_required
@check_admin
def SchoolBookingsPage(request):
    bookings = SchoolBooking.objects.order_by('-id')
    context = {
        'dash_title': 'School Bookings',
        'bookings': bookings
    }
    return render(request, 'dashboard/ind-bookings.html', context)


@login_required
@check_admin
def PropertyBookingsPage(request):
    bookings = PropertyBooking.objects.order_by('-id')
    context = {
        'dash_title': 'Property Bookings',
        'bookings': bookings
    }
    return render(request, 'dashboard/ind-bookings.html', context)

@login_required
@check_admin
def HotelBookingsPage(request):
    bookings = HotelBooking.objects.order_by('-id')
    context = {
        'dash_title': 'Hotel Bookings',
        'bookings': bookings
    }
    return render(request, 'dashboard/ind-bookings.html', context)

@login_required
@check_admin
def RealEstateBookingsPage(request):
    bookings = RealEstateBooking.objects.order_by('-id')
    context = {
        'dash_title': 'Real Estate Bookings',
        'bookings': bookings
    }
    return render(request, 'dashboard/ind-bookings.html', context)

@login_required
@check_admin
def HotelRoomBookingsPage(request):
    bookings = HotelRoomBooking.objects.order_by('-id')
    context = {
        'dash_title': 'Hotel Room Bookings',
        'bookings': bookings
    }
    return render(request, 'dashboard/ind-bookings.html', context)
