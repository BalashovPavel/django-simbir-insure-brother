from django.contrib import admin
from django.urls import path, include

from user.views import CompanyInfo, CompanyInsurance, add_insurance

urlpatterns = [
    path('', CompanyInfo.as_view(), name='company_info'),
    path('insurances/', CompanyInsurance.as_view(), name='company_insurance'),
    path('insurances/add', add_insurance, name='company_insurance-add'),
]
