from django.shortcuts import render, get_object_or_404

from article.models import Category
from .models import Product
from django.views.generic import ListView, DetailView
from django.db.models import Avg

# Create your views here.


class ProductList(ListView):
    template_name = 'product_module/product_List.html'
    model = Product
    context_object_name = 'products'
    ordering = ['final_price']
    paginate_by = 1

    def get_queryset(self):
        base_query = super(ProductList, self).get_queryset()
        category_title = self.kwargs.get('cat')
        if category_title is not None:
            products = base_query.filter(is_active=True, category__url_title__iexact=category_title)
            return products
        products = base_query.filter(is_active=True)
        return products



class ProductDetail(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product


def category_component(request):
    categories = Category.objects.filter(is_active=True)
    context = {
        'categories': categories
    }
    return render(request, 'component/product_category_component.html', context)



