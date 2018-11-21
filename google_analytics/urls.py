from django.conf.urls import url
from google_analytics.views import google_analytics


urlpatterns = [
    url(r'^google-analytics/(?P<uid>\d+)/$', google_analytics, name='google-analytics'),
    url(r'^google-analytics/$', google_analytics, name='google-analytics'),
]
