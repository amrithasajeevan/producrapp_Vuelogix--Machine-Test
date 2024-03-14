from django.db import models

# Create your models here.
class  register(models.Model):
    username=models.CharField(max_length=150,unique=True)
    email=models.EmailField(unique=True)
    phone=models.IntegerField()
    password = models.CharField(max_length=15)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    size = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    status = models.BooleanField(default=True,null=True, blank=True)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    username=models.ForeignKey(register,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date_ordered = models.DateTimeField(auto_now_add=True)