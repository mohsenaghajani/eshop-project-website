from django.http import HttpRequest
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from utils.my_decorator import permission_admin_panel_factory
from article.models import Article


# Create your views here.

@method_decorator(permission_admin_panel_factory(),name='dispatch')
class DashboardArticlesListView(ListView):
    model = Article
    paginate_by = 12
    template_name = 'admin_panel/articles_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardArticlesListView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        query = super(DashboardArticlesListView, self).get_queryset()
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)
        return query