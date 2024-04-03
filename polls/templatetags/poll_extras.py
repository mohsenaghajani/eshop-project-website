from django import template
from jalali_date import date2jalali
register = template.Library()


@register.filter(name='show_jalali_date')
def show_jalali_data(value):
    return date2jalali(value)


@register.filter(name='three_digit_currency')
def three_digit_currency(value: int):
    return '{:,}'.format(value)