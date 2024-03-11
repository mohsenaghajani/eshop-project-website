from django.shortcuts import render
from django.views.generic.base import TemplateView

from site_sittings.models import SiteSettings, FooterLink, FooterLinkBox, Slider


# Create your views here.


class HomePage(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slider = Slider.objects.filter(is_active=True)
        context['sliders'] = slider
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