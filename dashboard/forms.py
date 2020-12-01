from django import forms
from property.models import Property, PROPERTY_PURPOSE_TYPE



class PropertyForm(forms.ModelForm): 

    purpose = forms.ChoiceField(
        choices=PROPERTY_PURPOSE_TYPE, 
        widget=forms.RadioSelect(attrs={
            'class': 'custom-control-input'
        })
    )
    
    def __init__(self, *args, **kwargs):
        super(PropertyForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            # if not self.files[name].widget.RadioSelect:
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            }) 

            
    class Meta:
        model = Property
        fields = [
            'title', 
            'category', 
            'purpose',
            'price', 
        ]
        
# class AssetLandForm(forms.ModelForm): 
#     location =  forms.CharField(
#         required = True,
#         label='Location/Plot No./Description',
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Location/Plot No./Description'
#             }
#         )
#     )
    
#     nature_of_acquisition =  forms.CharField(
#         required = True,
#         label='Nature Of Acquisition',
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Nature Of Acquisition'
#             }
#         )
#     )
    
#     date_of_acquisition = forms.DateField(
#         input_formats=['%Y-%m-%d'],
#         required = True,
#         label='Date Of Acquisition',
#         widget=forms.DateTimeInput(attrs={
#             'id': 'example-date',
#             'placeholder': 'Date Of Acquisition',
#             'type': 'date'
#         })
#     )
    
#     town_or_district =  forms.CharField(
#         required = True,
#         label='Town / District',
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Town / District'
#             }
#         )
#     )
    

#     purpose_of_acquisition = forms.CharField(
#         required = True,
#         label='Purpose Of Acquisition',
#         widget=forms.Textarea(
#             attrs={
#             'id': 'example-textarea',
#             'placeholder': '',
#             'rows': 5
#             }
#         )
#     )
    
#     current_use = forms.CharField(
#         required = True,
#         label='Current Use/State Of Development',
#         widget=forms.TextInput(
#             attrs={
#             'id': 'simpleinput',
#             'placeholder': 'Some text value...',
#             }
#         )
#     )
    
#     user_agency = forms.CharField(
#         required = True,
#         label='User Agency/Allottee',
#         widget=forms.TextInput(
#             attrs={
#             'id': 'simpleinput',
#             'placeholder': 'Some text value...',
#             }
#         )
#     )

#     # encroachment = forms.CharField(
#     #     required = True,
#     #     label='User Agency/Allottee',
#     #     widget=forms.TextInput(
#     #         attrs={
#     #         'id': 'simpleinput',
#     #         'placeholder': 'Some text value...',
#     #         }
#     #     )
#     # )
    
#     comment = forms.CharField(
#         required = True,
#         label='Comments/Notes',
#         widget=forms.Textarea(
#             attrs={
#             'id': 'example-textarea',
#             'placeholder': '',
#             'rows': 5
#             }
#         )
#     )
    
    

#     def __init__(self, *args, **kwargs):
#         super(AssetLandForm, self).__init__(*args, **kwargs)
#         ## add a "form-control" class to each form input
#         ## for enabling bootstrap
#         for name in self.fields.keys():
#             self.fields[name].widget.attrs.update({
#                 'class': 'form-control',
#             })
#     class Meta:
#         model = AssetLand
#         fields = [
#             'location', 
#             'nature_of_acquisition',
#             'date_of_acquisition', 
#             'town_or_district',
#             'purpose_of_acquisition',
#             'current_use',
#             'user_agency',
#             'encroachment',
#             'comment'
#         ]





# class AssetVehicleForm(forms.ModelForm): 
    
#     vehicle_type = forms.ModelChoiceField(
#         queryset=VehicleType.objects.all(), empty_label='Select Option',
#         label= 'Type of Vehicle',
#         required=True,
#     )

#     chassis_no =  forms.CharField(
#         required = True,
#         label='Chassis No',
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Chassis No',
#                 'id': 'simpleinput'
#             }
#         )
#     )

#     supplier_invoice_no =  forms.CharField(
#         required = True,
#         label='Supplier’s Invoice No.',
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Supplier’s Invoice No.'
#             }
#         )
#     )

#     vehicle_cost = forms.FloatField(
#         required = True,
#         label='Original Vehicle Cost',
#         widget=forms.NumberInput(
#             attrs={
#                 'placeholder': 'Original Vehicle Cost',
#             }
#         )
#     )

#     cheque_no =  forms.CharField(
#         required = True,
#         label='Cheque No. Of Payment',
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Cheque No. Of Payment',
#             }
#         )
#     )

#     period_of_insurance = forms.DateField(
#         input_formats=['%Y-%m-%d'],
#         required = True,
#         label='Period Of Insurance',
#         widget=forms.DateTimeInput(attrs={
#             'id': 'example-date',
#             'placeholder': 'Period Of Insurance',
#             'type': 'date'
#         })
#     )
    
#     estimated_used =  forms.CharField(
#         required = True,
#         label='Estimated Useful Life',
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Estimated Useful Life'
#             }
#         )
#     )
    
    
#     vehicle_state = forms.ChoiceField(
#         choices=STATE_OF_VEHICLE,
#         required=True,
#         label='state / condition of vehicle',
#     )

