from django.shortcuts import redirect
from django.urls import reverse_lazy
from urllib.parse import urlencode


class AdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith("/admin/") and request.user.is_authenticated:
            if not request.user.is_superuser:
                return redirect(reverse_lazy("users:login") + "?" + urlencode({"next": request.path}))
            
        return self.get_response(request)