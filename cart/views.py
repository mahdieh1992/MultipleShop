from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
from product.models import product
from .CartSession import MyCart


class Cart(View):
    def get(self,request):
        cart=MyCart(request)
        return render(request,'cart/detail.html',{'cart':cart

        })

class AddCart(View):
    def post(self,request,slug):
        getslug = get_object_or_404(product,slug=slug)
        color,size,quantity=request.POST.get('color','empty'),request.POST.get('size','empty'),request.POST.get('quantity')
        cart=MyCart(request)
        cart.Cart_Add(getslug,color,size,quantity)
        return redirect('cart:detail')
# Create your views here.


class Deletecart(View):
    def get(self,request,k):
        cart=MyCart(request)
        cart.deletecart(k)
        return redirect('cart:detail')