#     user_designation = forms.CharField(
#         required = True,
#         label='User Name & Designation',
#         widget=forms.Textarea(
#             attrs={
#             'id': 'example-textarea',
#             'placeholder': '',
#             'rows': 5
#             }
#         )
#     )

    
#     comment = forms.CharField(
#         required = True,
#         label='Comments/Notes',
#         widget=forms.Textarea(
#             attrs={
#             'id': 'example-textarea',
#             'placeholder': '',
#             'rows': 5
#             }
#         )
#     )
    
    

#     def __init__(self, *args, **kwargs):
#         super(AssetVehicleForm, self).__init__(*args, **kwargs)
#         ## add a "form-control" class to each form input
#         ## for enabling bootstrap
#         for name in self.fields.keys():
#             self.fields[name].widget.attrs.update({
#                 'class': 'form-control',
#             })
#     class Meta:
#         model = AssetVehicle
#         fields = [
#             'vehicle_type',
#             'chassis_no',
#             'supplier_invoice_no', 
#             'vehicle_cost',
#             'cheque_no',
#             'period_of_insurance',
#             'estimated_used',
#             'vehicle_state',
#             'user_designation',
#             'comment',
#         ]




# class AssetEquipmentForm(forms.ModelForm): 
    
    
#     equipment_type = forms.ChoiceField(
#         choices=TYPE_OF_EQUIPMENT,
#         required=True,
#         label='Type of Equipment',
#     )

#     location =  forms.CharField(
#         required = True,
#         label='Location',
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Location',
#                 'id': 'simpleinput'
#             }
#         )
#     )

#     model =  forms.CharField(
#         required = True,
#         label='Model',
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Model'
#             }
#         )
#     )


#     serial_no =  forms.CharField(
#         required = True,
#         label='Serial Number',
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Serial Number',
#             }
#         )
#     )
    
    
#     equipment_state = forms.ChoiceField(
#         choices=STATE_OF_VEHICLE,
#         required=True,
#         label='State/Condition',
#     )

#     user_designation = forms.CharField(
#         required = True,
#         label='User Name & Designation',
#         widget=forms.Textarea(
#             attrs={
#             'id': 'example-textarea',
#             'placeholder': '',
#             'rows': 5
#             }
#         )
#     )

    
#     comment = forms.CharField(
#         required = True,
#         label='Comments/Notes',
#         widget=forms.Textarea(
#             attrs={
#             'id': 'example-textarea',
#             'placeholder': '',
#             'rows': 5
#             }
#         )
#     )
    
    

#     def __init__(self, *args, **kwargs):
#         super(AssetEquipmentForm, self).__init__(*args, **kwargs)
#         ## add a "form-control" class to each form input
#         ## for enabling bootstrap
#         for name in self.fields.keys():
#             self.fields[name].widget.attrs.update({
#                 'class': 'form-control',
#             })
#     class Meta:
#         model = AssetEquipment
#         fields = [
#             'equipment_type',
#             'location',
#             'model', 
#             'serial_no',
#             'equipment_state',
#             'user_designation',
#             'comment',
#         ]
        

# class AssetResidentialForm(forms.ModelForm): 
    
    
#     equipment_type = forms.ChoiceField(
#         choices=TYPE_OF_EQUIPMENT,
#         required=True,
#         label='Type of Equipment',
#     )

#     location =  forms.CharField(
#         required = True,
#         label='Location',
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Location',
#                 'id': 'simpleinput'
#             }
#         )
#     )

#     model =  forms.CharField(
#         required = True,
#         label='Model',
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Model'
#             }
#         )
#     )


#     serial_no =  forms.CharField(
#         required = True,
#         label='Serial Number',
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Serial Number',
#             }
#         )
#     )
    
    
#     equipment_state = forms.ChoiceField(
#         choices=STATE_OF_VEHICLE,
#         required=True,
#         label='State/Condition',
#     )

#     user_designation = forms.CharField(
#         required = True,
#         label='User Name & Designation',
#         widget=forms.Textarea(
#             attrs={
#             'id': 'example-textarea',
#             'placeholder': '',
#             'rows': 5
#             }
#         )
#     )

    
#     comment = forms.CharField(
#         required = True,
#         label='Comments/Notes',
#         widget=forms.Textarea(
#             attrs={
#             'id': 'example-textarea',
#             'placeholder': '',
#             'rows': 5
#             }
#         )
#     )
    
    

#     def __init__(self, *args, **kwargs):
#         super(AssetResidentialForm, self).__init__(*args, **kwargs)
#         ## add a "form-control" class to each form input
#         ## for enabling bootstrap
#         for name in self.fields.keys():
#             self.fields[name].widget.attrs.update({
#                 'class': 'form-control',
#             })
#     class Meta:
#         model = AssetResidential
#         fields = [
#             'equipment_type',
#             'location',
#             'model', 
#             'serial_no',
#             'equipment_state',
#             'user_designation',
#             'comment',
#         ]
        