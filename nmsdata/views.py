from django.shortcuts import render
from .models import Device, Cell, Trx
from .serializers import NmsDevicesSerializer, NmsCellsSerializer, NmsTrxSerializer

from rest_framework import viewsets
from rest_access_policy import AccessPolicy

# Create your views here.
class NmsDataAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve", "create", "update", "partial_update", "destroy"],
            "principal": "authenticated",
            "effect": "allow"
        },
        # {
        #     "action": ["create", "update", "partial_update", "destroy"],
        #     "principal": ["group:admins"],
        #     "effect": "allow"
        # }
    ]

class NmsDevicesView(viewsets.ModelViewSet):
    
    queryset = Device.objects.all()
    serializer_class = NmsDevicesSerializer
    permission_classes = (NmsDataAccessPolicy,)

class NmsCellsView(viewsets.ModelViewSet):
    
    queryset = Cell.objects.all()
    serializer_class = NmsCellsSerializer
    permission_classes = (NmsDataAccessPolicy,)

class NmsTrxView(viewsets.ModelViewSet):
    
    queryset = Trx.objects.all()
    serializer_class = NmsTrxSerializer
    permission_classes = (NmsDataAccessPolicy,)
