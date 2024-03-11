from django.urls import path

from article.views import ArticleView

urlpatterns = [
    path('article_list', ArticleView.as_view(), name='article-list'),
]