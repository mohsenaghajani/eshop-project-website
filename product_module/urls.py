from django.urls import path
from product_module import views

urlpatterns = [
    path('', views.ProductList.as_view(), name='products-list'),
    path('<slug:slug>', views.ProductDetail.as_view(), name='products-detail'),
    path('cat/<cat>/', views.ProductList.as_view(), name='category-list'),

]