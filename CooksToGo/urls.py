from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^api/', include('app.urls', namespace='api')),
    url(r'^', include(admin.site.urls)),
]
