from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

    def __str__(self):
        return f"{self.name} - {self.price}"

class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField() 

    def __str__(self):
        return f"{self.code} - {self.description} - {self.discount}"
