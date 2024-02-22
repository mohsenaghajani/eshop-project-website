from django.urls import path
from product_module import views

urlpatterns = [
    path('', views.products_list, name='products-list'),
    path('<int:product_id>/<slug:slug>', views.product_detail, name='products-detail'),

]