from django import forms
from property.models import Subscription 
from phonenumber_field.formfields import PhoneNumberField
from .models import Booking

class SubscriptionForm(forms.ModelForm):  
    class Meta:
        model = Subscription
        fields = ['email', 'locality', 'category', 'purpose', 'bed', 'from_price', 'to_price']





class BookingForm(forms.ModelForm):
    phone_number = PhoneNumberField(
        required = True,
        label='Phone Number',
        widget=forms.TextInput(
            attrs={
                'placeholder': '+233558733398',
                'required': True,
            }
        ),
    )

    email =  forms.CharField(
        required = True,
        label='Email',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'example@domain.com',
                'type': 'email',
            }
        )
    )
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone_number', 'subject', 'message']

