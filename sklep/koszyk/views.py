from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.urls import reverse
# Create your views here.
from .models import Cart
from .forms import Zmiana_Statusu, Status_f, Zmiana_Statusu_M

from produkty.models import Produkty, Kategoria


def view(request):
    cart = Cart.objects.all()[0]  # koszyk1
    kats = Kategoria.objects.all()
    form_f = Status_f(request.POST)
    if form_f.is_valid():
        return redirect("magazyn")
    context = {"cart": cart, "kats": kats, "form_f": form_f}
    template = "cart/cart.html"
    return render(request, template, context)


def cart_nr(request, c_id):
    cart = get_object_or_404(Cart, id=c_id)
    czy_sprzedawca = request.user.groups.filter(name='Sprzedawca').exists()
    if czy_sprzedawca:
        form = Zmiana_Statusu(request.POST or None, instance=cart)
    else:
        form = Zmiana_Statusu_M(request.POST or None, instance=cart)
    if form.is_valid():
        form.save()
        return redirect("magazyn")
    context = {"cart": cart, "form": form, 'czy_sprzedawca': czy_sprzedawca, }
    template = "cart/cart_nr.html"
    return render(request, template, context)


def carts(request):
    pass
    # all_carts = Cart.objects.all()
    # last_cart = Cart.objects.last()
    # wyslany_cart = Cart.objects.filter(status__iexact="NOWE")
    # form_f = Status_f(request.GET)
    # context = {"all_carts": all_carts,
    #            "last_cart":last_cart,
    #            "wyslany_cart": wyslany_cart,
    #            "form_f": form_f}
    # template = "cart/carts.html"
    # return render(request, template, context)

def magazyn(request):
    czy_sprzedawca = request.user.groups.filter(name='Sprzedawca').exists()
    if czy_sprzedawca: #request.user.groups.filter(name='Sprzedawca').exists():
        status_filtr = Cart.objects.all()
    else:
        status_filtr = Cart.objects.filter(status__iexact="WYSŁANE")
    form_f = Status_f(request.POST or None)
    all_carts = Cart.objects.all()
    last_cart = Cart.objects.last()
    count_carts = Cart.objects.count()

    context = {"czy_sprzedawca": czy_sprzedawca, "all_carts": all_carts,
               "last_cart": last_cart, 'count_carts': count_carts,
               "status_filtr": status_filtr, "form_f": form_f}
    template = "cart/carts.html"
    return render(request, template, context)


def magazyn_f(request,status_f):
    czy_sprzedawca = request.user.groups.filter(name='Sprzedawca').exists()
    if request.user.groups.filter(name='Sprzedawca').exists():
        if status_f != "all":
            status_filtr = Cart.objects.filter(status=status_f)
            print('1:',str(status_filtr))
        else:
            status_filtr = Cart.objects.all()
            print('2:',str(status_filtr))
    else:
        status_filtr = Cart.objects.filter(status=status_f)
    form_f = Status_f(request.POST or None)
    if form_f.is_valid():
        status_f = form_f.cleaned_data['status']
        print('valid 4')
        return redirect("magazyn_f",status_f)

    all_carts = Cart.objects.all()
    last_cart = Cart.objects.last()
    count_carts = Cart.objects.count()
    context = {"czy_sprzedawca": czy_sprzedawca, "all_carts": all_carts,
               "last_cart": last_cart, 'count_carts': count_carts,
               "status_filtr": status_filtr, "form_f": form_f}
    template = "cart/carts.html"
    return render(request, template, context)


def new_cart(request):
    new_cart = Cart()
    save = new_cart.save()
    last_cart = Cart.objects.last()
    cid = last_cart.id
    return redirect("cart_nr", cid)


def update_cart(request, nazwa):
    # cart = Cart.objects.last()
    cart = Cart()
    cart.save()
    product = Produkty.objects.get(nazwa=nazwa)
    cart.products.add(product)

    # template = 'cart_nr'
    # context = {"c_id": c_id }
    return HttpResponseRedirect(reverse("cart"))
    # return render(request, template, context)


def update_cart_m(request, nazwa, c_id):
    cart = Cart.objects.get(id=c_id)
    product = Produkty.objects.get(nazwa=nazwa)
    cart.products.add(product)
    template = "cart/cart_nr.html"
    context = {"c_id": c_id}
    #return HttpResponseRedirect(reverse("cart_nr"))
    return redirect("cart_nr", c_id)
    #render(request, template, context)

def remove_from_cart(request, id, c_id):
    cart = Cart.objects.get(id=c_id)
    cartitem = Produkty.objects.get(id=id)
    cart.products.remove(cartitem)
    return redirect("cart_nr",c_id)

# def remove_from_cart1(request, id):
#     cart = Cart.objects.all()[0]
#     cartitem = Produkty.objects.get(id=id)
#     cart.products.remove(cartitem)
#     return redirect(reverse("cart_nr"))


def delete_cart(request, id):
    c = Cart.objects.get(id=id)
    usun = c.delete()
    return HttpResponseRedirect(reverse("magazyn"))

def filtruj(request):
    if request.method == 'POST':
        form_f = Status_f(request.POST)
        if form_f.is_valid():
            status_f = form_f.cleaned_data['status']
            print('valid')
            return redirect("magazyn_f",status_f)
        else:
            print('invalid 1')
    else:
        print('invalid')
        return render (request, "magazyn_f")
