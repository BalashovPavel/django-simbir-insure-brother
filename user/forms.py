from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, Select, Textarea, NumberInput

from main.models import Insurance
from user.models import CompanyProfile


# Форма для регистрации нового аккаунта
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


# Форма для изменения полей User
class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {
            'username': TextInput(attrs={'class': 'input', 'placeholder': 'Логин :'}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'Email :'}),
        }


# Форма для изменения полей аккаунта
class AccountChangeForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = ('company_name', 'address')
        widgets = {
            'company_name': TextInput(attrs={'class': 'input', 'placeholder': 'Название компании :'}),
            'address': TextInput(attrs={'class': 'input', 'placeholder': 'Юридический адрес :'}),
        }


# Форма для добавления страхового предложения
class AddInsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurance
        fields = ('category', 'description', 'interest_rate', 'insurance_amount')
        widgets = {
            'category': Select(),
            'description': Textarea(attrs={'class': 'input', 'placeholder': 'Краткое описание'}),
            'interest_rate': NumberInput(attrs={'class': 'input', 'placeholder': 'Процентная ставка'}),
            'insurance_amount': NumberInput(attrs={'class': 'input', 'placeholder': 'Страховая сумма'})
        }
