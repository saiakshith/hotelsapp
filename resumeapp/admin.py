from django.contrib import admin
from .models import Hotels, UserBookedHotels

# Register your models here.

@admin.register(Hotels)
class HotelAdmin(admin.ModelAdmin):
  list_display = ['id', 'hotel_name', 'hotel_image', 'hotel_description', 'rooms_available', 'total_rooms', 'available_states', 'hotel_rating', 'starting_price']

@admin.register(UserBookedHotels)
class UserBookedHotelsAdmin(admin.ModelAdmin):
  list_display = ['id', 'user']
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  