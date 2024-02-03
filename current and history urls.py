from django.urls import path
from .views import *

urlpatterns = [   
    path('current_appointments/', current_appointments, name='current_appointments'),
    path('appointment_history/', appointment_history, name='appointment_history')]