from django.db import models

from account.models import User
from product_module.models import Product


# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    is_paid = models.BooleanField(verbose_name='پرداخت شده | نشده')
    date_paid = models.DateTimeField(null=True, blank=True, verbose_name='تاریخ پرداخت')

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید'


    def total_price_amount(self):
        total_amount = 0
        if self.is_paid:
            for order_detail in self.orderdetail_set.all():
                total_amount += order_detail.final_price * order_detail.count
            return total_amount
        else:
            for order_detail in self.orderdetail_set.all():
                total_amount += order_detail.product.price * order_detail.count
            return total_amount
    def __str__(self):
        return str(self.user)


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='محصول')
    final_price = models.IntegerField(null=True, blank=True, verbose_name='قیمت پرداخت شده')
    count = models.IntegerField()

    class Meta:
        verbose_name = 'جزیات سبد خرید'
        verbose_name_plural = 'لیست حزییات سبد خرید'

    def __str__(self):
        return f'{self.order}'

    def get_sum_price(self):
        return self.count * self.product.price
