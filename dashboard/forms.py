from django import forms
from property import models as propsModel
from cars import models as carModel
from core import models as coreModel


class PropertyForm(forms.ModelForm): 

    description = forms.CharField(
        required = True,
        label='Description',
        widget=forms.Textarea(
            attrs={
                'id': 'example-textarea',
                'rows': 5
            }
        )
    )

    owned_by = forms.ModelChoiceField(
        queryset= propsModel.RealEstate.objects.all(), 
        empty_label='Sandvet',
        label= 'Owned By',
        required=False,
        widget=forms.Select(
            attrs={
                'class': 'select2',
                'data-toggle': "select2"
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
            'price_negotiable',
            'region',
            'locality',
            'location_address', 
            'owned_by',
            'image',
            'description',
        ]
        
class PropertyLandForm(forms.ModelForm): 
    dimension =  forms.CharField(
        label='Dimension',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'eg: 700 ft × 100 ft'
            }
        )
    )
    area =  forms.CharField(
        label='Area (already in meter square)',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'eg: 6,503'
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
            'dimension',
            'area',
        ]



class PropertyHouseForm(forms.ModelForm): 
    
    amenities = forms.CharField(
        required = True,
        label='Amenities',
        widget=forms.Textarea(
            attrs={
                'id': 'example-textarea',
                'placeholder': 'eg: Fans, Refrigerator, Microwave',
                'rows': 5
            }
        )
    )
    area =  forms.CharField(
        label='Area (already in meter square)',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'eg: 6,503'
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super(PropertyHouseForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = propsModel.HouseProperty
        fields = [
            'bed',
            'bath',
            'garage',
            'area',
            'amenities',
        ]




class LocalityForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LocalityForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })
    class Meta:
        model = propsModel.Locality
        fields = ['region', 'name']


class CategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })
    class Meta:
        model = propsModel.Category
        fields = ['title',]



class PropertyImagesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PropertyImagesForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    images =  forms.CharField(
        required = False,
        label='Property Images',
        widget=forms.ClearableFileInput(
            attrs={'multiple': True}
        )
    ) 
    class Meta:
        model = propsModel.PropertyImage
        fields = ['images']

class RealEstateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RealEstateForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })
    class Meta:
        model = propsModel.RealEstate
        fields = ['title','region','locality', 'location_address' ,'url', 'logo', 'image', 'description']

class SocialHandleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SocialHandleForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })
    class Meta:
        model = propsModel.SocialHandle
        fields = ['facebook','linkedIn','instagram',]

        

class RealEstateImagesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RealEstateImagesForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    images =  forms.CharField(
        required = False,
        label='Real Estate Images',
        widget=forms.ClearableFileInput(
            attrs={'multiple': True}
        )
    ) 
    class Meta:
        model = propsModel.RealEstateImage
        fields = ['images']




class CarForm(forms.ModelForm): 

    year = forms.TypedChoiceField(coerce=int, choices=carModel.year_choices, initial=carModel.current_year)

    title =  forms.CharField(
        required = True,
        label='Title',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'eg: 2019 toyota corola'
            }
        )
    )

    
    def __init__(self, *args, **kwargs):
        super(CarForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            }) 

            
    class Meta:
        model = carModel.Car
        fields = [
            'title', 
            'price', 
            'region',
            'brand', 
            'car_type',
            'fuel_type',
            'gearbox',
            'mileage',
            'int_color',
            'ext_color',
            'year',
            'engine',
            'drive_type',
            'car_state',
            'air_con',
            'purpose',
            'image',
            'description',
        ]

class CarImagesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CarImagesForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    images =  forms.CharField(
        required = False,
        label='Car Images',
        widget=forms.ClearableFileInput(
            attrs={'multiple': True}
        )
    ) 
    class Meta:
        model = carModel.CarImage
        fields = ['images']
        
class BrandForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BrandForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })
    class Meta:
        model = carModel.Brand
        fields = ['name', 'image']


class TypeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TypeForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })
    class Meta:
        model = carModel.Type
        fields = ['name',]


class SparePartForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SparePartForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })
    class Meta:
        model = carModel.SparePart
        fields = ['title', 'price', 'region', 'locality', 'condition', 'description','image']



class SparePartImagesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SparePartImagesForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    images =  forms.CharField(
        required = False,
        label='Car Images',
        widget=forms.ClearableFileInput(
            attrs={'multiple': True}
        )
    ) 
    class Meta:
        model = carModel.SparePartImage
        fields = ['images']


class SchoolForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SchoolForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })
    class Meta:
        model = carModel.School
        fields = ['title', 'region', 'locality', 'location', 'description','image']



class SchoolImagesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SchoolImagesForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    images =  forms.CharField(
        required = False,
        label='Car Images',
        widget=forms.ClearableFileInput(
            attrs={'multiple': True}
        )
    ) 
    class Meta:
        model = carModel.SchoolImage
        fields = ['images']
            
class HotelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(HotelForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })
    class Meta:
        model = propsModel.Hotel
        fields = ['title', 'location_address', 'region', 'locality', 'logo', 'image','rate','free_parking', 'free_wiFi', 'pool', 'fitness_center', 'free_breakfast', 'free_airport_transportation', 'conference_facilities', 'bar_or_lounge', 'description']


class HotelImagesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(HotelImagesForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    images =  forms.CharField(
        required = False,
        label='Hotel Images',
        widget=forms.ClearableFileInput(
            attrs={'multiple': True}
        )
    ) 
    class Meta:
        model = propsModel.HotelImage
        fields = ['images']
            


class HotelRoomForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(HotelRoomForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })
    class Meta:
        model = propsModel.HotelRoom
        fields = ['title','price', 'hotel', 'image','housekeeping','refrigerator', 'flatscreen_tv', 'kitchenette', 'room_service', 'air_conditioning', 'description']


class HotelRoomImagesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(HotelRoomImagesForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    images =  forms.CharField(
        required = False,
        label='Hotel Room Images',
        widget=forms.ClearableFileInput(
            attrs={'multiple': True}
        )
    ) 
    class Meta:
        model = propsModel.HotelRoomImage
        fields = ['images']