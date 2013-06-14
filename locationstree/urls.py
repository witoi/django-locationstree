from django.conf.urls import url, patterns


urlpatterns = patterns('locationstree.views',
    url('$^', 'set_user_location', name='set_user_location')
)
