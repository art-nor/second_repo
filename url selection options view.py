from django.urls import path
from .views import *

urlpatterns = [
    path('clinic_selection/', clinic_selection, name='clinic_selection'),
    path('clinic_options/<int:clinic_id>/', clinic_options, name='clinic_options'),
    path('view_current_appointments/<int:clinic_id>/', view_current_appointments, name='view_current_appointments')
]

