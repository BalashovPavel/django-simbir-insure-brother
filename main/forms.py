from django import forms
from django.forms import TextInput, EmailInput

from main.models import ClientRequest
from user.models import CompanyProfile


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


class FilterInsuranceMainForm(forms.Form):
    company = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=CompanyProfile.objects.all(),
        required=False,
        label='Компания'
    )
    min_insurance_amount = forms.DecimalField(min_value=0, max_digits=8, decimal_places=0,
                                              required=False, label='')
    max_insurance_amount = forms.DecimalField(min_value=0, max_digits=8, decimal_places=0,
                                              required=False, label="")
    min_interest_rate = forms.DecimalField(min_value=0.00, max_digits=5, decimal_places=2,
                                           required=False, label='')
    max_interest_rate = forms.DecimalField(min_value=0.00, max_digits=5, decimal_places=2,
                                           required=False, label="")
