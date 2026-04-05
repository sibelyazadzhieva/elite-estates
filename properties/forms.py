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