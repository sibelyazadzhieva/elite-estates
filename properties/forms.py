from django import forms
from .models import Property, Feature

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        exclude = ['agent', 'created_at', 'likes']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'property_type': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'features': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Swimming Pool'}),
        }

class PropertySearchForm(forms.Form):
    query = forms.CharField(
        required=False,
        label='Search',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search location...'})
    )
    min_price = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    max_price = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('min_price') and cleaned_data.get('max_price'):
            if cleaned_data['min_price'] > cleaned_data['max_price']:
                raise forms.ValidationError("Min price cannot be above max price.")
        return cleaned_data