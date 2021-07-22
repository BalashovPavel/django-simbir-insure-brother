from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, label='Логин :')
    company_name = forms.CharField(max_length=150, label='Название компании :')
    email = forms.EmailField(max_length=200, label='Email :')
    address = forms.CharField(max_length=150, label='Юридический адрес :')
    password1 = forms.CharField(widget=forms.PasswordInput, label="Пароль")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Подтвердите пароль")

    class Meta:
        model = User
        fields = ('username', 'company_name', 'email', 'address', 'password1', 'password2',)

# class UserUpdateForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'first_name', 'last_name')
#         widgets = {
#             'username': TextInput(attrs={'class': 'input', 'placeholder': 'Логин'}),
#             'email': EmailInput(attrs={'class': 'input', 'placeholder': 'email'}),
#             'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'first_name'}),
#             'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'last_name'}),
#         }
#
#
# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = CompanyProfile
#         fields = ('phone', 'city', 'address')
#         widgets = {
#             'phone': TextInput(attrs={'class': 'input', 'placeholder': 'Телефон'}),
#             'city': TextInput(attrs={'class': 'input', 'placeholder': 'Город'}),
#             'address': TextInput(attrs={'class': 'input', 'placeholder': 'Адрес'}),
#         }
