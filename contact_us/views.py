from django.shortcuts import render, redirect
from .forms import ContactUsForms
# Create your views here.


def contact_us(request):
    if request.method == 'POST':
        contact_forms = ContactUsForms(request.POST)
        if contact_forms.is_valid():
            print(contact_forms.cleaned_data)
            return redirect('home-page')
        return redirect('contact-us')
    else:
        contact_forms = ContactUsForms()
    return render(request, 'contact_us/contact_us.html', {'contact_forms': contact_forms})