from django.urls import path

from main import views as main_views

urlpatterns = [
    path('', main_views.CategoryHome.as_view(), name='home'),
    path('category/<str:slug>/', main_views.ListInsurance.as_view(), name='insurance'),
    path('category/<str:slug>/<int:id>', main_views.create_client_request, name='create_client_request'),
    path('category/<str:slug>/info/<int:id>', main_views.InsuranceInfo.as_view(), name='insurance_info'),
    path('search/', main_views.ListSearch.as_view(), name='search_results'),
]
