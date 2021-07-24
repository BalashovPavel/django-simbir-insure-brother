from django import forms
from django.forms import Select, Textarea, NumberInput, TextInput, EmailInput

from main.models import Insurance, ClientRequest


# Форма для создания клиентского запроса
class CreateClientRequestForm(forms.ModelForm):
    class Meta:
        model = ClientRequest
        fields = ('last_name', 'first_name', 'patronymic', 'phone', 'email')
        widgets = {
            'last_name': TextInput(attrs={'class': 'input'}),
            'first_name': TextInput(attrs={'class': 'input'}),
            'patronymic': TextInput(attrs={'class': 'input'}),
            'phone': TextInput(attrs={'class': 'input'}),
            'email': EmailInput(attrs={'class': 'input'}),
        }
