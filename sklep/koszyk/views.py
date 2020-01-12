from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.urls import reverse
# Create your views here.
from .models import Cart
from .forms import Zmiana_Statusu

from produkty.models import Produkty, Kategoria

def view(request):
    cart = Cart.objects.all()[0]    #koszyk1
    kats = Kategoria.objects.all()
    context = {"cart": cart, "kats":kats,}
    template = "cart/cart.html"
    return render(request,template,context)

def cart_nr(request,id):
    cart = get_object_or_404(Cart,id=id)    #koszyk1
    kats = Kategoria.objects.all()
    form = Zmiana_Statusu(request.POST or None, instance=cart)
    if form.is_valid():
        form.save()
        return redirect("magazyn")
    context = {"cart": cart, "kats":kats,"form":form,}
    template = "cart/cart_nr.html"
    return render(request, template, context)


def carts(request):
    all_carts = Cart.objects.all()
    last_cart = Cart.objects.last()
    context = {"all_carts": all_carts, "last_cart":last_cart, }
    template = "cart/carts.html"
    return render(request, template, context)

def magazyn(request):
    all_carts = Cart.objects.all()
    last_cart = Cart.objects.last()
    context = {"all_carts": all_carts, "last_cart": last_cart, }
    template = "cart/baza_magazyn.html"
    return render(request, template, context)

def new_cart(request):
    new_cart = Cart()
    save = new_cart.save()
    return HttpResponseRedirect(reverse("magazyn"))

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

def delete_cart(request,id):
    c = Cart.objects.get(id=id)
    usun = c.delete()
    return HttpResponseRedirect(reverse("magazyn"))





