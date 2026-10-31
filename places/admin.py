from django.contrib import admin
from .models import Location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "lat", "lng", "created_at")
    list_filter = ("category",)
    search_fields = ("name", "description")