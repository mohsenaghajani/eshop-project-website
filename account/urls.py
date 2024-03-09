from django.urls import path
from .views import RegisterView, LoginView, ActivationAccount, ForgetPassword, ResetPassword, LogoutView

urlpatterns = [
    path('login', LoginView.as_view(), name='login-page'),
    path('sign-in', RegisterView.as_view(), name='sign-in-page'),
    path('activation/<email_active_code>', ActivationAccount.as_view(), name='activation'),
    path('forget-pass', ForgetPassword.as_view(), name='forget-pass'),
    path('reset-pass/<email_active_code>', ResetPassword.as_view(), name='reset-pass'),
    path('logout', LogoutView.as_view(), name='logout-page'),
]