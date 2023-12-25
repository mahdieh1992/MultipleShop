from django.urls import path
from . import views

app_name='Basket'
urlpatterns=[
    path('detail', views.Cart.as_view(), name='detail'),
    path('AddCart/<slug:slug>', views.AddCart.as_view(), name='AddCart'),
    path('deletecart/<str:pk>', views.Deletecart.as_view(), name='dletecart'),
    path('OrderDetail', views.OrderDtail, name='Orderdetail'),
    path('OrderDetailView/<int:id>', views.OrderDetailView, name='OrderDetailView'),
    path('coupn<int:pk>', views.ApplyCoupon.as_view(), name='Couponname'),
    path('adress', views.Adresuser.as_view(), name='adress'),
]
