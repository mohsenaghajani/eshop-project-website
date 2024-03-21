from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from account.models import User
from .forms import ProfileEditForm, ChangePassForm

# Create your views here.


class UserProfileView(TemplateView):
    template_name = 'user_panel/profile.html'


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


def user_profile_component(request):
    return render(request, 'profile_component/user_profile_component.html')


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