from django.urls import path, include
from django.conf.urls import url
from . import views

from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('edrar/', views.home, name='edrar_home'),
    
]