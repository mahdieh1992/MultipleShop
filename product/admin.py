from django.contrib import admin
from .models import product,Categories,Color,Size,Information


class InfoAdmin(admin.TabularInline):
    model = Information


@admin.register(product)
class productAdmin(admin.ModelAdmin):
    list_display = ['title','price']
    inlines = [InfoAdmin]


admin.site.register(Categories)
admin.site.register(Color)
admin.site.register(Size)
