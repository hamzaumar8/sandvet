from django.urls import path
from .views import *


app_name = 'core'

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),

    path('category/<str:category>/', CategoryListView.as_view(), name='category'),
    path('locality/<str:locality>/', LocalityListView.as_view(), name='locality'),
    path('region/<str:region>/', RegionListView.as_view(), name='region'),
    

    path('ajax_subscriptionform/', subscriptionForm),
    path('contact-us/', contactPage, name='contact'),
    path('about-us/', aboutPage, name='about'),
    path('terms-and-conditions/', ConditionPage, name='conditions'),
    path('privacy-policy/', PrivacyPolicyPage, name='privacy-policy'),
    path('return-policy/', ReturnPolicyPage, name='return-policy'),
    path('faqs/', FaqsPage, name='faqs'),
    path('safety-tips/', SafetyPage, name='safety-tips'),
]