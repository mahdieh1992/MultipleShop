from django.shortcuts import render
from django.views.generic import ListView
from product.models import product


class Homepage(ListView):
    model = product
    template_name = 'Home/index.html'
    context_object_name = 'product'

# Create your views here.
