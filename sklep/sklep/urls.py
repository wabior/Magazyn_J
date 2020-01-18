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
from koszyk.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produkty/<int:produkt_id>/', detail, name='detail'),
    path('produkt/<int:produkt_id>/<int:c_id>/', detail_m, name='detail_m'),
    path('',auth_views.LoginView.as_view(), name='login'),
    path('index',   index, name = 'index'),
    path('login',auth_views.LoginView.as_view(), name='login'),
    path('logout',auth_views.LogoutView.as_view(), name='logout'),
    path('s/', search, name='search'),
    path('cart/<int:id>/<int:c_id>', remove_from_cart, name='remove_from_cart'),
    # path('cart/<nazwa>', update_cart, name='update_cart'),
    path('cart/<nazwa>', update_cart, name='update_cart'),
    path('cart/<nazwa>/<c_id>', update_cart_m, name='update_cart_m'),
    path('cart/', view, name='cart'),
    path('cart_nr/<int:c_id>/', cart_nr, name='cart_nr'),
    path('new_cart',new_cart, name = 'new_cart'),
    path('carts', carts, name = 'carts'),
    #path('kats', kategorie, name='kategorie'),
    path('kats/<int:cart_id>', kategorie, name='kategorie'),
    path('kategoria/<int:id>', kategoria, name='kategoria'),
    path('kat_m/<int:id>/<int:c_id>', kat_m, name='kat_m'),
    path('zamow',zamowienie, name='zamowienie'),
    path('choice', choice, name='choice'),
    path('magazyn', magazyn, name='magazyn'),
    path('magazyn/<status_f>', magazyn_f, name='magazyn_f'),
    path('delete_cart/<int:id>', delete_cart, name='delete_cart'),
    path('filtruj', filtruj, name='filtruj')
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT )
