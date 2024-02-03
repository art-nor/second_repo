from .models import Queueing
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Queueing
        fields = ['clinic', 'datetime']  # Add other fields as needed
        widgets = {
            'datetime': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)


class CancelReservationForm(forms.Form):
    reservation_id = forms.ModelChoiceField(queryset=Queueing.objects.filter(status='confirmed'), empty_label=None, label='Select Reservation to Cancel')


class IncreaseAvailabilityForm(forms.Form):
    additional_availability = forms.IntegerField(min_value=1, label='Enter Additional Availability')

from django import forms
from .models import Clinic

class ClinicSelectionForm(forms.Form):
    clinic = forms.ModelChoiceField(queryset=Clinic.objects.all(), empty_label='Select a Clinic')