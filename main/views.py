from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.views.generic import ListView

from main.forms import CreateClientRequestForm
from main.models import Category, Insurance, ClientRequest


# Список типов страхований
class CategoryHome(ListView):
    model = Category
    context_object_name = "categories"
    template_name = "main/index.html"


# Список предложений для типа страхования
class ListInsurance(ListView):
    model = Insurance
    template_name = 'main/list-insurance.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Insurance.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListInsurance, self).get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


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
            print(client_request.insurance_id)
            client_request.save()
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
