# Django API Project

This project is a Django-based web application that provides a RESTful API for managing products and categories. It is built using Django and Django REST Framework.

## Features

- **Products API**:
  - List all products: `/api/products/`
  - Retrieve a single product by ID: `/api/products/<int:id>/`

- **Categories API**:
  - List all categories: `/api/categories/`
  - Retrieve a single category by ID: `/api/categories/<int:id>/`
  - List all products under a specific category: `/api/categories/<int:id>/products/`

## Models

### Product
- `name`: Name of the product.
- `description`: Detailed description of the product.
- `price`: Price of the product.
- `count`: Quantity available in stock.
- `is_active`: Boolean indicating if the product is active.
- `category`: Foreign key linking the product to a category.

### Category
- `name`: Name of the category.

## Prerequisites

- Python 3.8 or higher
- Django 4.2 or higher
- Django REST Framework

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url> # to be updated
   cd <repository-folder>
   ```

2. Create and activate virtual environment
    ```
    python -m venv venv
    venv\Scripts\activate  # On Windows
    ```
3. Install dependencies
    ```
    python -m pip install -r requirements.txt
    ```

4. Apply migrations 
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Run the development server
    ```
    python manage.py runserver
    ```