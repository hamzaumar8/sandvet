from django.urls import path
from . import views


app_name = 'cars'

urlpatterns = [
    path('', views.CarListView.as_view() , name='cars'),
    path('detail/<slug>/', views.CarDetail, name='car-detail'),
    path('brands/<slug>/', views.BrandListView.as_view(), name='brand'),
    path('brands/', views.BrandsView.as_view(), name='brands'),
    path('car/for-sale/', views.CarListSaleView.as_view(), name='car-for-sale'),
    path('for-hire/', views.CarListHireView.as_view(), name='car-for-hire'),
    path('spare-parts/', views.SparePartListView.as_view(), name='spare-parts'),
    path('spare-part/<slug>/', views.SparePartDetail, name='spare-part-detail'),
    path('driving-schools/', views.SchoolListView.as_view(), name='schools'),
    path('driving-school/<slug>/', views.SchoolDetail, name='school-detail'),
]