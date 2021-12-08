""" Views for products app """
from django.shortcuts import render
from .models import Product


def all_products(request):
    """ View to show all products, incl sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
