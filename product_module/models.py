from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=32, verbose_name='عنوان')
    url_title = models.CharField(max_length=32, verbose_name='عنوان url')
    created_time = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False, verbose_name='فعال /غیر فعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')

    def __str__(self):
        return f'{self.name}'


class Brand(models.Model):
    name = models.CharField(max_length=32, verbose_name='نام برند')
    country = models.CharField(max_length=32, verbose_name='کشور سازنده')
    created_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    title = models.CharField(max_length=32, verbose_name='عنوان محصول ')
    category = models.ManyToManyField(Category, related_name='product')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='product', verbose_name='برند')
    price = models.PositiveIntegerField(verbose_name='قیمت')
    discount = models.PositiveSmallIntegerField(default=0, null=True, blank=True,
                                                validators=[MaxValueValidator(99), MinValueValidator(1)],
                                                verbose_name='تخفیف')
    final_price = models.PositiveIntegerField(verbose_name='قیمت نهایی')
    rate = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    description = models.TextField(null=True, blank=True, verbose_name='توضیحات')
    short_description = models.TextField(max_length=300, verbose_name='توضیحات خلاصه')
    is_active = models.BooleanField(default=False, verbose_name='فعال /غیر فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده / نشده')
    slug = models.SlugField(default='', null=False, unique=True)
    created_time = models.DateTimeField(auto_now=True)
    modified_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/product', null=True, blank=True, verbose_name='تصویر محصول')

    def get_absolute_url(self):
        return reverse('products-detail', args=[self.id])

    def save(self, *args, **kwargs):
        self.final_price = self.price - (self.price * (self.discount / 100))
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'product : {self.title}  price : {self.price}'


class ProductTag(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_tag')
    caption = models.CharField(max_length=32, verbose_name='عنوان')

    def __str__(self):
        return f'{self.caption}'