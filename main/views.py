from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class QuizHome(TemplateView):
    template_name = "main/index.html"
