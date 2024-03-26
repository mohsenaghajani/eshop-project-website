from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

from article.models import Category
from site_sittings.models import Banner
from .models import Product, Brand
from django.views.generic import ListView, DetailView
from django.db.models import Avg, Count


# Create your views here.


class ProductList(ListView):
    template_name = 'product_module/product_List.html'
    model = Product
    context_object_name = 'products'
    ordering = ['final_price']
    paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductList, self).get_context_data()
        query = Product.objects.all()
        product: Product = query.order_by('-price').first()
        db_max_price = product.price or 100000
        context['db_max_price'] = db_max_price
        context['start_price'] = self.request.GET.get('start_price') or 0
        context['end_price'] = self.request.GET.get('end_price') or 100000
        context['banners'] = Banner.objects.filter(is_active=True, position=Banner.BannerPositions.product_list)
        return context

    def get_queryset(self):
        query = super(ProductList, self).get_queryset()
        category_title = self.kwargs.get('cat')
        brand_name = self.kwargs.get('brand')
        request: HttpRequest = self.request
        start_price = request.GET.get('start_price')
        end_price = request.GET.get('end_price')
        if start_price is not None:
            query = query.filter(price__gte=start_price)
        if end_price is not None:
            query = query.filter(price__lte=end_price)
        if category_title is not None:
            query = query.filter(is_active=True, category__url_title__iexact=category_title)
        if brand_name is not None:
            query = query.filter(is_active=True, brand__name__iexact=brand_name)
        return query


class ProductDetail(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product


def category_component(request):
    categories = Category.objects.filter(is_active=True)
    context = {
        'categories': categories
    }
    return render(request, 'component/product_category_component.html', context)


def brand_component(request):
    brands = Brand.objects.all().annotate(product_count=Count('product'))
    context = {
        'brands': brands
    }
    return render(request, 'component/brand_component.html', context)