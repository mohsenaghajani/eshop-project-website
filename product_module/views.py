from django.shortcuts import render, get_object_or_404
from .models import Product
from django.db.models import Avg

# Create your views here.


def products_list(request):
    products = Product.objects.filter(is_active=True).order_by('-price')[:3]

    context = {
        'products': products,
    }
    return render(request, 'product_module/product_List.html', context)


def product_detail(request, product_id, slug):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product
    }
    return render(request, 'product_module/product_detail.html', context)