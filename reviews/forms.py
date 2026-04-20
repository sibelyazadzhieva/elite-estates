from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Write your review here...'}),
        }

class ReviewSearchForm(forms.Form):
    query = forms.CharField(
        required=False,
        label='Search in reviews',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by keyword...'})
    )
    min_rating = forms.IntegerField(
        required=False,
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Min rating (1-5)'})
    )