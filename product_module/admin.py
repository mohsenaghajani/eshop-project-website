from django.contrib import admin

from product_module.models import Category, Brand, Product


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    readonly_fields = ['slug']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']
    readonly_fields = ['slug']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'brand', 'price_with_discount', 'price', 'is_active']
    readonly_fields = ['price_with_discount', 'slug']
