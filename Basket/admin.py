from django.contrib import admin
from .models import Discount,Orderdetailuser

@admin.register(Discount)
class couponadmin(admin.ModelAdmin):
    list_display = ('__str__','Expiredate')


admin.site.register(Orderdetailuser)
# Register your models here.
