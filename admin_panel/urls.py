from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', DashboardArticlesListView.as_view(), name='admin_panel')
]