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
from produkty.views import *
from django.urls import include
from koszyk.views import view, update_cart, remove_from_cart
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produkty/<int:produkt_id>/', detail, name='detail'),
    path('',auth_views.LoginView.as_view(), name='login'),
    path('index',   index, name = 'index'),
    #path('', include('django.contrib.auth.urls')),
    path('login',auth_views.LoginView.as_view(), name='login'),
    path('logout',auth_views.LogoutView.as_view(), name='logout'),
    path('s/', search, name='search'),
    path('cart/<int:id>', remove_from_cart, name='remove_from_cart'),
    path('cart/<nazwa>', update_cart, name='update_cart'),
    path('cart/', view, name='cart'),
    path('kats', kategorie, name='kategorie'),
    path('kategoria/<int:id>/', kategoria, name='kategoria'),
    path('zamow',zamowienie, name='zamowienie'),
    path('choice', choice, name='choice'),

] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT )
