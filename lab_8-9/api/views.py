from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Product, Category, Company, Vacancy
from .serializers import ProductSerializer, CategorySerializer, CompanySerializer, VacancySerializer, VacancyCompanySerializer

# Create your views here.
class ProductListView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryListView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductsByCategoryView(APIView):
    def get(self, request, category_id):
        products = Product.objects.filter(category_id=category_id)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
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

class CompanyListView(ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyVacanciesView(APIView):
    def get(self, request, company_id):
        vacancies = Vacancy.objects.filter(company_id=company_id)
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)    

class VacancyListView(ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer   

class VacancyDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class VacancyTopTenView(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.order_by('-salary')[:10]
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)