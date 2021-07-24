from django.contrib import admin
from django.urls import path, include

from user.views import CompanyInfo, CompanyInsurance, add_insurance, delete_insurance, change_insurance, change_account, \
    change_password, CompanyClientRequest, DetailClientRequest, delete_clients_requests

urlpatterns = [
    path('', CompanyInfo.as_view(), name='company_info'),
    path('change-account/', change_account, name='change-account'),
    path('change-password/', change_password, name='change-password'),
    path('insurances/', CompanyInsurance.as_view(), name='company_insurance'),
    path('insurances/add', add_insurance, name='company_insurance-add'),
    path('insurances/delete/<int:id>', delete_insurance, name='insurance-delete'),
    path('insurances/change/<int:id>', change_insurance, name='insurance-change'),
    path('clients-requests/', CompanyClientRequest.as_view(), name='company_clients_requests'),
    path('clients-requests/<int:pk>', DetailClientRequest.as_view(), name='company_clients_requests__detail'),
    path('clients-requests/<int:pk>/delete', delete_clients_requests, name='company_clients_requests__delete'),
]
