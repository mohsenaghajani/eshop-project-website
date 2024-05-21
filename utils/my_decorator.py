from django.http import HttpRequest
from django.shortcuts import redirect
from django.urls import reverse


def permission_admin_panel_factory(data=None):
    def permission_admin_panel(func):
        def wrapper(request: HttpRequest, *args, **kwargs):
            if request.user.is_authenticated and request.user.is_superuser:
                return func(request, *args, **kwargs)
            else:
                return redirect(reverse('login-page'))

        return wrapper
    return permission_admin_panel
