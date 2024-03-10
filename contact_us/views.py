from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import FormView, CreateView

from site_sittings.models import SiteSettings
from .forms import ContactUsForms, ContactUsModelForm
# Create your views here.


class ContactUsView(FormView):
    template_name = 'contact_us/contact_us.html'
    form_class = ContactUsModelForm
    success_url = '/contact-us/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ContactUsClassView(CreateView):
    template_name = 'contact_us/contact_us.html'
    form_class = ContactUsModelForm
    success_url = '/contact-us/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_setting'] = SiteSettings.objects.filter(is_main_site_setting=True).first()
        return context


