from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from authapp.models import FilmUser


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = FilmUser
        fields = ('username', 'password')


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = FilmUser
        fields = ('username', 'email')


class UserProfileForm(UserChangeForm):
    class Meta:
        model = FilmUser
        fields = ('username', 'email', 'first_name', 'last_name', 'age', 'gender')


