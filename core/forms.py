from django import forms
from property.models import Subscription , HotelRoomBooking
from phonenumber_field.formfields import PhoneNumberField
from .models import Booking, Contact


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

class HotelBookingForm(forms.ModelForm):
    check_in = forms.DateField(
        input_formats=["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"],
        required = True,
        label='Check In Date and Time',
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local'
        })
    )
    check_out = forms.DateField(
        input_formats=["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"],
        required = True,
        label='Check Out Date',
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local'
        })
    )

    class Meta:
        model = HotelRoomBooking
        fields = ['check_in', 'check_out']






class ContactForm(forms.ModelForm):
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
        model = Contact
        fields = ['name', 'email', 'phone_number',  'message']