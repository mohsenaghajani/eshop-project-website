from django.contrib import admin
from .models import ContactUs
# Register your models here.


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['title', 'email']
    readonly_fields = ['title', 'message', 'email', 'is_read_by_admin', 'full_name']

