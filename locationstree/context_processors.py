from django.core.cache import cache

from .models import Location
from .conf import settings


def locations(request):
    locations = cache.get('locations.locations')
    if locations is None:
        locations = Location.objects.all()
        cache.set('locations.locations', locations, settings.LOCATIONS_CACHE_TTL)
    return {
        settings.LOCATIONS_CONTEXT_VARIABLE_NAME: locations
    }
