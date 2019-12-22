from django.urls import path
from . import views

urlpattens = [
    path('produkty/<int:produkt_id>/', views.detail, name='detail'),
    path('', views.index, name='index'),
    path('s/', views.search, name='search'),
    path('kats',views.kategorie,name='kategorie')

]