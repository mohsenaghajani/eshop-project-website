from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .forms import ProfileEditForm

# Create your views here.


class UserProfileView(TemplateView):
    template_name = 'user_panel/profile.html'


class ProfileEditView(View):
    def get(self, request):
        edit_form = ProfileEditForm()
        context = {
            'form': edit_form
        }
        return render(request, 'user_panel/profile_edit.html', context)


    def post(self, request):
        pass



def user_profile_component(request):
    return render(request, 'profile_component/user_profile_component.html')