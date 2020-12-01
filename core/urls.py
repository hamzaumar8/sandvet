from django.urls import path
from .views import *


app_name = 'core'

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),

    path('category/<str:category>/', CategoryListView.as_view(), name='category'),
    path('locality/<str:locality>/', LocalityListView.as_view(), name='locality'),
    path('region/<str:region>/', RegionListView.as_view(), name='region'),
    path('land/', LandListView.as_view(), name='land'),
    

    path('ajax_subscriptionform/', subscriptionForm),
    path('contact-us/', contactPage, name='contact'),
    path('about-us/', aboutPage, name='about'),
]