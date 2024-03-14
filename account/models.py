from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class User(AbstractUser):
    phone_number = models.PositiveIntegerField(verbose_name='تلفن همراه',

                                               null=True)
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعال سازی ایمیل', null=True)
    about_user = models.TextField(null=True, blank=True, verbose_name='درباره شخص')
    avatar_image = models.ImageField(upload_to='images/profile', verbose_name='عکس پروفایل' , null=True)

    class Mete:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.first_name is not '':
            return self.get_full_name()
        else:
            return self.username
