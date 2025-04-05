from rest_framework import serializers
from .models import Product, Category, Company, Vacancy

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

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

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'

class VacancyCompanySerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Vacancy
        fields = '__all__'