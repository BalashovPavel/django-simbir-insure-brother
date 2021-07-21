from django.contrib import admin
from django.urls import path, include

from main.views import QuizHome

urlpatterns = [
    path('', QuizHome.as_view(), name='jopa'),
]