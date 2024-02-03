from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Queueing

#@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
