# backend/urls.py

from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("api.urls")),
    path('vets/', include('vets.urls')) # http://127.0.0.1:8000/vets/api/v1/vets/
]

urlpatterns += staticfiles_urlpatterns()