from django.db import models



class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)

class Customer(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)


# Create your models here.
