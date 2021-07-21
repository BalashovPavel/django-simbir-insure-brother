from django.contrib import admin

from main.models import CompanyProfile,Category,Insurance,ClientRequest


class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'company_name', 'email', 'address']
    # search_fields = ['company_name', 'email', 'address']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'slug']
    # search_fields = ['category_name', 'slug']


class InsuranceAdmin(admin.ModelAdmin):
    list_display = ['company', 'category', 'description', 'interest_rate', 'insurance_amount']
    # list_filter = ['company', 'category']
    # search_fields = ['description', 'interest_rate', 'insurance_amount']


class ClientRequestAdmin(admin.ModelAdmin):
    list_display = ['insurance', 'first_name', 'last_name', 'patronymic', 'phone', 'email']
    # list_filter = ['insurance'] patronymic
    # search_fields = ['phone', 'email', 'first_name', 'last_name']


admin.site.register(CompanyProfile, CompanyProfileAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Insurance, InsuranceAdmin)
admin.site.register(ClientRequest, ClientRequestAdmin)
