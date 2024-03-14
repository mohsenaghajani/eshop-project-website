from django.urls import path

from article.views import ArticlesListView, ArticleDetailView

urlpatterns = [
    path('article_list/', ArticlesListView.as_view(), name='article-list'),
    path('cat/<str:category>', ArticlesListView.as_view(), name='article-category'),
    path('<pk>', ArticleDetailView.as_view(), name='article-detail'),
]