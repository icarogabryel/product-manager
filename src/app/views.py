from django.shortcuts import render
from .models import Product
from django.views.generic import ListView

class ProductListView(ListView):
    model = Product
    template_name = 'product-list.html'
    context_object_name = 'products'
