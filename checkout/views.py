from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "No Item in the Cart")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HbrFLHReQY4VHFKhVAabxoF3TvQcohd1zoWXw2YR71t63C0QUy0O1mrEhcekP86elYc5gjMr6f6B2jtDdiYUobO00w8qKCVig',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

