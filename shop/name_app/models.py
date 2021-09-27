from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=128)
    producer = models.CharField(max_length=128)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    objects = models.Manager()

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.CharField(max_length=128)
    products = models.ManyToManyField(Product)
    date_added = models.DateTimeField(auto_now_add=True)
    date_payment = models.DateField()
    total_price = models.FloatField()


class Address(models.Model):
    username = models.CharField(max_length=128)
    company = models.CharField(max_length=128, null=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    street = models.CharField(max_length=128)
    house_number = models.IntegerField()
    premises_number = models.IntegerField(null=True)
    postcode = models.CharField(max_length=128)
    location = models.CharField(max_length=128)



