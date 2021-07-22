from django.contrib import admin
from django.urls import path, include

from main.views import CategoryHome, ListInsurance

urlpatterns = [
    path('', CategoryHome.as_view(), name='home'),
    path('category/<str:slug>/', ListInsurance.as_view(), name='insurance'),
]
