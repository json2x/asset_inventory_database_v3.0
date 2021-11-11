from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.db.models import Q
from django.utils.html import escape

from .models import Cell, Device, Trx, Location, SiteNeAsset, SmartNe, SmartSite, TocAor
from .serializers import CellsSerializer, DevicesSerializer, SmartSiteSerializer, SmartNeSerializer, SiteNeAssetSerializer, \
TocAorSerializer, LocationSerializer, DeviceAndCellsSerializer, SmartSiteAndNEsSerializer, SmartSiteCreateUpdateSerializer

from rest_framework import viewsets
from rest_access_policy import AccessPolicy
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from django_datatables_view.base_datatable_view import BaseDatatableView


#-------------------------------------
def index(request):

    return redirect('home')

#-------------------------------------
def home(request):

    return render(request, 'api/home.html')

#-------------------------------------
def api_docs(request):

    return render(request, 'api/api_docs.html')

#-------------------------------------
def datatableHome(request):

    return render(request, 'api/datatable.html')

#-------------------------------------
def datatable_device(request):

    return render(request, 'api/datatable_device.html')

#-------------------------------------
def datatable_cell(request):

    return render(request, 'api/datatable_cell.html')

#-------------------------------------
def datatable_trx(request):

    return render(request, 'api/datatable_trx.html')

#-------------------------------------
def datatable_smartsite(request):

    return render(request, 'api/datatable_smartsite.html')

#-------------------------------------
def datatable_smartne(request):

    return render(request, 'api/datatable_smartne.html')

#-------------------------------------
def datatable_location(request):

    return render(request, 'api/datatable_location.html')

#-------------------------------------
def datatable_tocaor(request):

    return render(request, 'api/datatable_tocaor.html')

#-------------------------------------
def docs_jwttoken(request):

    return render(request, 'api/docs_jwttoken.html')

#-------------------------------------
def docs_device(request):

    return render(request, 'api/docs_device.html')

#-------------------------------------
def docs_cell(request):

    return render(request, 'api/docs_cell.html')

#-------------------------------------
def docs_smartsite(request):

    return render(request, 'api/docs_smartsite.html')

#-------------------------------------
def docs_smartne(request):

    return render(request, 'api/docs_smartne.html')

#-------------------------------------
def docs_location(request):

    return render(request, 'api/docs_location.html')

#-------------------------------------
def docs_tocaor(request):

    return render(request, 'api/docs_tocaor.html')

#-------------------------------------
class datatableview_device(BaseDatatableView):
    model = Device
    columns = ['id', 'device_id', 'ems_id', 'vendor_id', 'ne_type', 'site_id', 'domain', 'subdomain', 'record_status']
    max_display_length = 500

#-------------------------------------
class datatableview_cell(BaseDatatableView):
    model = Cell
    columns = ['id', 'domain', 'ems_id', 'cell_name', 'site', 'band', 'subdomain', 'ne_type', 'record_status', 'device']
    max_display_length = 500

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(Q(domain__istartswith=search) | Q(ems_id__icontains=search) | Q(cell_name__icontains=search) | Q(site__istartswith=search)
            | Q(band__icontains=search) | Q(subdomain__icontains=search) | Q(ne_type__istartswith=search) | Q(device__device_id__icontains=search))
        return qs

#-------------------------------------
class datatableview_trx(BaseDatatableView):
    model = Trx
    columns = ['id', 'ems_id', 'trx_name', 'site_id', 'parent_id', 'homing_bts', 'record_status']
    max_display_length = 500

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(Q(ems_id__icontains=search) | Q(trx_name__icontains=search) | Q(site_id__istartswith=search)
            | Q(parent_id__icontains=search) | Q(homing_bts__icontains=search) | Q(homing_id__icontains=search))
        return qs

