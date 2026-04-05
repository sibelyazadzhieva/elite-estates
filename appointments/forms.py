from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    agency_info = forms.CharField(
        initial="EliteEstates",
        disabled=True,
        required=False,
        label="Agency"
    )

    class Meta:
        model = Appointment
        fields = ['agency_info', 'date_and_time', 'notes']
        widgets = {
            'date_and_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Any specific questions or requests?'}),
        }