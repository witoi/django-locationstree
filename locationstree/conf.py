from django.conf import settings as django_settings


class Settings(object):
    @property
    def LOCATIONS_CONTEXT_VARIABLE_NAME(self):
        return getattr(django_settings, 'LOCATIONS_CONTEXT_VARIABLE_NAME', 'locations')

    @property
    def LOCATIONS_CACHE_TTL(self):
        return getattr(django_settings, 'LOCATIONS_CACHE_TTL', 60*60*24*7)

settings = Settings()
