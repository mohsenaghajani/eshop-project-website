from django.contrib import admin
from .models import SiteSettings, FooterLink, FooterLinkBox, Slider
# Register your models here.


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['site_name', 'site_url']


@admin.register(FooterLinkBox)
class FooterLinkBoxAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(FooterLink)
class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'url']
    list_editable = ['url', 'is_active']

