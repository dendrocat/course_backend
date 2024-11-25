from urllib.parse import urlencode
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied


class AdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(request.path)
        if request.path.startswith("/admin"):
            if not request.user.is_authenticated:
                return redirect(
                    reverse_lazy("users:login")
                    + "?"
                    + urlencode({"next": request.path})
                )
            elif not request.user.is_superuser:
                print(request.user)
                raise PermissionDenied("Недостаточно прав для просмотра")

        return self.get_response(request)
