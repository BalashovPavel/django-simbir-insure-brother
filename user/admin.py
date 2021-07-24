from django.contrib import admin

# Register your models here.
from user.models import CompanyProfile


class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'company_name', 'email', 'address']
    # search_fields = ['company_name', 'email', 'address']


admin.site.register(CompanyProfile, CompanyProfileAdmin)
