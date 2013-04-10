from django.conf import settings as django_settings


class Settings(object):
    @property
    def LOCATIONSTREE_CONTEXT_VARIABLE_NAME(self):
        return getattr(django_settings, 'LOCATIONSTREE_CONTEXT_VARIABLE_NAME', 'locations')

    @property
    def LOCATIONSTREE_CACHE_TTL(self):
        return getattr(django_settings, 'LOCATIONSTREE_CACHE_TTL', 60*60*24*7)

settings = Settings()
