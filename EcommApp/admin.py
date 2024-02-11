from django.contrib import admin
from . models import Product,CartItem

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_id","product_name","category","price","image"]

admin.site.register(Product,ProductAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ["product_id","quantity","date_added"]
admin.site.register(CartItem,CartAdmin)