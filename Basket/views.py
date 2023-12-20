from django.shortcuts import render,redirect,get_object_or_404,reverse
from django.views.generic import View
from product.models import product
from .CartSession import MyCart
from .models import Discount,Orderdetailuser,OrderUser
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from account.models import CustomUser

now = timezone.now()


class Cart(View):
    def get(self,request):
        cart=MyCart(request)
        return render(request, 'Basket/detail.html', {'cart':cart

                                                      })


class AddCart(View):
    def post(self,request,slug):
        getslug = get_object_or_404(product,slug=slug)
        color,size,quantity=request.POST.get('color','empty'),request.POST.get('size','empty'),request.POST.get('quantity')
        cart=MyCart(request)
        cart.Cart_Add(getslug,color,size,quantity)
        return redirect('Basket:detail')
# Create your views here.


class Deletecart(View):
    def get(self,request,pk):
        cart=MyCart(request)
        cart.deletecart(pk)
        return redirect('Basket:detail')


class ApplyCoupon(View):

    def post(self,request,pk):
        couponname=request.POST.get('CouponName')
        print(couponname)
        orderuserid = OrderUser.objects.get(id=pk)
        print(orderuserid)
        CouponObject=get_object_or_404(Discount,DiscountName=couponname)
        if CouponObject.Quantity==0 or CouponObject.Expiredate < now:
            messages.info(request,'Coupon  Finished')
        orderuserid.total=orderuserid.total*CouponObject.DiscountPercent//100
        orderuserid.save()
        CouponObject.Quantity-=1
        CouponObject.save()
        return redirect(reverse('Basket:OrderDetailView',kwargs={'id':pk}))

@login_required(login_url='/account/login')
def OrderDtail(request):
        cart=MyCart(request)
        order=OrderUser.objects.create(userid=request.user, createDate=now, total=int(cart.total()))
        for item in cart:
            p=product.objects.get(slug=item['productid'])
            Orderdetailuser.objects.create(orderid=order,user=request.user,productid=p,size=item['size'],color=item['color'],price=int(item['price']),total=int(item['total']),createDate=now)
        cart.remove()
        orderid=order.id
        return redirect(reverse('Basket:OrderDetailView',kwargs={'id':orderid}))

def OrderDetailView(request,id):
    orderget=OrderUser.objects.get(id=id)
    orderdetail=orderget.OrderDtailid.all()
    return render(request,'Basket/OrderDetail.html',
       {
        'orderdetail':orderdetail,
        'orderget':orderget
       }
                  )

