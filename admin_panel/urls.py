from django.urls import path
from .views import *

urlpatterns = [
    path('admin-panel/', DashboardArticlesListView.as_view(), name='admin_panel')
]