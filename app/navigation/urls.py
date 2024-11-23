from django.urls import path
from .views import NavigationView

urlpatterns = [
    path("", NavigationView.as_view(), name="home")
]
