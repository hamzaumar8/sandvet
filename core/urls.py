from django.urls import path
from .views import *


app_name = 'core'

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),

    path('ctg/<str:category>/', CategoryListView.as_view(), name='category'),

    path('ajax_subscriptionform/', subscriptionForm),
]