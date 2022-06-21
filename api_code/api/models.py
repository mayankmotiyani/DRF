from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200,blank=True)
    title = models.TextField(blank=True,help_text="product description...")
    price = models.DecimalField(max_digits=15,decimal_places=2,default=5.00)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['created']

    def __str__(self):
        return '{}'.format(self.name)

    def get_time(self):
        return datetime.strftime(self.created,"%H:%M %p")


class Customer(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    delivered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']
    
    def __str__(self):
        return '{}'.format(self.customer.username)


class CustomerMultipleProduct(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    delivered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.customer.username)


