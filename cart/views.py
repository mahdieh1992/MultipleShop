from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
from product.models import product
from .cart import Cart


class Cart(View):

    def get(self,request):
        cart = Cart(request)
        return render(request,'cart/detail.html',{'cart':cart

        })


class AddCart(View):
    def post(self,request,slug):
        getslug = get_object_or_404(product,slug=slug)
        color,size,quantity=request.POST.get('color'),request.POST.get('size'),request.POST.get('quantity')
        cart=Cart(request)
        cart.add(getslug,color,size,quantity)

        return redirect('cart:detail')
# Create your views here.
