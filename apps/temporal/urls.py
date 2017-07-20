from django.conf.urls import patterns, include, url
from .views import Temporal


urlpatterns = patterns('',

                       url(r'^temporal/(?P<datos>.*)$', Temporal.as_view(), name='temporal'),
                       )


