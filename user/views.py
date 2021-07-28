from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.base import View

from main.models import Insurance, ClientRequest
from user.forms import SignUpForm, UserChangeForm, AccountChangeForm, AddInsuranceForm
from user.models import CompanyProfile


# Метод регистрации нового аккаунта
def signup_form(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            current_user = request.user
            data = CompanyProfile()
            data.user_id = current_user.id
            data.company_name = form.cleaned_data.get('company_name')
            data.email = current_user.email
            data.address = form.cleaned_data.get('address')
            data.save()
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect('/signup')
    form = SignUpForm()
    context = {
        'form': form,
    }
    return render(request, 'registration/signup.html', context)


# Изменение данных аккаунта
def change_account(request):
    if request.method == 'POST':
        user = UserChangeForm(request.POST, instance=request.user)
        info = AccountChangeForm(request.POST, request.FILES, instance=request.user.companyprofile)
        if user.is_valid() and info.is_valid():
            user.save()
            info.save()
            data = CompanyProfile.objects.get(user_id=request.user.id)
            data.email = user.cleaned_data.get('email')
            data.save()
            return HttpResponseRedirect('..')
        else:
            return HttpResponseRedirect('./change-account/')
    else:
        user = UserChangeForm(request.POST, instance=request.user)
        info = AccountChangeForm(request.POST, request.FILES, instance=request.user.companyprofile)
        context = {
            'user_form': user,
            'info_form': info
        }
        return render(request, 'user/profile__change.html', context)


# Изменение пароля аккаунта
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return HttpResponseRedirect('..')
        else:
            return HttpResponseRedirect('.')
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'user/profile__change_password.html', {'form': form})


# Выход из аккаунта
class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(self.request)
        return HttpResponseRedirect("/")


# Получение данных аккаунта
class CompanyInfo(View):

    def get(self, request, *args, **kwargs):
        company = CompanyProfile.objects.get(user=self.request.user)
        context = {
            'company': company,
        }
        return render(request, "user/profile__main.html", context)


# Список страховых услуг созданных аккаунтам
class CompanyInsurance(View):

    def get(self, request, *args, **kwargs):
        company = CompanyProfile.objects.get(user=self.request.user)
        insurances = Insurance.objects.filter(company_id=company.id)
        context = {
            'insurances': insurances,
        }
        return render(request, "user/profile__insurance.html", context)


# Добавление страховой услуги
def add_insurance(request):
    if request.method == 'POST':
        form = AddInsuranceForm(request.POST)
        if form.is_valid():
            data = Insurance()
            data.company_id = request.user.id
            data.category = form.cleaned_data.get('category')
            data.description = form.cleaned_data.get('description')
            data.interest_rate = form.cleaned_data.get('interest_rate')
            data.insurance_amount = form.cleaned_data.get('insurance_amount')
            data.save()
            return HttpResponseRedirect('./')
        else:
            return HttpResponseRedirect('./add')
    form = AddInsuranceForm()
    context = {
        'form': form,
    }
    return render(request, 'user/profile__insurance-add.html', context)


# Удаление страховой услуги
def delete_insurance(request, id):
    insurance = Insurance.objects.get(id=id)
    insurance.delete()
    return HttpResponseRedirect('..')


# Изменение полей страховой услуги
def change_insurance(request, id):
    if request.method == 'POST':
        form = AddInsuranceForm(request.POST)
        if form.is_valid():
            insurance = Insurance.objects.get(id=id)
            insurance.category = form.cleaned_data.get('category')
            insurance.description = form.cleaned_data.get('description')
            insurance.interest_rate = form.cleaned_data.get('interest_rate')
            insurance.insurance_amount = form.cleaned_data.get('insurance_amount')
            insurance.save()
            return HttpResponseRedirect('..')
        else:
            return HttpResponseRedirect('..')
    form = AddInsuranceForm()
    context = {
        'form': form,
    }
    return render(request, 'user/profile__insurance-add.html', context)


# Список клиентский запросов на страховую услугу
class CompanyClientRequest(View):

    def get(self, request, *args, **kwargs):
        company = CompanyProfile.objects.get(user=self.request.user)
        client_requests = ClientRequest.objects.filter(insurance__company__user_id=company.id)
        context = {
            'client_requests': client_requests,
        }
        return render(request, "user/profile__client_requests.html", context)


# Детальная информация о клиентском запросе
class DetailClientRequest(DetailView):
    model = ClientRequest
    template_name = "user/profile__client_requests__detail.html"
    slug_field = "pk"
    context_object_name = "detail"


# Удаление заявки
def delete_clients_requests(request, pk):
    clients_requests = ClientRequest.objects.get(pk=pk)
    clients_requests.delete()
    messages.success(request, 'Заявка удалена.')
    return HttpResponseRedirect('..')
