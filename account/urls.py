from django.urls import path
from .views import RegisterView, LoginView, ActivationAccount

urlpatterns = [
    path('login', LoginView.as_view(), name='login-page'),
    path('sign-in', RegisterView.as_view(), name='sign-in-page'),
    path('activation/<email_active_code>', ActivationAccount.as_view(), name='activation'),
]