from django import forms
from .models import TravelLog

class TravelLogForm(forms.ModelForm):
    class Meta:
        model = TravelLog
        fields = [
            'title', 'description', 'location', 'geolocation', 'image', 'cost',
            'heritage_sites', 'places_to_visit', 'convenience_rating',
            'safety_rating', 'population_density_rating', 'vegetation_rating'
        ]
