from django.db import models
from django.utils.html  import mark_safe

# Create your models here.
class Product(models.Model):
    product_id = models.IntegerField(primary_key = True)
    product_name = models.CharField(max_length = 50)
    type = (("Watch","Watch"),("Mobile","Mobile"),("Laptop","Laptop"))
    category = models.CharField(max_length = 100,choices = type)
    desc =models.CharField(max_length = 255)
    price = models.IntegerField()
    image = models.ImageField(upload_to='pics')

    def proImage(self):
        return mark_safe(f"<img src='{self.image.url}' width = '300px' >")
    
class CartItem(models.Model):
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 0)
    date_added = models.DateTimeField(auto_now_add = True)
