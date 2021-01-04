from django import forms
from property.models import Subscription 
from .models import Booking


class SubscriptionForm(forms.ModelForm):  
    class Meta:
        model = Subscription
        fields = ['email', 'locality', 'category', 'purpose', 'bed', 'from_price', 'to_price']





class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone_number', 'subject', 'message']

