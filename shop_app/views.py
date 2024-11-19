from itertools import product
from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from .models import Product, CategoryProduct


# Create your views here.
def home_page(request):
    # Достаем все из БД
    products = Product.objects.all()
    categories = CategoryProduct.objects.all()
    # Передаем данные на фронт
    context = {'products': products, 'categories': categories}

    return render(request, 'home.html', context)

def category_page(request, pk):
    category = CategoryProduct.objects.get(id=pk)
    products = Product.objects.filter(product_category=category)

    context ={'products': products}

    return render(request, 'category.html', context)

def product_page(request, pk):
    product = Product.objects.get(id=pk)

    context = {'product': product}

    return render(request, 'product.html', context)