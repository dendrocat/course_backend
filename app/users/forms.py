from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class RegisterForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ["username", "first_name", "password1", "password2"]
