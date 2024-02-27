from django.shortcuts import render

# Create your views here.


def home_page(request):
    return render(request, 'home/index.html')


def index_header_component(request):
    return render(request, 'shared/site_header.html', )


def index_footer_component(request):
    return render(request, 'shared/site_footer.html')