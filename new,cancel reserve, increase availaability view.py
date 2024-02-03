from .forms import ReservationForm

#@login_required
def new_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.status = 'pending'  # You can set the initial status as needed
            reservation.appointment_cost = 0  # You can set the initial cost as needed
            reservation.save()
            return redirect('current_appointments')  # Redirect to current appointments after successful reservation
    else:
        form = ReservationForm()

    return render(request, 'newreservation.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CancelReservationForm, IncreaseAvailabilityForm

# @login_required
def cancel_reservations(request, clinic_id):
    clinic = Clinic.objects.get(pk=clinic_id)

    if request.method == 'POST':
        form = CancelReservationForm(request.POST)
        if form.is_valid():
            reservation_id = form.cleaned_data['reservation_id']

            try:
                reservation = Queueing.objects.get(pk=reservation_id, status='confirmed', clinic=clinic)
                # Optionally, you may want to add further checks before canceling, e.g., datetime validation

                reservation.status = 'canceled'
                reservation.save()

                messages.success(request, 'Reservation canceled successfully.')
            except Queueing.DoesNotExist:
                messages.error(request, 'Invalid reservation ID or reservation cannot be canceled.')

            return redirect('clinic_options', clinic_id=clinic_id)
    else:
        form = CancelReservationForm()

    return render(request, 'cancel_reservations.html', {'clinic': clinic, 'form': form})

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CancelReservationForm, IncreaseAvailabilityForm

# @login_required
def increase_availability(request, clinic_id):
    clinic = Clinic.objects.get(pk=clinic_id)

    if request.method == 'POST':
        form = IncreaseAvailabilityForm(request.POST)
        if form.is_valid():
            additional_availability = form.cleaned_data['additional_availability']

            try:
                # Retrieve the clinic and update its availability
                clinic = Clinic.objects.get(pk=clinic_id)
                clinic.availability += additional_availability
                clinic.save()

                messages.success(request, 'Availability increased successfully.')
            except Clinic.DoesNotExist:
                messages.error(request, 'Invalid clinic ID.')

            return redirect('clinic_options', clinic_id=clinic_id)
    else:
        form = IncreaseAvailabilityForm()

    return render(request, 'increase_availability.html', {'clinic': clinic, 'form': form})