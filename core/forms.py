from django import forms
from property.models import Subscription 


class SubscriptionForm(forms.ModelForm):  
    class Meta:
        model = Subscription
        fields = ['email', 'locality', 'category', 'purpose', 'bed', 'from_price', 'to_price']