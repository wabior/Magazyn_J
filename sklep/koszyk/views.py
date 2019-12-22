from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from .models import Cart
from produkty.models import Produkty, Kategoria

def view(request):
    cart = Cart.objects.all()[0]    #koszyk1
    kats = Kategoria.objects.all()
    context = {"cart": cart, "kats":kats,}
    template = "cart/cart.html"
    return render(request,template,context)

def update_cart(request,nazwa):
    cart = Cart.objects.all()[0]
    product = Produkty.objects.get(nazwa=nazwa)
                                #if not product in cart.products.all():
    cart.products.add(product)
    # else:
    #     cart.products.remove(product)
    return HttpResponseRedirect(reverse("cart"))

def remove_from_cart(request,id):
    cart = Cart.objects.all()[0]
    cartitem = Produkty.objects.get(id=id)
    cart.products.remove(cartitem)
    #cartitem.delete()
    #cartitem.cart = None
    #cartitem.save()
    return HttpResponseRedirect(reverse("cart"))

