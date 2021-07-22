from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from main.models import Category, Insurance


class CategoryHome(ListView):
    model = Category
    context_object_name = "categories"
    template_name = "main/index.html"


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


