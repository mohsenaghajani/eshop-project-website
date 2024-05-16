from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

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


def basket(request: HttpRequest):
    current_order, created = Order.objects.get_or_create(user_id=request.user.id, is_paid=False)
    total_amount = current_order.total_price_amount()
    context = {
        'current_order': current_order,
        'total_price': total_amount
    }
    return render(request, 'basket/basket.html', context)


def basket_content(request: HttpRequest):

    detail_id = request.GET.get('detail_id')
    if detail_id is None:
        return JsonResponse({
            'status': 'detail_not_found'
        })
    delete_count, delete_dict = OrderDetail.objects.filter(id=detail_id, order__user_id=request.user.id,
                                                           order__is_paid=False).delete()
    if delete_count == 0:
        return JsonResponse({
            'status': 'not_found'
        })

    current_order, created = Order.objects.get_or_create(user_id=request.user.id, is_paid=False)
    total_amount = current_order.total_price_amount()
    context = {
        'current_order': current_order,
        'total_price': total_amount
    }
    data = render_to_string('basket/basket_content.html', context)
    return JsonResponse({
        'status': 'success',
        'data': data
    })


def change_order_detail_count(request: HttpRequest):
    detail_id = request.GET.get('detail_id')
    state = request.GET.get('state')
    if detail_id is None or state is None:
        return JsonResponse({
            'status': 'detail_or_state_not_found'
        })
    order_detail = OrderDetail.objects.filter(id=detail_id, order__user_id=request.user.id, order__is_paid=False).first()
    if order_detail is None:
        return JsonResponse({
            'status': 'detail_not_found'
        })
    if state == 'increase':
        order_detail.count += 1
        order_detail.save()
    elif state == 'decrease':
        if order_detail.count == 1:
            order_detail.delete()
        else:
            order_detail.count -= 1
            order_detail.save()
    else:
        return JsonResponse({
            'status': 'state is invalid'
        })
    current_order, created = Order.objects.get_or_create(user_id=request.user.id, is_paid=False)
    total_amount = current_order.total_price_amount()
    context = {
        'current_order': current_order,
        'total_price': total_amount
    }
    data = render_to_string('basket/basket_content.html', context)
    return JsonResponse({
        'status': 'success',
        'data': data
    })