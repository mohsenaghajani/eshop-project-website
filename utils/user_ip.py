from django.http import HttpRequest


def get_user_ip(request: HttpRequest):
    x_forward_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forward_for:
        user_ip = x_forward_for.split(',')[0]
    else:
        user_ip = request.META.get('REMOTE_ADDR')
    return user_ip