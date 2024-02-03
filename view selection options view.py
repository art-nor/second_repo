from django.shortcuts import render, redirect
from .models import Clinic
from .forms import ClinicSelectionForm

def clinic_selection(request):
     if request.method == 'POST':
        form = ClinicSelectionForm(request.POST)
        if form.is_valid():
            clinic_instance = form.cleaned_data['clinic']
            clinic_id = clinic_instance.pk
            return redirect('clinic_options', clinic_id = clinic_id)
     else:
         form = ClinicSelectionForm()

     clinics = Clinic.objects.all()

     return render(request, 'clinic_selection.html', {'form': form ,'clinics': clinics})


from django.shortcuts import render, redirect
from .models import Clinic, Queueing

# @login_required
def clinic_options(request, clinic_id):
    clinic = Clinic.objects.get(pk=clinic_id)

    return render(request, 'clinic_options.html', {'clinic': clinic})

from django.shortcuts import render
from .models import Clinic, Queueing

# @login_required
def view_current_appointments(request, clinic_id):
    clinic = Clinic.objects.get(pk=clinic_id)
    appointments = Queueing.objects.filter(clinic=clinic, status='confirmed')
   
    return render(request, 'view_current_appointments.html', {'clinic': clinic, 'appointments': appointments})
