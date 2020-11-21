from django.urls import path
from .views import *


app_name = 'core'

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),

    path('ctg/<str:category>/', CategoryListView.as_view(), name='category'),
    path('<str:locality>/locality/', LocalityListView.as_view(), name='locality'),

    path('ajax_subscriptionform/', subscriptionForm),
    path('contact-us/', contactPage, name='contact'),
]