from django.urls import path, include
from django.conf.urls import url
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cell', views.NmsCellsView)
router.register('device', views.NmsDevicesView)
router.register('trx', views.NmsTrxView)

urlpatterns = [
    path('nmsdata/', include(router.urls)),
]