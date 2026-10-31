from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Location
from .forms import LocationForm


def map_page(request):
    locations = [loc.to_dict() for loc in Location.objects.all()]
    return render(
        request,
        "places/index.html",
        {"locations": locations, "form": LocationForm()},
    )


def add_location(request):
    """AJAX endpoint used by the 'Add place' dialog."""
    if request.method != "POST":
        return redirect("places:map")

    form = LocationForm(request.POST)
    if form.is_valid():
        loc = form.save()
        return JsonResponse({"ok": True, "location": loc.to_dict()})

    return JsonResponse({"ok": False, "errors": form.errors}, status=400)