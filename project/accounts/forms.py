from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Добавление в группы при регистрации
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2", )


# Добавление в группы при регистрации
class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        common_users = Group.objects.get(name="common users")
        user.groups.add(common_users)
        return user

# add TestUser@mail.ru + NfNB7D_yyeD0
