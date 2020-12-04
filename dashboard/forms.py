from django import forms
from property import models as propsModel



class PropertyForm(forms.ModelForm): 

    title =  forms.CharField(
        required = True,
        label='Title',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'eg: 4plots of land at east legon'
            }
        )
    )

    
    def __init__(self, *args, **kwargs):
        super(PropertyForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            # if not self.files[name].widget.RadioSelect:
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            }) 

            
    class Meta:
        model = propsModel.Property
        fields = [
            'title', 
            'category', 
            'purpose',
            'price', 
            'image',
            'description',
        ]
        
class PropertyLandForm(forms.ModelForm): 
    dimension =  forms.CharField(
        label='Dimension',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'eg: 2500 ft2'
            }
        )
    )
    location =  forms.CharField(
        label='Location',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'eg: Tema Comm. 25'
            }
        )
    )
    def __init__(self, *args, **kwargs):
        super(PropertyLandForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = propsModel.LandProperty
        fields = [
            'region', 
            'locality',
            'location', 
            'dimension',
        ]





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
        