from django.urls import path
from . import views

app_name='cart'
urlpatterns=[
    path('detail',views.Cart.as_view(),name='detail'),
    path('AddCart<slug:slug>',views.AddCart.as_view(),name='AddCart')
]