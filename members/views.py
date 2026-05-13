from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Room, Reservation, Guest
from datetime import date, datetime

today = date.today()

@login_required
def dashboard(request):
    context = {
      'total_reserv': Room.objects.filter(status='Reserved').count(),
      'free_rooms': Room.objects.filter(status='Available').count(),
      'arrivals': Reservation.objects.filter(checkInDate=today).count(),
      'departures': Reservation.objects.filter(checkOutDate=today).count(),
      'reservations': Reservation.objects.select_related('guest', 'room').all()
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
    context = {
      'rooms': Room.objects.filter(status='Available').all().values(),
      'guests': Guest.objects.all().values(),
    }
    return render(request, 'reservation_form.html', context)  
    
@login_required
def check_av(request):   
    return render(request, 'check_av.html')  

@login_required
def addReservation(request):
    if request.method == 'POST':
      guest_id = request.POST.get('guest_id')
      room_id = request.POST.get('room_id')
      start_date_str = request.POST.get('startDate')
      end_date_str = request.POST.get('endDate')
      
      start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
      end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
      duration = end_date - start_date
      
      selected_room = Room.objects.get(id=room_id)
      selected_room.status = 'Occupied'
      selected_room.save()
      
      selected_guest = Guest.objects.get(id=guest_id)
      total_price = selected_room.price * duration.days
      
      new_res = Reservation.objects.create(
            guest = selected_guest,
            room = selected_room,
            checkInDate = start_date,
            checkOutDate = end_date,
            totalPrice = total_price,
        )
       
    context = {
      'payment': total_price,
      'room': selected_room,
      'guest': selected_guest,
      'start': start_date,
      'end': end_date,
    }
       
    return render(request, 'success.html', context)
     