#-------------------------------------
class datatableview_smartsite(BaseDatatableView):
    model = SmartSite
    columns = ['id', 'siteid', 'sitename', 'address', 'city', 'province', 'area', 'aor', 'lat', 'lng', 'record_status']
    max_display_length = 500

    def render_column(self, row, column):
        # We want to render user as a custom column
        if column == 'city':
            # escape HTML for security reasons
            return escape('{}'.format(row.location.city))
        if column == 'province':
            # escape HTML for security reasons
            return escape('{}'.format(row.location.province))
        if column == 'aor':
            # escape HTML for security reasons
            return escape('{}'.format(row.toc_aor.cluster))
        if column == 'area':
            # escape HTML for security reasons
            return escape('{}'.format(row.location.area))
        else:
            return super(datatableview_smartsite, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(Q(siteid__istartswith=search) | Q(sitename__icontains=search) | Q(address__icontains=search) | Q(location__city__istartswith=search) 
            | Q(location__province__istartswith=search) | Q(location__area__istartswith=search) | Q(toc_aor__cluster__icontains=search))
        return qs

#-------------------------------------
class datatableview_smartne(BaseDatatableView):
    model = SmartNe
    columns = ['id', 'siteid', 'sitename', 'band', 'tech', 'aor', 'record_status']
    max_display_length = 500
    
    def render_column(self, row, column):
        # We want to render user as a custom column
        if column == 'sitename':
            # escape HTML for security reasons
            return escape('{}'.format(row.smartsite.sitename))
        if column == 'aor':
            # escape HTML for security reasons
            return escape('{}'.format(row.smartsite.toc_aor.cluster))
        else:
            return super(datatableview_smartne, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(Q(siteid__istartswith=search) | Q(smartsite__sitename__icontains=search) | Q(smartsite__toc_aor__cluster__icontains=search)
            | Q(band__istartswith=search) | Q(tech__istartswith=search))
        return qs

#-------------------------------------
class datatableview_location(BaseDatatableView):
    model = Location
    columns = ['id', 'city', 'province', 'region', 'area']
    max_display_length = 500

#-------------------------------------
class datatableview_tocaor(BaseDatatableView):
    model = TocAor
    columns = ['id', 'cluster', 'area']
    max_display_length = 500
    
#-------------------------------------
class InventoryAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve"],
            "principal": "authenticated",
            "effect": "allow"
        },
        {
            "action": ["create", "update", "partial_update", "destroy"],
            "principal": ["group:admins"],
            "effect": "allow"
        }
    ]

#-------------------------------------
class CellsView(viewsets.ModelViewSet):
    
    queryset = Cell.objects.all()
    serializer_class = CellsSerializer
    permission_classes = (InventoryAccessPolicy,)

    @action (detail=False, methods=['GET'], permission_classes=[IsAuthenticated])
    def filter(self, request):
        get_param = {}
        get_param['parent_id'] = request.GET.get('parent_id', '')
        get_param['cell_name'] = request.GET.get('cell_name', '')
        get_param['subdomain'] = request.GET.get('subdomain', '')
        get_param['site'] = request.GET.get('site_id', '')
        queries = {}

        for key, value in get_param.items():
            if key == 'parent_id' and value != '':
                 queries['parent_id'] = Q(parent_id=value)
            elif key == 'cell_name' and value != '':
                 queries['cell_name'] = Q(cell_name=value)
            elif key == 'site' and value != '':
                 queries['site'] = Q(site=value)
            elif key == 'subdomain' and value != '':
                if value.find(',') > -1:
                    subdomains = value.split(',')
                    queries['subdomain'] = [Q(subdomain=subdomain) for subdomain in subdomains]
                else:
                    queries['subdomain'] = Q(subdomain=value)
        
        if queries:
            ctr = 0
            for key, query in queries.items():
                if ctr == 0:
                    if key == 'subdomain' and type(query) is list:
                        for item in query:
                            if ctr == 0:
                                criteria = item
                                ctr += 1
                            else:
                                criteria |= item
                    else:
                        criteria = query
                else:
                    if key == 'subdomain' and type(query) is list:
                        for item in query:
                            criteria |= item
                    else:
                        criteria &= query
                ctr += 1
            devices = Cell.objects.all().filter(criteria)
            
            page = self.paginate_queryset(devices)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_paginated_response(devices, many=True)
            return Response(serializer.data, status=200)
        else:
            return Response({'detail': 'parent_id, cell_name, site_id or subdomain parameter required.', 'param received': [
                {'parent_id': get_param['parent_id'], 'cell_name': get_param['cell_name'],  'subdomain': get_param['subdomain'], 'site_id': get_param['site']}
            ]}, status=204)

#-------------------------------------
class DevicesView(viewsets.ModelViewSet):
    
    queryset = Device.objects.all()
    serializer_class = DevicesSerializer
    permission_classes = (InventoryAccessPolicy,)

    @action (detail=True, methods=['GET'], permission_classes=[IsAuthenticated])
    def cells(self, request, pk=None):
        device = self.get_object()
        serializer = DeviceAndCellsSerializer(device)
        return Response(serializer.data, status=200)

    @action (detail=False, methods=['GET'], permission_classes=[IsAuthenticated])
    def filter(self, request):
        get_param = {}
        get_param['domain'] = request.GET.get('domain', '')
        get_param['ne_type'] = request.GET.get('ne_type', '')
        get_param['device_id'] = request.GET.get('device_id', '')
        get_param['site_id'] = request.GET.get('site_id', '')
        queries = {}

        for key, value in get_param.items():
            if key == 'domain' and value != '':
                 queries['domain'] = Q(domain=value)
            elif key == 'device_id' and value != '':
                 queries['device_id'] = Q(device_id=value)
            elif key == 'site_id' and value != '':
                 queries['site_id'] = Q(site_id=value)
            elif key == 'ne_type' and value != '':
                if value.find(',') > -1:
                    ne_types = value.split(',')
                    queries['ne_type'] = [Q(ne_type=ne_type) for ne_type in ne_types]
                else:
                    queries['ne_type'] = Q(ne_type=value)
        
        if queries:
            ctr = 0
            for key, query in queries.items():
                if ctr == 0:
                    if key == 'ne_type' and type(query) is list:
                        for item in query:
                            if ctr == 0:
                                criteria = item
                                ctr += 1
                            else:
                                criteria |= item
                    else:
                        criteria = query
                else:
                    if key == 'ne_type' and type(query) is list:
                        for item in query:
                            criteria |= item
                    else:
                        criteria &= query
                ctr += 1
            devices = Device.objects.all().filter(criteria)
            
            page = self.paginate_queryset(devices)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_paginated_response(devices, many=True)
            return Response(serializer.data, status=200)
        else:
            return Response({'detail': 'domain, ne_type, site_id or device_id parameter required.', 'param received': [
                {'domain': get_param['domain'], 'ne_type': get_param['ne_type'],  'site_id': get_param['site_id'], 'device_id': get_param['device_id']}
            ]}, status=204)

