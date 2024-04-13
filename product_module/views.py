from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from article.models import Category
from site_sittings.models import Banner
from .models import Product, Brand, ProductVisit, ProductImage
from django.views.generic import ListView, DetailView
from django.db.models import Avg, Count
from utils.user_ip import get_user_ip
from utils.conveter import create_group_list
# Create your views here.


class ProductList(ListView):
    template_name = 'product_module/product_List.html'
    model = Product
    context_object_name = 'products'
    ordering = ['final_price']
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductList, self).get_context_data()
        query = Product.objects.all()
        product: Product = query.order_by('-price').first()
        db_max_price = product.price or 100000
        context['db_max_price'] = db_max_price
        context['start_price'] = self.request.GET.get('start_price') or 0
        context['end_price'] = self.request.GET.get('end_price') or 15000000
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_product = self.object
        user_ip = get_user_ip(self.request)
        context['images_group'] = create_group_list(list(ProductImage.objects.filter(product_id=loaded_product.id)), 3)
        user = None
        if self.request.user.is_authenticated:
            user = self.request.user
        has_been_visited = ProductVisit.objects.filter(user_ip__iexact=user_ip, product=loaded_product).exists()
        if not has_been_visited:
            ProductVisit.objects.create(user_ip=user_ip, user=user, product=loaded_product)
        return context


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