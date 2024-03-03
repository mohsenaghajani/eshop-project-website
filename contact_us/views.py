from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import FormView, CreateView
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