#-------------------------------------
class SmartSiteView(viewsets.ModelViewSet):
    
    queryset = SmartSite.objects.all()
    serializer_class = SmartSiteSerializer
    permission_classes = (InventoryAccessPolicy,)

    def create(self, request):
        serializer = SmartSiteCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response({'detail': serializer.errors}, status=204)

    def update(self, request, pk=None):
        smartsite = self.get_object()
        serializer = SmartSiteCreateUpdateSerializer(smartsite, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response({'detail': serializer.errors}, status=204)

    def partial_update(self, request, pk=None):
        smartsite = self.get_object()
        serializer = SmartSiteCreateUpdateSerializer(smartsite, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response({'detail': serializer.errors}, status=204)

    @action (detail=True, methods=['GET'], permission_classes=[IsAuthenticated])
    def nes(self, request, pk=None):
        smartsite = self.get_object()
        serializer = SmartSiteAndNEsSerializer(smartsite)
        return Response(serializer.data, status=200)

    @action (detail=False, methods=['GET'], permission_classes=[IsAuthenticated])
    def filter(self, request):
        get_param = {}
        get_param['site_id'] = request.GET.get('site_id', '')
        get_param['city'] = request.GET.get('city', '')
        get_param['province'] = request.GET.get('province', '')
        get_param['toc_aor'] = request.GET.get('toc_aor', '')
        get_param['l_area'] = request.GET.get('l_area', '')
        get_param['t_area'] = request.GET.get('t_area', '')
        queries = {}

        for key, value in get_param.items():
            if key == 'site_id' and value != '':
                 queries['site_id'] = Q(siteid=value)
            elif key == 'city' and value != '':
                 queries['city'] = Q(location__city=value)
            elif key == 'province' and value != '':
                 queries['province'] = Q(location__province=value)
            elif key == 'l_area' and value != '':
                 queries['l_area'] = Q(location__area=value)
            elif key == 'toc_aor' and value != '':
                 queries['toc_aor'] = Q(toc_aor__cluster=value)
            elif key == 't_area' and value != '':
                 queries['t_area'] = Q(toc_aor__area=value)
        
        if queries:
            ctr = 0
            for key, query in queries.items():
                if ctr == 0:
                    criteria = query
                else:
                    criteria &= query
                ctr += 1
            devices = SmartSite.objects.all().filter(criteria)
            
            page = self.paginate_queryset(devices)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_paginated_response(devices, many=True)
            return Response(serializer.data, status=200)
        else:
            return Response({'detail': 'site_id, city, province or toc_aor parameter required.', 'param received': [
                {'site_id': get_param['site_id'], 'city': get_param['city'],  'province': get_param['province'], 'toc_aor': get_param['toc_aor']}
            ]}, status=204)

#-------------------------------------
class SmartNeView(viewsets.ModelViewSet):
    
    queryset = SmartNe.objects.all()
    serializer_class = SmartNeSerializer
    permission_classes = (InventoryAccessPolicy,)

    def list(self, request):
        pass

#-------------------------------------
class SiteNeAssetView(viewsets.ModelViewSet):
    
    queryset = SiteNeAsset.objects.all()
    serializer_class = SiteNeAssetSerializer
    permission_classes = (InventoryAccessPolicy,)

#-------------------------------------
class TocAorView(viewsets.ModelViewSet):
    
    queryset = TocAor.objects.all()
    serializer_class = TocAorSerializer
    permission_classes = (InventoryAccessPolicy,)

#-------------------------------------
class LocationView(viewsets.ModelViewSet):
    
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (InventoryAccessPolicy,)

#-------------------------------------
class GetUserToken(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        refresh = RefreshToken.for_user(request.user)
        content = {
            'user_id': str(request.user.id),  # `django.contrib.auth.User` instance.
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }
        return Response(content)