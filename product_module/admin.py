from django.contrib import admin

from product_module.models import Category, Brand, Product, ProductTag


# Register your models here.

class ProductTagAdmin(admin.TabularInline):
    model = ProductTag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'discount', 'final_price', 'is_active']
    list_editable = ['is_active', 'price', 'discount']
    list_filter = ['price', 'is_active']
    inlines = [ProductTagAdmin]
    readonly_fields = ['slug', 'is_delete', 'final_price']




