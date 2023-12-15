from django.shortcuts import render
from .models import product,Size
from django.views.generic import ListView,DetailView

class ProductView(ListView):
    model = product
    paginate_by = 1
    template_name = 'product/Shop.html'


class ProductDetail(DetailView):
    model = product
    template_name = 'product/detail.html'
    context_object_name = 'ProductDetail'

# Create your views here.
