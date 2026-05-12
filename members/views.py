from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Room, Reservation
from datetime import date

today = date.today()

@login_required
def dashboard(request):
    context = {
      'total_reserv': Room.objects.filter(status='Reserved').count(),
      'free_rooms': Room.objects.filter(status='Available').count(),
      'arrivals': Reservation.objects.filter(checkInDate=today).count(),
      'departures': Reservation.objects.filter(checkOutDate=today).count(),
      'reservations': Reservation.objects.all().values(),
    }
    return render(request, 'dashboard.html', context)

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
