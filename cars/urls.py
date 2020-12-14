from django.urls import path
from . import views


app_name = 'cars'

urlpatterns = [
    path('', views.CarListView.as_view() , name='cars'),
    path('detail/<slug>/', views.CarDetail, name='car-detail'),
    path('brands/<slug>/', views.BrandListView.as_view(), name='brand'),
    path('brands/', views.BrandsView.as_view(), name='brands'),
]