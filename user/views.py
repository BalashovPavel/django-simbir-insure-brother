from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView
from django.views.generic.base import View

from main.forms import AddInsuranceForm
from main.models import Insurance
from user.forms import SignUpForm
from user.models import CompanyProfile


class CompanyInfo(View):

    def get(self, request, *args, **kwargs):
        company = CompanyProfile.objects.get(user=self.request.user)
        context = {
            'company': company,
        }
        return render(request, "user/profile__main.html", context)


class CompanyInsurance(View):

    def get(self, request, *args, **kwargs):
        company = CompanyProfile.objects.get(user=self.request.user)
        insurances = Insurance.objects.filter(company_id=company.id)
        context = {
            'insurances': insurances,
        }
        return render(request, "user/profile__insurance.html", context)


def add_insurance(request):
    if request.method == 'POST':
        form = AddInsuranceForm(request.POST)
        if form.is_valid():
            form.save()
            data = Insurance()
            data.company_id = request.user.id
            data.category = form.cleaned_data.get('category')
            data.description = form.cleaned_data.get('description')
            data.interest_rate = form.cleaned_data.get('interest_rate')
            data.insurance_amount = form.cleaned_data.get('insurance_amount')
            data.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
    form = AddInsuranceForm()
    context = {
        'form': form,
    }
    return render(request, 'user/profile__insurance-add.html', context)


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(self.request)
        return HttpResponseRedirect("/")


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
