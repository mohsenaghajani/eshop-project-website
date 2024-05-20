from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView

from article.models import Article


# Create your views here.


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