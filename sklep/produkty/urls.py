from django.urls import path
from . import views

urlpattens = [
    path('produkty/<int:produkt_id>/', views.detail, name='detail'),
    path('', views.index, name='index'),
    path('kats',views.kategorie,name='kategorie')

]