from django.core.cache import cache

from .models import Location
from .conf import settings


def locations(request):
    locations = cache.get('locationstree.locations')
    if locations is None:
        locations = Location.objects.all()
        cache.set('locationstree.locations', locations, settings.LOCATIONSTREE_CACHE_TTL)
    return {
        settings.LOCATIONSTREE_CONTEXT_VARIABLE_NAME: locations
    }


def session_location(request):
    location_id = request.session.get(settings.LOCATIONSTREE_LOCATION_SESSION_NAME,
                                      settings.LOCATIONSTREE_LOCATION_DEFAULT_ID)
    try:
        location = Location.objects.get(id=location_id)
    except Location.DoesNotExist:
        return {}
    return {'session_location': location}
