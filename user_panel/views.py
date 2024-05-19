from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView, ListView

from account.models import User
from order_module.models import Order
from .forms import ProfileEditForm, ChangePassForm

# Create your views here.


@method_decorator(login_required, 'dispatch')
class UserProfileView(TemplateView):
    template_name = 'user_panel/profile.html'


@method_decorator(login_required, 'dispatch')
class ProfileEditView(View):

    def get(self, request):
        user = User.objects.get(id=request.user.id)
        edit_form = ProfileEditForm(instance=user)
        context = {
            'form': edit_form,
            'user': user
        }
        return render(request, 'user_panel/profile_edit.html', context)

    def post(self, request):
        user = User.objects.get(id=request.user.id)
        edit_form = ProfileEditForm(request.POST, request.FILES, instance=user)
        if edit_form.is_valid():
            edit_form.save(commit=True)
        context = {
            'form': edit_form
        }
        return render(request, 'user_panel/profile_edit.html', context)


@login_required()
def user_profile_component(request):
    return render(request, 'profile_component/user_profile_component.html')


@method_decorator(login_required, 'dispatch')
class ChangePassView(View):
    def get(self, request):
        context = {
            'form': ChangePassForm()
        }
        return render(request, 'user_panel/change_pass.html', context)

    def post(self, request):
        form = ChangePassForm(request.POST)
        if form.is_valid():
            user = User.objects.get(id=request.user.id)
            if user.check_password(form.cleaned_data.get('current_password')):
                user.set_password(form.cleaned_data.get('password'))
                user.save()
                logout(request)
                return redirect(reverse('login-page'))
            else:
                form.add_error('current_password', 'کلمه عبور اشتباه است')
        context = {
            'form': form
        }
        return render(request, 'user_panel/change_pass.html', context)


class MyShoppingList(ListView):
    template_name = 'user_panel/my_shopping.html'
    model = Order

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(is_paid=True, user_id=self.request.user.id)
        return query


def shopping_detail(request: HttpRequest, order_id):
    order = Order.objects.filter(id=order_id, user_id=request.user.id).first()
    if order is None:
        return Http404('سبد خرید پیدا نشد')
    return render(request, 'user_panel/shopping_detail.html', {
        'order': order
    })
