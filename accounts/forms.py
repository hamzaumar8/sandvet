from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    
    first_name = forms.CharField(
        min_length=7,
        widget=forms.TextInput(attrs={
            'placeholder': 'first Name',
            'required': True,
            # 'class': 'col-md-6'
        }),
    )
    Last_name = forms.CharField(
        min_length=7,
        widget=forms.TextInput(attrs={
            'placeholder': 'Last Name',
            'required': True,
            # 'class': 'col-md-6'
        }),
    )


    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        cleaned_data = super(CustomSignupForm, self).clean()
        first_name = cleaned_data["first_name"]
        last_name = cleaned_data["last_name"]
        # if ' ' in fullname:
        #     print(fullname)
        #     user.first_name = fullname.split(' ')[0]
        #     user.last_name = fullname.split(' ')[1]
        # else:
        #     user.first_fullname = fullname
        user.first_name = first_name
        user.last_name = last_name
        user.save() 
        return user

