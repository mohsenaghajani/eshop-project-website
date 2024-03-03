from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactUsClassView.as_view(), name='contact-us' )
]