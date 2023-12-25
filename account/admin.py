from django.contrib import admin
from .models import CustomUser,AdressUser


class adresuser(admin.TabularInline):
    model = AdressUser


@admin.register(CustomUser)
class Customuser(admin.ModelAdmin):
    list_display = ('email','Mobile')
    inlines = (adresuser,)

# Register your models here.
