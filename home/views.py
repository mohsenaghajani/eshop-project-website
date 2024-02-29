from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.


class HomePage(TemplateView):
    template_name = 'home/index.html'


def index_header_component(request):
    return render(request, 'shared/site_header.html', )


def index_footer_component(request):
    return render(request, 'shared/site_footer.html')