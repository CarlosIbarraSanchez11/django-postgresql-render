# from django.urls import path, include
# from rest_framework.documentation import include_docs_urls
# from rest_framework import routers
# from vets import views

# # api versioning
# router = routers.DefaultRouter()
# router.register(r'vets', views.VetView, 'vets') ## Pasar 3 parametros

# urlpatterns = [
#     path("api/v1/", include(router.urls)), ## Generan GET, POST, DELETE and PUT
#     # path("docs/", include_docs_urls(title = "Vets API"))
# ]
# vets/urls.py

# from django.urls import path
# from . import views
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from vets import views

# api versioning
router = routers.DefaultRouter()
router.register(r'vets', views.VetView, 'vets') ## Pasar 3 parametros


urlpatterns = [
    path('api/v1/vets-by-user/<int:user_id>/', views.VetListByUserView.as_view(), name='vet-list-by-user'),
    # Puedes añadir otras URLs aquí si es necesario
    path("api/v1/", include(router.urls)), ## Generan GET, POST, DELETE and PUT
]