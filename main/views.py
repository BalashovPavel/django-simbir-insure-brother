from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import View
from elasticsearch_dsl.query import MultiMatch

from main.documents import InsuranceDocument
from main.forms import CreateClientRequestForm, FilterInsuranceMainForm
from main.models import Category, Insurance, ClientRequest
from main.tasks import client_request_created, get_mongodb


# Список типов страхований
class CategoryHome(ListView):
    model = Category
    context_object_name = "categories"
    template_name = "main/index.html"


# Список предложений для типа страхования
class ListInsurance(View):

    def get(self, request, *args, **kwargs):
        products = Insurance.objects.filter(category__slug=self.kwargs['slug'])
        category = Category.objects.get(slug=self.kwargs['slug'])
        form = FilterInsuranceMainForm(self.request.GET)
        if form.is_valid():

            """
            Получение крайних значений для слайдеров
            """
            list_rate = products.values_list('interest_rate', flat=True)
            list_amount = products.values_list('insurance_amount', flat=True)
            min_rate_slider = min(list_rate)
            max_rate_slider = max(list_rate)
            min_amount_slider = min(list_amount)
            max_amount_slider = max(list_amount)

            """
            Фильтр по сумме и проценту
            """
            min_amount = form.cleaned_data.get('min_insurance_amount')
            max_amount = form.cleaned_data.get('max_insurance_amount')
            if not (min_amount and max_amount) is None:
                products = products.filter(insurance_amount__range=[min_amount, max_amount])

            min_rate = form.cleaned_data.get('min_interest_rate')
            max_rate = form.cleaned_data.get('max_interest_rate')
            if not (min_rate and max_rate) is None:
                products = products.filter(interest_rate__range=[min_rate, max_rate])

            """
            Фильтр по компаниям
            """
            companies = form.cleaned_data.get('company')
            if companies:
                products = products.filter(company__in=companies)

            context = {
                'products': products,
                'category': category,
                'form': form,
                'min_amount': min_amount_slider,
                'max_amount': max_amount_slider,
                'min_rate': min_rate_slider,
                'max_rate': max_rate_slider,
            }
            return render(request, 'main/list-insurance.html', context)

        context = {
            'products': products,
            'category': category,
            'form': form,
        }
        return render(request, 'main/list-insurance.html', context)


# Поиск через elasticsearch
class ListSearch(View):

    def get(self, request, *args, **kwargs):
        search = self.request.GET.get("search")
        # search_query = MultiMatch(query=search, fields=["company.company_name", "category.category_name", "description"])
        search_query = MultiMatch(query=search,
                                  fields=["description"])
        search_result = InsuranceDocument.search().query(search_query)
        products = search_result.to_queryset()
        return render(request, "main/search_list.html", context={'products': products, 'search': search})


class InsuranceInfo(View):

    def get(self, request, *args, **kwargs):
        insurance = Insurance.objects.get(pk=self.kwargs['id'])
        db = get_mongodb()
        collection = db.insurance
        query = {'insurance_id': insurance.id}
        new_values = {'$inc': {'number_views': 1}}
        collection.update_one(query, new_values)
        return render(request, "main/service_info.html", {"insurance": insurance})


# Создание клиентского запроса на предложение о страховке
def create_client_request(request, slug, id):
    insurance = Insurance.objects.get(id=id)
    if request.method == 'POST':
        form = CreateClientRequestForm(request.POST)
        if form.is_valid():
            client_request = ClientRequest()
            client_request.first_name = form.cleaned_data.get('first_name')
            client_request.last_name = form.cleaned_data.get('last_name')
            client_request.patronymic = form.cleaned_data.get('patronymic')
            client_request.phone = form.cleaned_data.get('phone')
            client_request.email = form.cleaned_data.get('email')
            client_request.insurance_id = insurance.id
            client_request.save()
            client_request_created.delay(client_request.id)
            messages.success(request, 'Заявка отправлена.')
            return HttpResponseRedirect('.')
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect('./' + str(id))
    form = CreateClientRequestForm()
    context = {
        'form': form,
        'insurance': insurance,
    }
    return render(request, 'main/create_client_request.html', context)
