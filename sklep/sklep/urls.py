"""sklep URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

#moje
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from produkty.views import index, detail, kategorie ,kategoria, detail, zamowienie

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produkty/<int:produkt_id>/', detail, name='detail'),
    path('', index, name='index'),
    path('kats', kategorie, name='kategorie'),
    path('kategoria/<int:id>/', kategoria, name='kategoria'),
    path('zamow',zamowienie, name='zamowienie'),
 #   path('image', static(settings.MEDIA_URL), document_root=settings.MEDIA_ROOT),
   # path('image',MEDIA_URL)
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT )
