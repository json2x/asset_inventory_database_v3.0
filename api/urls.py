
from django.urls import path, include
from django.conf.urls import url
from . import views
from rest_framework import routers
from django.contrib.auth.decorators import login_required

router = routers.DefaultRouter()
router.register('Cells', views.CellsView)
router.register('Devices', views.DevicesView)
router.register('SmartSite', views.SmartSiteView)
router.register('SmartNe', views.SmartNeView)
router.register('SiteNeAsset', views.SiteNeAssetView)
router.register('TocAor', views.TocAorView)
router.register('Location', views.LocationView)

urlpatterns = [
    path('', views.index),
    path('home/', views.home, name='home'),
    
    #path('datatable/', login_required(views.datatableHome), name='datatable'),
    path('datatable/device/', login_required(views.datatable_device), name='datatable_device'),
    path('datatable/cell/', login_required(views.datatable_cell), name='datatable_cell'),
    path('datatable/smartsite/', login_required(views.datatable_smartsite), name='datatable_smartsite'),
    path('datatable/smartne/', login_required(views.datatable_smartne), name='datatable_smartne'),
    path('datatable/location/', login_required(views.datatable_location), name='datatable_location'),
    path('datatable/tocaor/', login_required(views.datatable_tocaor), name='datatable_tocaor'),
    url(r'^datatable/data/device/$', login_required(views.datatableview_device.as_view()), name='datatable-data-device'),
    url(r'^datatable/data/cell/$', login_required(views.datatableview_cell.as_view()), name='datatable-data-cell'),
    url(r'^datatable/data/smartsite/$', login_required(views.datatableview_smartsite.as_view()), name='datatable-data-smartsite'),
    url(r'^datatable/data/smartne/$', login_required(views.datatableview_smartne.as_view()), name='datatable-data-smartne'),
    url(r'^datatable/data/location/$', login_required(views.datatableview_location.as_view()), name='datatable-data-location'),
    url(r'^datatable/data/tocaor/$', login_required(views.datatableview_tocaor.as_view()), name='datatable-data-tocaor'),

    path('datatable/doc/jwttoken/', login_required(views.docs_jwttoken), name='docs_jwttoken'),
    path('datatable/doc/device/', login_required(views.docs_device), name='docs_device'),
    path('datatable/doc/cell/', login_required(views.docs_cell), name='docs_cell'),
    path('datatable/doc/smartsite/', login_required(views.docs_smartsite), name='docs_smartsite'),
    path('datatable/doc/smartne/', login_required(views.docs_smartne), name='docs_smartne'),
    path('datatable/doc/location/', login_required(views.docs_location), name='docs_location'),
    path('datatable/doc/tocaor/', login_required(views.docs_tocaor), name='docs_tocaor'),

    #path('datatable/data/', login_required(views.datatable.as_view()), name='datatable-data'),
    path('api/docs/', views.api_docs, name='apiDocs'),

    path('api/', include(router.urls)),
]
