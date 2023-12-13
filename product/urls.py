from django.urls import path
from . import views

app_name='product'
urlpatterns=[

    path('list', views.ProductView.as_view(), name='list'),
    path('detail<slug:slug>',views.ProductDetail.as_view(),name='detail')
]