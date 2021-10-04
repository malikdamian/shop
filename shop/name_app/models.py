from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, null=True)
    email = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128)
    producer = models.CharField(max_length=128)
    description = models.TextField()
    price = models.FloatField()
    discount_price = models.FloatField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    objects = models.Manager()

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=128, null=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.pk)

    @property
    def get_cart_total(self):
        orderitem = self.orderitem_set.all()
        total = sum(item.get_total for item in orderitem)
        return total

    @property
    def get_cart_items(self):
        orderitem = self.orderitem_set.all()
        total = sum(item.quantity for item in orderitem)
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.pk)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.CASCADE)
    company = models.CharField(max_length=128, null=True)
    street = models.CharField(max_length=128)
    house_number = models.IntegerField()
    premises_number = models.IntegerField(null=True)
    postcode = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    date_added = models.DateTimeField(auto_now_add=True)
