from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import Select, Textarea, NumberInput, TextInput

from main.models import Insurance, Category


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
