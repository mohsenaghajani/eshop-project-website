from django.db.models import Count
from django.shortcuts import render
from django.views.generic.base import TemplateView

from product_module.models import Product, Category
from utils.conveter import create_group_list
from site_sittings.models import SiteSettings, FooterLink, FooterLinkBox, Slider


# Create your views here.


class HomePage(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slider = Slider.objects.filter(is_active=True)
        context['sliders'] = slider
        products = Product.objects.filter(is_active=True).order_by('-id')[:12]
        context['group_list'] = create_group_list(products)
        most_visited = (Product.objects.filter(is_active=True).annotate(visit_count=Count('productvisit'))
                        .order_by('-visit_count'))[:12]
        context['most_visited'] = create_group_list(most_visited)
        categories_products = []
        categories = list(Category.objects.annotate(product_count=Count('product')).
                          filter(is_active=True, product_count__gt=0))
        for category in categories:
            item = {
                'title': category.name,
                'id': category.id,
                'products': category.product.all()
            }
            categories_products.append(item)

        context['category_products'] = categories_products
        return context


def index_header_component(request):
    setting = SiteSettings.objects.filter(is_main_site_setting=True).first()
    context = {
        'site_setting': setting
    }

    return render(request, 'shared/site_header.html', context)


def index_footer_component(request):
    setting = SiteSettings.objects.filter(is_main_site_setting=True).first()
    footer_link_box = FooterLinkBox.objects.all()
    context = {
        'site_setting': setting,
        'footer_link_boxes': footer_link_box
    }
    return render(request, 'shared/site_footer.html', context)