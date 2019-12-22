from django.shortcuts import render,get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from .models import Produkty,Kategoria
from .forms import *
# Create your views here.

def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    if q:
        kats = Kategoria.objects.all()
        produkty = Produkty.objects.filter(nazwa__icontains=q)
        produkty |= Produkty.objects.filter(opis__icontains=q)
        produkty |= Produkty.objects.filter(numer__icontains=q)
        context = {'query' : q,
                   'produkty' : produkty,
                   'kats'   : kats,}
        template = 'produkty/result.html'
    else:
        context = {}
        template = 'produkty/index.html'

    return render(request,template,context)


def detail(request, produkt_id):
    produkt = Produkty.objects.get(pk=produkt_id)
    kats = Kategoria.objects.all()

    return render(request, 'produkty/detail_block.html', {'produkt': produkt,
                                                          'kats': kats,})

def index(request):
    prod_list = Produkty.objects.all()
    kats = Kategoria.objects.all()
    template = loader.get_template('produkty/index.html')
    context = {
        'prod_list': prod_list,
        'kats': kats,
    }
    return HttpResponse(template.render(context, request))

def kategorie(request):
    kats = Kategoria.objects.all()
    template = loader.get_template('produkty/kategorie.html')
    context = {
        'kats': kats,
    }
    return HttpResponse(template.render(context, request))
    #return HttpResponse(kats)

def kategoria(request,id):
    kategoria_widok = Produkty.objects.filter(kategoria=id)
    kat = Kategoria.objects.get(pk=id)
    kats = Kategoria.objects.all()
    form1 = Zamowienie()
    context = {
        'kategoria_widok'   : kategoria_widok,
        'kat'               : kat,
        'kats'              : kats,
        'form1'             : form1,       }
    return render(request, 'produkty/katf kopia.html', context)

def zamowienie(request):
    form = Zamowienie()
    prod_list = Produkty.objects.all()
    context = {
        "form" : form,
        'prod_list': prod_list,
    }
    return render(request,'produkty/zamow.html',context)