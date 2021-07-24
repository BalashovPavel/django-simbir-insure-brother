from django.contrib import admin

from main.models import Category, Insurance, ClientRequest


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'slug']
    # search_fields = ['category_name', 'slug']
    prepopulated_fields = {'slug': ('category_name',)}


class InsuranceAdmin(admin.ModelAdmin):
    list_display = ['company', 'category', 'description', 'interest_rate', 'insurance_amount', 'create_at', 'update_at']
    # list_filter = ['company', 'category']
    # search_fields = ['description', 'interest_rate', 'insurance_amount']


class ClientRequestAdmin(admin.ModelAdmin):
    list_display = ['insurance', 'first_name', 'last_name', 'patronymic', 'phone', 'email', 'create_at']
    # list_filter = ['insurance'] patronymic
    # search_fields = ['phone', 'email', 'first_name', 'last_name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Insurance, InsuranceAdmin)
admin.site.register(ClientRequest, ClientRequestAdmin)
