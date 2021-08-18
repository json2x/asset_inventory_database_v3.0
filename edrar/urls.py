from django.urls import path, include
from django.conf.urls import url
from . import views

from django.contrib.auth.decorators import login_required

from edrar.views import siteid_autocomplete, DeviceDatatableView

urlpatterns = [
    path('edrar/', views.home, name='edrar_home'),
    path('edrar/activity/add', views.activity_add, name='edrar_add'),
    
    path('edrar/smart_site_list', views.SiteList.as_view()),

    path('edrar/data/device/', views.DeviceDatatableView.as_view(), name='device-lookup'),
    path('edrar/data/cell/', views.CellDatatableView.as_view(), name='cell-lookup'),
    url('edrar/data/siteid-autocomplete/', siteid_autocomplete.as_view(), name='siteid-autocomplete'),
]