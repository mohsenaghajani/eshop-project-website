from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from django.views.generic.list import ListView

from article.models import Article, Category


# Create your views here.

class ArticlesListView(ListView):
    model = Article
    paginate_by = 1
    template_name = 'article/article.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticlesListView, self).get_context_data(*args, **kwargs)
        return context
    
    def get_queryset(self):
        query = super(ArticlesListView, self).get_queryset()
        query = query.filter(is_active=True)
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)
        return query


def article_categories_component(request: HttpRequest):
    main_categories = Category.objects.filter(is_active=True, parent_id=None)
    context = {
        'main_categories': main_categories
    }
    return render(request, 'article/article_categories_component.html', context)


class ArticleDetailView(DetailView):
    template_name = 'article/article_detail.html'
    model = Article

    def get_queryset(self):
        query = super(ArticleDetailView, self).get_queryset()
        query = query.filter(is_active=True)
        return query

