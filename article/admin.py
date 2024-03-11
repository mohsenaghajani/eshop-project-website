from django.contrib import admin

from article.models import Category, Article


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title', 'is_active']
    list_editable = ['is_active']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_active']
    list_editable = ['is_active']
