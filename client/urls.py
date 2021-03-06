from django import urls
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers, serializers, viewsets

from api.views import ClientViewSet

router = routers.DefaultRouter()
router.register('cliente', ClientViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]
