from django.contrib import admin
from .models import Guest, Room

# Register your models here.
class GuestAdmin(admin.ModelAdmin):
  list_display = ("id", "name", "email", "phone",)
  
admin.site.register(Guest, GuestAdmin)

class RoomAdmin(admin.ModelAdmin):
  list_display = ("id", "roomNumber", "roomType", "price", "status",)
  
admin.site.register(Room, RoomAdmin)

