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
