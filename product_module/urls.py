from django.urls import path
from product_module import views

urlpatterns = [
    path('', views.ProductList.as_view(), name='products-list'),
    path('<int:product_id>/<slug:slug>', views.ProductDetail.as_view(), name='products-detail'),

]