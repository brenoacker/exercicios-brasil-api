from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from exercicios.views import Exercicio1ViewSet, Exercicio2ViewSet, Exercicio3ViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Exercícios Brasil API",
      default_version='v1',
      description="Realização de exercícios propostos com relação ao consumo de uma API do site Brasil API",
      terms_of_service="#",
      contact=openapi.Contact(email="brenoacker@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('exercicio1', Exercicio1ViewSet, basename='Exercicio 1')
router.register('exercicio2', Exercicio2ViewSet, basename='Exercicio 2')
router.register('exercicio3', Exercicio3ViewSet, basename='Exercicio 3')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
    path('doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    #path('doc2/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
