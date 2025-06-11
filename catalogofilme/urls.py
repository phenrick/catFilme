from django.urls import include, path
from rest_framework.routers import DefaultRouter
from catalogofilme.views import FilmeViewSet

router = DefaultRouter()

router.register(r'filmes', FilmeViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
