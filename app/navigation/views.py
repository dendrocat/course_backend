from django.views.generic import TemplateView

# Create your views here.
url_for_all = [
    {"text": "Таблица лидеров", "url": "game:leaderboard"}
]

urls_not_authorized = url_for_all + [
    {"text": "Зарегистрироваться", "url": "users:register"},
    {"text": "Войти", "url": "users:login"},
]

urls_authorized = url_for_all + [
    {"text": "Играть", "url": "game:index"},
    {"text": "Выйти", "url": "users:logout"},
]

url_admin = [
    {"text": "Админ-панель", "url": "admin:index", "is_superuser": True}
]



class NavigationView(TemplateView):
    title = "Добро пожаловать"

    template_name = "navigation/nav.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        urls = []
        if user.is_authenticated:
            context["title"] = self.title + f", {user.username}!"
            urls = urls_authorized
            if user.is_superuser:
                urls = url_admin + urls
        else:
            context["title"] = self.title + "!"
            urls = urls_not_authorized
        context["urls"] = urls
        return context
