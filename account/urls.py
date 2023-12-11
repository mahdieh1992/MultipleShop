from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('Register',views.RgisterUser,name='Register'),
    path('login',views.LoginUser.as_view(),name='login'),
    path('logout',views.LogoutUser,name='logout'),
    path('forgetpassword',views.ForgetPassView.as_view(),name='ForgetPass'),
    path('Confirm',views.ConfirmCode.as_view(),name='Confirm'),
]