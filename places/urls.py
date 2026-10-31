from django.urls import path
from . import views

app_name = "places"

urlpatterns = [
    path("", views.map_page, name="map"),
    path("add/", views.add_location, name="add_location"),
]