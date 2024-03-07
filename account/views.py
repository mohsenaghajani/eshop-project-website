from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views import View
from .models import User
from .forms import UserForms, LoginForm
from django.contrib.auth import login, logout

# Create your views here.


class RegisterView(View):
    def get(self, request):
        register_form = UserForms()
        context = {
            'register_form': register_form
        }
        return render(request, 'login/sign_in.html', context)

    def post(self, request):
        register_form = UserForms(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'ایمیل وارد شده تکراری است')
            else:
                new_user = User(
                    username=user_email,
                    email_active_code=get_random_string(72),
                    email=user_email,
                    is_active=False,
                )
                new_user.set_password(user_password)
                new_user.save()
                return redirect(reverse('home-page'))

        context = {
            'register_form': register_form
        }
        return render(request, 'login/login.html', context)


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'login/login.html', context)

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_pass = login_form.cleaned_data.get('password')
            user = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'حساب کاربری فعال نشده است')
                else:
                    is_password_correct = user.check_password(user_pass)
                    if is_password_correct:
                        login(request, user)
                        return redirect('home-page')
                    else:
                        login_form.add_error('email', 'نام کاربری و یا کلمه عبور اشتباه است')
            else:
                login_form.add_error('email', 'نام کاربری و یا کلمه عبور اشتباه است0')
        context = {
            'context': login_form
        }
        return render(request, 'login/login.html', context)


class ActivationAccount(View):
    def get(self, request, email_active_code):
        user = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            user.is_active = True
            user.email_active_code = get_random_string(72)
            user.save()
            return redirect('home-page')
        else:
            return redirect('sign-in-page')
