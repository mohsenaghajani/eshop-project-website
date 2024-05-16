from django.urls import path
from . import views

urlpatterns = [
    path('add_to_basket', views.add_product_to_basket, name='add_to_basket'),
    path('basket', views.basket, name='basket'),
    path('remove_basket_detail', views.basket_content, name='basket_detail_remove'),
    path('change_basket_detail', views.change_order_detail_count, name='basket_detail_change'),
]