from django.db import models

# Create your models here.


class SiteSettings(models.Model):
    address = models.CharField(max_length=330, verbose_name='آدرس')
    phone_number = models.CharField(max_length=14, verbose_name='شماره تلقن', null=True, blank=True)
    fax = models.CharField(max_length=15, verbose_name='فکس', null=True, blank=True)
    site_name = models.CharField(max_length=330, verbose_name='اسم سایت')
    site_url = models.CharField(max_length=32, verbose_name='آدرس سایت')
    copy_right = models.TextField(verbose_name='کپی رایت')
    email = models.EmailField(max_length=200, verbose_name='ایمیل')
    about_us = models.TextField(verbose_name='درباره ما')
    site_logo = models.ImageField(upload_to='images/site_setting', verbose_name='لوگوی سایت')
    is_main_site_setting = models.BooleanField(default=False, verbose_name='تظیم به عوان اصلی')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات'

    def __str__(self):
        return self.site_name


class FooterLinkBox(models.Model):
    title = models.CharField(max_length=32, verbose_name='عنوان')

    class Meta:
        verbose_name = 'دسته بندی لینک های فوتر'
        verbose_name_plural = 'دسته بندی های لینک های فوتر'

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    footer_link_box = models.ForeignKey(FooterLinkBox, on_delete=models.CASCADE, verbose_name='دسته بندی لینک های فوتر')
    title = models.CharField(max_length=320, verbose_name='عنوان')
    url = models.URLField(max_length=500, verbose_name='لینک')

    class Meta:
        verbose_name = 'لینک  فوتر'
        verbose_name_plural = 'لینک های فوتر'

    def __str__(self):
        return self.title


class Slider(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    url_title = models.CharField(max_length=330, verbose_name='عنوان لینک')
    url = models.URLField(max_length=300, verbose_name='لینک ')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to='images/slider', verbose_name='عکس ')
    is_active = models.BooleanField(default=True, verbose_name='فعال | غیر فعال ')

    class Meta:
        verbose_name = 'تنظیمات اسلاید'
        verbose_name_plural = 'تنظیمات اسلایدر'

    def __str__(self):
        return self.title


class Banner(models.Model):
    class BannerPositions(models.TextChoices):
        product_list = ('product_list', 'صفحه لیست محصولات')
        product_detail = ('product_detail', 'صفحه جزئیات محصول')
        about_us = ('about_us', 'صفحه درباره ما')

    title = models.CharField(max_length=320, verbose_name='عنوان')
    url = models.URLField(max_length=320, verbose_name='لینک')
    image = models.ImageField(upload_to='images/banner', verbose_name='تصویر')
    position = models.CharField(max_length=320, choices=BannerPositions.choices, verbose_name='محل قرارگیری')
    is_active = models.BooleanField(verbose_name='فعال / غیر فعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تبلیغات'
        verbose_name_plural = 'بنر های تبلیغاتی'
