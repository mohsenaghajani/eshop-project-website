from django.db import models

from account.models import User


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=32, verbose_name='عنوان')
    url_title = models.CharField(max_length=33, verbose_name='عنوان در لینک')
    parent = models.ForeignKey('Category', on_delete=models.CASCADE,
                               verbose_name='والد', null=True, blank=True,
                               related_name='category')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    slug = models.SlugField(max_length=32, verbose_name='عنوان در لینک')
    image = models.ImageField(upload_to='images/article', verbose_name='تصویر')
    category = models.ManyToManyField(Category, verbose_name='دسته بندی')
    short_description = models.TextField(verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات')
    is_active = models.BooleanField(default=True , verbose_name='فعال / غیر فعال')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده', editable=False, null=True)

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def __str__(self):
        return self.title
