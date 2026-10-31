from django.db import models


class Location(models.Model):
    CATEGORY_CHOICES = [
        ("Landmark", "Landmark"),
        ("Park", "Park"),
        ("Historic site", "Historic site"),
        ("Religious site", "Religious site"),
        ("Museum", "Museum"),
        ("Cafe", "Cafe"),
        ("Other", "Other"),
    ]

    name = models.CharField(max_length=200)
    category = models.CharField(
        max_length=50, choices=CATEGORY_CHOICES, default="Landmark"
    )
    description = models.TextField(blank=True)
    lat = models.FloatField()
    lng = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def to_dict(self):
        """Shape used by the map JS (same keys as the old LOCATIONS list)."""
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "lat": self.lat,
            "lng": self.lng,
        }