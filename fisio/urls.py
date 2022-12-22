from django.contrib import admin
from django.urls import path, include
from aqzfisio.views import AplicativoViewSet, EspecialidadeViewSet, ClienteViewSet, AgendaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('aplicativo', AplicativoViewSet, basename='aplicativo')
router.register('especialidade', EspecialidadeViewSet, basename='especialidade')
router.register('cliente', ClienteViewSet, basename='cliente')
router.register('agenda', AgendaViewSet, basename='agenda')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
