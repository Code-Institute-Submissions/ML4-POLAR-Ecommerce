from django.shortcuts import render

# Create your views here.

def view_cart(request):
    """ a view that returns the cart """

    return render(request, 'cart/cart.html')