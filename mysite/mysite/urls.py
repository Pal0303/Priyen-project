
from django.contrib import admin
from django.conf.urls import include,url


urlpatterns = [
    url(r'^', include('jobs.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^jobs/', include('jobs.urls')),
    url(r'^register/', include('register.urls')),
]
