from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class TravelLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    geolocation = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='travel_images/', blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    heritage_sites = models.TextField(blank=True)
    places_to_visit = models.TextField(blank=True)
    convenience_rating = models.IntegerField()
    safety_rating = models.IntegerField()
    population_density_rating = models.IntegerField()
    vegetation_rating = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

