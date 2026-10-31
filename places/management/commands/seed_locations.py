from django.core.management.base import BaseCommand
from places.models import Location

DATA = [
    {
        "name": "Ivano-Frankivsk City Hall",
        "category": "Landmark",
        "description": "A historic city hall in the heart of the city, now home to the Museum of History.",
        "lat": 48.9226, "lng": 24.7111,
    },
    {
        "name": "Shevchenko Park",
        "category": "Park",
        "description": "A popular green space with walking paths, a lake, and recreational areas.",
        "lat": 48.9155, "lng": 24.7047,
    },
    {
        "name": "Potocki Palace",
        "category": "Historic site",
        "description": "The remains of a 17th-century palace complex associated with the city's founders.",
        "lat": 48.9228, "lng": 24.7068,
    },
    {
        "name": "Cathedral of the Holy Resurrection",
        "category": "Religious site",
        "description": "A landmark Greek Catholic cathedral located near the central square.",
        "lat": 48.9227, "lng": 24.7092,
    },
    {
        "name": "Bastion",
        "category": "Historic site",
        "description": "A restored section of the city's old defensive fortifications with shops and galleries.",
        "lat": 48.9205, "lng": 24.7103,
    },
]


class Command(BaseCommand):
    help = "Seed the initial set of Ivano-Frankivsk locations"

    def handle(self, *args, **options):
        created = 0
        for item in DATA:
            _, was_created = Location.objects.get_or_create(
                name=item["name"], defaults=item
            )
            created += was_created
        self.stdout.write(
            self.style.SUCCESS(f"Seeded {created} new location(s).")
        )