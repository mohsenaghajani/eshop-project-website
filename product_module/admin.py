from django.contrib import admin

from product_module.models import Category, Brand, Product, ProductTag, ProductVisit, ProductImage


# Register your models here.

class ProductImageAdmin(admin.TabularInline):
    model = ProductImage

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
    inlines = [ProductTagAdmin, ProductImageAdmin]
    readonly_fields = ['slug', 'is_delete', 'final_price']

@admin.register(ProductVisit)
class ProductVisitAdmin(admin.ModelAdmin):
    list_display = ['product', 'user']

