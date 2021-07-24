from django.contrib import admin
from django.urls import path, include

from main import views as main_views

urlpatterns = [
    path('', main_views.CategoryHome.as_view(), name='home'),
    path('category/<str:slug>/', main_views.ListInsurance.as_view(), name='insurance'),
    path('category/<str:slug>/<int:id>', main_views.create_client_request, name='create_client_request')
]
