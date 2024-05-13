from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

from order_module.models import Order, OrderDetail
from product_module.models import Product


# Create your views here.


def add_product_to_basket(request: HttpRequest):
    print(request.GET)
    product_id = request.GET.get('product_id')
    product_count = int(request.GET.get('count'))
    if product_count < 1:
        return JsonResponse({'status': 'invalid count',
                             'text': 'تعداد معتبر نمی باشد',
                             'icon': 'error',
                             'confirm_button_text': 'ادامه دادن'})


    if request.user.is_authenticated:
        product = Product.objects.filter(id=product_id, is_active=True).first()
        if product is not None:
            current_order, created = Order.objects.get_or_create(user_id=request.user.id, is_paid=False)
            current_order_detail = current_order.orderdetail_set.filter(product_id=product_id).first()
            if current_order_detail is not None:
                current_order_detail.count += product_count
                current_order_detail.save()
            else:
                OrderDetail.objects.create(product_id=product_id, count=product_count, order_id=current_order.id)
            return JsonResponse({'status': 'success',
                                 'text': 'به سبد خرید اضافه شد',
                                 'icon': 'success',
                                 'confirm_button_text': 'ادامه خرید' })
        else:
            return JsonResponse({'status': 'not found',
                                 'text': 'محصول پیدا نشد',
                                 'icon': 'error',
                                 'confirm_button_text': 'ادامه ' })
    else:
        return JsonResponse({'status': 'not_auth',
                            'text': 'برای خرید ابتدا وارد شوید',
                             'icon': 'warning',
                             'confirm_button_text': 'وارد شدن' })
