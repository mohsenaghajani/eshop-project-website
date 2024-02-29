from django.db import models

# Create your models here.


class ContactUs(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    full_name = models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(max_length=300, verbose_name='ایمیل')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')
    message = models.TextField(verbose_name='متن پیام ')
    response = models.TextField(verbose_name='پیام ادمین', null=True, blank=True)
    is_read_by_admin = models.BooleanField(verbose_name='خوانده شده توسط ادمین', default=False)

    class Meta:
        verbose_name = 'ارتباط با ما'
        verbose_name_plural = 'لیست ارتباط با ما'

    def __str__(self):
        return self.title
