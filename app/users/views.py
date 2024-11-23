from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import FormView
from app.settings import LOGIN_REDIRECT_URL

from .mixins import FormMixin
from .forms import RegisterForm


# Create your views here.
class Login(FormMixin, LoginView):
    template_name = "users/form.html"
    title = "Страница входа"
    button_text = "Войти"

    class Meta:
        model = get_user_model()
        fields = ["login", "password"]


class Register(FormMixin, FormView):
    form_class = RegisterForm

    template_name = "users/form.html"
    title = "Страница регистрации"
    button_text = "Зарегистрироваться"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

    success_url = reverse_lazy(LOGIN_REDIRECT_URL)


class Logout(LogoutView):
    http_method_names = ["get"]

    def get(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
