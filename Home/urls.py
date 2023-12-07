from django.urls import path
from . import views

app_name = 'Home'

urlpatterns = [
    path('',views.Homepage.as_view(),name='main')
]
