from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views.generic import ListView, DetailView
from django.db.models import Avg

# Create your views here.


class ProductList(ListView):
    template_name = 'product_module/product_List.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        base_query = super().get_queryset()
        products = base_query.filter(is_active=True)
        return products


class ProductDetail(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product

