from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Room

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def rooms(request):
    rooms = Room.objects.all().values()
    context = {
      'rooms': rooms,
    }
    return render(request, 'all_rooms.html', context)  
    
@login_required
def report(request):
    return render(request, 'report.html')  

@login_required
def reservation(request):   
    return render(request, 'reservation_form.html')  
    
@login_required
def check_av(request):   
    return render(request, 'check_av.html')  
