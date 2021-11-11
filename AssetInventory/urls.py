"""AssetInventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users import views as user_view

urlpatterns = [
    #path('api/api-auth/', include('rest_framework.urls')),
    path('', include('api.urls')),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('api/token/', TokenObtainPairView.as_view(), name='obtainToken'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refreshToken'),
    path('register/', user_view.register, name='register'),
    path('user_router/', user_view.user_router, name='user_router'),

    path('', include('edrar.urls')),
    path('', include('nmsdata.urls')),
]
