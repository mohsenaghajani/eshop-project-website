from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import FormView
from .forms import ContactUsForms, ContactUsModelForm
# Create your views here.


class ContactUsView(FormView):
    template_name = 'contact_us/contact_us.html'
    form_class = ContactUsModelForm
    success_url = '/contact-us/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    # def get(self, request):
    #     contact_forms = ContactUsModelForm()
    #     return render(request, 'contact_us/contact_us.html',
    #                   {'contact_forms': contact_forms})
    #
    # def post(self, request):
    #     contact_forms = ContactUsModelForm(request.POST)
    #     if contact_forms.is_valid():
    #         contact_forms.save()
    #         return redirect('home-page')
    #     return render(request, 'contact_us/contact_us.html',
    #                   {'contact_forms': contact_forms})


