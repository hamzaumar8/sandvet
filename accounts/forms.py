from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import SignupForm
from phonenumber_field.formfields import PhoneNumberField

class CustomSignupForm(SignupForm):
    
    fullname = forms.CharField(
        min_length=7,
        widget=forms.TextInput(attrs={
            'placeholder': 'Full Name',
            'required': True,
        }),
    )

    phone_number = PhoneNumberField(
        required = True,
        label='Phone Number',
        widget=forms.TextInput(
            attrs={
                'placeholder': '+233557866983',
                'required': True
            }
        ),
    )
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        cleaned_data = super(CustomSignupForm, self).clean()
        fullname = cleaned_data["fullname"]
        if ' ' in fullname:
            user.first_name = fullname.split(' ')[0]
            user.last_name = fullname.split(' ')[1]
        else:
            user.first_fullname = fullname

        user_profile = user.profile
        user_profile.phone_number = cleaned_data['phone_number']
        user.save() 
        user_profile.save()
        return user

