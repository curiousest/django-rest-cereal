
from django.conf.urls import include, url
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'as', views.AViewSet,)
router.register(r'bs', views.BViewSet,)
router.register(r'cs', views.CViewSet,)


urlpatterns = [
    url(r'^', include(router.urls)),
]
