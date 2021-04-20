from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Hotels(models.Model):
  STATE_CHOICES = (
    ('Telangana', 'Telangana'),
    ('AP', 'AP'),
    ('UP', 'UP'),
    ('MP', 'MP'),
    ('Kerala', 'Kerala'),
  )
  hotel_name = models.CharField(max_length=100)
  hotel_image = models.ImageField(upload_to='hotel-images')
  hotel_description = models.TextField()
  available_states = models.CharField(max_length=100, choices=STATE_CHOICES)
  total_rooms = models.PositiveIntegerField()
  rooms_available = models.PositiveIntegerField()
  hotel_rating = models.DecimalField(max_digits=10, decimal_places=2)
  starting_price = models.DecimalField(max_digits=10, decimal_places=2)
  
  
class UserBookedHotels(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  hotel_names = models.ManyToManyField(Hotels)
  

      
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  