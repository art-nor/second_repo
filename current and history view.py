from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Queueing

#@login_required
def current_appointments(request):
    user = request.user
    appointments = Queueing.objects.filter(user=user, status='confirmed')  # Adjust the filter condition as needed
    return render(request, 'current_appointments.html', {'appointments': appointments})

#@login_required
def appointment_history(request):
    user = request.user
    appointments_history = Queueing.objects.filter(user=user, status=['completed','canceled'])  
    return render(request, 'appointment_history.html', {'appointments_history': appointments_history})