from django.urls import path
from .views import *


app_name = 'property'

urlpatterns = [
    path('property/', PropertyListView.as_view(), name='property'),
    path('for-sale/', ForSaleListView.as_view(), name='for-sale'),
    path('<str:category>/for-sale/', CategoryForSaleListView.as_view(), name='for-sale-cate'),
    path('for-rent/', ForRentListView.as_view(), name='for-rent'),
    path('<str:category>/for-rent/', CategoryForRentListView.as_view(), name='for-rent-cate'),

    path('detail/<slug>/', propertyDetail, name='property'),

]