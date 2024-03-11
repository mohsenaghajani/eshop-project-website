from django.shortcuts import render
from django.views import View

from article.models import Article


# Create your views here.


class ArticleView(View):
    def get(self, request):
        articles = Article.objects.filter(is_active=True)
        context = {
            'articles': articles
        }

        return render(request, 'article/article.html', context)