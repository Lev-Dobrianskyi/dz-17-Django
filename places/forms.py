from django import forms
from .models import Location


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ["name", "category", "description", "lat", "lng"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "e.g. City Hall"}),
            "description": forms.Textarea(
                attrs={"rows": 3, "placeholder": "Short description"}
            ),
            "lat": forms.NumberInput(
                attrs={"step": "any", "placeholder": "48.9226"}
            ),
            "lng": forms.NumberInput(
                attrs={"step": "any", "placeholder": "24.7111"}
            ),
        }