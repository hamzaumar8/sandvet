from django.urls import path
from .views import *


app_name = 'property'

urlpatterns = [
    path('', PropertyListView.as_view(), name='property'),
    path('for-sale/', ForSaleListView.as_view(), name='for-sale'),
    path('<slug>/for-sale/', CategoryForSaleListView.as_view(), name='for-sale-cate'),
    path('for-rent/', ForRentListView.as_view(), name='for-rent'),
    path('<slug>/for-rent/', CategoryForRentListView.as_view(), name='for-rent-cate'),

    path('detail/<slug>/', propertyDetail, name='property'),


    path('search/', SearchListView.as_view(), name='search'),


    path('check/', checkPage, name='check'),

    path('land/', LandListView.as_view(), name='land'),

    # path('actor/', ActorsSearchList.as_view(), name='actor'),
]