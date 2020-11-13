from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    
    fullname = forms.CharField(
        min_length=7,
        widget=forms.TextInput(attrs={
            'placeholder': 'Full fullname',
            'required': True
        }),
    )

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        cleaned_data = super(CustomSignupForm, self).clean()
        fullname = cleaned_data["fullname"]
        if ' ' in fullname:
            print(fullname)
            user.first_name = fullname.split(' ')[0]
            user.last_name = fullname.split(' ')[1]
        else:
            user.first_fullname = fullname
        user.save() 
        return user

