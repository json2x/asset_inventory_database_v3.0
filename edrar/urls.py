from django.urls import path, include
from django.conf.urls import url
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('edrar/', login_required(views.home), name='edrar_home'),
    #path('edrar/activity/add', login_required(views.activity_add), name='edrar_add'),
    path('edrar/activity/log', login_required(views.AddActivity.as_view()), name='edrar_log'),
    
    #path('edrar/smart_site_list', views.SiteList.as_view()),

    url('edrar/data/select2/activity-autocomplete/', views.ActivityAutocomplete.as_view(), name='activity-autocomplete'),
    url('edrar/data/select2/siteid-autocomplete/', views.SiteIdAutocomplete.as_view(), name='siteid-autocomplete'),
    url('edrar/data/select2/mobiletech-autocomplete/', views.MobileTechAutocomplete.as_view(), name='mobiletech-autocomplete'),
    url('edrar/data/select2/mobilefreqband-autocomplete/', views.MobileFreqBandAutocomplete.as_view(), name='mobilefreqband-autocomplete'),
    
    path('edrar/data/datatable/device/aid/', views.DeviceDatatableView.as_view(), name='aid-device-datatable'),
    path('edrar/data/datatable/cell/aid/', views.CellDatatableView.as_view(), name='aid-cell-datatable'),
    path('edrar/data/datatable/trx/aid/', views.TrxDatatableView.as_view(), name='aid-trx-datatable'),

    path('edrar/data/datatable/device/nms/', views.NmsDeviceDatatableView.as_view(), name='nms-device-datatable'),
    path('edrar/data/datatable/cell/nms/', views.NmsCellDatatableView.as_view(), name='nms-cell-datatable'),
    path('edrar/data/datatable/trx/nms/', views.NmsTrxDatatableView.as_view(), name='nms-trx-datatable'),
    
    #path('edrar/data/tfdata/', authentication_classes([])(permission_classes([AllowAny])(views.ActivityLogTextFieldData)).as_view(), name='tfdata-lookup'),
    path('edrar/data/ne/', authentication_classes([])(permission_classes([AllowAny])(views.GetNEData)).as_view(), name='ne-lookup'),
    #path('edrar/data/tfdata/nms/', authentication_classes([])(permission_classes([AllowAny])(views.ActivityLogTextFieldData)).as_view(), name='tfdata-lookup'),

    # url('edrar/data/device/', authentication_classes([])(permission_classes([AllowAny])(views.GetDeviceDataByID)).as_view(), name='device-lookup'),
    # url('edrar/data/cell/', authentication_classes([])(permission_classes([AllowAny])(views.GetCellDataByID)).as_view(), name='cell-lookup'),
    # url('edrar/data/trx/', authentication_classes([])(permission_classes([AllowAny])(views.GetTrxDataByID)).as_view(), name='trx-lookup'),
]