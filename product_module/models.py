from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(default='')
    created_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Brand(models.Model):
    name = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    created_time = models.DateTimeField(auto_now=True)
    slug = models.SlugField(default='')

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    title = models.CharField(max_length=32)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='product')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='product')
    price = models.PositiveIntegerField()
    discount = models.PositiveSmallIntegerField(default=0, null=True, blank=True,
                                                validators=[MaxValueValidator(99), MinValueValidator(1)])
    price_with_discount = models.PositiveIntegerField()
    rate = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    description = models.TextField(null=True, blank=True)
    short_description = models.TextField(max_length=300)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(default='', null=False)
    created_time = models.DateTimeField(auto_now=True)
    modified_time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.price_with_discount = self.price - (self.price * (self.discount / 100))
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'product : {self.title}  price : {self.price}'