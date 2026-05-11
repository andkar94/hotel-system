from django.db import models
from django.conf import settings
    
class Guest(models.Model):
  user = models.OneToOneField(
    settings.AUTH_USER_MODEL, 
    on_delete=models.CASCADE,
    related_name='guest_profile',
    null=True,
    blank=True,
  )
  name=models.CharField(max_length=255)
  phone = models.IntegerField(null=True, unique=True)
  email = models.CharField(max_length=255, unique=True)
  
  def __str__(self):
    return f"{self.name}"
 
class Room(models.Model):
  class RoomStatus(models.TextChoices):
        AVAILABLE = 'Available'
        OCCUPIED = 'Occupied'
        RESERVED = 'Reserverd',
        MAINTENANCE = 'Maintenance'
        
  class RoomType(models.TextChoices):
        SINGLE = 'Single'
        DOUBLE = 'Double'
        SUITE = 'Suite'

  roomNumber = models.IntegerField(unique=True)
  roomType = models.CharField(choices=RoomType.choices)
  price = models.IntegerField(null=True)
  status = models.CharField(choices=RoomStatus.choices, default=RoomStatus.AVAILABLE)
  
  def __str__(self):
    return f"{self.roomNumber}"
 
class Reservation(models.Model):
  guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
  room = models.ForeignKey(Room, on_delete=models.CASCADE)
  checkInDate = models.DateField(null=True)
  checkOutDate = models.DateField(null=True)
  totalPrice = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
   
class Payment(models.Model):
  reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
  amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
  paymentDate = models.DateField(null=True)
  paymentMethod = models.CharField(max_length=12)