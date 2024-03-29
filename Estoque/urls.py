"""Estoque URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from API.urls import router
from django.conf import settings
from django.conf.urls.static import static
from .views import notfound404

urlpatterns = [
    path('', include('inicio.urls')),
    path('welcome/', include('produtos.urls')),
    path('welcome/', include('perfil.urls')),
    path('welcome/', include('sua_api.urls')),
    path('ryandev/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('gerenciamento/api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = notfound404


