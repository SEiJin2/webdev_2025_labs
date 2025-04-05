from django.urls import path
from .views import (
    ProductListView, ProductDetailView, CategoryListView, 
    CategoryDetailView, ProductsByCategoryView, CompanyListView, 
    CompanyDetailView, CompanyVacanciesView, VacancyListView,
    VacancyDetailView, VacancyTopTenView
)
# You have to model with the following fields:
# Company
# name - CharField
# description - TextField
# city - CharField
# address - TextField
# Vacancy
# name - CharField
# description - TextField
# salary - FloatField
# company - ForeignKey

# Write API endpoints with JSON format:
# /api/companies - List of all Companies
# /api/companies/<int:id>/ - Get one Company
# /api/companies/<int:id>/vacancies/ - List of Vacancies by Company
# /api/vacancies/ - List of all Vacancies
# /api/vacancies/<int:id>/ - Get one Vacancy
# /api/vacancies/top_ten/ - List of top 10 vacancies sorted by decreasing salary
urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('categories/<int:category_id>/products/', ProductsByCategoryView.as_view(), name='products-by-category'),
    path('companies/', CompanyListView.as_view(), name='company-list'),
    path('companies/<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('companies/<int:company_id>/vacancies/', CompanyVacanciesView.as_view(), name='company-vacancies'),
    path('vacancies/', VacancyListView.as_view(), name='vacancy-list'),
    path('vacancies/<int:pk>/', VacancyDetailView.as_view(), name='vacancy-detail'),
    path('vacancies/top_ten/', VacancyTopTenView.as_view(), name='vacancy-top-ten'),
]