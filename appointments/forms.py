from django import forms
from .models import Appointment
from django.utils import timezone
from django.core.exceptions import ValidationError

class AppointmentForm(forms.ModelForm):
    agency_info = forms.CharField(
        initial="EliteEstates",
        disabled=True,
        required=False,
        label="Agency" )

    def clean_date_and_time(self):
        date = self.cleaned_data.get('date_and_time')

        if date and date < timezone.now():
            raise ValidationError("You cannot book an appointment in the past. Please select a valid future date.")

        return date


    class Meta:
        model = Appointment
        fields = ['agency_info', 'date_and_time', 'notes']
        widgets = {
            'date_and_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Any specific questions or requests?'}),
        }